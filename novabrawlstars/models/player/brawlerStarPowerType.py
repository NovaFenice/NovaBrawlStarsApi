class BrawlerStarPowerType:
    def __init__(self, data: dict):
        """
        Initialize the BrawlerStarPowerType.

        data: dict
            Dictionary containing star power info from the API
            Expected keys: 'name', 'id'
        """
        if data is None:
            data = {}

        self.name: str = data.get("name", "")
        self.id: int = data.get("id", 0)
        self.iconUrl: str = f"https://cdn.brawlify.com/star-powers/borderless/{self.id}.png" if self.id != 0 else ""

    def __repr__(self):
        cls_name = self.__class__.__module__ + "." + self.__class__.__qualname__
        return f"<{cls_name} id={self.id} mode={self.mode!r} map={self.map!r}>"