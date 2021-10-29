# Written by Walan 1057
# This script shows how BonusCard and Card class work.

import pygame
from classButton import Button
from classCard import BonusCard, Card
from classPlayer import Player

pygame.init()
#Set variable for window size
# WIDTH, HEIGHT = 1280,720
res = (1280, 720)
screen = pygame.display.set_mode(res)
#Set FPS of the game
FPS = 60

# set requirements for all cards on screen
def set_show_card_req(cards_list, req_list):
    for i, card in enumerate(cards_list):
        card.set_req(req_list[i])

def set_player(player: Player):
    # set number of cards owned by player
    player.cards = {
        "white": 0,
        "blue": 1,
        "green": 1,
        "red": 0,
        "black": 2
    }
    # set tokens player has
    player.tokens = {
        "white": 2,
        "blue": 1,
        "green": 1,
        "red": 2,
        "black": 1,
        "gold": 0
    }

# reduce required tokens from player
def pay_tokens(card_group: pygame.sprite.Group, card: Card, player: Player):
    print('card requirement:')
    print(f'{card.requirements}')
    card.pay_tokens(player.tokens, player.cards)
    player.score += card.point
    player.cards[card.colors] += 1
    card_group.remove(card)
    print(f'take card: +{card.point} points')
    print(f'owned cards: {player.cards}')
    print()

def hold_card(card_group: pygame.sprite.Group, card: Card, player: Player):
    player.hold_cards.append(card)
    if player.tokens['gold'] < 3:
        player.tokens['gold'] += 1
    card_group.remove(card)
    print(f'hold {len(player.hold_cards)} card(s)')
    print()

def get_big_card(card: Card):
    big_card = pygame.image.load(card.bg_path).convert_alpha()
    big_card = pygame.transform.scale(big_card, (card.size[0]*3, card.size[1]*3))
    return big_card

def show_big_card(screen, big_card, close_btn, button_group):
    big_card_rect = big_card.get_rect(center = (res[0]/2, res[1]/2))
    close_btn.sprite.position = big_card_rect.topright
    for i, btn in enumerate(button_group.sprites()):
        # btn.rect.topright = (big_card_rect.right+10, big_card_rect.top + 80 + 60*i)
        btn.position = (big_card_rect.right - 80, big_card_rect.top + 145 + 65*i)
    screen.blit(big_card, big_card_rect)
    close_btn.draw(screen)
    close_btn.update()
    button_group.draw(screen)
    button_group.update()

