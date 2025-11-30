from .playerClubType import PlayerClubType
from .playerIconType import PlayerIconType
from .brawlerStatsType import BrawlerStatsListType

class Player:
    def __init__(self, data: dict):
        """
        Initialize the Player.

        data: dict
            Dictionary containing player info from the API
            Expected keys: 'tag', 'name', 'nameColor', 'trophies', 'highestTrophies',
                           'soloVictories', 'duoVictories', '3vs3Victories', 'bestRoboRumbleTime',
                           'bestTimeAsBigBrawler', 'expLevel', 'expPoints', 'isQualifiedFromChampionshipChallenge',
                           'club', 'icon', 'brawlerStats'
        """
        if data is None:
            data = {}

        self.tag: str = data.get("tag", "")
        self.name: str = data.get("name", "")
        self.nameColor: str = data.get("nameColor", "")
        self.trophies: int = data.get("trophies", 0)
        self.highestTrophies: int = data.get("highestTrophies", 0)

        self.soloVictories: int = data.get("soloVictories", 0)
        self.duoVictories: int = data.get("duoVictories", 0)
        self.threeVsThreeVictories: int = data.get("3vs3Victories", 0)
        self.bestRoboRumbleTime: int = data.get("bestRoboRumbleTime", 0)
        self.bestTimeAsBigBrawler: int = data.get("bestTimeAsBigBrawler", 0)

        self.expLevel: int = data.get("expLevel", 0)
        self.expPoints: int = data.get("expPoints", 0)

        self.isQualifiedFromChampionshipChallenge: bool = data.get("isQualifiedFromChampionshipChallenge", False)

        club_data = data.get("club", {})
        self.club: PlayerClubType = PlayerClubType(club_data)

        icon_data = data.get("icon", {})
        self.icon: PlayerIconType = PlayerIconType(icon_data)

        brawlers_data = data.get("brawlers", [])
        self.brawlers: BrawlerStatsListType = BrawlerStatsListType(brawlers_data)

    def __repr__(self):
        cls_name = self.__class__.__module__ + "." + self.__class__.__qualname__
        return f"<{cls_name} id={self.id} mode={self.mode!r} map={self.map!r}>"