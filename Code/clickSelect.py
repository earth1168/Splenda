# Written by Walan 1057
# This script shows clickable buttons on the screen, 
# can run at this script

import pygame
from sys import exit
from classButton import Button    

pygame.init()

res = (800, 400)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

# group of buttons. work with sprite (Button class in this context)
button_group = pygame.sprite.Group()
# to create Button instance, you don't have to specify bg_path, colors, and t_font
# button with 'start' text, button's background image, set colors, and set font 
b0 = Button((res[0]/2, res[1]/2), (128, 64), 'start', 25, 'Image/Button/testButton-01.png', 'darkorange1', 'Font/Roboto/Roboto-Black.ttf')
# button with 'exit' text, button's background image, set colors, and default font 
b1 = Button((res[0]/2, res[1]/2+res[1]/5), (128, 64), 'exit', 25, 'Image/Button/testButton-01.png', 'firebrick1')
# button with no text, only button's background image 
b2 = Button((res[0]/2, res[1]/3), (48, 48), '', 25, 'Image/Button/game icon.png')
# button with 'test' text, no background image, set colors using (r, g, b), and default font 
b4 = Button((res[0]/2, res[1]/2+res[1]/5*2), (128, 64), 'test', 25, '', (0,0,225))

while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEMOTION:
            # if mouse is hovering on b0
            if b0.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                # change text color and button's image
                b0.hover('red', 'Image/Button/game icon.png')
                # keep other button normal
                b1.hover('firebrick1') 

            # if mouse is hovering on b1
            elif b1.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                # change text color
                b1.hover('yellow')
                # keep other button normal
                b0.hover('darkorange', 'Image/Button/testButton-01.png')
            
            # if not hovering on b0 and b1
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                # change text color and button's image back to normal
                b0.hover('darkorange', 'Image/Button/testButton-01.png')
                b1.hover('firebrick1')                
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if b0.rect.collidepoint(pygame.mouse.get_pos()):
                    print('click b0')
                # if left click on b1, then exit the program
                if b1.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    exit()
    # add button to group
    button_group.add(b0, b1, b2, b4)

    # Display
    screen.fill("dimgrey")
    # draw all button on the screen
    button_group.draw(screen)
    button_group.update()    

    # Update the screen
    pygame.display.update()
    clock.tick(60)
