from typing import Optional, Tuple, Union
import pygame
'''
    ButtonDirty class
    An object for button with customizable background, size, and text.
    Inherit from DirtySprite class.

    Argument:
      * position    -- Position of the button
      * size        -- Size of the button
      * text        -- Text on the button
      * t_size      -- Size of text
      * bg_path     -- Path of button image 
      * t_colors    -- Text's color
      * t_font      -- Path of text's font
    * -> that argument is also an attribute.

    Attributes:
        bg_hover_path   -- Path of button image when the mouse is hovering on this button
        is_hover        -- Boolean that tell if the mouse is hovering on this button
'''

class ButtonDirty(pygame.sprite.DirtySprite):
    def __init__(self, 
                position: Tuple[int, int], 
                size: Tuple[int, int],
                text: str,
                t_size: int,
                bg_path: str = '',
                t_colors: Union[str, Tuple[int, int, int]] = '',
                t_font: Optional[str] = None):
        super().__init__()
        self.position = position
        self.size = size
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
        self.bg_hover_path = ''
        self.is_hover = False

        self.draw_button()

    # Draw button on this object's surface
    def draw_button(self):
        self.font = pygame.font.Font(self.font, self.t_size)
        # Create surface to draw button on
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = self.position)
        # Text on the button
        self.t_render = self.font.render(self.text, True, self.t_colors)
        self.t_rect = self.t_render.get_rect(center = self.image.get_rect().center)
        # if specify an image, then use image as button image
        # if not specify an image, then button image is transparent
        if self.bg_path != '':
            self.bg = pygame.image.load(self.bg_path).convert_alpha()
            self.bg = pygame.transform.smoothscale(self.bg, self.size)
            self.bg_rect = self.bg.get_rect(center = self.image.get_rect().center)            
            self.image.blit(self.bg, self.bg_rect) # Draw button image on the surface                
        self.image.blit(self.t_render, self.t_rect) # Draw text on the surface

    # When mouse is hovering on button. change text's color and/or button image
    # Only update in the first frame that mouse hover on the button
    # Argument:
    #   colors_new    -- text's color when the mouse is hovering on this button
    #   bg_new        -- path of button image when the mouse is hovering onthis button
    def hover(self,
                colors_new: Union[str, Tuple[int, int, int]]='',
                bg_new: str=''):
        if not self.is_hover:
            if bg_new != '':
                if self.bg_hover_path != bg_new:
                    self.bg_hover_path = bg_new
                    self.bg_hover = pygame.image.load(self.bg_hover_path).convert_alpha()
                    self.bg_hover = pygame.transform.scale(self.bg_hover, self.size)
                self.image.blit(self.bg_hover, self.bg_rect)
            if colors_new != '':
                self.t_hover_render = self.font.render(self.text, True, colors_new)
                self.image.blit(self.t_hover_render, self.t_rect)
            self.is_hover = True            
            self.dirty = 1 # update button image

    # When mouse is not hovering on the button. change back to normal
    # Only update in the first frame that mouse doesn't hover on the button
    def unhover(self):
        if self.is_hover:
            self.image.blit(self.bg, self.bg_rect)
            self.image.blit(self.t_render, self.t_rect)
            self.is_hover = False
            self.dirty = 1

    # Change the text on the button
    # Argument:
    #   text_new    -- new button text
    def update_text(self, text_new):
        self.text = text_new
        self.t_render = self.font.render(self.text, True, self.t_colors)
        self.image.blit(self.bg, self.bg_rect)
        self.image.blit(self.t_render, self.t_rect)
        self.dirty = 1

    # Change position of button
    # Argument:
    #   x -- new position on x axis
    #   y -- new position on y axis
    def reposition(self, x: int, y: int):
        self.position = (x, y)
        self.rect.center = self.position

    # Chage size of button
    # Argument:
    #   - size_new  -- new button size 
    def resize(self, size_new: Tuple[int, int]):
        self.size = size_new