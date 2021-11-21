import pygame
from typing import Optional, Tuple, Union

'''
    TButton class
    An object for using text as button.

    Argument:
      * position    -- Position of the button
      * text        -- Text on the button
      * t_size      -- Size of text
      * colors    -- Text's color
      * t_font      -- Path of text's font

'''
class TButton(pygame.sprite.Sprite):
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
        font = pygame.font.Font(t_font, t_size)
        # Create surface to draw button on
        word_surface = font.render(text, True, colors).convert_alpha()
        # Get size of all the text from the surface
        self.size = word_surface.get_size()
        self.image = pygame.Surface(word_surface.get_size(), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft = position)

    # draw button
    def draw_button(self):
        font = pygame.font.Font(self.font, self.t_size)
        # Create surface to draw button on
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft = self.position)
        # Text on the button
        text = font.render(self.text, True, self.colors)
        t_rect = text.get_rect(center = self.image.get_rect().center)
        # Draw text on the surface        
        self.image.blit(text, t_rect)

    # When mouse is hovering on button. change text's color
    #   - colors_new: text | tuple(r, g, b) -- text's color when hovering
    #       default: text's color is not changed
    def hover(self,
                colors_new: Union[str, Tuple[int, int, int]]=''):
        if colors_new != '':
            self.colors = colors_new

    # update button
    def update(self):
        self.draw_button()
