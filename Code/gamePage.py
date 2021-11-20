#Written by Pimanus 62070501039
import pygame
import csv
import random
import RuleDirtyButton 
from typing import List
from classButtonDirty import ButtonDirty
from classCardDirty import CardDirty, BonusCardDirty
from classToken import Token
from classPlayer import Player
from classBigCard import BigCard
pygame.init()

FPS = 30
res = [1280, 720]

screen = pygame.display.set_mode(res)
Deck_font = pygame.font.Font("Font/Roboto/Roboto-Bold.ttf",20)

name_user = ['testB01','testB02']
act_user = [0, 1]
result_player_list = []

# read card data from csv file
def read_card_data(data_path, card_list):
    with open(data_path, mode='r') as data_file:
        data_reader = csv.DictReader(data_file, delimiter=',')
        for id, row in enumerate(data_reader):
            card = CardDirty(id, int(row['point']), (112, 167), row['image_path'], int(row['level']), row['colors'])
            for colors in card.requirements.keys():
                card.requirements[colors] = int(row[colors])
            card_list[card.level-1].append(card)

# read noble card data from csv file 
def read_noble_data(data_path, noble_list):
    with open(data_path, mode='r') as data_file:
        data_reader = csv.DictReader(data_file, delimiter=',')
        for id, row in enumerate(data_reader):
            noble = BonusCardDirty(id, int(row['point']), (122, 122), row['image_path'])
            for colors in noble.requirements.keys():
                noble.requirements[colors] = int(row[colors])
            noble_list.append(noble)

# Create list of Player object from 
def getPlayerData(name_user: List[int], 
                  act_user: List[int]):
    allplayer = 0
    name_font = pygame.font.Font("Font/Roboto/Roboto-Bold.ttf",20)
    score_font = pygame.font.Font("Font/Roboto/Roboto-Bold.ttf",30)
    player_name = []
    cha = []
    bg_player = []
    player_list = []
    player_score = []    

    print(f'act_user length: {len(act_user)}')
    for act_id in act_user:
        print(f'selected character id: {act_id}')
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
        # player name sprite
        playerName = pygame.sprite.DirtySprite()
        playerName.image = name_font.render(name_user[i],'AA','White')
        playerName.rect = playerName.image.get_rect(bottomleft = (10, 177+(177*i)))
        player_name.append(playerName)               
        # player score sprite
        playerScore = pygame.sprite.DirtySprite()        
        playerScore.image = score_font.render(f'{player.score}','AA','White')
        playerScore.rect = playerScore.image.get_rect(bottomleft = (30, 50+(177*i)))
        player_score.append(playerScore)

        player_list.append(player)
        allplayer += 1
    return allplayer, player_list, cha, bg_player, player_name, player_score

def get_tokens(allsprites, allplayer):
    tok_col = ['white', 'blue', 'green', 'red', 'black']
    for i in range(5):
        tok = Token((494, 184+118*i), (108, 108), 'Image\Coin\\'+tok_col[i]+'Coin-01.png', tok_col[i], 2+int(allplayer*5/4))
        allsprites.add(tok)
        # move token that show how many token player has selected to 2nd layer (layer 1)
        # allsprites.change_layer(tok, 1)
    tokGold = Token((494, 66), (108, 108), 'Image\Coin\goldCoin-01.png', 'gold', 5)
    allsprites.add(tokGold)
    allsprites.change_layer(tokGold, 0)
    for i in range(5):
        tok_in_pane = Token((614, 184+118*i), (108, 108), 'Image\Coin\\'+tok_col[i]+'Coin-01.png', tok_col[i], 0)
        tok_in_pane.visible = 0
        allsprites.add(tok_in_pane)
        # move token that show how many token player has selected to 2nd layer (layer 1)
        # allsprites.change_layer(tok_in_pane, 1)

def place_cards(card_list: List[List[CardDirty]], allsprites, order: List[List[int]]):
    card_counter = [0, 0, 0]
    for i in range(3):
        for card_counter[i] in range(4):
            card = card_list[i][order[i][card_counter[i]]]  
            card.reposition(751+132*card_counter[i], 262+((2-i)*177))
            allsprites.add(card)
    return card_counter

