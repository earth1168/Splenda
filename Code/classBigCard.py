import pygame
from typing import Tuple
from classButtonDirty import ButtonDirty
from classCardDirty import CardDirty

class BigCard(pygame.sprite.DirtySprite):
    def __init__(self, card: CardDirty, position: Tuple[int, int], is_hold: bool = False):
        super().__init__()
        self.selected_card = card
        self.is_hold = is_hold
        self._layer = 4        
        self.image = pygame.Surface((card.size[0]*3+100, card.size[1]*3+100), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = position)

        card_img = pygame.image.load(card.image_path).convert_alpha()
        card_img = pygame.transform.scale(card_img, (card.size[0]*3, card.size[1]*3))
        card_img_rect = card_img.get_rect(center = self.image.get_rect().center)

        self.btn_close = ButtonDirty(card_img_rect.topright, (75, 75), '', 0, 'Image\Button\CloseButton.png')
        self.btn_buy = ButtonDirty((card_img_rect.right-80, card_img_rect.top + 210), (130, 50), 'Buy', 30, 'Image\Button\ButtonNewUnhover.png', 'black')
        if not is_hold:
            self.btn_hold = ButtonDirty((card_img_rect.right-80, card_img_rect.top + 145), (130, 50), 'Hold', 30, 'Image\Button\ButtonNewUnhover.png', 'black')
        
        self.image.blit(card_img, card_img_rect)
        self.image.blit(self.btn_close.image, self.btn_close.rect)
        self.image.blit(self.btn_buy.image, self.btn_buy.rect)
        if not is_hold:
            self.image.blit(self.btn_hold.image, self.btn_hold.rect)