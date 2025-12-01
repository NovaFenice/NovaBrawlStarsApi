from .clubMember import ClubMemberList

class Club:
    """
    Class representing a club
    """
    def __init__(self, data: dict):
        """
        Initialize the Club.

        data: dict
            Dictionary containing club info from the API
            Expected keys: 'tag', 'name', description', 'trophies', 'requiredTrophies',
                           'members', 'type', 'badgeId'
        """

        if data is None:
            data = {}

        self.tag: str = data.get("tag", "")
        self.name: str = data.get("name", "")
        self.description: str = data.get("description", "")
        self.trophies: int = data.get("trophies", 0)
        self.requiredTrophies: int = data.get("requiredTrophies", 0)
        self.members: ClubMemberList = ClubMemberList(data.get("members", []))
        self.type: str = data.get("type", "")
        self.badgeId: int = data.get("badgeId", 0)