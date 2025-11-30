class BrawlerAccessoryType:
    def __init__(self, data: dict):
        self.name: str = data["name"]
        self.id: int = data["id"]
        self.iconUrl: str = f"https://cdn.brawlify.com/gadgets/borderless/{self.id}.png"

    def __repr__(self):
        return f"<BrawlerAccessory name={self.name} id={self.id}>"
    
    def __str__(self):
        return f"BrawlerAccessory: {self.name} ({self.id}) ({self.iconUrl})"