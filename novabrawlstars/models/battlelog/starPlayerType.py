from .brawlerBattleType import BrawlerBattleType

class StarPlayerType:
    def __init__(self, data: dict):
        """
        Initialize the StarPlayerType.

        data: dict
            Dictionary containing star player info from the API
            Expected keys: 'tag', 'name', 'brawler'
        """
        if data is None:
            data = {}

        self.tag: str = data.get("tag", "")
        self.name: str = data.get("name", "")
        self.brawler: BrawlerBattleType = BrawlerBattleType(data.get("brawler", {}))

    def __repr__(self):
        cls_name = self.__class__.__module__ + "." + self.__class__.__qualname__
        return f"<{cls_name} mode={self.mode!r} result={self.result!r}>"