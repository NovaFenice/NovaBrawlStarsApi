from typing import List
from .brawlerAccessoryType import BrawlerAccessoryType
from .brawlerStarPowerType import BrawlerStarPowerType
from .brawlerGearStatsType import BrawlerGearStatsType

class BrawlerStatsType:
    def __init__(self, data: dict):
        """
        Initialize the BrawlerStatsType.

        data: dict
            Dictionary containing brawler stats info from the API
            Expected keys: 'id', 'name', 'rank', 'trophies', 'highestTrophies', 'power', 'maxWinStreak', 'currentWinStreak', 'gadgets', 'starPowers', 'gearStats'
        """
        if data is None:
            data = {}

        self.id: int = data.get("id", 0)
        self.name: str = data.get("name", "")
        self.rank: int = data.get("rank", 0)
        self.trophies: int = data.get("trophies", 0)
        self.highestTrophies: int = data.get("highestTrophies", 0)
        self.power: int = data.get("power", 0)
        self.maxWinStreak: int = data.get("maxWinStreak", 0)
        self.currentWinStreak: int = data.get("currentWinStreak", 0)

        self.iconUrl: str = f"https://cdn.brawlify.com/brawlers/borderless/{self.id}.png" if self.id != 0 else ""

        self.gadgets: List[BrawlerAccessoryType] = [BrawlerAccessoryType(a) for a in data.get("gadgets", []) if a]

        self.starPowers: List[BrawlerStarPowerType] = [BrawlerStarPowerType(sp) for sp in data.get("starPowers", []) if sp]

        self.gears: List[BrawlerGearStatsType] = [BrawlerGearStatsType(g) for g in data.get("gears", []) if g]

    def __repr__(self):
        cls_name = self.__class__.__module__ + "." + self.__class__.__qualname__
        return f"<{cls_name} id={self.id} mode={self.mode!r} map={self.map!r}>"

class BrawlerStatsListType:
    def __init__(self, data: List[dict]):
        """
        Initialize the BrawlerStatsListType.

        data: List[dict]
            List of dictionaries containing brawler stats info from the API
            Expected keys: 'id', 'name', 'rank', 'trophies', 'highestTrophies', 'power', 'maxWinStreak', 'currentWinStreak', 'gadgets', 'starPowers', 'gearStats'
        """
        self.brawlersList: List[BrawlerStatsType] = [BrawlerStatsType(b) for b in data if b]

    def __repr__(self):
        cls_name = self.__class__.__module__ + "." + self.__class__.__qualname__
        return f"<{cls_name} id={self.id} mode={self.mode!r} map={self.map!r}>"