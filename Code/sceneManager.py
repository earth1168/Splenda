# Written by Walan 1057
# This script handles scene management.
# Run code at this script.

import pygame

# import scene
import choosecharacter
import gamePage
import result
import MainMenu
import RuleDirtyButton
import SettingDirtyButton2

# This class will call scene that should run next when current scene end.
# variables:
#   self.scene -- tell what scene that running now.

class GameState():
    #Frist open setup
    # Screen Setup
    isFullscreen = False
    # music volume setup
    volume = 0.5
    pygame.mixer.music.set_volume(volume)

    def __init__(self):
        # start at menu scene
        self.scene = 'menu'
        self.name_user = []
        self.act_user = []
        self.result_player_list = []

    def menu(self):
        # self.scene = menuDummy.menu_screen(screen, res, FPS)
        pygame.mixer.music.load("Music\Mystical  Loop #1.wav")
        pygame.mixer.music.play(-1)
        self.name_user = []
        self.act_user = []
        self.scene = MainMenu.mainmenu(screen, FPS)

    def select_character(self):
        pygame.mixer.music.load("Music\Medieval Theme #1.wav")
        pygame.mixer.music.play(-1)
        self.scene = choosecharacter.selectCharacter(screen, self.name_user, self.act_user)

    def game(self):
        pygame.mixer.music.load("Music\Medieval Theme #1.wav")
        pygame.mixer.music.play(-1)
        self.scene, self.result_player_list = gamePage.gameBoard(self.name_user, self.act_user,self.result_player_list)
    
    def rule_book(self):
        pygame.mixer.music.load("Music\Mystical  Loop #1.wav")
        pygame.mixer.music.play(-1)
        self.scene = RuleDirtyButton.rulebook(screen, FPS)

    def setting(self):
        pygame.mixer.music.load("Music\Mystical  Loop #1.wav")
        pygame.mixer.music.play(-1)
        self.scene, self.isFullscreen, self.volume   = SettingDirtyButton2.setting(screen, FPS, res, self.isFullscreen, self.volume)

    def result(self):
        pygame.mixer.music.load("Music\Dreams of Glory.wav")
        pygame.mixer.music.play(-1)
        print("In SM result")
        self.scene = result.result(screen,self.result_player_list)
    
    def scene_manager(self):
        if self.scene == 'menu':
            self.menu()
        
        if self.scene == 'select_character':
            self.select_character()

        if self.scene == 'game':
            self.game()

        if self.scene == 'rule_book':
            self.rule_book()

        if self.scene == 'setting':
            self.setting()

        if self.scene == 'result':
            self.result()

# General Setup
pygame.init()
game_state = GameState()
FPS = 25
#Music

# game resolution (width, height)
res = (1280, 720)
screen = pygame.display.set_mode(res)

# In-game variables
# I don't know if this is appropiate or not
# contain character ID that selected by players
chr_list = []

while True:
    game_state.scene_manager()
    
