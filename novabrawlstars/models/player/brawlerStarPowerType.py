class BrawlerStarPowerType:
    def __init__(self, data: dict):
        self.name: str = data["name"]
        self.id: int = data["id"]
        self.iconUrl: str = f"https://cdn.brawlify.com/star-powers/borderless/{self.id}.png"

    def __repr__(self):
        return f"<BrawlerStarPower name={self.name} id={self.id}>"
    
    def __str__(self):
        return f"BrawlerStarPower: {self.name} ({self.id}) ({self.iconUrl})"