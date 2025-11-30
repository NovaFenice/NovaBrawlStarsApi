from typing import Any
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
    """Brawl Stars API client."""
    BASE_URL: str
    def __init__(self, token: str) -> None: 
        """
        Initialize the Brawl Stars API client.

        Parameters:
        -----------
        token : str
            Your Brawl Stars API token.
            You can get it from https://developer.brawlstars.com/
        """
        ...
    
    def _request(self, endpoint: str) -> Any:
        """
        Perform a synchronous HTTP GET request to the API.
        """
        ...

    def _clean_tag(self, tag: str) -> str:
        """
        Clean the player tag by removing #, spaces, and converting to uppercase.
        """
        ...
    
    def get_player(self, tag: str) -> Player:
        """
        Get a Player object from the API using the player tag.
        """
        ...

    def get_battlelog(self, tag: str) -> BattleLogListType:
        """
        Get a BattleLog object from the API using the player tag.
        """
        ...