from .starPlayerType import StarPlayerType
from .battleTeamsType import BattleTeamsListType

class BattleResultType:
    def __init__(self, data: dict):
        """
        Initialize the BattleResultType.

        data: dict
            Dictionary containing battle info from the API
            Expected keys: 'mode', 'type', 'result', 'duration', 'trophyChange', 'starPlayer', 'teams', 'rank'
        """
        if data is None:
            data = {}

        self.mode: str = data.get("mode", "")
        self.type: str = data.get("type", "")
        self.result: str = data.get("result", "")
        self.duration: int = data.get("duration", 0)
        self.trophyChange: int = data.get("trophyChange", 0)
        self.rank: int = data.get("rank", 0)
        self.starPlayer: StarPlayerType = StarPlayerType(data.get("starPlayer", {}))
        self.teams: BattleTeamsListType = BattleTeamsListType(data.get("teams", []))