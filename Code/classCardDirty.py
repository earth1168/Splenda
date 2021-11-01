# Written by Walan 1057
# This script contains 2 classes:
#   - bonusCard
#   - Card

from typing import Dict, List, Tuple
from classButtonDirty import ButtonDirty

# BonusCard class:
# create bonus card object
# inherit from Button class
#  attributes:
#   - card_id: int -- id of bonus card
#   - point: int -- point of bonus card
#   - card_size: Tuple[width, height] -- size of bonus card
#   - img_path: text -- path of bonus card's image
#   - status: test -- status of bonus card
#                       - 'in_deck', 'on_board', 'taken'
#   - player_id: int -- id of player who take this bonus card
#   - requirements: Dict[color name, int] -- number of card required to get this bonus card
#   - position: Tuple[x, y] -- position of bonus card
class BonusCardDirty(ButtonDirty):
    def __init__(self, 
                card_id: int, 
                point: int, 
                card_size: Tuple[int, int],
                img_path: str):
        super().__init__((0, 0), card_size, '', 30, img_path)       
        self.card_id = card_id
        self.point = point
        self.image_path = img_path
        self.status = 'in_deck'
        self.player_id = -1
        self._layer = 2
        self.requirements = {
            "white": 0,
            "blue": 0,
            "green": 0,
            "red": 0,
            "black": 0
        }

    # set requirements of bonus card
    def set_req(self, req_list: List[int]):
        i = 0
        for colors in self.requirements.keys():
            self.requirements[colors] = req_list[i]
            i+=1

    # check if player can take this bonus card
    def check_req(self, p_cards: Dict[str, int]) -> bool:
        is_enough = True
        for colors in self.requirements.keys():
            if p_cards[colors] < self.requirements[colors]:
                is_enough = False
            if not is_enough:
                return is_enough
        return is_enough
       


# Card class:
# create card object
# inherit from BonusCard class
#  attributes:
#   - card_id: int -- id of card
#   - point: int -- point of card
#   - card_size: Tuple[width, height] -- size of card
#   - img_path: text -- path of card's image
#   - colors: text -- color of this card
#   - status: test -- status of card
#                       - 'in_deck', 'on_board', 'taken'
#   - player_id: int -- id of player who take this card
#   - requirements: Dict[color name, int] -- number of card required to get this card
#   - position: Tuple[x, y] -- position of card
class CardDirty(BonusCardDirty):
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

    # check if player can take this card
    def check_req(self, p_tokens: Dict[str, int], p_cards: Dict[str, int]) -> bool:
        is_enough = True
        remain_gold = p_tokens['gold']
        for colors in self.requirements.keys():
            if p_tokens[colors] + p_cards[colors] < self.requirements[colors]:                
                if remain_gold <= 0:
                    is_enough = False
                else:
                    remain_gold = (p_tokens[colors] + p_cards[colors] + remain_gold) - self.requirements[colors]
                if not is_enough:
                    return is_enough            
        if remain_gold < 0:
            is_enough = False
        return is_enough

    # reduce tokens that are required in this card from player
    # return: Dictionary of tokens that reduce from player
    def pay_tokens(self, p_tokens: Dict[str, int], p_cards: Dict[str, int]):
        paid_tokens = {
            "white": 0,
            "blue": 0,
            "green": 0,
            "red": 0,
            "black": 0
        }
        for colors in self.requirements.keys():
            print(f'tokens: {p_tokens}')
            col_diff = self.requirements[colors] - p_cards[colors]
            if col_diff > 0:
                p_tokens[colors] = p_tokens[colors] - col_diff
                paid_tokens.update({colors: col_diff})
                if p_tokens[colors] < 0:
                    p_tokens['gold'] = p_tokens['gold'] + p_tokens[colors]
                    paid_tokens[colors] += p_tokens[colors]
                    p_tokens[colors] = 0
        return paid_tokens
                          
        