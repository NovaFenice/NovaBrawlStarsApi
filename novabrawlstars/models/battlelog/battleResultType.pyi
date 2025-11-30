from .starPlayerType import StarPlayerType
from .battleTeamsType import BattleTeamsListType

class BattleResultType:
    mode: str
    type: str
    result: str
    duration: int
    trophyChange: int
    rank: int
    starPlayer: StarPlayerType
    teams: BattleTeamsListType

    """
    Initialize the BattleResultType.

    data: dict
        Dictionary containing battle info from the API
        Expected keys: 'mode', 'type', 'result', 'duration', 'trophyChange', 'starPlayer', 'teams', 'rank'
    """
    def __init__(self, data: dict) -> None: ...