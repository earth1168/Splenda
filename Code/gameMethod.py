import pygame
import csv
from typing import List
from classButtonDirty import ButtonDirty
from classCardDirty import CardDirty
from classNobleCardDirty import NobleCardDirty
from classToken import Token
from classPlayer import Player
from classBigCard import BigCard

# read development card data from csv file
# Argument:
#   data_path   -- path of card data csv file
# Return:
#   card_list   -- list of CardDirty objects that read from csv file 
def read_card_data(data_path):
    card_list = [[], [], []]
    with open(data_path, mode='r') as data_file:
        data_reader = csv.DictReader(data_file, delimiter=',')
        for id, row in enumerate(data_reader):
            card = CardDirty(id, int(row['point']), (112, 167), row['image_path'], int(row['level']), row['colors'])
            for colors in card.requirements.keys():
                card.requirements[colors] = int(row[colors])
            card_list[card.level-1].append(card)
    return card_list

# read noble card data from csv file 
# Argument:
#   data_path   -- Path of noble card data csv file
# Return:
#   noble_list  -- list of NobleCardDirty objects that read from csv file 
def read_noble_data(data_path):
    noble_list = []
    with open(data_path, mode='r') as data_file:
        data_reader = csv.DictReader(data_file, delimiter=',')
        for id, row in enumerate(data_reader):
            noble = NobleCardDirty(id, int(row['point']), (122, 122), row['image_path'])
            for colors in noble.requirements.keys():
                noble.requirements[colors] = int(row[colors])
            noble_list.append(noble)
    return noble_list

# Create list of Player object and
# Instantiate player box, selected character, player's name text, and player's score text 
# Argument:
#   name_user   -- list of players' name
#   act_user    -- list of character ID selected by player
# Return:
#   allplayer       -- number of player in the game
#   player_list     -- list of Player objects
#   cha             -- list of selected character sprite
#   bg_player       -- list of background image for each player
#   player_name     -- list of player's name sprite
#   player_score    -- list of player's score sprite
def getPlayerData(name_user: List[str], 
                  act_user: List[int]):
    allplayer = 0
    name_font = pygame.font.Font("Font/Roboto/Roboto-Bold.ttf",20)
    score_font = pygame.font.Font("Font/Roboto/Roboto-Bold.ttf",30)
    player_name = []
    cha = []
    bg_player = []
    player_list = []
    player_score = []    

    for i in range(len(act_user)): 
        player = Player(i, act_user[i], name_user[i]) 
        player.chr_id = act_user[i]               
        if i%2 == 0:
            #player 0,2
            bg_player.append(pygame.image.load('Image/Card/bgEven.png').convert_alpha())
            bg_player[i] = pygame.transform.smoothscale(bg_player[i], (430, 167))            
        else:
            #player 1,3
            bg_player.append(pygame.image.load('Image/Card/bgOdd.png').convert_alpha())
            bg_player[i] = pygame.transform.smoothscale(bg_player[i], (430, 167))
        # character image sprite
        cha_img = pygame.sprite.DirtySprite()
        cha_img.image = pygame.image.load(f'Character/character/character{act_user[i]+1}.png').convert_alpha()
        cha_img.image = pygame.transform.smoothscale(cha_img.image, (108, 108))
        cha_img.rect = cha_img.image.get_rect(bottomleft = (10, 157+(177*i)))
        cha.append(cha_img)
        # player's name sprite
        playerName = pygame.sprite.DirtySprite()
        playerName.image = name_font.render(name_user[i],'AA','White')
        playerName.rect = playerName.image.get_rect(bottomleft = (10, 177+(177*i)))
        player_name.append(playerName)               
        # player's score sprite
        playerScore = pygame.sprite.DirtySprite()        
        playerScore.image = score_font.render(f'{player.score}','AA','White')
        playerScore.rect = playerScore.image.get_rect(bottomleft = (30, 50+(177*i)))
        player_score.append(playerScore)

        player_list.append(player)
        allplayer += 1
    return allplayer, player_list, cha, bg_player, player_name, player_score

# Create token pile and tokens selected by player from Token object
# Argument:
#   allsprites  -- group of Sprite object
#   allplaye    -- number of player in the game
def get_tokens(allsprites, allplayer):
    tok_col = ['white', 'blue', 'green', 'red', 'black']
    # token pile
    for i in range(5):
        tok = Token((494, 184+118*i), (108, 108), 'Image\Coin\\'+tok_col[i]+'Coin-01.png', tok_col[i], 2+int(allplayer*5/4))
        allsprites.add(tok)
    tokGold = Token((494, 66), (108, 108), 'Image\Coin\goldCoin-01.png', 'gold', 5)
    allsprites.add(tokGold)
    allsprites.change_layer(tokGold, 0)
    # selected tokens
    for i in range(5):
        tok_in_pane = Token((614, 184+118*i), (108, 108), 'Image\Coin\\'+tok_col[i]+'Coin-01.png', tok_col[i], 0)
        tok_in_pane.visible = 0
        allsprites.add(tok_in_pane)

