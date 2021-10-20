import pygame
import sys
import os

path = os.getcwd()
sys.path.insert(0, path)
from Code.classButton import Button 

pygame.init()
#Set variable for window size
WIDTH, HEIGHT = 1280,720
res = (1280,720)
screen = pygame.display.set_mode(res)
#Set FPS of the game
FPS = 60

def change_resolution(screen, res_old, res_new):
    res_old = res_new
    screen = pygame.display.set_mode(res_old)

def btn_reposition(group, res, btn_size, t_size):
    i = 1
    for btn in group:
        btn.resize(btn_size)
        btn.reposition((res[0]/4*i, res[1]/2))
        btn.resize_text(t_size)
        i+=1
        

def option_screen(screen, FPS, res):
    clock = pygame.time.Clock()
    run = True
    btn_size = list(((176, 88), (216, 108), (256, 128)))
    t_size = list((20, 25, 30))
    button_group = pygame.sprite.Group()    
    b0 = Button((res[0]/4, res[1]/2), (256, 128), '800 x 600', 30, 'Image/Button/testButton-01.png', 'black')
    b1 = Button((res[0]/4*2, res[1]/2), (256, 128), '1280 x 720', 30, 'Image/Button/testButton-01.png', 'black')
    b2 = Button((res[0]/4*3, res[1]/2), (256, 128), '1920 x 1080', 30, 'Image/Button/testButton-01.png', 'black')
    button_group.add(b0, b1, b2)    

    while run:
        for event in pygame.event.get():
            # press x key on keyboard to exit
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
                run = False

            if event.type == pygame.MOUSEMOTION:
                if b0.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                
                elif b1.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                
                elif b2.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if b0.rect.collidepoint(pygame.mouse.get_pos()):
                        print("click b0")
                        # change_resolution(screen, res, (800, 600))
                        res = (800, 600)
                        btn_reposition(button_group, res, btn_size[0], t_size[0])
                        screen = pygame.display.set_mode(res)
                    elif b1.rect.collidepoint(pygame.mouse.get_pos()):
                        print("click b1")
                        # change_resolution(screen, res, (1280, 720))
                        res = (1280, 720)
                        btn_reposition(button_group, res, btn_size[1], t_size[1])
                        screen = pygame.display.set_mode(res)
                    elif b2.rect.collidepoint(pygame.mouse.get_pos()):
                        print("click b2")
                        # change_resolution(screen, res, (1920, 1080))
                        res = (1920, 1080)
                        btn_reposition(button_group, res, btn_size[2], t_size[2])
                        screen = pygame.display.set_mode(res)
                    print(f'resolution: {res[0]} x {res[1]}')

        clock.tick(FPS)
        screen.fill("grey")
        button_group.draw(screen)
        button_group.update()
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":
    option_screen(screen, FPS, res)