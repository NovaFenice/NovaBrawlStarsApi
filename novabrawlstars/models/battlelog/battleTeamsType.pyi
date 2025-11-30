from typing import List
from .brawlerBattleType import BrawlerBattleType

class BattlePlayerType:
    tag: str
    name: str
    brawler: BrawlerBattleType

    """
    Initialize the BattlePlayerType.

    data: dict
        Dictionary containing player info from the API
        Expected keys: 'tag', 'name', 'brawler'
    """
    def __init__(self, data: dict) -> None: ...

class BattleTeamType:
    players: List[BattlePlayerType]

    """
    Initialize the BattleTeamType.

    data: list
        List of dictionaries containing player info from the API
    """
    def __init__(self, data: list) -> None: ...

class BattleTeamsListType:
    teamsList: List[BattleTeamType]

    """
    Initialize the BattleTeamsListType.

    data: list
        List of dictionaries containing player info from the API
    """
    def __init__(self, data: list) -> None: ...