# Set development cards on game board
# Argument:
#   card_list   -- list of CardDirty objects
#   allsprites  -- group of Sprite object
#   order       -- list of card order for each level
# Return:
#   card_counter    -- list of card counter for each level
def place_cards(card_list: List[List[CardDirty]], allsprites, order: List[List[int]]):
    card_counter = [0, 0, 0]
    for i in range(3):
        for card_counter[i] in range(4):
            card = card_list[i][order[i][card_counter[i]]]  
            card.reposition(751+132*card_counter[i], 262+((2-i)*177))
            allsprites.add(card)
    return card_counter

# Set noble cards on game board
# Argument:
#   noble_list  -- list of CardDirty objects
#   allsprites  -- group of Sprite object
#   order       -- list of card order
#   btn_list    -- list of button use for select a noble card
def place_nobles(noble_list: List[NobleCardDirty], allsprites, order: List[int], btn_list: List[ButtonDirty]):
    for i, idx in enumerate(order):
        noble = noble_list[idx]
        noble.reposition(619+(132*i), 90)
        btn_list[i].reposition(noble.rect.centerx+25, noble.rect.y+20)
        btn_list[i].visible = 0
        allsprites.add(noble, btn_list[i])
        allsprites.change_layer(btn_list[i], 2)

# Set position for each player's token 
# Argument:
#   player_list -- list of Player objects
#   allsprites  -- group of Sprite object
def place_player_tokens(player_list, allsprites):
    for i, player in enumerate(player_list):
        for token in player.tokens.values():
            player.repos_tokens(138, 50+(177*i))
            allsprites.add(token)

# Set position for each player's card 
# Argument:
#   player_list -- list of Player objects
#   allsprites  -- group of Sprite object
def place_own_cards(player_list, allsprites):
    for i, player in enumerate(player_list):
        for card in player.cards.values():
            player.repos_cards(138, 120+(177*i))
            allsprites.add(card)

# Display the selected token
# Argument:
#   sel_token   -- a token selected by player
#   show_token  -- a token that tell player how many token he has selected 
#   sel_qty     -- number of token that player has choosen
#   can_select  -- boolean that tell if player can select token
# Return:
#   sel_qty     -- number of token that player has choosen
#   can_select  -- boolean that tell if player can select token
def select_token(sel_token: Token, show_token: Token, sel_qty: int, can_select: bool):
    if can_select:
        if sel_token.qty > 0 and sel_qty < 3 and\
             (show_token.qty == 0 or (sel_token.qty >= 3 and sel_qty == 1 and show_token.qty > 0)):
            show_token.visible = 1
            show_token.qty += 1
            sel_token.qty -= 1
            show_token.update_text(f'{show_token.qty}')
            sel_token.update_text(f'{sel_token.qty}')
            sel_qty += 1
            if show_token.qty > 1 or sel_qty == 3:
                can_select = False
    sel_token.show_token()
    return sel_qty, can_select

# Unselect a token and return that token back to token pile
# Argument:
#   token       -- a token selected by player
#   show_token  -- a token that tell player how many token he has selected 
#   sel_qty     -- number of token that player has choosen
#   can_select  -- boolean that tell if player can select token
# Return:
#   sel_qty     -- number of token that player has choosen
#   can_select  -- boolean that tell if player can select token
def get_token_back(token: Token, show_token: Token, sel_qty, can_select):
    token.qty += 1
    show_token.qty -= 1
    sel_qty -= 1
    can_select = True
    token.visible = 1
    show_token.show_token()      
    token.update_text(f'{token.qty}')
    show_token.update_text(f'{show_token.qty}')
    return sel_qty, can_select 

# Cancel all selected tokens and return them back to token pile
# Argument:
#   token_list      -- token pile
#   show_token_list -- list of token selected by player
def cancel_token(token_list: List[Token], show_token_list: List[Token]):
    for i, show_tok in enumerate(show_token_list):
        if show_tok.qty > 0:
            token_list[i].qty += show_tok.qty
            show_tok.qty = 0
            token_list[i].visible = 1
            show_tok.visible = 0       
            token_list[i].update_text(f'{token_list[i].qty}')
            show_tok.update_text(f'{show_tok.qty}') 

