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

    def __repr__(self):
        cls_name = self.__class__.__module__ + "." + self.__class__.__qualname__
        return f"<{cls_name} id={self.id} mode={self.mode!r} map={self.map!r}>"