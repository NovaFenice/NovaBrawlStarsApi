from .playerClubType import PlayerClubType
from .playerIconType import PlayerIconType
from .brawlerStatsType import BrawlerStatsListType

class Player:
    tag: str
    name: str
    nameColor: str
    trophies: int
    highestTrophies: int
    soloVictories: int
    duoVictories: int
    threeVsThreeVictories: int
    bestRoboRumbleTime: int
    bestTimeAsBigBrawler: int
    expLevel: int
    expPoints: int
    isQualifiedFromChampionshipChallenge: bool
    club: PlayerClubType
    icon: PlayerIconType
    brawlerStats: BrawlerStatsListType
    """
    Initialize the Player.

    data: dict
        Dictionary containing player info from the API
        Expected keys: 'tag', 'name', 'nameColor', 'trophies', 'highestTrophies',
                        'soloVictories', 'duoVictories', '3vs3Victories', 'bestRoboRumbleTime',
                        'bestTimeAsBigBrawler', 'expLevel', 'expPoints', 'isQualifiedFromChampionshipChallenge',
                        'club', 'icon', 'brawlerStats'
    """
    def __init__(self, data: dict) -> None: ...