# Written by Walan 1057
# This script shows dummy menu screen.

import pygame
from sys import exit

# menu_screen: called by scene manager to display menu screen
# parameters:
# screen -> screen to draw component onto
# res -> game resolution
# FPS -> FPS capped
def menu_screen(screen, res, FPS):
    clock = pygame.time.Clock()

    font1 = pygame.font.Font(None, 50)
    message1 = font1.render('Select Character: press ENTER', False, 'white')
    msg1_rect = message1.get_rect(midtop = (res[0]/2, res[1]/10*8))

    while True:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                # If pressed ENTER key
                if event.key == pygame.K_RETURN:
                    print("change to: select character")
                    # go to select character scene
                    return "select_character"

        screen.fill("grey")
        screen.blit(message1, msg1_rect)

        # Update the screen
        pygame.display.update()
        # capped fps
        clock.tick(FPS)


# Code below:
# work like menu_screen module
# used for test the scene before put to module 
# can uncomment (ctrl+/) to run from this file

# pygame.init()

# res = (800, 400)
# screen = pygame.display.set_mode(res)
# clock = pygame.time.Clock()

# font1 = pygame.font.Font(None, 50)
# message1 = font1.render('Select Character: press ENTER', False, 'white')
# msg1_rect = message1.get_rect(midtop = (res[0]/2, res[1]/10*8))

# while True:
#     # Event loop
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
#             pygame.quit()
#             exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 print("you pressed ENTER")

#     screen.fill("grey")
#     screen.blit(message1, msg1_rect)

#     # Update the screen
#     pygame.display.update()
#     clock.tick(60)