def place_nobles(noble_list: List[BonusCardDirty], allsprites, order: List[int], btn_list: List[ButtonDirty]):
    for i, idx in enumerate(order):
        noble = noble_list[idx]
        noble.reposition(619+(132*i), 90)
        btn_list[i].reposition(noble.rect.centerx+25, noble.rect.y+20)
        btn_list[i].visible = 0
        allsprites.add(noble, btn_list[i])
        allsprites.change_layer(btn_list[i], 2)

def place_player_tokens(player_list, allsprites):
    for i, player in enumerate(player_list):
        for token in player.tokens.values():
            player.repos_tokens(138, 50+(177*i))
            allsprites.add(token)

def place_own_cards(player_list, allsprites):
    for i, player in enumerate(player_list):
        for card in player.cards.values():
            player.repos_cards(138, 120+(177*i))
            allsprites.add(card)

# select a token
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
    sel_token.out_of_stock()
    print(f'selected {show_token.colors}: {show_token.qty}')
    return sel_qty, can_select

# return token to pile
def get_token_back(token: Token, show_token: Token, sel_qty, can_select):
    token.qty += 1
    show_token.qty -= 1
    sel_qty -= 1
    can_select = True
    token.visible = 1
    show_token.out_of_stock()      
    token.update_text(f'{token.qty}')
    show_token.update_text(f'{show_token.qty}')
    return sel_qty, can_select 

# cancel all selected tokens
def cancel_token(token_list: List[Token], show_token_list: List[Token]):
    for i, show_tok in enumerate(show_token_list):
        if show_tok.qty > 0:
            token_list[i].qty += show_tok.qty
            show_tok.qty = 0
            token_list[i].visible = 1
            show_tok.visible = 0       
            token_list[i].update_text(f'{token_list[i].qty}')
            show_tok.update_text(f'{show_tok.qty}') 

# add token to player
def take_tokens(token_list, player: Player):
    for token in token_list:
        player.tokens[token.colors].qty += token.qty
        player.tokens[token.colors].update_text(f'{player.tokens[token.colors].qty}')
        player.tokens[token.colors].out_of_stock()
        token.qty = 0
        token.visible = 0
        token.dirty = 1

# get a card from draw pile after buy or hold a card
def get_new_card(card: CardDirty, card_list: List[List[CardDirty]], card_counter, order):
    card_counter[card.level-1] += 1
    if card_counter[card.level-1] >= len(card_list[card.level-1]):
        return None
    else:
        order_idx = order[card.level-1][card_counter[card.level-1]]
        new_card = card_list[card.level-1][order_idx]
        new_card.reposition(card.position[0], card.position[1])
        new_card.t_colors = 'black'  
        print(f'new card ID: {new_card.card_id}')
        print()
        return new_card

def update_card_qty(card_counter, card_list, card_qty_list, allsprites):
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
        token.out_of_stock()
    card.kill()
    print(f'take card: +{card.point} points')
    # print(f'owned cards: {player.cards}')
    print()
    return paid_tokens

# add card to player's hold card list and give gold token to player
def hold_card(card: CardDirty, player: Player, token_gold: Token):
    player.hold_cards.append(card)
    if player.tokens['gold'].qty < 3 and token_gold.qty > 0:
        player.tokens['gold'].qty += 1
        player.tokens['gold'].update_text(f"{player.tokens['gold'].qty}")
        player.tokens['gold'].out_of_stock()
        token_gold.qty -= 1
        token_gold.update_text(f'{token_gold.qty}')
        token_gold.out_of_stock()
    card.kill()
    print(f'hold {len(player.hold_cards)} card(s)')
    print()

def check_player_token(player: Player):
    total_token = 0
    for p_token in player.tokens.values():
        total_token += p_token.qty
    print(player.name)
    print(f'total token: {total_token}')    
    return total_token > 10

def return_token(token_list: List[Token], token_gold: Token, player: Player, m_pos):
    total_token = 0
    for p_token in player.tokens.values():
        total_token += p_token.qty
    if total_token > 10:
        for i, token in enumerate(player.tokens.values()):
            if token.is_collide_mouse(m_pos) and token.qty > 0:
                token.qty -= 1
                token.update_text(f'{token.qty}')
                token.out_of_stock()
                if i < 5:
                    token_list[i].qty += 1                
                    token_list[i].update_text(f'{token_list[i].qty}')                
                    token_list[i].out_of_stock()
                else:
                    token_gold.qty += 1                
                    token_gold.update_text(f'{token_gold.qty}')                
                    token_gold.out_of_stock()
                total_token -= 1
    return total_token

