class BattleEventType:
    def __init__(self, data: dict):
        """
        Initialize the BattleEventType.

        data: dict
            Dictionary containing battle info from the API
            Expected keys: 'id', 'mode', 'modeId', 'modeIconUrl', 'map', 'mapIconUrl'
        """
        if data is None:
            data = {}

        self.id: int = data.get("id", 0)
        self.mode: str = data.get("mode", "")
        self.modeId: int = data.get("modeId", 0)
        self.modeIconUrl: str = f"https://cdn.brawlify.com/game-modes/regular/{48_000_000 + self.modeId}.png" if self.modeId != 0 else ""
        self.map: str = data.get("map", "")
        self.mapIconUrl: str = f"https://cdn.brawlify.com/maps/regular/{self.id}.png"