# Written by Walan 1057
# This script shows click button on the screen, 
# can run at this script

import pygame
from sys import exit
from classButton import Button

# class Button(pygame.sprite.Sprite):
#     def __init__(self, position, btn_size, text, t_size, bg_path, colors=''):
#         super().__init__()
#         self.font = pygame.font.Font(None, t_size)
#         if colors == '':
#             self.colors = 'white'
#         else:
#             self.colors = colors

#         # Create surface to draw button on
#         self.image = pygame.Surface(btn_size, pygame.SRCALPHA)
#         self.rect = self.image.get_rect(center = position)
#         # Text on the button
#         self.text = self.font.render(text, False, self.colors)
#         self.t_rect = self.text.get_rect(center = self.image.get_rect().center)
#         # Button image
#         self.bg = pygame.image.load(bg_path).convert_alpha()
#         self.bg = pygame.transform.scale(self.bg, btn_size)
#         self.bg_rect = self.bg.get_rect(center = self.image.get_rect().center)
#         # Draw text and image on the surface
#         self.image.blit(self.bg, self.bg_rect)
#         self.image.blit(self.text, self.t_rect)        


# Code below:
# work like select_screen module
# used for test the scene before put to module 
# can uncomment (ctrl+/) to run from this file

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
b1 = Button((res[0]/2, res[1]/2+res[1]/10), (128, 64), 'exit', 25, 'Image/Button/testButton-01.png', 'firebrick1')
# button with no text, only button's background image 
b2 = Button((res[0]/2, res[1]/3), (48, 48), '', 25, 'Image/Button/game icon.png')
# button with 'test' text, no background image, set colors using (r, g, b), and default font 
b4 = Button((res[0]/2, res[1]/2+res[1]/5), (128, 64), 'test', 25, '', (0,0,225))

while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEMOTION:
            # if mouse is hovering on b0
            if b0.rect.collidepoint(pygame.mouse.get_pos()):
                b0.hover()                
        
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

    # Update the screen
    pygame.display.update()
    clock.tick(60)
