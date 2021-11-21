import pygame
import random
import RuleText
from typing import List
from classButtonDirty import ButtonDirty
from classCardDirty import CardDirty
from classBigCard import BigCard
from gameMethod import *
pygame.init()

FPS = 30
res = [1280, 720]

screen = pygame.display.set_mode(res)


name_user = ['testB01','testB02']
act_user = [0, 1]
result_player_list = []


# Show game scene
# Argument:
#   name_user           -- list of players' name
#   act_user            -- list of character ID selected by player
#   result_player_list  -- list of player order by their score and card quantity
def gameBoard(name_user: List[str], act_user: List[int], result_player_list: List[Player]): 
    result_player_list = []
    clock = pygame.time.Clock()
    score_font = pygame.font.Font("Font\Roboto\Roboto-Bold.ttf",30)
    Deck_font = pygame.font.Font("Font/Roboto/Roboto-Bold.ttf",20)
    # Run until the user asks to quit
    run = True
    turn = 0
    End = 0
    sel_qty = 0
    can_select = True
    big_card = None
    new_card = None
    Now = Window = 0
    paid_tokens = {}

    allplayer, player_list, cha, bg_player, player_name, player_score = getPlayerData(name_user, act_user)

    card_list = read_card_data('CSV\CardData.csv')
    noble_list = read_noble_data('CSV\\NobleData.csv')

    # random development card and noble card order
    random_order = []
    for i in range(3):
        rand_lv = random.sample(range(len(card_list[i])), len(card_list[i]))
        random_order.append(rand_lv)
    noble_qty = allplayer + 1
    noble_order = random.sample(range(len(noble_list)), noble_qty)

    allsprites = pygame.sprite.LayeredDirty()

    # create turn frame that tell whose turn now
    turn_frame = pygame.sprite.DirtySprite()
    turn_frame.image = pygame.image.load('Image\Card\\frame.png').convert_alpha()
    turn_frame.image = pygame.transform.smoothscale(turn_frame.image, (430, 167))
    turn_frame.rect = turn_frame.image.get_rect(topleft = (0, 10))
    allsprites.add(turn_frame)

    get_tokens(allsprites, allplayer)
    place_player_tokens(player_list, allsprites)
    place_own_cards(player_list, allsprites)
    card_counter = place_cards(card_list, allsprites, random_order)      

    # create card quantity sprite for each card deck
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

    # create background image when select a token
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

    # create text box to warn player when he has more than 10 tokens
    msg_font = pygame.font.Font('Font\Roboto\Roboto-Regular.ttf', 15)
    msg_text = 'You have more than 10 Tokens! \nplease click on your token to return.'
    msg_box = pygame.sprite.DirtySprite()
    msg_box.image = pygame.image.load('Image\Card\\ballon.png').convert_alpha()
    msg_box.image = pygame.transform.smoothscale(msg_box.image, (325, 80))
    RuleText.text_block(msg_font, msg_text, 'Black', (25,15), 325, msg_box.image, 10)
    msg_box.rect = msg_box.image.get_rect(bottomleft = (95, 160))
    msg_box.visible = 0
    allsprites.add(msg_box)

    # load background image
    bgimage = pygame.image.load("Image/Card/bg-01.png")
    bgimage = pygame.transform.scale(bgimage, (1280, 720))
    # load deck images
    Deck1 = pygame.image.load('Image/Card/D01.png')
    Deck1 = pygame.transform.smoothscale (Deck1, (122, 167))
    Deck2 = pygame.image.load('Image/Card/D02.png')
    Deck2 = pygame.transform.smoothscale (Deck2, (122, 167))
    Deck3 = pygame.image.load('Image/Card/D03.png')
    Deck3 = pygame.transform.smoothscale (Deck3, (122, 167))

    background = pygame.Surface(screen.get_size()).convert()
    # put background image in background surface
    background.blit(bgimage, (0,0))
    # put players' background image in background surface
    for i, bg in enumerate(bg_player):
        background.blit(bg, (0, 10+177*i))
    # put deck images in background surface
    background.blit(Deck1,(558,533))
    background.blit(Deck2,(558,356))
    background.blit(Deck3,(558,179))

    # draw background
    allsprites.clear(screen, background)

    ################################## For Windowgame when press ESC #########################################
    #define variable for state of the game 0 = No Window , 1 = Window
    freeze = 0
    #Rule start page
    page = 1
    allpage = 20
    #Text for rule
    text_font_bold = pygame.font.Font("Font\Roboto\Roboto-Bold.ttf",40)
    text_font_regular = pygame.font.Font("Font\Roboto\Roboto-Regular.ttf",30)
    #When open rule, set Window = 2
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
            
            # Change cursor mouse to hand when hover hold slot of that player turn
            if event.type == pygame.MOUSEMOTION:
                if player_list[turn].cards['hold'].visible:
                    if player_list[turn].cards['hold'].rect.collidepoint(event.pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    else:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1:
                    if freeze == 0:
                        # main window 
                        if Window == 0:
                            # open select token window when player click on any token pile except gold token pile
                            for i, token in enumerate(allsprites.get_sprites_from_layer(2)[:5]):
                                if token.rect.collidepoint(event.pos) and token.qty > 0:
                                    select_popup.visible = 1
                                    btn_cancel.visible = 1
                                    Window = 1
                                    break    
                            # open big card window when player click on any development card
                            for card in allsprites.get_sprites_from_layer(1):
                                if isinstance(card, CardDirty) and card.rect.collidepoint(event.pos): 
                                    big_card = BigCard(card, (res[0]/2+300, res[1]/2))
                                    allsprites.add(big_card)
                                    Now = Window
                                    Window = 2
                                    break 
                            # if player has held any card, open hold slot window when click on cold card button
                            if player_list[turn].cards['hold'].visible:
                                if player_list[turn].cards['hold'].rect.collidepoint(event.pos):
                                    allsprites.add(hold_pane, btn_close)
                                    for i, card in enumerate(player_list[turn].hold_cards):
                                        card.reposition(hold_pane.rect.x+150+250*i, hold_pane.rect.y+150)
                                        allsprites.add(card)
                                        allsprites.change_layer(card, 3)
                                    Window = 3
                            card.dirty = 1   
                                         
                        # select token window
                        elif Window == 1:
                            # show how many token player has selected
                            for i, token in enumerate(allsprites.get_sprites_from_layer(2)[:5]):
                                if token.rect.collidepoint(event.pos) and token.qty > 0:                             
                                    sel_qty, can_select = select_token(token, allsprites.get_sprites_from_layer(2)[i+5], sel_qty, can_select)
                                    btn_confirm.visible = 1
                                    break
                            # reduce quantity of selected token when click on it
                            for i, sel_token in enumerate(allsprites.get_sprites_from_layer(2)[5:10], start=5):
                                if not sel_token.visible:
                                    continue
                                if sel_token.rect.collidepoint(event.pos):
                                    sel_qty, can_select = get_token_back(allsprites.get_sprites_from_layer(2)[i-5], sel_token, sel_qty, can_select)
                                    if sel_qty == 0:
                                        select_popup.visible = 0                                    
                                        btn_cancel.visible = btn_confirm.visible = 0
                                        Window = 0
                            # cancel selected tokens. return all selected tokens to the pile
                            if btn_cancel.visible:
                                if btn_cancel.rect.collidepoint(event.pos):
                                    cancel_token(allsprites.get_sprites_from_layer(2)[:5], allsprites.get_sprites_from_layer(2)[5:10])
                                    sel_qty = 0
                                    can_select = True
                                    btn_cancel.unhover()   
                                    select_popup.visible = 0                         
                                    btn_cancel.visible = btn_confirm.visible = 0
                                    Window = 0
                            # take all selected tokens
                            if btn_confirm.visible:
                                if btn_confirm.rect.collidepoint(event.pos):
                                    take_tokens(allsprites.get_sprites_from_layer(2)[5:10], player_list[turn])
                                    sel_qty = 0
                                    can_select = True
                                    btn_confirm.unhover()
                                    select_popup.visible = 0
                                    btn_cancel.visible = btn_confirm.visible = 0
                                    # check if player has token mor than 10. if true, go to return token window
                                    if check_player_token(player_list[turn]):
                                        msg_box.visible = 1
                                        Window = 4
                                    else:
                                        # check if player can take any noble card
                                        available_idx = check_noble(noble_list, noble_order, player_list[turn])
                                        # no noble card available for player. change turn and go back to main window
                                        if not available_idx:  
                                            turn = endturn(turn,allplayer)                                            
                                            turn_frame.rect.topleft = (0, 10+177*turn)
                                            msg_box.rect.bottomleft = (95, 160+177*turn)
                                            turn_frame.dirty = 1 
                                            Window = 0  
                                        # noble card available. go to select noble card window
                                        else:
                                            for idx in available_idx:
                                                btn_sel_list[idx].visible = 1
                                            Window = 5       

                        # big card window
                        elif Window == 2:
                            # recalculate mouse position for using with button in big card window
                            pos_check = (
                                event.pos[0] - big_card.rect.topleft[0],
                                event.pos[1]- big_card.rect.topleft[1]
                            )
                            # close big card
                            if big_card.btn_close.rect.collidepoint(pos_check):
                                # delete big card from the screen and allsprites. 
                                big_card.kill()
                                Window = Now
                            #  hold a card
                            if not big_card.is_hold:
                                if big_card.btn_hold.rect.collidepoint(pos_check):
                                    if len(player_list[turn].hold_cards) < 3:
                                        hold_card(big_card.selected_card, player_list[turn], allsprites.sprites()[1])
                                        player_list[turn].cards['hold'].qty = len(player_list[turn].hold_cards)
                                        player_list[turn].cards['hold'].update_text(f'{player_list[turn].cards["hold"].qty}')
                                        player_list[turn].cards['hold'].visible = player_list[turn].is_hold_card()                                        
                                        ####################################################################Change player to player_list[turn]
                                        new_card = get_new_card(big_card.selected_card, card_list, card_counter, random_order)
                                        update_card_qty(card_counter, card_list, card_qty_list, big_card.selected_card.level, allsprites)
                                        big_card.kill()
                                        if new_card != None:
                                            allsprites.add(new_card)
                                        #####################################################
                                        # check if player has token mor than 10. if true, go to return token window
                                        if check_player_token(player_list[turn]):
                                            msg_box.visible = 1
                                            Window = 4
                                        else:
                                            # check if player can take any noble card
                                            available_idx = check_noble(noble_list, noble_order, player_list[turn])
                                            # no noble card available for player. change turn and go back to main window
                                            if not available_idx:  
                                                turn = endturn(turn,allplayer)
                                                turn_frame.rect.topleft = (0, 10+177*turn)
                                                msg_box.rect.bottomleft = (95, 160+177*turn)
                                                turn_frame.dirty = 1 
                                                Window = 0
                                            # noble card available. go to select noble card window
                                            else:
                                                for idx in available_idx:
                                                    btn_sel_list[idx].visible = 1
                                                Window = 5
                                            #################################################################################################
                                            turn_frame.rect.topleft = (0, 10+177*turn)
                                            msg_box.rect.bottomleft = (95, 160+177*turn)
                                            turn_frame.dirty = 1                                    
                            # buy a card
                            if big_card.btn_buy.rect.collidepoint(pos_check):                                
                                # check if player can buy a card
                                if big_card.selected_card.check_req(player_list[turn].tokens, player_list[turn].cards):
                                    paid_tokens = pay_tokens(big_card.selected_card, player_list[turn])
                                    player_score[turn].image = score_font.render(f'{player_list[turn].score}','AA','White')
                                    player_score[turn].rect = player_score[turn].image.get_rect(bottomleft = player_score[turn].rect.bottomleft)
                                    player_score[turn].dirty = 1
                                    ####################################################################Change player to player_list[turn]
                                    # get new card from card pile if bought card is not held
                                    if not big_card.is_hold:
                                        new_card = get_new_card(big_card.selected_card, card_list, card_counter, random_order)
                                        update_card_qty(card_counter, card_list, card_qty_list, big_card.selected_card.level, allsprites)
                                    # return tokens to pile
                                    for i, token in enumerate(allsprites.get_sprites_from_layer(2)[:5]):
                                        if paid_tokens[token.colors] > 0:
                                            token.qty += paid_tokens[token.colors]
                                            token.update_text(f'{token.qty}')                                    
                                            token.visible = 1
                                    gold_token = allsprites.sprites()[1]
                                    gold_token.qty += paid_tokens['gold']
                                    gold_token.update_text(f'{gold_token.qty}')
                                    gold_token.show_token()
                                    # remove card from player's hold card list, if any
                                    if big_card.selected_card in player_list[turn].hold_cards:
                                        player_list[turn].hold_cards.remove(big_card.selected_card)
                                        player_list[turn].cards['hold'].qty = len(player_list[turn].hold_cards)
                                        player_list[turn].cards['hold'].update_text(f'{player_list[turn].cards["hold"].qty}')
                                        player_list[turn].cards['hold'].visible = player_list[turn].is_hold_card()
                                    big_card.kill()   
                                    if new_card != None:
                                        allsprites.add(new_card)                
                                    if big_card.is_hold:
                                        allsprites.remove_sprites_of_layer(3)   
                                    # check if player can take any noble card                         
                                    available_idx = check_noble(noble_list, noble_order, player_list[turn])
                                    # no noble card available for player. change turn and go back to main window
                                    if not available_idx: 
                                        Window = 0                                  
                                        ##############################################################
                                        End = endgame(turn,player_list,End)
                                        turn = endturn(turn,allplayer)
                                        ########################################################################################################
                                        turn_frame.rect.topleft = (0, 10+177*turn)
                                        msg_box.rect.bottomleft = (95, 160+177*turn)
                                        turn_frame.dirty = 1
                                    # noble card available. go to select noble card window
                                    else:
                                        for idx in available_idx:
                                            btn_sel_list[idx].visible = 1
                                        Window = 5 
                            big_card.dirty = 1 

                        # select noble card window
                        elif Window == 5:
                            for idx in available_idx:
                                noble = noble_list[noble_order[idx]]
                                if btn_sel_list[idx].rect.collidepoint(event.pos):
                                    take_noble(noble, player_list[turn], btn_sel_list)
                                    player_score[turn].image = score_font.render(f'{player_list[turn].score}','AA','White')                                    
                                    player_score[turn].rect = player_score[turn].image.get_rect(bottomleft = player_score[turn].rect.bottomleft)
                                    player_score[turn].dirty = 1
                                    End = endgame(turn,player_list,End)
                                    turn = endturn(turn,allplayer)
                                    turn_frame.rect.topleft = (0, 10+177*turn)
                                    msg_box.rect.bottomleft = (95, 160+177*turn)
                                    turn_frame.dirty = 1 
                                    Window = 0
                                    break 

                        # hold card slot window
                        if Window == 3:
                            # show big card when click on hold card  
                            for card in player_list[turn].hold_cards:
                                if card.rect.collidepoint(event.pos):
                                    big_card = BigCard(card, (res[0]/2+300, res[1]/2), True)                                
                                    allsprites.add(big_card)
                                    Now = Window
                                    Window = 2
                                    break  
                            # close hold card slot
                            if btn_close.rect.collidepoint(event.pos):
                                allsprites.remove_sprites_of_layer(3)
                                Window = 0                        
                            hold_pane.dirty = 1 

                        # return token window
                        if Window == 4:
                            total_token = return_token(allsprites.get_sprites_from_layer(2)[:5], allsprites.sprites()[1], player_list[turn], event.pos)
                            if total_token <= 10:
                                msg_box.visible = 0
                                # check if player can take any noble card
                                available_idx = check_noble(noble_list, noble_order, player_list[turn])
                                # no noble card available for player. change turn and go back to main window
                                if not available_idx: 
                                    turn = endturn(turn,allplayer)
                                    turn_frame.rect.topleft = (0, 10+177*turn)
                                    msg_box.rect.bottomleft = (95, 160+177*turn)
                                    turn_frame.dirty = 1 
                                    Window = 0
                                # noble card available. go to select noble card window
                                else:
                                    for idx in available_idx:
                                        btn_sel_list[idx].visible = 1
                                    Window = 5
                                    
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
            result_player_list = sorted(player_list, key=lambda x: (-x.score,x.sum_card()))
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
            if Window == 1:
                if btn_cancel.rect.collidepoint(pygame.mouse.get_pos()):
                    btn_cancel.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                else:
                    btn_cancel.unhover()

                if btn_confirm.rect.collidepoint(pygame.mouse.get_pos()):
                    btn_confirm.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                else:
                    btn_confirm.unhover()                    

            if Window == 5:
                for btn_select in btn_sel_list:
                    if btn_select.rect.collidepoint(pygame.mouse.get_pos()):
                        btn_select.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                    else:
                        btn_select.unhover()

            if Window == 3:
                if btn_close.rect.collidepoint(pygame.mouse.get_pos()):
                    btn_close.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                else:
                    btn_close.unhover()
                
            if big_card != None:
                pos_check = (
                    pygame.mouse.get_pos()[0] - big_card.rect.topleft[0],
                    pygame.mouse.get_pos()[1]- big_card.rect.topleft[1]
                )
                if big_card.btn_close.rect.collidepoint(pos_check):
                    big_card.btn_close.hover((153,0,0), 'Image\Button\CloseButtonhover.png')
                    big_card.update_button()
                else:
                    big_card.btn_close.unhover()
                    big_card.update_button()

                if big_card.btn_buy.rect.collidepoint(pos_check):
                    big_card.btn_buy.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                    big_card.update_button()
                else:
                    big_card.btn_buy.unhover()
                    big_card.update_button()

                if not big_card.is_hold:
                    if big_card.btn_hold.rect.collidepoint(pos_check):
                        big_card.btn_hold.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                        big_card.update_button()
                    else:
                        big_card.btn_hold.unhover()
                        big_card.update_button()
            
            if Window == 4:
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
            RuleText.ruletext (page,text_font_bold,text_font_regular,screen)
        
        pygame.display.update(rects)
    # Done! Time to quit.
    pygame.quit()
    exit()
if __name__ == "__main__":
    gameBoard(name_user, act_user,result_player_list)



    