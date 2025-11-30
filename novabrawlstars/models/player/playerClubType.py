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
        return f"<PlayerClub name={self.name} tag={self.tag}>"
    
    def __str__(self):
        return f"Club: {self.name} ({self.tag})"