class BrawlerGearStatsType:
    name: str
    id: int
    iconUrl: str
    """
    Initialize the BrawlerGearStatsType.

    data: dict
        Dictionary containing gear stats info from the API
        Expected keys: 'name', 'id'
    """
    def __init__(self, data: dict) -> None: ...