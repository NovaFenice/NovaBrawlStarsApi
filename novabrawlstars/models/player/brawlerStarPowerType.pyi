class BrawlerStarPowerType:
    name: str
    id: int
    iconUrl: str
    """
    Initialize the BrawlerStarPowerType.

    data: dict
        Dictionary containing star power info from the API
        Expected keys: 'name', 'id'
    """
    def __init__(self, data: dict) -> None: ...