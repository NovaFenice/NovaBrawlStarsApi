class BrawlerGearStatsType:
    def __init__(self, data: dict):
        self.name: str = data["name"]
        self.id: int = data["id"]
        self.iconUrl: str = f"https://cdn.brawlify.com/gears/regular/{self.id}.png"

    def __repr__(self):
        return f"<BrawlerGearStat name={self.name} id={self.id}>"
    
    def __str__(self):
        return f"BrawlerGearStat: {self.name} ({self.id}) ({self.iconUrl})"