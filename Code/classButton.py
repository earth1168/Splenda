# Written by Walan 1057
# Button class:
# create button with customizable background, size, and text
# inherit form Sprite class in pygame
# To create a button instance, you must have these attributes:
#   - position: tuple(x, y) -> position of the button
#   - btn_size: tuple(height, width) -> size of the button
#   - text: text -> text on the button
#   - t_size: int -> size of text
#   - bg_path: text -> path of button's background image 
#       default - transparent background
#   - colors: text/ tuple(r, g, b) -> text's color
#       default - white color
#   - t_font: text -> text's font
#       default: pygame default font

import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, position, btn_size, text, t_size, bg_path='', colors='', t_font = None):
        super().__init__()
        self.font = pygame.font.Font(t_font, t_size)
        # if not specify a text color, then text color is white
        if colors == '':
            self.colors = 'white'
        else:
            self.colors = colors
        # Create surface to draw button on
        self.image = pygame.Surface(btn_size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = position)
        # Text on the button
        self.text = self.font.render(text, True, self.colors)
        self.t_rect = self.text.get_rect(center = self.image.get_rect().center)
        # if specify an image, then use image as button's background
        # if not specify an image, then background is transparent
        if bg_path != '':
            self.bg = pygame.image.load(bg_path).convert_alpha()
            self.bg = pygame.transform.scale(self.bg, btn_size)
            self.bg_rect = self.bg.get_rect(center = self.image.get_rect().center)
            # Draw button background on the surface
            self.image.blit(self.bg, self.bg_rect)
        # Draw text on the surface        
        self.image.blit(self.text, self.t_rect) 

    # When mouse is hovering on button. change color of the button (not done yet)
    def hover(self):
        print('mouse on b0')
        surf_copy = self.image.copy() 
        btn_pixarr = pygame.PixelArray(surf_copy)
