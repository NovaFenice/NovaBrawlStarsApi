import requests
from .exceptions import (
    ApiError,
    InvalidTokenError,
    RateLimitError,
    NotFoundError,
    UnexpectedError,
    ServiceErrorMaintenance
)
from .models import Player, BattleLogListType

class NovaBrawlStars:
    BASE_URL = "https://api.brawlstars.com/v1"

    def __init__(self, token: str):
        """
        Initialize the Brawl Stars API client.

        Parameters:
        -----------
        token : str
            Your Brawl Stars API token.
            You can get it from https://developer.brawlstars.com/
        """
        if not token or not isinstance(token, str) or token.strip() == "":
            raise InvalidTokenError("API token is required")
        
        self.token = token

        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "User-Agent": "NovaBrawlStarsAPI/1.0"
        })

    def _request(self, endpoint: str):
        """
        Perform a synchronous HTTP GET request to the API.
        """
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.get(url)
        status = response.status_code

        if status == 200:
            return response.json()
        if status == 403:
            raise InvalidTokenError("Invalid API token.", code=400)
        if status == 404:
            raise NotFoundError("Resource not found.", code=404)
        if status == 429:
            raise RateLimitError("Rate limit exceeded.", code=429)
        if status == 500:
            raise UnexpectedError("Internal server error.", code=500)
        if status == 503:
            raise ServiceErrorMaintenance("Service is under maintenance.", code=503)

        raise ApiError(response.text, code=status)

    def _clean_tag(self, tag: str) -> str:
        """
        Clean the player tag by removing #, spaces, and converting to uppercase.
        """
        return tag.strip().replace("#", "").replace(" ", "").upper()

    def get_player(self, tag: str) -> Player:
        """
        Get a Player object from the API using the player tag.
        """
        tag = self._clean_tag(tag)
        data = self._request(f"/players/%23{tag}")
        return Player(data)
    
    def get_battlelog(self, tag: str) -> BattleLogListType:
        """
        Get a BattleLog object from the API using the player tag.
        """
        tag = self._clean_tag(tag)
        data = self._request(f"/players/%23{tag}/battlelog")
        return BattleLogListType(data)