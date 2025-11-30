class PlayerClubType:
    def __init__(self, data: dict):
        """
        Initialize the PlayerClub.

        data: dict
            Dictionary containing club info from the API
            Expected keys: 'tag' and 'name'
        """
        if data is None:
            data = {}
        self.tag: str = data.get("tag", "")
        self.name: str = data.get("name", "")

    def __repr__(self):
        cls_name = self.__class__.__module__ + "." + self.__class__.__qualname__
        return f"<{cls_name} id={self.id} mode={self.mode!r} map={self.map!r}>"