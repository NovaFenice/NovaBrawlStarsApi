from .brawlerBattleType import BrawlerBattleType

class StarPlayerType:
    tag: str
    name: str
    brawler: BrawlerBattleType

    """
    Initialize the StarPlayerType.

    data: dict
        Dictionary containing star player info from the API
        Expected keys: 'tag', 'name', 'brawler'
    """
    def __init__(self, data: dict) -> None: ...