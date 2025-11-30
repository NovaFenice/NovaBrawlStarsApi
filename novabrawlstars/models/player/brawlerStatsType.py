from typing import List
from .brawlerAccessoryType import BrawlerAccessoryType
from .brawlerStarPowerType import BrawlerStarPowerType
from .brawlerGearStatsType import BrawlerGearStatsType

class BrawlerStatsType:
    def __init__(self, data: dict):
        self.id: int = data.get("id", 0)
        self.name: str = data.get("name", "")
        self.rank: int = data.get("rank", 0)
        self.trophies: int = data.get("trophies", 0)
        self.highestTrophies: int = data.get("highestTrophies", 0)
        self.power: int = data.get("power", 0)
        self.maxWinStreak: int = data.get("maxWinStreak", 0)
        self.currentWinStreak: int = data.get("currentWinStreak", 0)

        self.iconUrl: str = f"https://cdn.brawlify.com/brawlers/borderless/{self.id}.png" if self.id else ""

        self.gadgets: List[BrawlerAccessoryType] = [BrawlerAccessoryType(a) for a in data.get("gadgets", []) if a]

        self.starPowers: List[BrawlerStarPowerType] = [BrawlerStarPowerType(sp) for sp in data.get("starPowers", []) if sp]

        self.gears: List[BrawlerGearStatsType] = [BrawlerGearStatsType(g) for g in data.get("gears", []) if g]

    def __repr__(self):
        return f"<BrawlerStat id={self.id} name={self.name} trophies={self.trophies}>"
    
    def __str__(self):
        gadgets_str = ", ".join([str(g) for g in self.gadgets]) if self.gadgets else "{}"
        starpowers_str = ", ".join([str(sp) for sp in self.starPowers]) if self.starPowers else "{}"
        gears_str = ", ".join([str(g) for g in self.gears]) if self.gears else "{}"

        return (
            f"Brawler: {self.name} (ID: {self.id})\n"
            f"Trophies: {self.trophies}, Highest: {self.highestTrophies}, Power: {self.power}\n"
            f"Rank: {self.rank}, CurrentWinStreak: {self.currentWinStreak}, MaxWinStreak: {self.maxWinStreak}\n"
            f"Icon: {self.iconUrl}\n"
            f"Gadgets: {gadgets_str}\n"
            f"StarPowers: {starpowers_str}\n"
            f"Gears: {gears_str}\n"
        )

class BrawlerStatsListType:
    def __init__(self, data: List[dict]):
        self.brawlers_list: List[BrawlerStatsType] = [BrawlerStatsType(b) for b in data if b]

    def __repr__(self):
        return f"<BrawlerStatList count={len(self.brawlers_list)}>"
    
    def __str__(self):
        return "\n".join([str(b) for b in self.brawlers_list]) if self.brawlers_list else "{}"