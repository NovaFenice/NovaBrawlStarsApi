class BrawlerBattleType:
    id: int
    name: str
    iconBrawlerUrl: str
    power: int
    trophies: int
    
    """
    Initialize the BrawlerBattleType.

    data: dict
        Dictionary containing brawler info from the API
        Expected keys: 'id', 'name', 'power', 'trophies'
    """
    def __init__(self, data: dict) -> None: ...