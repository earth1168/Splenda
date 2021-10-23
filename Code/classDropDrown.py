# Written by Walan 1057
# This script contains 1 class:
#   - DropDown
# Run optionDummy to see how dropdown object works

import pygame

# DropDown class:
# create dropdown that user can choose any options
# attributes:
#  - x: int -- x position
#  - y: int -- y position
#  - width: int
#  - height: int
#  - main: text -- text on the main part
#  - options: List[text] -- list of options
#  - t_size: int -- size of text
#  - color_main: [color_deactive, color_deactive] -- color when hovering or not hovering on main
#       default: blue-ish color
#  - color_option: [color_deactive, color_deactive] -- color when hovering or not hovering on options
#       default: gray-ish color
#  - color_text: color name | (r, g, b)
#       default: black color
#  - font: text -- path of font
#       default: pygame's default font
#  - draw_menu: bool -- is option drawing?
#  - menu_active: bool -- is user clicking on main?
#  - active_option: int -- option user currently hovering on
class DropDown():
    def __init__(self, x, y, width, height, main, options, t_size,
                color_main = ['dodgerblue3', 'deepskyblue1'], 
                color_option = ['gray80', 'gray93'],
                color_text = 'black', 
                font = None):
        self.rect = pygame.Rect(x, y, width, height)
        self.main = main
        self.options = options
        self.t_size = t_size
        self.color_main = color_main
        self.color_option = color_option
        self.color_text = color_text
        self.font = pygame.font.Font(font, t_size)
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    # draw dropdown on surface
    def draw(self, surface):
       pygame.draw.rect(surface, self.color_main[self.menu_active], self.rect)
       msg = self.font.render(self.main, True, self.color_text)
       msg_rect = msg.get_rect(center = self.rect.center)
       surface.blit(msg, msg_rect)

       if self.draw_menu:
           for i, text in enumerate(self.options):
               rect = self.rect.copy()
               rect.y += self.rect.height * (i+1)   
               pygame.draw.rect(surface, self.color_option[1 if i == self.active_option else 0], rect)
               msg = self.font.render(text, True, self.color_text)
               msg_rect = msg.get_rect(center = rect.center)
               surface.blit(msg, msg_rect)

    # update dropdown, return selected option
    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)

        # check what option that user hover on
        self.active_option = -1
        for i in range(len(self.options)):
            rect = self.rect.copy()
            rect.y += self.rect.height * (i+1)
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEMOTION:
                if self.menu_active:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # if click on main, then close or open the options
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                # if click on any option, return that option
                elif self.draw_menu and self.active_option >= 0:
                    self.draw_menu = False
                    return self.active_option
        return -1
