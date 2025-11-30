from .battleEventType import BattleEventType
from .battleResultType import BattleResultType
from typing import List

class BattleLogType:
    def __init__(self, data: dict):
        """
        Initialize the BattleLogType.

        data: dict
            Dictionary containing battle info from the API
            Expected keys: 'battleTime', 'event', 'battle'
        """
        if data is None:
            data = {}
        self.battleTime: str = data.get("battleTime", "")
        self.event: BattleEventType = BattleEventType(data.get("event", {}))
        self.battle: BattleResultType = BattleResultType(data.get("battle", {}))

    def __repr__(self):
        cls_name = self.__class__.__module__ + "." + self.__class__.__qualname__
        return f"<{cls_name} battleTime={self.battleTime!r}>"

class BattleLogListType:
    def __init__(self, data: dict):
        """
        Initialize the BattleLogListType.

        data: dict
            Dictionary containing battle info from the API
            Expected keys: 'items'
        """
        if data is None:
            data = {}
        self.battlesLogList: List[BattleLogType] = [BattleLogType(b) for b in data.get("items", []) if b]

    def __repr__(self):
        cls_name = self.__class__.__module__ + "." + self.__class__.__qualname__
        return f"<{cls_name} battles={len(self.battlesLogList)}>"