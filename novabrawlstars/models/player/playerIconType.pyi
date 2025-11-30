class PlayerIconType:
    id: int
    iconUrl: str

    """
    Initialize the PlayerIconType.

    data: dict
        Dictionary containing club info from the API
        Expected key: 'id'
    """

    def __init__(self, data: dict) -> None: ...