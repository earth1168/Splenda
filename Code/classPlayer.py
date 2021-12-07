from classToken import Token

'''
    Player class:
    An object for keep information about player.

    Argument:
      * id        -- Player's ID
      * chr_id    -- ID odf character selected by player
      * name      -- Player's name
    * -> that argument is also an attribute.

    Attributes:
        score       -- Player's score
        card_qty    -- Quantity of a player's owned cards
        hold_cards  -- List of CardDirty objects that player's holding
        tokens      -- Dictionary of Token objects. Show number of earch color token that player currently keeps
        cards       -- Dictionary of Token objects. Show number of earch color card that player has
'''
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
        self.tokens = {
            "white": Token((520, 60), (50, 50), 'Image\Coin\whiteCoin-01.png', "white", 0),
            "blue": Token((600, 60), (50, 50), 'Image\Coin\\blueCoin-01.png', "blue", 0),
            "green": Token((680, 60), (50, 50), 'Image\Coin\greenCoin-01.png', "green", 0),
            "red": Token((760, 60), (50, 50), 'Image\Coin\\redCoin-01.png', "red", 0),
            "black": Token((840, 60), (50, 50), 'Image\Coin\\blackCoin-01.png', "black", 0),
            "gold": Token((440, 60), (50, 50), 'Image\Coin\goldCoin-01.png', "gold", 0)
        }  
        self.cards = {
            "white": Token((520, 130), (50, 70), 'Image\Card\whiteBG.png', "white", 0),
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

    # Reposition playr's tokens
    # Argument:
    #   pos_x       -- new position on x axis
    #   pos_y       -- new position on y axis
    #   distance    -- distance between each token
    def repos_tokens(self, pos_x, pos_y, distance=0):
        self.tokens['gold'].reposition(pos_x, pos_y)
        for i, token in enumerate(self.tokens.values(), start=1):
            if i > 5:
                break
            token.reposition(pos_x+((50+distance)*i), pos_y)

    # Reposition playr's cards
    # Argument:
    #   pos_x       -- new position on x axis
    #   pos_y       -- new position on y axis
    #   distance    -- distance between each card
    def repos_cards(self, pos_x, pos_y, distance=0):
        self.cards['hold'].reposition(pos_x, pos_y)
        for i, card in enumerate(self.cards.values(), start=1):
            if i > 5:
                break
            card.reposition(pos_x+((50+distance)*i), pos_y)

    # Check if player is holding any card now
    # Return:
    #   boolean value
    def is_hold_card(self):
        if not self.hold_cards:
            return False
        else:
            return True
    
    # Sum quantity of each color card that player has
    # Return:
    #   quantity of all cards that player has
    def sum_card(self):
        for card in self.cards.values():
            self.card_qty += card.qty
        return self.card_qty