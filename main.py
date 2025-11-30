from novabrawlstars import NovaBrawlStars
import os
from dotenv import load_dotenv

load_dotenv()

api_bs = os.getenv("api_bs") # Your Brawl Stars API token
tag_p1 = os.getenv("tag_p1") # Brawl Stars Player tag (es. #12345678 or 12345678)
tag_p2 = os.getenv("tag_p2") # Brawl Stars Player tag (es. #12345678 or 12345678)

nb = NovaBrawlStars(api_bs) # Initialize the Brawl Stars API client

player_1 = nb.get_player(tag_p1) # Get a Player object from the API
player_2 = nb.get_player(tag_p2) # Get a Player object from the API

print(player_1)
print(player_2)