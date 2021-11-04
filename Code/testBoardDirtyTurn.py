from typing import List, Tuple
import pygame
import csv
import random
from classPlayer import Player
from classButtonDirty import ButtonDirty
from classCardDirty import CardDirty
from classToken import Token
from classBigCard import BigCard

pygame.init()
#Set variable for window size
res = (1280, 720)
screen = pygame.display.set_mode(res)
#Set FPS of the game
FPS = 30
# read cards' data from csv file
def read_card_data(data_path, card_list):
    with open(data_path, mode='r') as data_file:
        data_reader = csv.DictReader(data_file, delimiter=',')
        for id, row in enumerate(data_reader):
            card = CardDirty(id, int(row['point']), (110, 175), row['image_path'], int(row['level']), row['colors'])
            for colors in card.requirements.keys():
                card.requirements[colors] = int(row[colors])
            card_list.append(card)

# place cards on board
def place_cards(card_list: List[CardDirty], allsprites, order):
    for i in range(3):
        card = card_list[order[i]]  
        card.reposition(700+140*i, 500)    
        allsprites.add(card)
        # move cards to 3rd layer (layer 2)
        allsprites.change_layer(card, 2)
        card.t_colors = 'black'  
        # show card id on card 
        card.update_text(f'{card.card_id}')     
    print(order)

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

def return_token(token: Token, show_token: Token, sel_qty, can_select):
    token.qty += 1
    show_token.qty -= 1
    sel_qty -= 1
    can_select = True
    token.visible = 1
    show_token.out_of_stock()      
    token.update_text(f'{token.qty}')
    show_token.update_text(f'{show_token.qty}')
    return sel_qty, can_select 

def cancel_token(token_list: List[Token], show_token_list: List[Token]):
    for i, show_tok in enumerate(show_token_list):
        if show_tok.qty > 0:
            token_list[i].qty += show_tok.qty
            show_tok.qty = 0
            token_list[i].visible = 1
            show_tok.visible = 0       
            token_list[i].update_text(f'{token_list[i].qty}')
            show_tok.update_text(f'{show_tok.qty}') 

def take_tokens(token_list, player: Player):
    for token in token_list:
        player.tokens[token.colors].qty += token.qty
        player.tokens[token.colors].update_text(f'{player.tokens[token.colors].qty}')
        player.tokens[token.colors].out_of_stock()
        token.qty = 0
        token.visible = 0
        token.dirty = 1

def get_tokens(token: Token, player: Player):
    if token.qty > 0:
        player.tokens[token.colors].qty += 1
        token.qty -= 1
        token.dirty = 1
    print(f'take {token.colors}')
    print(f'player: {token.colors} = {player.tokens[token.colors].qty}')
    token.out_of_stock()

def reduce_token(token: Token, player: Player):
    player.tokens[token.colors].qty -= 1
    token.qty += 1
    token.visible = 1

def pay_tokens(card: CardDirty, player: Player):
    paid_tokens = card.pay_tokens(player.tokens, player.cards)
    player.score += card.point
    player.cards[card.colors] += 1
    for token in player.tokens.values():
        token.update_text(f'{token.qty}')
        token.out_of_stock()
    card.kill()
    print(f'take card: +{card.point} points')
    print(f'owned cards: {player.cards}')
    print()
    return paid_tokens

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

#EndTurn #############################################################################################################   
def endturn(turn,count_turn,allplayer) :
    turn = (turn+1)%allplayer
    count_turn = count_turn + 1
    return turn, count_turn

#Set 4 player #############################################################################################################
player1 = Player(0, 0, 'testB0i1')
player2 = Player(0, 0, 'testB0i2')
player3 = Player(0, 0, 'testB0i3')
player4 = Player(0, 0, 'testB0i4')
player_list = [player1, player2, player3, player4]
allplayer = 4
#Use 'player_list[0]' instead of 'player' in original code
#Set 4 player #############################################################################################################
def testBoard(screen, res, FPS, player_list: List[Player], allplayer):
    #Set turn variabel #############################################################################################################
    turn = 0
    count_turn = 1
    clock = pygame.time.Clock()
    run = True
    sel_qty = 0
    can_select = True
    big_card = None
    Pause = 0
    paid_tokens = {}
    tok_col = ['white', 'blue', 'green', 'red', 'black']
    font = pygame.font.Font(None, 30)

