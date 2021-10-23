# Written by Walan 1057
# This script shows dummy setting screen.
# dropdown object Demo

import pygame
import sys
import os

path = os.getcwd()
sys.path.insert(0, path)
from Code.classButton import Button
from Code.classDropDrown import DropDown 

pygame.init()
#Set variable for window size
WIDTH, HEIGHT = 1280,720
res = (1280,720)
infoObj = pygame.display.Info()
screen = pygame.display.set_mode(res)
#Set FPS of the game
FPS = 60

# change screen resolution. return new resolution
def change_resolution(screen, res_new, isFullscreen):
    if isFullscreen:
        # flags = pygame.FULLSCREEN | pygame.SCALED
        flags = pygame.FULLSCREEN
    else:
        flags = 0
    screen = pygame.display.set_mode(res_new, flags)
    return res_new

# reposition buttons after change resolution. (need to be refined)
def btn_reposition(group, res, btn_size, t_size):
    for i, btn in enumerate(group.sprites(), start=1):
        btn.resize(btn_size)
        btn.reposition((res[0]/4*i, res[1]/2))
        btn.resize_text(t_size)
    group.sprites()[-1].reposition((int(res[0]/2), int(res[1]/10*8)))        

def option_screen(screen, FPS, res):
    clock = pygame.time.Clock()
    run = True
    old_option = -1
    isFullscreen = False
    window_mode = ['Window', 'Fullscreen']
    res_list = [
        (1280, 720),
        (1920, 1080)
    ]
    # Define color in dropdown ((r, g, b) is allowed to use)
    # hover on main option
    main_active = 'gold1'
    # not hover on main option
    main_deactive = 'goldenrod1'
    # hover on option list
    option_active = 'gainsboro'
    # not hover on option list
    option_deactive = 'gray70'
    btn_size = list(((176, 88), (256, 128), (296, 148)))
    t_size = list((20, 30, 35))
    # Define resolution dropdown object. use default dropdown color and font
    res_option = DropDown(
        0, 0, 200, 50,
        f'{res[0]} x {res[1]}',
        ['1280 x 720', '1920 x 1080'],
        30
    )
    # Change resolution dropdown's position
    res_option.rect.center = screen.get_rect().center
    # Define test dropdown object
    option2 = DropDown(
        0, 0, 200, 50,
        'main',
        ['option 1', 'option 2', 'option 3'],
        30,
        [main_deactive, main_active],
        [option_deactive, option_active],
        'black',
        'Font\Roboto\Roboto-Regular.ttf'
    )
    # Change test dropdown's position
    option2.rect.center = (res[0]/10, res[1]/2)

    # Define buttons and their group (only use fullscreen/window button(b3))
    button_group = pygame.sprite.Group()    
    b0 = Button((res[0]/4, res[1]/2), (256, 128), '800 x 600', 30, 'Image/Button/testButton-01.png', 'black')
    b1 = Button((res[0]/4*2, res[1]/2), (256, 128), '1280 x 720', 30, 'Image/Button/testButton-01.png', 'black')
    b2 = Button((res[0]/4*3, res[1]/2), (256, 128), '1920 x 1080', 30, 'Image/Button/testButton-01.png', 'black')
    b3 = Button((res[0]/2, res[1]/10*8), (256, 128), window_mode[1], 30, 'Image/Button/testButton-01.png', 'black')
    button_group.add(b3)

    # Define text
    font = pygame.font.Font(None, 50)
    msg1 = font.render(f'screen resotution: {res[0]} x {res[1]}', True, 'black')
    msg1_rect = msg1.get_rect(center = (res[0]/2, res[1]/10))

    print(f'monitor width: {infoObj.current_w}')
    print(f'monitor height: {infoObj.current_h}')    

    while run:
        event_list = pygame.event.get()
        for event in event_list:
            # press x key on keyboard to exit
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
                run = False

            if event.type == pygame.MOUSEMOTION:
                
            #     if b0.rect.collidepoint(pygame.mouse.get_pos()):
            #         pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                
            #     elif b1.rect.collidepoint(pygame.mouse.get_pos()):
            #         pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                
            #     elif b2.rect.collidepoint(pygame.mouse.get_pos()):
            #         pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                if b3.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
            #         if b0.rect.collidepoint(pygame.mouse.get_pos()):
            #             print("click b0")
            #             res = change_resolution(screen, (800, 600), isFullscreen)
            #             btn_reposition(button_group, res, btn_size[0], t_size[0])
            #         elif b1.rect.collidepoint(pygame.mouse.get_pos()):
            #             print("click b1")
            #             res = change_resolution(screen, (1280, 720), isFullscreen)
            #             btn_reposition(button_group, res, btn_size[1], t_size[1])
            #         elif b2.rect.collidepoint(pygame.mouse.get_pos()):
            #             print("click b2")
            #             res = change_resolution(screen, (1920, 1080), isFullscreen)
            #             btn_reposition(button_group, res, btn_size[2], t_size[2])
                    # if click on fullscreen/window button, then change display mode
                    if b3.rect.collidepoint(pygame.mouse.get_pos()):
                        print("click b2")
                        isFullscreen = not isFullscreen
                        # change text on the button
                        if isFullscreen:
                            b3.text = window_mode[0]
                        else:
                            b3.text = window_mode[1]
                        # res = (infoObj.current_w, infoObj.current_h)
                        res = change_resolution(screen, res, isFullscreen)                                        
            #         print(f'resolution: {res[0]} x {res[1]}')
            #         msg1 = font.render(f'screen resotution: {res[0]}x{res[1]}', True, 'black')
            #         msg1_rect = msg1.get_rect(center = (res[0]/2, res[1]/10))

        # get selected option from dropdown
        selected_option = res_option.update(event_list)
        if selected_option >= 0:
            res_option.main = res_option.options[selected_option]
            # if select a new resolution, then change resolution
            if old_option != selected_option:
                # change resolution to the selected resolution
                res = change_resolution(screen, res_list[selected_option], isFullscreen)
                # update resolution dropdown's position
                res_option.rect.center = screen.get_rect().center
                old_option = selected_option
                print(f'resolution: {res[0]} x {res[1]}')
                # update text
                msg1 = font.render(f'screen resotution: {res[0]} x {res[1]}', True, 'black')
                msg1_rect = msg1.get_rect(center = (res[0]/2, res[1]/10))

        # get selected option from dropdown
        sel_op = option2.update(event_list)
        if sel_op >= 0:
            option2.main = option2.options[sel_op]               

        clock.tick(FPS)
        screen.fill("grey")
        screen.blit(msg1, msg1_rect)
        # draw button
        button_group.draw(screen)
        button_group.update()
        # draw resolution option
        res_option.draw(screen)
        # draw test option
        option2.draw(screen)
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":
    option_screen(screen, FPS, res)