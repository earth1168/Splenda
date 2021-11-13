# Written by Walan 1057
# This script contains 1 class:
#   - Player

from classToken import Token

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
        self.card_qty = 0
        self.hold_cards = []
        # self.tokens = {
        #     "white": 0,
        #     "blue": 0,
        #     "green": 0,
        #     "red": 0,
        #     "black": 0,
        #     "gold": 0
        # }
        self.tokens = {
            "white": Token((520, 60), (50, 50), 'Image\Coin\whiteCoin-01.png', "white", 0),
            "blue": Token((600, 60), (50, 50), 'Image\Coin\\blueCoin-01.png', "blue", 0),
            "green": Token((680, 60), (50, 50), 'Image\Coin\greenCoin-01.png', "green", 0),
            "red": Token((760, 60), (50, 50), 'Image\Coin\\redCoin-01.png', "red", 0),
            "black": Token((840, 60), (50, 50), 'Image\Coin\\blackCoin-01.png', "black", 0),
            "gold": Token((440, 60), (50, 50), 'Image\Coin\goldCoin-01.png', "gold", 0)
        }
        # self.cards = {
        #     "white": 0,
        #     "blue": 0,
        #     "green": 0,
        #     "red": 0,
        #     "black": 0
        # }  
        self.cards = {
            "white": Token((520, 130), (50, 70), 'Image\Card\yellowBG.png', "white", 0),
            "blue": Token((600, 130), (50, 70), 'Image\Card\\blueBG.png', "blue", 0),
            "green": Token((680, 130), (50, 70), 'Image\Card\greenBG.png', "green", 0),
            "red": Token((760, 130), (50, 70), 'Image\Card\\redBG.png', "red", 0),
            "black": Token((840, 130), (50, 70), 'Image\Card\\blackBG.png', "black", 0),
            "hold": Token((440, 130), (50, 70), 'Image\Card\HoldCard.png', "hold", 0, 'white')
        }

        for token in self.tokens.values():
            token.visible = 0  

        for card in self.cards.values():
            card._layer = 0
            card.visible = 0          

    # reposition tokens
    def repos_tokens(self, pos_x, pos_y, distance=0):
        self.tokens['gold'].reposition(pos_x, pos_y)
        for i, token in enumerate(self.tokens.values(), start=1):
            if i > 5:
                break
            token.reposition(pos_x+((50+distance)*i), pos_y)

    def repos_cards(self, pos_x, pos_y, distance=0):
        self.cards['hold'].reposition(pos_x, pos_y)
        for i, card in enumerate(self.cards.values(), start=1):
            if i > 5:
                break
            card.reposition(pos_x+((50+distance)*i), pos_y)

    def is_hold_card(self):
        if not self.hold_cards:
            return False
        else:
            return True
        
    def sum_card(self):
        for card in self.cards.values():
            self.card_qty += card.qty
        return self.card_qty