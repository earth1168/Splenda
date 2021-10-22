# Written by Pojnarin 62070501041

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
class TextButton(pygame.sprite.Sprite):
    def __init__(self, 
                position: Tuple[int, int], 
                text: str,
                t_size: int,
                colors: Union[str, Tuple[int, int, int]]='',
                t_font: Optional[str] = None):
        super().__init__()
        self.position = position
        self.text = text
        self.t_size = t_size   
        # if not specify a text color, then text color is white
        if colors == '':
            self.colors = 'white'
        else:
            self.colors = colors
        self.font = t_font

    # draw button
    def draw_button(self):
        font = pygame.font.Font(self.font, self.t_size)
        # Text on the button
        text = font.render(self.text, True, self.colors)
        t_rect = text.get_rect(topleft =  self.position)
        # Draw text on the surface        
        self.blit(text, t_rect)

    # When mouse is hovering on button. change text's color and/or button background image
    #   - colors_new: text | tuple(r, g, b) -- text's color when hovering
    #       default: text's color is not changed
    #   - bg_new: text --  path of button's background image when hovering
    #       default: button's background image is not changed
    def hover(self,
                colors_new: Union[str, Tuple[int, int, int]]=''):
        if colors_new != '':
            self.colors = colors_new

    # change position of button
    #   - pos_new: tuple(x, y) -- new position to put button on
    def reposition(self, pos_new: Tuple[int, int]):
        self.position = pos_new

    # change size of button's text
    #   - t_size_new: int -- new text's size
    def resize_text(self, t_size_new: int):
        self.t_size = t_size_new

    # update button
    def update(self):
        self.draw_button()
