import pygame
from classButton import Button
from classPlayer import Player

pygame.init()
#Set variable for window size
res = (1280, 720)
screen = pygame.display.set_mode(res)
#Set FPS of the game
FPS = 30

player = Player(0, 0, 'testB0i')

class Token(Button):
    def __init__(self, position, size, img_path, colors, qty):
        super().__init__(position, size, '', 0, img_path)
        self.colors = colors
        self.qty = qty

    def destroy(self):
        if self.qty == 0:
            self.kill()

def take_tokens(token: Token, player: Player):
    if token.qty > 0:
        player.tokens[token.colors] += 1
        token.qty -= 1
    else:
        token.to_draw = False
    token.destroy()

def pay_token(token: Token, player: Player):
    player.tokens[token.colors] -= 1
    token.qty += 1

def testBoard(screen, res, FPS, player):
    clock = pygame.time.Clock()
    run = True
    tok_col = ['white', 'blue', 'green', 'red', 'black']
    #         'white', 'blue', 'green', 'red', 'black', 'gold'
    tok_qty = [5,       5,      5,      5,      5,      5]

    tok_group = pygame.sprite.Group()
    for i in range(5):
        tok = Token((150, 150+100*i), (100, 100), 'Image\Button\CloseButton.png', tok_col[i], 5)
        tok_group.add(tok)

    tokens_box_rect = pygame.Rect(100, 100, 100, 500)

    font = pygame.font.Font(None, 30)
    msg1 = font.render('Owned Tokens:', True, 'white')
    msg1_rect = msg1.get_rect(center = (res[0]/2, res[1]/8))
    tokens_text = font.render(f'{player.tokens}', True, 'white')
    tok_t_rect = tokens_text.get_rect(center = (res[0]/2, res[1]/6))

    while run:
        m_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # press x key on keyboard to exit
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i, tok in enumerate(tok_group):
                        tok.to_draw = True
                        if tok.is_collide_mouse(event.pos):
                            print(f'hit {tok.colors}')
                            take_tokens(tok, player)
                            print(tok.to_draw)
                            break

            if event.type == pygame.KEYDOWN:
                for key, token in enumerate(tok_group, start=pygame.K_1):
                    if event.key == key:
                        pay_token(token, player)

        tokens_text = font.render(f'{player.tokens}', True, 'white')

        clock.tick(FPS)
        screen.fill('darkorchid3')
        screen.blit(msg1, msg1_rect)
        screen.blit(tokens_text, tok_t_rect)
        pygame.draw.rect(screen, 'gray84', tokens_box_rect)
        tok_group.draw(screen)
        tok_group.update()
        pygame.display.update()
    
    pygame.quit()
    exit()

if __name__ == '__main__':
    testBoard(screen, res, FPS, player)