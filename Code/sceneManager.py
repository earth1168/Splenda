# Written by Walan 1057
# This script handles scene management.
# Run code at this script.

import pygame

# import scene
from SceneDemo import selectDummy
from SceneDemo import menuDummy
from SceneDemo import gameDummy
import MainMenu
import Rule

# This class will call scene that should run next when current scene end.
# variables:
#   self.scene -> tell what scene that running now.
class GameState():
    def __init__(self):
        # start at menu scene
        self.scene = 'menu'

    def menu(self):
        # self.scene = menuDummy.menu_screen(screen, res, FPS)
        self.scene = MainMenu.mainmenu(screen, FPS)

    def select_character(self):
        self.scene = selectDummy.select_screen(screen, res, FPS, chr_list)

    def game(self):
        self.scene = gameDummy.game_screen(screen, res, FPS, chr_list)
    
    def rule_book(self):
        self.scene = Rule.rulebook(screen, FPS)
    
    def scene_manager(self):
        if self.scene == 'menu':
            self.menu()
        
        if self.scene == 'select_character':
            self.select_character()

        if self.scene == 'game':
            self.game()

        if self.scene == 'rule_book':
            self.rule_book()

# General Setup
pygame.init()
game_state = GameState()
FPS = 60

# Screen Setup
# game resolution (width, height)
res = (1280, 720)
screen = pygame.display.set_mode(res)

# In-game variables
# I don't know if this is appropiate or not
# contain character ID that selected by players
chr_list = []

while True:
    game_state.scene_manager()
