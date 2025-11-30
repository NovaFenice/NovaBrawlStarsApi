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