# Written by Walan 1057
# This script shows how BonusCard and Card class work.

import pygame
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
    for i in range(len(cards_list)):
        cards_list[i].set_req(req_list[i])

# reduce required tokens from player
def pay_tokens(card_group: pygame.sprite.Group, card: Card, player: Player):
    print('card requirement:')
    print(f'{card.requirements}')
    card.pay_tokens(player.tokens)
    player.score += card.point
    card_group.remove(card)
    print(f'take card: +{card.point} points')
    print()

def showCard(screen, FPS):
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    run = True
    isEnough = True
    card_points = [1, 3, 4]
    card_req = [ 
        [2, 2, 0, 0, 2],
        [0, 3, 2, 4, 0],
        [0, 5, 2, 2, 2]
    ]
    card_colors = ['white', 'black', 'red']

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
        card_group.add(Card(i, card_points[i], (110, 175), 'Image/Card/Potion.png', card_colors[i]))
    # set cards' position
    for i in range(3):
        card_group.sprites()[i].set_pos(res[0]/4*(i+1), res[1]/2)
    # set cards' requirements
    set_show_card_req(card_group.sprites(), card_req)    
    c0 = card_group.sprites()[0]
    c1 = card_group.sprites()[1]
    c2 = card_group.sprites()[2]

    # instantiate player object
    p0 = Player(0, 0, 'TEST b0i')
    # set number of cards owned by player
    p0.cards = {
        "white": 5,
        "blue": 4,
        "green": 4,
        "red": 5,
        "black": 5
    }
    # set tokens player has
    p0.tokens = {
        "white": 2,
        "blue": 4,
        "green": 1,
        "red": 2,
        "black": 1,
        "gold": 3
    }


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
    msg2 = font.render('Not enough TOKENS!', True, 'red')
    msg2_resct = msg2.get_rect(center = (res[0]/2, res[1]/8*6))

    while run:
        for event in pygame.event.get():
            # press x key on keyboard to exit
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
                run = False

            # change cursor when hover on a card
            if event.type == pygame.MOUSEMOTION:
                if card_group.has(c0) and c0.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                
                elif card_group.has(c1) and c1.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                
                elif card_group.has(c2) and c2.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isEnough = True
                    # if c0 still on the screen and click on it, then sheck player's tokens
                    if card_group.has(c0) and c0.rect.collidepoint(pygame.mouse.get_pos()):
                        isEnough = c0.check_req(p0.tokens)
                        if isEnough :
                            pay_tokens(card_group, c0, p0)
                    # if c1 still on the screen and click on it, then sheck player's tokens
                    if card_group.has(c1) and c1.rect.collidepoint(pygame.mouse.get_pos()):
                        isEnough = c1.check_req(p0.tokens)
                        if isEnough :
                            pay_tokens(card_group, c1, p0)
                    # if c2 still on the screen and click on it, then sheck player's tokens
                    if card_group.has(c2) and c2.rect.collidepoint(pygame.mouse.get_pos()):
                        isEnough = c2.check_req(p0.tokens)
                        if isEnough :
                            pay_tokens(card_group, c2, p0)
                    # update text after click a card
                    score_text = font.render(f'SCORE: {p0.score}', True, 'white')
                    tokens_text = font.render(f'{p0.tokens}', True, 'white')

        

        # draw texts and cards
        clock.tick(FPS)
        screen.fill('blue4')
        screen.blit(msg1, msg1_rect)
        screen.blit(score_text, score_t_rect)
        screen.blit(tokens_text, tok_t_rect)
        # if tokens not enough, the show text 'Not enough TOKENS!'
        if not isEnough:
            screen.blit(msg2, msg2_resct)
        card_group.draw(screen)
        card_group.update()
        pygame.display.update()        
    
    pygame.quit()
    exit()

if __name__ == '__main__':
    showCard(screen, FPS)