from typing import Dict, List, Tuple
from classToken import Token
from classButtonDirty import ButtonDirty

'''
    NobleCardDirty class:
    An object for noble cards use in the game.
    inherit from ButtonDirty class.

    Argument:
      * card_id     -- Card's ID
      * point       -- Card's point
      * card_size   -- Card's size
      * img_path    -- Path of card image
    * -> that argument is also an attribute.

    Attributes:   
        player_id       -- ID of player who take this noble card
        requirements    -- Dictionary of number of cards (or tokens in CardDirty case) required to get this card
'''

class NobleCardDirty(ButtonDirty):
    def __init__(self, 
                card_id: int, 
                point: int, 
                card_size: Tuple[int, int],
                img_path: str):
        super().__init__((0, 0), card_size, '', 30, img_path)       
        self.card_id = card_id
        self.point = point
        self.img_path = img_path
        self.player_id = -1
        self._layer = 1
        self.requirements = {
            "white": 0,
            "blue": 0,
            "green": 0,
            "red": 0,
            "black": 0
        }

    # Check if player can take this noble card
    # Argument:
    #   p_cards     -- Dictionary of Token objects. Show number of earch color card that player has
    # Return:
    #   boolean value
    def check_req(self, p_cards: Dict[str, Token]) -> bool:
        is_enough = True
        for colors in self.requirements.keys():
            if p_cards[colors].qty < self.requirements[colors]:
                is_enough = False
            if not is_enough:
                return is_enough
        return is_enough