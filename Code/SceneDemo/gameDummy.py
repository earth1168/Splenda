# Written by Walan 1057
# This script shows dummy game screen that tells character choosen by each player.

import pygame
from sys import exit

# show_players: shows character choosen by each player
# parameters:
# screen -> screen to draw component onto
# res -> game resolution
# chr_list -> list of the selected characters
def show_players(screen, res, chr_list):
    font = pygame.font.Font(None, 30)
    i = 0

    for playerID in chr_list:
        player_text = f'player {i+1}: choose {playerID}'
        player_msg = font.render(player_text, False, 'white')
        pmsg_rect = player_msg.get_rect(midleft = (res[0]/4, res[1]/10*(3+i)))
        screen.blit(player_msg, pmsg_rect)
        i += 1

# game_screen: called by scene manager to display game screen
# parameters:
# screen -> screen to draw component onto
# res -> game resolution
# FPS -> FPS capped
# chr_list -> list of the selected characters
def game_screen(screen, res, FPS, chr_list):
    clock = pygame.time.Clock()
    player_num = len(chr_list)

    font1 = pygame.font.Font(None, 30)
    font2 = pygame.font.Font(None, 50)
    message1 = font1.render(f'{player_num} players', False, 'white')
    msg1_rect = message1.get_rect(midtop = (res[0]/2, res[1]/6))
    message2 = font2.render(f'Press ENTER to go back to menu', False, 'white')
    msg2_rect = message2.get_rect(midtop = (res[0]/2, res[1]/10*9))

    while True:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                # If pressed ENTER key
                if event.key == pygame.K_RETURN:
                    # clear the selected character list
                    chr_list.clear()
                    print("change to: menu")
                    # go to menu scene
                    return "menu"

        # Display text
        screen.fill("lightcyan4")
        screen.blit(message1, msg1_rect)
        show_players(screen, res, chr_list)
        screen.blit(message2, msg2_rect)

        # Update the screen
        pygame.display.update()
        # capped fps
        clock.tick(FPS)


# Code below:
# work like game_screen module
# used for test the scene before put to module 
# can uncomment (ctrl+/) to run from this file

# pygame.init()

# res = (800, 400)
# screen = pygame.display.set_mode(res)
# clock = pygame.time.Clock()

# chr_list = [0, 2, 1]
# player_num = len(chr_list)

# font1 = pygame.font.Font(None, 30)
# message1 = font1.render(f'Select {player_num} Characters', False, 'white')
# msg1_rect = message1.get_rect(midtop = (res[0]/2, res[1]/6))


# while True:
#     # Event loop
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
#             pygame.quit()
#             exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 print("you pressed ENTER")

#     screen.fill("lightcyan4")
#     screen.blit(message1, msg1_rect)

#     show_players(screen, res, chr_list)

#     # Update the screen
#     pygame.display.update()
#     clock.tick(60)
