class PlayerClubType:
    tag: str
    name: str

    """
    Initialize the PlayerClub.

    data: dict
        Dictionary containing club info from the API
        Expected keys: 'tag' and 'name'
    """
    def __init__(self, data: dict) -> None: ...