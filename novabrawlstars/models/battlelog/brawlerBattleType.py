class BrawlerBattleType:
    def __init__(self, data: dict):
        """
        Initialize the BrawlerBattleType.

        data: dict
            Dictionary containing brawler info from the API
            Expected keys: 'id', 'name', 'power', 'trophies'
        """
        if data is None:
            data = {}

        self.id: int = data.get("id", 0)
        self.name: str = data.get("name", "")
        self.iconBrawlerUrl: str = f"https://cdn.brawlify.com/brawlers/borderless/{self.id}.png" if self.id != 0 else ""
        self.power: int = data.get("power", 0)
        self.trophies: int = data.get("trophies", 0)