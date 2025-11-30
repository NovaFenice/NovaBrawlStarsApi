class BattleEventType:
    id: int
    mode: str
    modeId: int
    modeIconUrl: str
    map: str
    mapIconUrl: str
    
    """
    Initialize the BattleEventType.

    data: dict
        Dictionary containing battle info from the API
        Expected keys: 'id', 'mode', 'modeId', 'modeIconUrl', 'map', 'mapIconUrl'
    """
    def __init__(self, data: dict) -> None: ...