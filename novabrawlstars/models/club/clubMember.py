from ..player.playerIconType import PlayerIconType
from typing import List

class ClubMember:
    """
    Class representing a member of a club
    """
    def __init__(self, data: dict):
        """
        Initialize the ClubMember.

        data: dict
            Dictionary containing player info from the API
            Expected keys: 'icon', 'tag', 'name', 'trophies', 'role', 'nameColor'
        """

        if data is None:
            data = {}

        self.icon: PlayerIconType = PlayerIconType(data.get("icon", {}))
        self.tag: str = data.get("tag", "")
        self.name: str = data.get("name", "")
        self.trophies: int = data.get("trophies", 0)
        self.role: str = data.get("role", "")
        self.nameColor: str = data.get("nameColor", "")

class ClubMemberList:
    """
    Class representing a list of members of a club
    """
    def __init__(self, data: List[dict]):
        """
        Initialize the ClubMemberList.

        data: List[dict]
            List of dictionaries containing player info from the API
            Expected keys: 'icon', 'tag', 'name', 'trophies', 'role', 'nameColor'
        """
        
        self.clubMemberList: List[ClubMember] = [ClubMember(m) for m in data if m]