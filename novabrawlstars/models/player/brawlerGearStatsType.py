class BrawlerGearStatsType:
    def __init__(self, data: dict):
        """
        Initialize the BrawlerGearStatsType.

        data: dict
            Dictionary containing gear stats info from the API
            Expected keys: 'name', 'id'
        """
        if data is None:
            data = {}

        self.name: str = data.get("name", "")
        self.id: int = data.get("id", 0)
        self.iconUrl: str = f"https://cdn.brawlify.com/gears/regular/{self.id}.png" if self.id != 0 else ""