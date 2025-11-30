from typing import List
from .brawlerBattleType import BrawlerBattleType

class BattlePlayerType:
    def __init__(self, data: dict):
        """
        Initialize the BattlePlayerType.

        data: dict
            Dictionary containing player info from the API
            Expected keys: 'tag', 'name', 'brawler'
        """
        if data is None:
            data = {}
        self.tag: str = data.get("tag", "")
        self.name: str = data.get("name", "")
        self.brawler: BrawlerBattleType = BrawlerBattleType(data.get("brawler", {}))

    def __repr__(self):
        cls_name = self.__class__.__module__ + "." + self.__class__.__qualname__
        return f"<{cls_name} mode={self.mode!r} result={self.result!r}>"

class BattleTeamType:
    def __init__(self, data: list):
        """
        Initialize the BattleTeamType.

        data: list
            List of dictionaries containing player info from the API
        """
        if data is None:
            data = []
        self.players: List[BattlePlayerType] = [BattlePlayerType(p) for p in data if p]

    def __repr__(self):
        cls_name = self.__class__.__module__ + "." + self.__class__.__qualname__
        return f"<{cls_name} mode={self.mode!r} result={self.result!r}>"

class BattleTeamsListType:
    def __init__(self, data: list):
        """
        Initialize the BattleTeamsListType.

        data: list
            List of dictionaries containing player info from the API
        """
        if data is None:
            data = []
        self.teamsList: List[BattleTeamType] = [BattleTeamType(t) for t in data if t]

    def __repr__(self):
        cls_name = self.__class__.__module__ + "." + self.__class__.__qualname__
        return f"<{cls_name} mode={self.mode!r} result={self.result!r}>"