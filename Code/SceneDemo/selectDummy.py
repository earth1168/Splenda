# Written by Walan 1057
# This script shows dummy select character screen, 
#             determine character that selected by player,
#             and update character list.
# You can select character by press number key (1-6). 
# Minimum player: 2
# Maximum player: 4

import pygame
from sys import exit

# display_chr: display text to show what character that player currently choose before confirm
# parameters:
# screen -> screen to draw component onto
# res -> game resolution
# chr_id -> ID of the choosen character
def display_chr(screen, res, chr_id):
    font = pygame.font.Font(None, 50)
    chr_message = font.render(f'select: {chr_id}', False, 'white')
    chr_msg_rect = chr_message.get_rect(center = (res[0]/2, res[1]/3))
    screen.blit(chr_message, chr_msg_rect)

# display_list: display text to show list of selected characters
# parameters:
# screen -> screen to draw component onto
# res -> game resolution
# chr_list -> list of the selected characters
def display_list(screen, res, chr_list):
    font = pygame.font.Font(None, 30)
    message2 = font.render(f'Selected character:{chr_list}', False, 'white')
    msg2_rect = message2.get_rect(topleft = (res[1]/15, res[1]/15))
    screen.blit(message2, msg2_rect)

# check_select: check if choosen character is valid and can be selected. if valid, then add to character list
# parameters:
# chr_id -> ID of the choosen character
# chr_list -> list of the selected characters
def check_select(chr_id, chr_list):
    # if player has chose character and the choosen character not it the list yet
    if chr_id != -1 and chr_id not in chr_list and len(chr_list) < 4:
        # add choosen character to the character list
        chr_list.append(chr_id)
        print(f'add {chr_id}')

# check_player_number: check if there are at least 2 players. if true, then display start game text
# parameters:
# screen -> screen to draw component onto
# res -> game resolution
# num -> number of players that have selected a chaaracter
def check_player_number(screen, res, num):
    font = pygame.font.Font(None, 50)
    message3 = font.render('press ENTER to continue', False, 'white')
    msg3_rect = message3.get_rect(midtop = (res[0]/2, res[1]/10*9))

    if num >= 2:
        screen.blit(message3, msg3_rect)

# select_screen: called by scene manager to display select character screen
# parameters:
# screen -> screen to draw component onto
# res -> game resolution
# FPS -> FPS capped
# chr_list -> list of the selected characters
def select_screen(screen, res, FPS, chr_list):
    clock = pygame.time.Clock()

    chr_font1 = pygame.font.Font(None, 50)
    chr_id = -1 #-1 -> player doesn't choose any character 
    message1 = chr_font1.render('Press SPACE to select', False, 'white')
    msg1_rect = message1.get_rect(midtop = (res[0]/2, res[1]/10*7))

    while True:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                # if press SPACE key
                if event.key == pygame.K_SPACE:
                    check_select(chr_id, chr_list)

                # if press ENTER key when there are at least 2 players
                if event.key == pygame.K_RETURN and player_num >= 2:
                    print("change to: game")
                    # go to game scene
                    return "game"

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            chr_id = 0
        elif keys[pygame.K_2]:
            chr_id = 1
        elif keys[pygame.K_3]:
            chr_id = 2
        elif keys[pygame.K_4]:
            chr_id = 3
        elif keys[pygame.K_5]:
            chr_id = 4
        elif keys[pygame.K_6]:
            chr_id = 5        
        player_num = len(chr_list)
        
        # Display text
        screen.fill("black")
        display_list(screen, res, chr_list)
        display_chr(screen, res, chr_id)
        screen.blit(message1, msg1_rect)
        check_player_number(screen, res, player_num)

        # Update the screen
        pygame.display.update()
        # capped fps 
        clock.tick(FPS)


# Code below:
# work like select_screen module
# used for test the scene before put to module 
# can uncomment (ctrl+/) to run from this file

# pygame.init()

# res = (800, 400)
# screen = pygame.display.set_mode(res)
# clock = pygame.time.Clock()

# chr_list = []

# chr_font1 = pygame.font.Font(None, 50)
# chr_id = -1
# message1 = chr_font1.render('Press SPACE to select', False, 'white')
# msg1_rect = message1.get_rect(midtop = (res[0]/2, res[1]/10*7))


# while True:
#     # Event loop
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
#             pygame.quit()
#             exit()

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 check_select(chr_id, chr_list)
#             if event.key == pygame.K_RETURN and player_num >= 2:
#                 print("change to: game")

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_1]:
#         chr_id = 0
#     elif keys[pygame.K_2]:
#         chr_id = 1
#     elif keys[pygame.K_3]:
#         chr_id = 2
#     elif keys[pygame.K_4]:
#         chr_id = 3
#     elif keys[pygame.K_5]:
#         chr_id = 4
#     elif keys[pygame.K_6]:
#         chr_id = 5        
#     player_num = len(chr_list)   

#     # Display text
#     screen.fill("black")
#     display_list(screen, res, chr_list)
#     display_chr(screen, res, chr_id)
#     screen.blit(message1, msg1_rect)
#     check_player_number(screen, res, player_num)

#     # Update the screen
#     pygame.display.update()
#     clock.tick(60)
