from typing import List
from .brawlerAccessoryType import BrawlerAccessoryType
from .brawlerStarPowerType import BrawlerStarPowerType
from .brawlerGearStatsType import BrawlerGearStatsType

class BrawlerStatsType:
    id: int
    name: str
    rank: int
    trophies: int
    highestTrophies: int
    power: int
    maxWinStreak: int
    currentWinStreak: int
    iconUrl: str
    gadgets: List[BrawlerAccessoryType]
    starPowers: List[BrawlerStarPowerType]
    gears: List[BrawlerGearStatsType]
    """
    Initialize the BrawlerStatsType.

    data: dict
        Dictionary containing brawler stats info from the API
        Expected keys: 'id', 'name', 'rank', 'trophies', 'highestTrophies', 'power', 'maxWinStreak', 'currentWinStreak', 'gadgets', 'starPowers', 'gearStats'
    """
    def __init__(self, data: dict) -> None: ...

class BrawlerStatsListType:
    brawlersList: List[BrawlerStatsType]
    """
    Initialize the BrawlerStatsListType.

    data: List[dict]
        List of dictionaries containing brawler stats info from the API
        Expected keys: 'id', 'name', 'rank', 'trophies', 'highestTrophies', 'power', 'maxWinStreak', 'currentWinStreak', 'gadgets', 'starPowers', 'gearStats'
    """
    def __init__(self, data: List[dict]) -> None: ...