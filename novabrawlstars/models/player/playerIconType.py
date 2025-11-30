class PlayerIconType:
    def __init__(self, data: dict):
        """
        Initialize the PlayerIconType.

        data: dict
            Dictionary containing club info from the API
            Expected key: 'id'
        """
        if data is None:
            data = {}
        self.id: int = data.get("id", "")
        self.iconUrl: str = f"https://cdn.brawlify.com/profile-icons/regular/{self.id}.png"