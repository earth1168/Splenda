from typing import Dict, List, Tuple
from classToken import Token
from classNobleCardDirty import NobleCardDirty

""" 
    CardDirty class:
    An object for development cards use in the game.
    inherit from NobleCardDirty class
    
    Argument:
      * card_id     -- Card's ID
      * point       -- Card's point
      * card_size   -- Card's size
      * img_path    -- Path of card image
      * level       -- Card's level
      * colors      -- Card's color
    * -> that argument is also an attribute.
# """
class CardDirty(NobleCardDirty):
    def __init__(self, 
                card_id: int, 
                point: int, 
                card_size: Tuple[int, int],
                img_path: str, 
                level: int,
                colors: str):
        super().__init__(card_id, point, card_size, img_path)
        self.level = level
        self.colors = colors

    # Check if player can take this noble card
    # Argument:
    #   p_tokens     -- Dictionary of Token objects. Show number of earch color token that player has
    #   p_cards     -- Dictionary of Token objects. Show number of earch color card that player has
    # Return:
    #   boolean value
    def check_req(self, p_tokens: Dict[str, Token], p_cards: Dict[str, Token]) -> bool:
        is_enough = True
        remain_gold = p_tokens['gold'].qty
        for colors in self.requirements.keys():
            if p_tokens[colors].qty + p_cards[colors].qty < self.requirements[colors]:                
                if remain_gold <= 0:
                    is_enough = False
                else:
                    remain_gold = (p_tokens[colors].qty + p_cards[colors].qty + remain_gold) - self.requirements[colors]
                if not is_enough:
                    return is_enough            
        if remain_gold < 0:
            is_enough = False
        return is_enough

    # Reduce tokens that are required in this card from player
    # Argument:
    #   p_tokens     -- Dictionary of Token objects. Show number of earch color token that player has
    #   p_cards     -- Dictionary of Token objects. Show number of earch color card that player has
    # Return: 
    #   Dictionary of tokens that reduce from player
    def pay_tokens(self, p_tokens: Dict[str, Token], p_cards: Dict[str, Token]):
        paid_tokens = {
            "white": 0,
            "blue": 0,
            "green": 0,
            "red": 0,
            "black": 0,
            "gold": 0
        }
        for colors in self.requirements.keys():
            col_diff = self.requirements[colors] - p_cards[colors].qty
            if col_diff > 0:
                p_tokens[colors].qty = p_tokens[colors].qty - col_diff
                paid_tokens[colors] = col_diff
                if p_tokens[colors].qty < 0:
                    p_tokens['gold'].qty = p_tokens['gold'].qty + p_tokens[colors].qty
                    paid_tokens['gold'] -= p_tokens[colors].qty
                    paid_tokens[colors] += p_tokens[colors].qty
                    p_tokens[colors].qty = 0
        return paid_tokens
                          
        