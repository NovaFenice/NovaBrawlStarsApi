class PlayerIconType:
    def __init__(self, data: dict):
        """
        Initialize the PlayerIconType.

        data: dict
            Dictionary containing club info from the API
            Expected key: 'id'
        """

        self.id: int = data["id"]
        self.iconUrl: str = f"https://cdn.brawlify.com/profile-icons/regular/{self.id}.png"

    def __repr__(self):
        return f"<PlayerIcon id={self.id} iconUrl={self.iconUrl}>"
    
    def __str__(self):
        return f"PlayerIcon: {self.id} ({self.iconUrl})"