#Set 4 player  text #############################################################################################################
    #Player 1
    msg1 = font.render('Player 1 Owned Tokens:', True, 'white')
    msg1_rect = msg1.get_rect(center = (res[0]/2, 20))
    tokens_text1 = font.render(f'{player_list[0].tokens}', True, 'white', 'green')
    tok_t_rect1 = tokens_text1.get_rect(center = (res[0]/2, 50))
    #Player 2
    msg2 = font.render('Player 2 Owned Tokens:', True, 'white')
    msg2_rect = msg1.get_rect(center = (res[0]/2, 120))
    tokens_text2 = font.render(f'{player_list[1].tokens}', True, 'white', 'green')
    tok_t_rect2 = tokens_text2.get_rect(center = (res[0]/2, 110))
    #Player 3
    msg3 = font.render('Player 3 Owned Tokens:', True, 'white')
    msg3_rect = msg1.get_rect(center = (res[0]/2, 220))
    tokens_text3 = font.render(f'{player_list[2].tokens}', True, 'white', 'green')
    tok_t_rect3 = tokens_text3.get_rect(center = (res[0]/2, 170))
    #Player 4
    msg4 = font.render('Player 4 Owned Tokens:', True, 'white')
    msg4_rect = msg1.get_rect(center = (res[0]/2, 320))
    tokens_text4 = font.render(f'{player_list[3].tokens}', True, 'white', 'green')
    tok_t_rect4 = tokens_text4.get_rect(center = (res[0]/2, 230))
#Set 4 player  text #############################################################################################################

    # set background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill('darkorchid3')
    background.blit(msg1, msg1_rect)
    background.blit(msg2, msg2_rect)
    background.blit(msg3, msg3_rect)
    background.blit(msg4, msg4_rect)
