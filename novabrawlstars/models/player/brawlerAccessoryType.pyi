class BrawlerAccessoryType:
    """
    Initialize the BrawlerAccessoryType.

    data: dict
        Dictionary containing accessory info from the API
        Expected keys: 'name', 'id'
    """

    name: str
    id: int
    iconUrl: str

    def __init__(self, data: dict) -> None: ...