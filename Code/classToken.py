from classButtonDirty import ButtonDirty

'''
    Token class:
    An object for tokens use in the game.
    Inherit from ButtonDirty class.

    Argument:
      * position  -- Position of the button
      * size      -- Size of the button
      * img_path  -- Path of button image
      * colors    -- Token's color
      * qty       -- Quantity of this token
      * t_colors  -- Text's color
    * -> that argument is also an attribute.
'''

class Token(ButtonDirty):
    def __init__(self, position, size, img_path, colors, qty, t_colors='black'):
        super().__init__(position, size, f'{qty}', 30, img_path, t_colors, 'Font\Roboto\Roboto-Bold.ttf')
        self.colors = colors
        self.qty = qty
        self._layer = 2

    # Set this token's visibility depend on its quantity
    def show_token(self):
        if self.qty == 0:
            self.visible = 0
        else:
            self.visible = 1

    