def testCard(screen, res, FPS):
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    run = True
    isEnough = True
    big_card = None
    big_card_rect = None
    card_points = [1, 3, 4]
    card_req = [ 
        [2, 2, 0, 0, 2],
        [0, 3, 2, 4, 0],
        [0, 5, 2, 2, 2]
    ]
    card_colors = ['red', 'black', 'white']

    # instantiate sprite group
    bonus_group = pygame.sprite.Group()
    card_group = pygame.sprite.Group()
    btn_group = pygame.sprite.Group()

    # instantiate bonus card object
    bc0 = BonusCard(0, 4, (110, 175), 'Image/Card/Potion.png')
    # set bonus card's position
    bc0.set_pos(res[0]/2, res[1]/2)
    # set bonus card's requirements
    bc0.set_req((0, 4, 4, 4, 0))
    bonus_group.add(bc0)

    # instantiate card objects
    for i in range(3):
        card_group.add(Card(i, card_points[i], (110, 175), 'Image/Card/Potion.png', 1, card_colors[i]))
    # set cards' position
    for i, card in enumerate(card_group.sprites(), start=1):
        card.set_pos(res[0]/4*i, res[1]/2+100)
    # set cards' requirements
    set_show_card_req(card_group.sprites(), card_req)    
    c0 = card_group.sprites()[0]
    c1 = card_group.sprites()[1]
    c2 = card_group.sprites()[2]

    # instantiate player object
    p0 = Player(0, 0, 'TEST b0i')
    set_player(p0)

    btn_hold = Button((200, 200), (130, 50), 'Hold', 30, 'Image\Button\ButtonNewUnhover.png', 'black')
    btn_buy = Button((400, 200), (130, 50), 'Buy', 30, 'Image\Button\ButtonNewUnhover.png', 'black')
    btn_group.add(btn_hold, btn_buy)

    btn_close = pygame.sprite.GroupSingle()
    btn_close.add(Button((100, 100), (75, 75), '', 0, 'Image\Button\CloseButton.png'))

    # test check requirement function for bonus class
    print('Bonus Card:')
    print(bc0.requirements)
    # if player can take a bonus card (pass the requirements), then add score
    if bc0.check_req(p0.cards):
        print(f'enough cards: +{bc0.point} points')
        p0.score += bc0.point
    else:
        print("not enough cards")
    print()

    # instatiate texts to show on screen
    msg1 = font.render('Owned Tokens:', True, 'white')
    msg1_rect = msg1.get_rect(center = (res[0]/2, res[1]/8))
    score_text = font.render(f'SCORE: {p0.score}', True, 'white')
    score_t_rect = score_text.get_rect(topright = (res[0]-res[0]/25, res[1]/20))
    tokens_text = font.render(f'{p0.tokens}', True, 'white')
    tok_t_rect = tokens_text.get_rect(center = (res[0]/2, res[1]/6))
    cards_text = font.render(f'{p0.cards}', True, 'white')
    cards_t_rect = cards_text.get_rect(center = (res[0]/2, res[1]/6+100))
    msg2 = font.render('Not enough TOKENS!', True, 'red')
    msg2_resct = msg2.get_rect(center = (res[0]/2, res[1]/8*7))
    msg3 = font.render('Owned Cards:', True, 'white')
    msg3_rect = msg3.get_rect(center = (res[0]/2, res[1]/8+100))

    while run:
        m_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # press x key on keyboard to exit
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
                run = False

            # change cursor when hover on a card
            if event.type == pygame.MOUSEMOTION:
                if big_card == None:
                    if card_group.has(c0) and c0.rect.collidepoint(m_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    
                    elif card_group.has(c1) and c1.rect.collidepoint(m_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    
                    elif card_group.has(c2) and c2.rect.collidepoint(m_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    else:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                else:
                    if btn_close.sprite.rect.collidepoint(m_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    elif btn_group.sprites()[0].rect.collidepoint(m_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                    elif btn_group.sprites()[1].rect.collidepoint(m_pos):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    
                    else:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isEnough = True
                    
                    if big_card == None:
                        # if c0 still on the screen and click on it, then sheck player's tokens
                        if card_group.has(c0) and c0.rect.collidepoint(m_pos):
                            big_card = get_big_card(c0)
                            selected_card = c0
                            # isEnough = c0.check_req(p0.tokens, p0.cards)
                            # if isEnough :
                            #     pay_tokens(card_group, c0, p0)
                        # if c1 still on the screen and click on it, then sheck player's tokens
                        if card_group.has(c1) and c1.rect.collidepoint(m_pos):
                            big_card = get_big_card(c1)
                            selected_card = c1
                            # isEnough = c1.check_req(p0.tokens, p0.cards)
                            # if isEnough :
                            #     pay_tokens(card_group, c1, p0)
                        # if c2 still on the screen and click on it, then sheck player's tokens
                        if card_group.has(c2) and c2.rect.collidepoint(m_pos):
                            big_card = get_big_card(c2)
                            selected_card = c2
                            # isEnough = c2.check_req(p0.tokens, p0.cards)
                            # if isEnough :
                            #     pay_tokens(card_group, c2, p0)
                    else:
                        if btn_close.sprite.rect.collidepoint(m_pos):
                            big_card = None
                        
                        if btn_group.sprites()[0].rect.collidepoint(m_pos):
                            hold_card(card_group, selected_card, p0)
                            big_card = None

                        if btn_group.sprites()[1].rect.collidepoint(m_pos):
                            isEnough = selected_card.check_req(p0.tokens, p0.cards)
                            if isEnough :
                                pay_tokens(card_group, selected_card, p0)
                            big_card = None
                        
                    # update text after click a card
                    score_text = font.render(f'SCORE: {p0.score}', True, 'white')
                    tokens_text = font.render(f'{p0.tokens}', True, 'white')
                    cards_text = font.render(f'{p0.cards}', True, 'white')        

        # draw texts and cards
        clock.tick(FPS)
        screen.fill('blue4')
        screen.blit(msg1, msg1_rect)
        screen.blit(score_text, score_t_rect)
        screen.blit(tokens_text, tok_t_rect)
        screen.blit(msg3, msg3_rect)
        screen.blit(cards_text, cards_t_rect)
        # if tokens not enough, the show text 'Not enough TOKENS!'
        if not isEnough:
            screen.blit(msg2, msg2_resct)
        card_group.draw(screen)
        card_group.update()
        if big_card != None:
            show_big_card(screen, big_card, btn_close, btn_group)
        pygame.display.update()        

    pygame.quit()
    exit()

if __name__ == '__main__':
    testCard(screen, res, FPS)