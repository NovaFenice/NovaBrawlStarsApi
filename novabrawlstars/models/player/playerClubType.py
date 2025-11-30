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