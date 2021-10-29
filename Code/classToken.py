import pygame
from classButtonDirty import ButtonDirty

class Token(ButtonDirty):
    def __init__(self, position, size, img_path, colors, qty):
        super().__init__(position, size, f'{qty}', 30, img_path, 'black')
        self.colors = colors
        self.qty = qty

    def change_qty(self, qty_new):
        if self.qty != qty_new:
            self.qty = qty_new

    # not draw the token when there is no token
    def out_of_stock(self):
        if self.qty == 0:
            self.visible = 0

    