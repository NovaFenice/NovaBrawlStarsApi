from .playerClubType import PlayerClubType
from .playerIconType import PlayerIconType
from .brawlerStatsType import BrawlerStatsListType

class Player:
    def __init__(self, data: dict):
        self.tag: str = data["tag"]
        self.name: str = data["name"]
        self.nameColor: str = data["nameColor"]
        self.trophies: int = data["trophies"]
        self.highestTrophies: int = data["highestTrophies"]

        self.soloVictories: int = data["soloVictories"]
        self.duoVictories: int = data["duoVictories"]
        self.threeVsThreeVictories: int = data["3vs3Victories"]
        self.bestRoboRumbleTime: int = data["bestRoboRumbleTime"]
        self.bestTimeAsBigBrawler: int = data["bestTimeAsBigBrawler"]

        self.expLevel: int = data["expLevel"]
        self.expPoints: int = data["expPoints"]

        self.isQualifiedFromChampionshipChallenge: bool = data["isQualifiedFromChampionshipChallenge"]

        club_data = data["club"]
        self.club: PlayerClubType | None = PlayerClubType(club_data) if club_data else None

        icon_data = data["icon"]
        self.icon: PlayerIconType | None = PlayerIconType(icon_data) if icon_data else None

        brawlers_data = data.get("brawlers", [])
        self.brawlers: BrawlerStatsListType = BrawlerStatsListType(brawlers_data)

    def __repr__(self):
        return f"<Player name={self.name} tag={self.tag}>"
    
    def __str__(self):
        """
        Pretty printing player.
        """
        if self.club is None:
            club_str = "{}"
        else:
            club_str = (
                "{\n"
                f"    tag: {self.club.tag},\n"
                f"    name: {self.club.name}\n"
                "}"
            )

        if self.icon is None:
            player_icon_str = "{}"
        else:
            player_icon_str = (
                "{\n"
                f"    id: {self.icon.id},\n"
                f"    iconUrl: {self.icon.iconUrl}\n"
                "}"
            )

        brawlers_str = "\n".join([f"    {brawler.name} (Trophies: {brawler.trophies})" for brawler in self.brawlers.brawlers])

        return (
            f"Name: {self.name}\n"
            f"Tag: {self.tag}\n"
            f"NameColor: {self.nameColor}\n"
            f"PlayerIcon: {player_icon_str} \n"
            f"Club: {club_str}\n"
            f"Trophies: {self.trophies}\n"
            f"HighestTrophies: {self.highestTrophies}\n"
            f"SoloVictories: {self.soloVictories}\n"
            f"DuoVictories: {self.duoVictories}\n"
            f"3vs3Victories: {self.threeVsThreeVictories}\n"
            f"BestRoboRumbleTime: {self.bestRoboRumbleTime}\n"
            f"BestTimeAsBigBrawler: {self.bestTimeAsBigBrawler}\n"
            f"ExpLevel: {self.expLevel}\n"
            f"ExpPoints: {self.expPoints}\n"
            f"IsQualifiedFromChampionshipChallenge: {self.isQualifiedFromChampionshipChallenge}\n"
            f"Brawlers:\n{brawlers_str}\n"
        )