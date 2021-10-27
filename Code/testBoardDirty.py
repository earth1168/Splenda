from typing import List
import pygame
from classPlayer import Player
from classButtonDirty import ButtonDirty

pygame.init()
#Set variable for window size
res = (1280, 720)
screen = pygame.display.set_mode(res)
#Set FPS of the game
FPS = 30

player = Player(0, 0, 'testB0i')

class Token(ButtonDirty):
    def __init__(self, position, size, img_path, colors, qty):
        super().__init__(position, size, f'{qty}', 30, img_path, 'black')
        self.colors = colors
        self.qty = qty
        self.qty_change = False

    def change_qty(self, qty_new):
        if self.qty != qty_new:
            self.qty = qty_new
            self.qty_change = True

    def out_of_stock(self):
        if self.qty == 0:
            self.visible = 0

    def update_text(self, text_new):
        if self.qty_change:
            self.text = text_new
            self.t_render = self.font.render(self.text, True, self.t_colors)
            self.image.blit(self.bg, self.bg_rect)
            self.image.blit(self.t_render, self.t_rect)
            self.dirty = 1
            self.qty_change = False

def select_token(sel_token: Token, show_token: Token, sel_qty: int, can_select: bool):
    if can_select:
        if sel_token.qty > 0 and sel_qty < 3 and\
             (show_token.qty == 0 or (sel_token.qty >= 3 and sel_qty == 1 and show_token.qty > 0)):
            show_token.visible = 1
            show_token.change_qty(show_token.qty+1)
            sel_token.change_qty(sel_token.qty-1)
            show_token.update_text(f'{show_token.qty}')
            sel_token.update_text(f'{sel_token.qty}')
            sel_qty += 1
            if show_token.qty > 1 or sel_qty == 3:
                can_select = False
    sel_token.out_of_stock()
    print(f'selected {show_token.colors}: {show_token.qty}')
    return sel_qty, can_select

def return_token(token: Token, show_token: Token, sel_qty, can_select):
    token.change_qty(token.qty + 1)
    show_token.change_qty(show_token.qty - 1)
    sel_qty -= 1
    can_select = True
    token.visible = 1
    if show_token.qty == 0:
        show_token.visible = 0       
    token.update_text(f'{token.qty}')
    show_token.update_text(f'{show_token.qty}')
    return sel_qty, can_select 

def cancel_token(token_list: List[Token], show_token_list: List[Token]):
    for i, show_tok in enumerate(show_token_list):
        if show_tok.qty > 0:
            token_list[i].change_qty(token_list[i].qty + show_tok.qty)
            show_tok.change_qty(0)
            token_list[i].visible = 1
            show_tok.visible = 0       
            token_list[i].update_text(f'{token_list[i].qty}')
            show_tok.update_text(f'{show_tok.qty}') 

def take_tokens(token_list, player: Player):
    for token in token_list:
        player.tokens[token.colors] += token.qty
        token.qty = 0
        token.visible = 0
        token.dirty = 1

def get_tokens(token: Token, player: Player):
    if token.qty > 0:
        player.tokens[token.colors] += 1
        token.qty -= 1
        token.dirty = 1
    print(f'take {token.colors}')
    print(f'player: {token.colors} = {player.tokens[token.colors]}')
    token.out_of_stock()

def pay_token(token: Token, player: Player):
    player.tokens[token.colors] -= 1
    token.qty += 1
    token.visible = 1

def testBoard(screen, res, FPS, player):
    clock = pygame.time.Clock()
    run = True
    sel_qty = 0
    can_select = True
    tok_col = ['white', 'blue', 'green', 'red', 'black']
    #         'white', 'blue', 'green', 'red', 'black', 'gold'
    tok_qty = [5,       5,      5,      5,      5,      5]

    tokens_box_rect = pygame.Rect(250, 150, 100, 500)

    font = pygame.font.Font(None, 30)
    msg1 = font.render('Owned Tokens:', True, 'white')
    msg1_rect = msg1.get_rect(center = (res[0]/2, 20))
    tokens_text = font.render(f'{player.tokens}', True, 'white', 'green')
    tok_t_rect = tokens_text.get_rect(center = (res[0]/2, 50))

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill('darkorchid3')
    background.blit(msg1, msg1_rect)
    # pygame.draw.rect(background, 'gray84', tokens_box_rect)
    
    allsprites = pygame.sprite.LayeredDirty()
    for i in range(5):
        tok = Token((150, 200+100*i), (100, 100), 'Image\Button\CloseButton.png', tok_col[i], 5)
        tok_in_pane = Token((300, 200+100*i), (100, 100), 'Image\Button\CloseButton.png', tok_col[i], 0)
        tok_in_pane.visible = 0
        allsprites.add(tok, tok_in_pane)
        allsprites.change_layer(tok_in_pane, 1)
    tokGold = Token((150, 100), (100, 100), 'Image\Button\CloseButton.png', 'gold', 5)
    allsprites.add(tokGold)

    btn_pane = ButtonDirty((500, 300), (130, 50), 'cancle', 30, 'Image\Button\ButtonNewUnhover.png', 'black')
    btn_confirm = ButtonDirty((500, 400), (130, 50), 'confirm', 30, 'Image\Button\ButtonNewUnhover.png', 'black')
    btn_pane.visible = btn_confirm.visible = 0
    allsprites.add(btn_pane, btn_confirm)

    allsprites.clear(screen, background)
    spr_layer0 = allsprites.get_sprites_from_layer(0)
    spr_layer1 = allsprites.get_sprites_from_layer(1)

    while run:
        for event in pygame.event.get():
            # press x key on keyboard to exit
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # if tokens_box_rect.collidepoint(event.pos):
                    #     print('click on box')
                    for i, token in enumerate(spr_layer0):
                        if i > 4:
                            break
                        if token.is_collide_mouse(event.pos) and token.qty > 0:
                            print(f'hit {token.colors}')
                            btn_pane.visible = btn_confirm.visible = 1
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
                                btn_pane.visible = btn_confirm.visible = 0

                    if btn_pane.visible:
                        if btn_pane.rect.collidepoint(event.pos):
                            print('close token pane')
                            cancel_token(spr_layer0, spr_layer1)
                            sel_qty = 0
                            can_select = True
                            btn_pane.visible = btn_confirm.visible = 0

                    if btn_confirm:
                        if btn_confirm.rect.collidepoint(event.pos):
                            print('take token(s)')
                            take_tokens(spr_layer1, player)
                            sel_qty = 0
                            can_select = True
                            btn_pane.visible = btn_confirm.visible = 0

            # if event.type == pygame.KEYDOWN:
            #     for key, token in enumerate(allsprites.sprites(), start=pygame.K_0):
            #         if event.key == key:
            #             token.visible = not token.visible

            if event.type == pygame.KEYDOWN:
                for key, token in enumerate(allsprites.get_sprites_from_layer(0), start=pygame.K_1):
                    if event.key == key:
                        pay_token(token, player)

        tokens_text = font.render(f'{player.tokens}', True, 'white', 'chartreuse4')

        clock.tick(FPS)        
        rects = allsprites.draw(screen)
        screen.blit(tokens_text, tok_t_rect)
        # pygame.draw.rect(screen, 'gray84', tokens_box_rect, width=4)            
        pygame.display.update(rects)
    
    pygame.quit()
    exit()

if __name__ == '__main__':
    testBoard(screen, res, FPS, player)