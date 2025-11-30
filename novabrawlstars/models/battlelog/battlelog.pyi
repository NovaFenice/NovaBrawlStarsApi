from .battleEventType import BattleEventType
from .battleResultType import BattleResultType
from typing import List

class BattleLogType:
    battleTime: str
    event: BattleEventType
    battle: BattleResultType
    
    """
    Initialize the BattleLogType.

    data: dict
        Dictionary containing battle info from the API
        Expected keys: 'battleTime', 'event', 'battle'
    """
    def __init__(self, data: dict) -> None: ...

class BattleLogListType:
    battlesLogList: List[BattleLogType]

    """
    Initialize the BattleLogListType.

    data: dict
        Dictionary containing battle info from the API
        Expected keys: 'items'
    """
    def __init__(self, data: dict) -> None: ...