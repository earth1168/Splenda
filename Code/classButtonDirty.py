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
#   - t_colors: text or tuple(r, g, b) -- text's color
#       default - white color
#   - t_font: text -- text's font
#       default: pygame default font
class ButtonDirty(pygame.sprite.DirtySprite):
    def __init__(self, 
                position: Tuple[int, int], 
                btn_size: Tuple[int, int],
                text: str,
                t_size: int,
                bg_path: str='',
                t_colors: Union[str, Tuple[int, int, int]]='',
                t_font: Optional[str] = None):
        super().__init__()
        self.position = position
        self.size = btn_size
        self.text = text
        self.t_size = t_size
        self.bg_path = bg_path        
        # if not specify a text color, then text color is white
        if t_colors == '':
            self.t_colors = 'white'
        else:
            self.t_colors = t_colors
        self.font = t_font
        self._layer = 0
        # Create surface to draw button on
        self.image = pygame.Surface(btn_size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = position)

        self.draw_button()

    # draw button
    def draw_button(self):
        self.font = pygame.font.Font(self.font, self.t_size)
        # Create surface to draw button on
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = self.position)
        # Text on the button
        self.t_render = self.font.render(self.text, True, self.t_colors)
        self.t_rect = self.t_render.get_rect(center = self.image.get_rect().center)
        # if specify an image, then use image as button's background
        # if not specify an image, then background is transparent
        if self.bg_path != '':
            self.bg = pygame.image.load(self.bg_path).convert_alpha()
            self.bg = pygame.transform.scale(self.bg, self.size)
            self.bg_rect = self.bg.get_rect(center = self.image.get_rect().center)
            # Draw button background on the surface
            self.image.blit(self.bg, self.bg_rect)
        # Draw text on the surface        
        self.image.blit(self.t_render, self.t_rect)

    # When mouse is hovering on button. change text's color and/or button background image
    #   - colors_new: text | tuple(r, g, b) -- text's color when hovering
    #       default: text's color is not changed
    #   - bg_new: text --  path of button's background image when hovering
    #       default: button's background image is not changed
    def hover(self,
                colors_new: Union[str, Tuple[int, int, int]]='',
                bg_new: str=''):
        if colors_new != '':
            self.t_colors = colors_new
        if bg_new != '':
            self.bg_path = bg_new
        self.draw_button()
        self.dirty = 1

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

    def is_collide_mouse(self, mouse):
        return self.rect.collidepoint(mouse)

    # update button
    # def update(self):
    #     # if self.to_draw:
    #     # self.draw_button()
    #     # self.to_draw = False
    #     # self.dirty = 1
    #     pass
