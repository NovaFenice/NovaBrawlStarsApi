import requests
from .exceptions import ApiError, InvalidTokenError, RateLimitError, NotFoundError
from .models.player import Player

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
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json"
        })

    def _request(self, endpoint: str):
        """
        Internal method to make a GET request.
        """
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.get(url)

        if response.status_code == 401:
            raise InvalidTokenError(response.text, code=401)
        elif response.status_code == 404:
            raise NotFoundError(response.text, code=404)
        elif response.status_code == 429:
            raise RateLimitError(response.text, code=429)
        elif response.status_code != 200:
            raise ApiError(response.text, code=response.status_code)

        return response.json()
    
    def get_player(self, tag: str) -> Player:
        tag = tag.replace("#", "").upper()
        data = self._request(f"/players/%23{tag}")
        return Player(data)