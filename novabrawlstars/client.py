import asyncio
import httpx

from .exceptions import (
    ApiError,
    InvalidTokenError,
    RateLimitError,
    NotFoundError
)
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
        if not token or not isinstance(token, str) or token.strip() == "":
            raise InvalidTokenError("API token is required")
        
        self.token = token

        self._async_client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/json",
                "User-Agent": "NovaBrawlStarsAPI/1.0"
            },
            timeout=10.0
        )

    async def _async_request(self, endpoint: str):
        response = await self._async_client.get(endpoint)
        status = response.status_code

        if status == 200:
            return response.json()
        
        if status == 401:
            raise InvalidTokenError("Invalid API token.", code=401)
        if status == 404:
            raise NotFoundError("Resource not found.", code=404)
        if status == 429:
            raise RateLimitError("Rate limit exceeded.", code=429)

        raise ApiError(response.text, code=status)
    
    def _run(self, coro):
        """
        Runs async code safely even if the user is not using asyncio.
        """
        try:
            return asyncio.run(coro)
        except RuntimeError:
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(coro)
    
    def _clean_tag(self, tag: str) -> str:
        return (
            tag.strip() 
            .replace("#", "")
            .replace(" ", "")
            .upper()          
        )
    
    def get_player(self, tag: str) -> Player:
        tag = self._clean_tag(tag)
        data = self._run(self._async_request(f"/players/%23{tag}"))
        return Player(data)