# Written by Walan 1057
# This script contains 1 class:
#   - Button

from typing import Optional, Tuple, Union
import pygame

# Button class:
# create button object with customizable background, size, and text
# inherit from Sprite class in pygame
#  attributes:
#   - position: tuple(x, y) -- position of the button
#   - btn_size: tuple(height, width) -- size of the button
#   - text: text -- text on the button
#   - t_size: int -- size of text
#   - bg_path: text -- path of button's background image 
#       default - transparent background
#   - colors: text or tuple(r, g, b) -- text's color
#       default - white color
#   - t_font: text -- text's font
#       default: pygame default font
class Button(pygame.sprite.Sprite):
    def __init__(self, 
                position: Tuple[int, int], 
                btn_size: Tuple[int, int],
                text: str,
                t_size: int,
                bg_path: str='',
                colors: Union[str, Tuple[int, int, int]]='',
                t_font: Optional[str] = None):
        super().__init__()
        self.position = position
        self.size = btn_size
        self.text = text
        self.t_size = t_size
        self.bg_path = bg_path        
        # if not specify a text color, then text color is white
        if colors == '':
            self.colors = 'white'
        else:
            self.colors = colors
        self.font = t_font
        # Create surface to draw button on
        self.image = pygame.Surface(btn_size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = position)

    # draw button
    def draw_button(self):
        font = pygame.font.Font(self.font, self.t_size)
        # Create surface to draw button on
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = self.position)
        # Text on the button
        text = font.render(self.text, True, self.colors)
        t_rect = text.get_rect(center = self.image.get_rect().center)
        # if specify an image, then use image as button's background
        # if not specify an image, then background is transparent
        if self.bg_path != '':
            bg = pygame.image.load(self.bg_path).convert_alpha()
            bg = pygame.transform.scale(bg, self.size)
            bg_rect = bg.get_rect(center = self.image.get_rect().center)
            # Draw button background on the surface
            self.image.blit(bg, bg_rect)
        # Draw text on the surface        
        self.image.blit(text, t_rect)

    # When mouse is hovering on button. change text's color and/or button background image
    #   - colors_new: text | tuple(r, g, b) -- text's color when hovering
    #       default: text's color is not changed
    #   - bg_new: text --  path of button's background image when hovering
    #       default: button's background image is not changed
    def hover(self,
                colors_new: Union[str, Tuple[int, int, int]]='',
                bg_new: str=''):
        if colors_new != '':
            self.colors = colors_new
        if bg_new != '':
            self.bg_path = bg_new

    # change position of button
    #   - pos_new: tuple(x, y) -- new position to put button on
    def reposition(self, pos_new: Tuple[int, int]):
        self.position = pos_new

    # chage size of button
    #   - size_new: tuple(width, height) -- new button's size 
    def resize(self, size_new: Tuple[int, int]):
        self.size = size_new

    # change size of button's text
    #   - t_size_new: int -- new text's size
    def resize_text(self, t_size_new: int):
        self.t_size = t_size_new

    # update button
    def update(self):
        self.draw_button()
