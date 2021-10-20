# Written by Walan 1057
# This script contains 1 class:
#   - Player

# Player class:
# create button object with customizable background, size, and text
# inherit from Sprite class in pygame
#  attributes:
#   - card_id: int -- id of player
#   - chr_id: int -- id of character selected by this player
#   - name: text -- name of player
#   - score: int -- score of player
#   - tokens: Dict[color name, int] -- tokens this player has
#   - cards: Dict[color name, int] -- cards this player own
class Player():
    def __init__(self, 
                id: int, 
                chr_id: int, 
                name: str):
        self.id = id
        self.chr_id = chr_id
        self.name = name
        self.score = 0
        self.tokens = {
            "white": 0,
            "blue": 0,
            "green": 0,
            "red": 0,
            "black": 0,
            "gold": 0
        }
        self.cards = {
            "white": 0,
            "blue": 0,
            "green": 0,
            "red": 0,
            "black": 0
        }