#Set 4 player  text #############################################################################################################


    # contain all sprites that must be drawn and update on screen
    allsprites = pygame.sprite.LayeredDirty()
    for i in range(5):
        tok = Token((150, 200+100*i), (100, 100), 'Image\Button\CloseButton.png', tok_col[i], 5)
        tok_in_pane = Token((300, 200+100*i), (100, 100), 'Image\Button\CloseButton.png', tok_col[i], 0)
        tok_in_pane.visible = 0
        allsprites.add(tok, tok_in_pane)
        # move token that show how many token player has selected to 2nd layer (layer 1)
        allsprites.change_layer(tok_in_pane, 1)
    tokGold = Token((150, 100), (100, 100), 'Image\Button\CloseButton.png', 'gold', 5)
    allsprites.add(tokGold)

    for i, p in enumerate(player_list):
        for token in p.tokens.values():
            allsprites.add(token)
        p.repos_tokens(490, 60+(100*i), 10)

    btn_cancel = ButtonDirty((500, 300), (130, 50), 'cancle', 30, 'Image\Button\ButtonNewUnhover.png', 'black')
    btn_confirm = ButtonDirty((500, 400), (130, 50), 'confirm', 30, 'Image\Button\ButtonNewUnhover.png', 'black')
    btn_cancel.visible = btn_confirm.visible = 0
    allsprites.add(btn_cancel, btn_confirm)

    card_list = []
    read_card_data('CSV\CardData_example.csv', card_list)

    # set order of cards to appeqr
    random_order = random.sample(range(len(card_list)), len(card_list))
    place_cards(card_list, allsprites, random_order)

    # draw background (static image, cannot change)
    allsprites.clear(screen, background)

    # get sprites from each layer
    # tokens and other buttons (may change button's layer later)
    spr_layer0 = allsprites.get_sprites_from_layer(0)
    # token that show how many token player has selected
    spr_layer1 = allsprites.get_sprites_from_layer(1)
    # cards
    spr_layer2 = allsprites.get_sprites_from_layer(2)


    while run:
        for event in pygame.event.get():
            # press x key on keyboard to exit
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
                run = False

            if event.type == pygame.MOUSEMOTION:
                # hover effect on cancel button
                if btn_cancel.visible:
                    if btn_cancel.rect.collidepoint(event.pos):
                        btn_cancel.hover('white', 'Image\Button\ButtonNewhover.png')
                    else:
                        btn_cancel.unhover()

                # hover effect on confirm button
                if btn_confirm.visible:
                    if btn_confirm.rect.collidepoint(event.pos):
                        btn_confirm.hover('white', 'Image\Button\ButtonNewhover.png')
                    else:
                        btn_confirm.unhover()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # board is showing
                    if Pause == 0:
                        for i, token in enumerate(spr_layer0):
                            if i > 4:
                                break
                            if token.is_collide_mouse(event.pos) and token.qty > 0:
                                # print(f'hit {token.colors}')
                                btn_cancel.visible = btn_confirm.visible = 1
                                sel_qty, can_select = select_token(token, spr_layer1[i], sel_qty, can_select)
                                # get_tokens(token, player)
                                break

                        for i, sel_token in enumerate(spr_layer1):
                            if not token.visible:
                                continue
                            if sel_token.is_collide_mouse(event.pos) and sel_token.qty > 0:
                                print(f'hit showed {sel_token.colors}')
                                sel_qty, can_select = return_token(spr_layer0[i], sel_token, sel_qty, can_select)
                                if sel_qty == 0:
                                    btn_cancel.visible = btn_confirm.visible = 0

                        for card in spr_layer2:
                            if card.is_collide_mouse(event.pos):
                                print(f'click c{card.card_id}')
                                print(f'colors: {card.colors}')
                                print(f'cost: {card.requirements}')
                                # show big card from the card player clicked
                                big_card = BigCard(card, (res[0]/2+300, res[1]/2))
                                allsprites.add(big_card)
                                Pause = 1
                                break
                    
                    # big card is showing
                    if Pause == 1:
                        big_card.dirty = 1
                        # calculate coordinate to check with buttons on big card
                        pos_check = (
                            event.pos[0] - big_card.rect.topleft[0],
                            event.pos[1]- big_card.rect.topleft[1]
                        )
                        # close big card
                        if big_card.btn_close.is_collide_mouse(pos_check):
                            # print('click close')
                            # delete big card from the screen and allsprites. 
                            big_card.kill()
                            Pause = 0

                        #  hold a card
                        elif big_card.btn_hold.is_collide_mouse(pos_check):
                            print('click hold')
                            hold_card(big_card.selected_card, player_list[turn], allsprites.sprites()[5])
                            big_card.kill()
                            turn,count_turn = endturn(turn,count_turn,allplayer)
                            Pause = 0

                        # buy a card
                        elif big_card.btn_buy.is_collide_mouse(pos_check):
                            # print('click buy')
                            # check if player can buy a card
                            if big_card.selected_card.check_req(player_list[turn].tokens, player_list[turn].cards):
                                print(f'can buy c{big_card.selected_card.card_id}')
                                paid_tokens = pay_tokens(big_card.selected_card, player_list[turn])
                                for i, token in enumerate(spr_layer0):
                                    if i > 4:
                                        break
                                    token.qty += paid_tokens[token.colors]
                                    token.update_text(f'{token.qty}')
                                    token.visible = 1
                                big_card.kill()
                                turn,count_turn = endturn(turn,count_turn,allplayer)
                                Pause = 0
                            else:
                                print(f'can not buy c{big_card.selected_card.card_id}')

                    # cancel selected tokens. return all selected tokens to the pile
                    if btn_cancel.visible:
                        if btn_cancel.rect.collidepoint(event.pos):
                            print('close token pane')
                            cancel_token(spr_layer0, spr_layer1)
                            sel_qty = 0
                            can_select = True
                            btn_cancel.unhover()                            
                            btn_cancel.visible = btn_confirm.visible = 0

                    # take all selected tokens
                    if btn_confirm.visible:
                        if btn_confirm.rect.collidepoint(event.pos):
                            print('take token(s)')
                            take_tokens(spr_layer1, player_list[turn])
                            sel_qty = 0
                            can_select = True
                            btn_confirm.unhover()
                            btn_cancel.visible = btn_confirm.visible = 0
                            turn,count_turn = endturn(turn,count_turn,allplayer)

            # if event.type == pygame.KEYDOWN:
            #     for key, token in enumerate(allsprites.sprites(), start=pygame.K_0):
            #         if event.key == key:
            #             token.visible = not token.visible

            # if event.type == pygame.KEYDOWN:
            #     for key, token in enumerate(allsprites.get_sprites_from_layer(0), start=pygame.K_1):
            #         if event.key == key:
            #             reduce_token(token, player)

        # update text: number of tokens that player has ##########################################################################
        # tokens_text1 = font.render(f'{player_list[0].tokens}', True, 'white', 'chartreuse4')
        # print(f'{player_list[0].tokens}')
        # tokens_text2 = font.render(f'{player_list[1].tokens}', True, 'white', 'chartreuse4')
        # print(f'{player_list[1].tokens}')
        # tokens_text3 = font.render(f'{player_list[2].tokens}', True, 'white', 'chartreuse4')
        # print(f'{player_list[2].tokens}')
        # tokens_text4 = font.render(f'{player_list[3].tokens}', True, 'white', 'chartreuse4')
        # print(f'{player_list[3].tokens}')
        

        clock.tick(FPS)     
        # get all rects of sprites on screen   
        rects = allsprites.draw(screen)
        # screen.blit(tokens_text1, tok_t_rect1) 
        # screen.blit(tokens_text2, tok_t_rect2) 
        # screen.blit(tokens_text3, tok_t_rect3) 
        # screen.blit(tokens_text4, tok_t_rect4) 
        # only update sprites in allsprites 
        pygame.display.update(rects)
    
    pygame.quit()
    exit()

if __name__ == '__main__':
    testBoard(screen, res, FPS, player_list, allplayer)