# Add selected token to player
# Argument:
#   token_list  -- list of token selected by player
#   player      -- a Player object
def take_tokens(token_list, player: Player):
    for token in token_list:
        player.tokens[token.colors].qty += token.qty
        player.tokens[token.colors].update_text(f'{player.tokens[token.colors].qty}')
        player.tokens[token.colors].show_token()
        token.qty = 0
        token.visible = 0
        token.dirty = 1

# Get a card from draw pile after buy or hold a card
# Argument:
#   card            -- CardDirty object 
#   card_list       -- 
#   card_counter    -- list of card counter for each level
#   order           -- list of card order
# Return:
#   new_card    -- new development card from deck or None if there is no card left
def get_new_card(card: CardDirty, card_list: List[List[CardDirty]], card_counter, order):
    card_counter[card.level-1] += 1
    if card_counter[card.level-1] >= len(card_list[card.level-1]):
        return None
    else:
        order_idx = order[card.level-1][card_counter[card.level-1]]
        new_card = card_list[card.level-1][order_idx]
        new_card.reposition(card.position[0], card.position[1])
        new_card.t_colors = 'black'  
        return new_card

def update_card_qty(card_counter, card_list, card_qty_list, allsprites):
    Deck_font = pygame.font.Font("Font/Roboto/Roboto-Bold.ttf",20)
    for i, c_list in enumerate(card_list):
        remaining = len(c_list) - (card_counter[i]+1)
        card_qty_list[i].image = Deck_font.render(f'{remaining}', True, 'white')
        card_qty_list[i].dirty = 1
        if remaining <= 0:
            empty_card = pygame.sprite.DirtySprite()
            empty_card.image = pygame.image.load('Image\Card\emptyCard.png').convert_alpha()
            empty_card.image = pygame.transform.smoothscale (empty_card.image, (122, 167))
            empty_card.rect = empty_card.image.get_rect(topleft = (558, 179+(177*(2-i))))
            allsprites.add(empty_card)

# reduce player's token and add point to player
def pay_tokens(card: CardDirty, player: Player):
    paid_tokens = card.pay_tokens(player.tokens, player.cards)
    player.score += card.point
    player.cards[card.colors].qty += 1
    player.cards[card.colors].update_text(f'{player.cards[card.colors].qty}')
    player.cards[card.colors].visible = 1
    for token in player.tokens.values():
        token.update_text(f'{token.qty}')
        token.show_token()
    card.kill()
    return paid_tokens

# add card to player's hold card list and give gold token to player
def hold_card(card: CardDirty, player: Player, token_gold: Token):
    player.hold_cards.append(card)
    if player.tokens['gold'].qty < 3 and token_gold.qty > 0:
        player.tokens['gold'].qty += 1
        player.tokens['gold'].update_text(f"{player.tokens['gold'].qty}")
        player.tokens['gold'].show_token()
        token_gold.qty -= 1
        token_gold.update_text(f'{token_gold.qty}')
        token_gold.show_token()
    card.kill()

def check_player_token(player: Player):
    total_token = 0
    for p_token in player.tokens.values():
        total_token += p_token.qty   
    return total_token > 10

def return_token(token_list: List[Token], token_gold: Token, player: Player, m_pos):
    total_token = 0
    for p_token in player.tokens.values():
        total_token += p_token.qty
    if total_token > 10:
        for i, token in enumerate(player.tokens.values()):
            if token.rect.collidepoint(m_pos) and token.qty > 0:
                token.qty -= 1
                token.update_text(f'{token.qty}')
                token.show_token()
                if i < 5:
                    token_list[i].qty += 1                
                    token_list[i].update_text(f'{token_list[i].qty}')                
                    token_list[i].show_token()
                else:
                    token_gold.qty += 1                
                    token_gold.update_text(f'{token_gold.qty}')                
                    token_gold.show_token()
                total_token -= 1
    return total_token

def check_noble(noble_list, noble_order, player):
    available_idx = []  
    for i in range(len(noble_order)):
        noble = noble_list[noble_order[i]]
        if noble.player_id < 0 and noble.check_req(player.cards):
            available_idx.append(i)
    return available_idx

def take_noble(noble: NobleCardDirty, player: Player, btn_sel_list: List[ButtonDirty]):
    player.score += noble.point
    noble.player_id = player.id 
    noble.visible = 0
    for i in range(len(btn_sel_list)):
        btn_sel_list[i].visible = 0

#EndTurn #############################################################################################################   
def endturn(turn,count_turn,allplayer) :
    turn = (turn+1)%allplayer
    count_turn = count_turn + 1
    return turn, count_turn

#EndGame ############################################################################################################# 
def endgame(turn,player_list,End) :
    if End == 0 and player_list[turn].score >= 15:
        End = 1
    return End