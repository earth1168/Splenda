import pygame
from typing import Tuple
from classButtonDirty import ButtonDirty
from classCardDirty import CardDirty

'''
    BigCard class
    An object for display a bigger picture of a card that selected by player.
    Player can buy or hold a card if it's not held yet.
    Inherit from DirtySprite class.

    Argument:
        card            -- CardDirty object that selected by player
        position        -- Position of this object 
      * is_hold         -- Boolean that tell if this card is held
    * -> that argument is also an attribute.

    Attributes:  
        selected_card   -- CardDirty object that selected by player
        btn_close       -- Button for closing this object
        btn_buy         -- Button for buying a selected card
        btn_hold        -- Button for holding a selected card
'''
class BigCard(pygame.sprite.DirtySprite):
    def __init__(self, card: CardDirty, position: Tuple[int, int], is_hold: bool = False):
        super().__init__()
        self.selected_card = card
        self.is_hold = is_hold
        self._layer = 4
        self.image = pygame.Surface((card.size[0]*3+100, card.size[1]*3+100), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = position)

        card_img = pygame.image.load(card.img_path).convert_alpha()
        card_img = pygame.transform.smoothscale(card_img, (card.size[0]*3, card.size[1]*3))
        card_img_rect = card_img.get_rect(center = self.image.get_rect().center)

        self.btn_close = ButtonDirty(card_img_rect.topright, (75, 75), '', 0, 'Image\Button\CloseButton.png')
        self.btn_buy = ButtonDirty((card_img_rect.right-80, card_img_rect.top + 210), (130, 50), 'Buy', 20, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font\Roboto\Roboto-Bold.ttf')
        if not self.is_hold:
            self.btn_hold = ButtonDirty((card_img_rect.right-80, card_img_rect.top + 145), (130, 50), 'Hold', 20, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font\Roboto\Roboto-Bold.ttf')
        
        self.image.blit(card_img, card_img_rect)
        self.image.blit(self.btn_close.image, self.btn_close.rect)
        self.image.blit(self.btn_buy.image, self.btn_buy.rect)
        if not is_hold:
            self.image.blit(self.btn_hold.image, self.btn_hold.rect)

     
    # Update button image when the image is changed.    
    def update_button(self):
        self.image.blit(self.btn_close.image, self.btn_close.rect)
        self.image.blit(self.btn_buy.image, self.btn_buy.rect)
        if not self.is_hold:
            self.image.blit(self.btn_hold.image, self.btn_hold.rect)