def check_noble(noble_list, noble_order, player):
    available_idx = []  
    for i in range(len(noble_order)):
        noble = noble_list[noble_order[i]]
        if noble.player_id < 0 and noble.check_req(player.cards):
            available_idx.append(i)
    return available_idx

def take_noble(noble: BonusCardDirty, player: Player, btn_sel_list: List[ButtonDirty]):
    player.score += noble.point
    noble.player_id = player.id 
    noble.visible = 0
    for i in range(len(btn_sel_list)):
        btn_sel_list[i].visible = 0
    print(f'{player.name}\'s score: {player.score}')

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

def gameBoard(name_user, act_user,result_player_list): 
    result_player_list = []
    clock = pygame.time.Clock()
    score_font = pygame.font.Font("Font\Roboto\Roboto-Bold.ttf",30)
    # Run until the user asks to quit
    run = True
    turn = 0
    count_turn = 0
    End = 0
    sel_qty = 0
    can_select = True
    big_card = None
    new_card = None
    Now = Pause = 0
    paid_tokens = {}

    allplayer, player_list, cha, bg_player, player_name, player_score = getPlayerData(name_user, act_user)

    card_list = [[], [], []]
    read_card_data('CSV\CardData.csv', card_list)
    noble_list = []
    read_noble_data('CSV\\NobleData.csv' , noble_list)

    random_order = []
    for i in range(3):
        rand_lv = random.sample(range(len(card_list[i])), len(card_list[i]))
        random_order.append(rand_lv)
    for rand in random_order:
        print(rand)
    noble_qty = allplayer + 1
    noble_order = random.sample(range(len(noble_list)), noble_qty)
    print(noble_order)

    allsprites = pygame.sprite.LayeredDirty()
    turn_frame = pygame.sprite.DirtySprite()
    turn_frame.image = pygame.image.load('Image\Card\\frame.png').convert_alpha()
    turn_frame.image = pygame.transform.smoothscale(turn_frame.image, (430, 167))
    turn_frame.rect = turn_frame.image.get_rect(topleft = (0, 10))
    allsprites.add(turn_frame)

    get_tokens(allsprites, allplayer)
    place_player_tokens(player_list, allsprites)
    place_own_cards(player_list, allsprites)
    card_counter = place_cards(card_list, allsprites, random_order)      

    card_qty_list = []
    for i in range(3):
        remaining = len(card_list[i]) - (card_counter[i]+1)
        qty_text = pygame.sprite.DirtySprite()        
        qty_text.image = Deck_font.render(f'{remaining}', True, 'white') 
        qty_text.rect = qty_text.image.get_rect(topleft = (611,675-(177*i)))
        card_qty_list.append(qty_text)
        allsprites.add(qty_text) 

    for cha_spr in cha:
        allsprites.add(cha_spr)
    for name_spr in player_name:  
        allsprites.add(name_spr)
    for score_spr in player_score:
        allsprites.add(score_spr)

    # create buttons
    btn_cancel = ButtonDirty((494, 66), (100, 50), 'cancel', 20, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font\Roboto\Roboto-Regular.ttf')
    btn_confirm = ButtonDirty((614, 66), (100, 50), 'confirm', 20, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font\Roboto\Roboto-Regular.ttf')
    btn_cancel.visible = btn_confirm.visible = 0
    allsprites.add(btn_cancel, btn_confirm)  
    allsprites.change_layer(btn_cancel, 2)
    allsprites.change_layer(btn_confirm, 2)
    btn_sel_list = []
    for i in range(noble_qty):
        btn_select = ButtonDirty((500, 500), (60, 30), 'select', 15, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font\Roboto\Roboto-Regular.ttf')
        btn_sel_list.append(btn_select)  
    place_nobles(noble_list, allsprites, noble_order, btn_sel_list) 

    select_popup = pygame.sprite.DirtySprite()
    select_popup.image = pygame.image.load('Image\Card\selectCoin.png').convert_alpha()
    select_popup.image = pygame.transform.smoothscale(select_popup.image, (265, 700))
    select_popup.rect = select_popup.image.get_rect(topleft = (420, 10))
    select_popup.visible = 0
    allsprites.add(select_popup)
    allsprites.change_layer(select_popup, 1)

    # create objects for showing hold cards
    hold_pane = pygame.sprite.DirtySprite()
    hold_pane.image = pygame.image.load('Image\Card\holdBG.png').convert_alpha()
    hold_pane.image = pygame.transform.smoothscale(hold_pane.image, (800, 370))
    hold_pane.rect = hold_pane.image.get_rect(center = (res[0]/2+200, res[1]/2))
    hold_pane._layer = 3
    btn_close = ButtonDirty((hold_pane.rect.centerx, hold_pane.rect.bottom-70), (100, 50), 'close', 25, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font\Roboto\Roboto-Regular.ttf')
    btn_close._layer = 3

    msg_font = pygame.font.Font('Font\Roboto\Roboto-Regular.ttf', 15)
    msg_text = 'You have more than 10 Tokens! \nplease click on your token to return.'
    msg_box = pygame.sprite.DirtySprite()
    msg_box.image = pygame.image.load('Image\Card\\ballon.png').convert_alpha()
    msg_box.image = pygame.transform.smoothscale(msg_box.image, (325, 80))
    RuleDirtyButton.text_block(msg_font, msg_text, 'Black', (25,15), 325, msg_box.image, 10)
    msg_box.rect = msg_box.image.get_rect(bottomleft = (95, 160))
    msg_box.visible = 0
    allsprites.add(msg_box)

    bgimage = pygame.image.load("Image/Card/bg-01.png")
    bgimage = pygame.transform.scale(bgimage, (1280, 720))
    Deck1 = pygame.image.load('Image/Card/D01.png')
    Deck1 = pygame.transform.smoothscale (Deck1, (122, 167))
    Deck2 = pygame.image.load('Image/Card/D02.png')
    Deck2 = pygame.transform.smoothscale (Deck2, (122, 167))
    Deck3 = pygame.image.load('Image/Card/D03.png')
    Deck3 = pygame.transform.smoothscale (Deck3, (122, 167))

    background = pygame.Surface(screen.get_size()).convert()
    background.blit(bgimage, (0,0))
    for i, bg in enumerate(bg_player):
        background.blit(bg, (0, 10+177*i))
    background.blit(Deck1,(558,533))
    background.blit(Deck2,(558,356))
    background.blit(Deck3,(558,179))

    allsprites.clear(screen, background)

    ################################## For pausegame when press ESC #########################################
    #By Pojnarin 62070501041
    #define variable for state of the game 0 = No pause , 1 = Pause
    freeze = 0
    #Rule start page
    page = 1
    allpage = 20
    #Text for rule
    text_font_bold = pygame.font.Font("Font\Roboto\Roboto-Bold.ttf",40)
    text_font_regular = pygame.font.Font("Font\Roboto\Roboto-Regular.ttf",30)
    #When open rule, set Pause = 2
    POPINBG = pygame.sprite.DirtySprite()
    POPINBG.image = pygame.image.load("Image\Background\PauseGame720p.png").convert_alpha()
    POPINBG.rect = POPINBG.image.get_rect(topleft = (0, 0))
    RULEPBG = pygame.sprite.DirtySprite()
    RULEPBG.image = pygame.image.load("Image\Background\RuleInGame720p.png").convert_alpha()
    RULEPBG.rect = RULEPBG.image.get_rect(topleft = (0, 0))
    POPINBG.visible = 0
    RULEPBG.visible = 0
    POPINBG._layer = RULEPBG._layer = 5
    allsprites.add(POPINBG,RULEPBG) 
    #DirtyButton Start Here ################################### NNNNNNNNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEEEEWWWWWWWWWWWWWWWWWWWWWWWWWWW
    
    #Pop up button
    btn_Rule = ButtonDirty((670,300), (140, 70), 'Rule', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    btn_Resume = ButtonDirty((670,400), (140, 70), 'Resume', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    btn_Back = ButtonDirty((670,520), (250, 70), 'Back to Menu', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    #Rule Button
    Next = ButtonDirty((1180,140), (130, 50), 'Next', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    Prev = ButtonDirty((85,140), (140, 50), 'Previous', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    Back = ButtonDirty((1180,640), (130, 50), 'Back', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    #Set visibility
    btn_Rule.visible = btn_Resume.visible = btn_Back.visible = Next.visible = Prev.visible = Back.visible = 0
    btn_Rule._layer = btn_Resume._layer = btn_Back._layer = Next._layer = Prev._layer = Back._layer = 5
    #Add button in group
    allsprites.add(btn_Rule, btn_Resume, btn_Back, Next, Prev, Back)

    ##################################

    while run:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            ########################################## vvvvvvvvv When press key 'ESC'
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    if freeze == 1 : 
                        freeze = 0
                    elif freeze == 0 : 
                        freeze = 1
                    else : freeze = 0
            ########################################## ^^^^^^^^^^
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1:
                    if freeze == 0:
                        if Pause == 0:
                            for i, token in enumerate(allsprites.get_sprites_from_layer(2)[:5]):
                                if token.is_collide_mouse(event.pos) and token.qty > 0:
                                    select_popup.visible = 1
                                    btn_cancel.visible = 1
                                    Pause = 1
                                    break                        

                            for card in allsprites.get_sprites_from_layer(1):
                                if isinstance(card, CardDirty) and card.is_collide_mouse(event.pos):
                                    print(f'click c{card.card_id}')
                                    print(f'colors: {card.colors}')
                                    print(f'cost: {card.requirements}')
                                    print(f'point: {card.point}') 
                                    big_card = BigCard(card, (res[0]/2+300, res[1]/2))
                                    allsprites.add(big_card)
                                    Now = Pause
                                    Pause = 2
                                    break   

                            if player_list[turn].cards['hold'].visible:
                                if player_list[turn].cards['hold'].is_collide_mouse(event.pos):
                                    print('click show hold cards')
                                    allsprites.add(hold_pane, btn_close)
                                    for i, card in enumerate(player_list[turn].hold_cards):
                                        card.reposition(hold_pane.rect.x+150+250*i, hold_pane.rect.y+150)
                                        allsprites.add(card)
                                        allsprites.change_layer(card, 3)
                                    Pause = 3
                            card.dirty = 1                    
                        # selecting tokens
                        elif Pause == 1:
                            for i, token in enumerate(allsprites.get_sprites_from_layer(2)[:5]):
                                if token.is_collide_mouse(event.pos) and token.qty > 0:                             
                                    sel_qty, can_select = select_token(token, allsprites.get_sprites_from_layer(2)[i+5], sel_qty, can_select)
                                    btn_confirm.visible = 1
                                    break
                            # reduce quantity of selected token when click on it
                            for i, sel_token in enumerate(allsprites.get_sprites_from_layer(2)[5:10], start=5):
                                if not sel_token.visible:
                                    continue
                                print(sel_token.colors)
                                if sel_token.is_collide_mouse(event.pos):
                                    print(f'hit showed {sel_token.colors}')
                                    sel_qty, can_select = get_token_back(allsprites.get_sprites_from_layer(2)[i-5], sel_token, sel_qty, can_select)
                                    if sel_qty == 0:
                                        select_popup.visible = 0                                    
                                        btn_cancel.visible = btn_confirm.visible = 0
                                        Pause = 0
                            # cancel selected tokens. return all selected tokens to the pile
                            if btn_cancel.visible:
                                if btn_cancel.rect.collidepoint(event.pos):
                                    print('close token pane')
                                    cancel_token(allsprites.get_sprites_from_layer(2)[:5], allsprites.get_sprites_from_layer(2)[5:10])
                                    sel_qty = 0
                                    can_select = True
                                    btn_cancel.unhover()   
                                    select_popup.visible = 0                         
                                    btn_cancel.visible = btn_confirm.visible = 0
                                    Pause = 0
                            # take all selected tokens
                            if btn_confirm.visible:
                                if btn_confirm.rect.collidepoint(event.pos):
                                    print('take token(s)')
                                    take_tokens(allsprites.get_sprites_from_layer(2)[5:10], player_list[turn])
                                    sel_qty = 0
                                    can_select = True
                                    btn_confirm.unhover()
                                    select_popup.visible = 0
                                    btn_cancel.visible = btn_confirm.visible = 0
                                    if check_player_token(player_list[turn]):
                                        print('return tokens')
                                        msg_box.visible = 1
                                        Pause = 4
                                    else:
                                        available_idx = check_noble(noble_list, noble_order, player_list[turn])
                                        if not available_idx:  
                                            turn,count_turn = endturn(turn,count_turn,allplayer)                                            
                                            turn_frame.rect.topleft = (0, 10+177*turn)
                                            msg_box.rect.bottomleft = (95, 160+177*turn)
                                            turn_frame.dirty = 1 
                                            Pause = 0  
                                        else:
                                            for idx in available_idx:
                                                btn_sel_list[idx].visible = 1
                                            Pause = 5                                                                     
                        # big card is showing
                        elif Pause == 2:
                            pos_check = (
                                event.pos[0] - big_card.rect.topleft[0],
                                event.pos[1]- big_card.rect.topleft[1]
                            )
                            # close big card
                            if big_card.btn_close.is_collide_mouse(pos_check):
                                # print('click close')
                                # delete big card from the screen and allsprites. 
                                big_card.kill()
                                Pause = Now

                            #  hold a card
                            if not big_card.is_hold:
                                if big_card.btn_hold.is_collide_mouse(pos_check):
                                    print('click hold')
                                    if len(player_list[turn].hold_cards) < 3:
                                        hold_card(big_card.selected_card, player_list[turn], allsprites.sprites()[1])
                                        player_list[turn].cards['hold'].qty = len(player_list[turn].hold_cards)
                                        player_list[turn].cards['hold'].update_text(f'{player_list[turn].cards["hold"].qty}')
                                        player_list[turn].cards['hold'].visible = player_list[turn].is_hold_card()                                        
                                        ####################################################################Change player to player_list[turn]
                                        new_card = get_new_card(big_card.selected_card, card_list, card_counter, random_order)
                                        update_card_qty(card_counter, card_list, card_qty_list, allsprites)
                                        big_card.kill()
                                        if new_card != None:
                                            allsprites.add(new_card)
                                        #####################################################
                                        if check_player_token(player_list[turn]):
                                            print('return tokens')
                                            msg_box.visible = 1
                                            Pause = 4
                                        else:
                                            available_idx = check_noble(noble_list, noble_order, player_list[turn])
                                            if not available_idx:  
                                                turn,count_turn = endturn(turn,count_turn,allplayer)
                                                turn_frame.rect.topleft = (0, 10+177*turn)
                                                msg_box.rect.bottomleft = (95, 160+177*turn)
                                                turn_frame.dirty = 1 
                                                Pause = 0
                                            else:
                                                for idx in available_idx:
                                                    btn_sel_list[idx].visible = 1
                                                Pause = 5
                                            #################################################################################################
                                            turn_frame.rect.topleft = (0, 10+177*turn)
                                            msg_box.rect.bottomleft = (95, 160+177*turn)
                                            turn_frame.dirty = 1                                    
                            # buy a card
                            if big_card.btn_buy.is_collide_mouse(pos_check):                                
                                # check if player can buy a card
                                if big_card.selected_card.check_req(player_list[turn].tokens, player_list[turn].cards):
                                    print(f'can buy c{big_card.selected_card.card_id}')
                                    paid_tokens = pay_tokens(big_card.selected_card, player_list[turn])
                                    player_score[turn].image = score_font.render(f'{player_list[turn].score}','AA','White')
                                    player_score[turn].rect = player_score[turn].image.get_rect(bottomleft = player_score[turn].rect.bottomleft)
                                    player_score[turn].dirty = 1
                                    ####################################################################Change player to player_list[turn]
                                    # get new card from card pile if bought card is not held
                                    if not big_card.is_hold:
                                        new_card = get_new_card(big_card.selected_card, card_list, card_counter, random_order)
                                        update_card_qty(card_counter, card_list, card_qty_list, allsprites)
                                    # return tokens to pile
                                    for i, token in enumerate(allsprites.get_sprites_from_layer(2)[:5]):
                                        if paid_tokens[token.colors] > 0:
                                            token.qty += paid_tokens[token.colors]
                                            token.update_text(f'{token.qty}')                                    
                                            token.visible = 1
                                    gold_token = allsprites.sprites()[1]
                                    gold_token.qty += paid_tokens['gold']
                                    gold_token.update_text(f'{gold_token.qty}')
                                    gold_token.out_of_stock()
                                    # remove card from player's hold card list, if any
                                    if big_card.selected_card in player_list[turn].hold_cards:
                                        player_list[turn].hold_cards.remove(big_card.selected_card)
                                        player_list[turn].cards['hold'].qty = len(player_list[turn].hold_cards)
                                        player_list[turn].cards['hold'].update_text(f'{player_list[turn].cards["hold"].qty}')
                                        player_list[turn].cards['hold'].visible = player_list[turn].is_hold_card()
                                        print(f'hold {len(player_list[turn].hold_cards)} card(s)')
                                    big_card.kill()   
                                    if new_card != None:
                                        allsprites.add(new_card)                
                                    if big_card.is_hold:
                                        allsprites.remove_sprites_of_layer(3)   
                                    # check noble cards                                
                                    available_idx = check_noble(noble_list, noble_order, player_list[turn])
                                    if not available_idx: 
                                        Pause = 0                                  
                                        ##############################################################
                                        End = endgame(turn,player_list,End)
                                        turn,count_turn = endturn(turn,count_turn,allplayer)
                                        ########################################################################################################
                                        turn_frame.rect.topleft = (0, 10+177*turn)
                                        msg_box.rect.bottomleft = (95, 160+177*turn)
                                        turn_frame.dirty = 1
                                    else:
                                        for idx in available_idx:
                                            btn_sel_list[idx].visible = 1
                                        Pause = 5
                                else:
                                    print(f'can not buy c{big_card.selected_card.card_id}')  
                            big_card.dirty = 1 
                        # taking a noble card
                        elif Pause == 5:
                            for idx in available_idx:
                                noble = noble_list[noble_order[idx]]
                                # btn_sel_list[idx].visible = 1
                                if btn_sel_list[idx].is_collide_mouse(event.pos):
                                    take_noble(noble, player_list[turn], btn_sel_list)
                                    player_score[turn].image = score_font.render(f'{player_list[turn].score}','AA','White')                                    
                                    player_score[turn].rect = player_score[turn].image.get_rect(bottomleft = player_score[turn].rect.bottomleft)
                                    player_score[turn].dirty = 1
                                    End = endgame(turn,player_list,End)
                                    turn,count_turn = endturn(turn,count_turn,allplayer)
                                    turn_frame.rect.topleft = (0, 10+177*turn)
                                    msg_box.rect.bottomleft = (95, 160+177*turn)
                                    turn_frame.dirty = 1 
                                    Pause = 0
                                    break 
                        # hold cards are showing
                        if Pause == 3:
                            # show big card when click on hold card  
                            for card in player_list[turn].hold_cards:
                                if card.is_collide_mouse(event.pos):
                                    print(f'click c{card.card_id}')
                                    print(f'colors: {card.colors}')
                                    print(f'cost: {card.requirements}')
                                    big_card = BigCard(card, (res[0]/2+300, res[1]/2), True)                                
                                    allsprites.add(big_card)
                                    Now = Pause
                                    Pause = 2
                                    break  
                            # close hold card pane
                            if btn_close.is_collide_mouse(event.pos):
                                print('close hold cards')
                                allsprites.remove_sprites_of_layer(3)
                                Pause = 0                        
                            hold_pane.dirty = 1 
                        # player return tokens
                        if Pause == 4:
                            total_token = return_token(allsprites.get_sprites_from_layer(2)[:5], allsprites.sprites()[1], player_list[turn], event.pos)
                            if total_token <= 10:
                                print('return complete')
                                msg_box.visible = 0
                                available_idx = check_noble(noble_list, noble_order, player_list[turn])
                                if not available_idx: 
                                    turn,count_turn = endturn(turn,count_turn,allplayer)
                                    turn_frame.rect.topleft = (0, 10+177*turn)
                                    msg_box.rect.bottomleft = (95, 160+177*turn)
                                    turn_frame.dirty = 1 
                                    Pause = 0
                                else:
                                    Pause = 5
                    elif freeze == 1:
                        if btn_Back.rect.collidepoint(pygame.mouse.get_pos()):
                            return 'menu', []
                            freeze = 0
                        if btn_Resume.rect.collidepoint(pygame.mouse.get_pos()):
                            freeze = 0
                        if btn_Rule.rect.collidepoint(pygame.mouse.get_pos()):
                            freeze = 2
                    elif freeze == 2:
                        if Next.rect.collidepoint(pygame.mouse.get_pos()):
                            if page != allpage :
                                page += 1
                        if Prev.rect.collidepoint(pygame.mouse.get_pos()):
                            if page != 1 :
                                page -= 1
                        if Back.rect.collidepoint(pygame.mouse.get_pos()):
                            freeze = 1
                
        
        if End == 1 and turn == 0 :
            print("In the  End")
            result_player_list = sorted(player_list, key=lambda x: (-x.score,x.sum_card()))
            print("After sort")
            for player in result_player_list:
                print(f'{player.name}: {player.score}')
            #for Game Result scence use next line Return; 
            return 'result',  result_player_list      

        ####### Button Hover #############################################################
        if freeze == 1 :
            ########################################### Hover effect of Pause Menu Option
            if btn_Rule.rect.collidepoint(pygame.mouse.get_pos()): 
                btn_Rule.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            else :
                btn_Rule.unhover()

            if btn_Resume.rect.collidepoint(pygame.mouse.get_pos()):
                btn_Resume.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            else :
                btn_Resume.unhover()

            if btn_Back.rect.collidepoint(pygame.mouse.get_pos()):  
                btn_Back.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            else :
                btn_Back.unhover()
            ###########################################
        elif freeze == 2 :
            if Next.rect.collidepoint(pygame.mouse.get_pos()) and page != allpage :  
                Next.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            elif page == allpage :
                Next.hover((68,68,68), 'Image\Button\ButtonNewGray.png')
            else :
                Next.unhover()

            if Prev.rect.collidepoint(pygame.mouse.get_pos()) and page != 1 :  
                Prev.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            elif page == 1 : 
                Prev.hover((68,68,68), 'Image\Button\ButtonNewGray.png')
            else :
                Prev.unhover()

            if Back.rect.collidepoint(pygame.mouse.get_pos()): 
                Back.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            else :
                Back.unhover()
        else :
            if Pause == 1:
                if btn_cancel.is_collide_mouse(pygame.mouse.get_pos()):
                    btn_cancel.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                else:
                    btn_cancel.unhover()

                if btn_confirm.is_collide_mouse(pygame.mouse.get_pos()):
                    btn_confirm.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                else:
                    btn_confirm.unhover()                    

            if Pause == 5:
                for btn_select in btn_sel_list:
                    if btn_select.is_collide_mouse(pygame.mouse.get_pos()):
                        btn_select.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                    else:
                        btn_select.unhover()

            if Pause == 3:
                if btn_close.is_collide_mouse(pygame.mouse.get_pos()):
                    btn_close.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                else:
                    btn_close.unhover()
                
            if big_card != None:
                pos_check = (
                    pygame.mouse.get_pos()[0] - big_card.rect.topleft[0],
                    pygame.mouse.get_pos()[1]- big_card.rect.topleft[1]
                )
                if big_card.btn_close.is_collide_mouse(pos_check):
                    big_card.btn_close.hover((153,0,0), 'Image\Button\CloseButtonhover.png')
                    big_card.update_button()
                else:
                    big_card.btn_close.unhover()
                    big_card.update_button()

                if big_card.btn_buy.is_collide_mouse(pos_check):
                    big_card.btn_buy.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                    big_card.update_button()
                else:
                    big_card.btn_buy.unhover()
                    big_card.update_button()

                if not big_card.is_hold:
                    if big_card.btn_hold.is_collide_mouse(pos_check):
                        big_card.btn_hold.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                        big_card.update_button()
                    else:
                        big_card.btn_hold.unhover()
                        big_card.update_button()
            
            if Pause == 4:
                if msg_box.rect.collidepoint(pygame.mouse.get_pos()):
                    msg_box.visible = 0
                else:
                    msg_box.visible = 1
            
        #############################################################################^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        clock.tick(FPS)
        ########################################## After Pause : Render Pause Menu option 
        if freeze == 1 :
            page = 1
            POPINBG.visible = 1
            RULEPBG.visible = 0
            Next.visible = Prev.visible = Back.visible = 0
            btn_Back.visible = btn_Resume.visible = btn_Rule.visible = 1
        ##########################################
        ########################################## If Click on Rule while Pause, Render Rule scene
        elif freeze == 2 :
            POPINBG.visible = 0
            btn_Back.visible = btn_Resume.visible = btn_Rule.visible = 0
            RULEPBG.visible = 1
            Next.visible = Prev.visible = Back.visible = 1
        else : 
            POPINBG.visible = 0
            RULEPBG.visible = 0
            btn_Back.visible = btn_Resume.visible = btn_Rule.visible = Next.visible = Prev.visible = Back.visible = 0
        ##########################################
        
        rects = allsprites.draw(screen)
        if freeze == 2 :
            Page_surface = text_font_regular.render('Page '+str(page)+'/'+str(allpage),True,'Black')
            screen.blit(Page_surface,(25,640))
            RuleDirtyButton.ruletext (page,text_font_bold,text_font_regular,screen)
        
        pygame.display.update(rects)
    # Done! Time to quit.
    pygame.quit()
    exit()
if __name__ == "__main__":
    gameBoard(name_user, act_user,result_player_list)



    