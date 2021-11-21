import pygame
import choosecharacter
import gamePage
import result
import MainMenu
import Rule
import Setting

pygame.init()

'''
    GameState class:
    An object for handle scene management.

    Attribute:
        isFullscreen        -- Boolean that tell if the game is full screen
        icon                -- Game icon image 
        volume              -- Game volume
        scene               -- Scene name
        name_user           -- list of players' name
        act_user            -- list of character ID selected by player
        result_player_list  -- list of player order by their score and card quantity
'''

class GameState():
    #Frist open setup
    # Screen Setup
    isFullscreen = False
    #Set name of screen caption
    pygame.display.set_caption("SPLENDA")
    #Set game icon of screen caption
    icon = pygame.image.load('Character/splenda.png')
    pygame.display.set_icon(icon)
    # music volume setup
    volume = 0.5
    pygame.mixer.music.set_volume(volume)

    def __init__(self):
        # start at menu scene
        self.scene = 'menu'
        self.name_user = []
        self.act_user = []
        self.result_player_list = []

    # Call menu scene
    def menu(self):
        pygame.mixer.music.load("Music\Mystical  Loop #1.wav")
        pygame.mixer.music.play(-1)
        self.name_user = []
        self.act_user = []
        self.scene = MainMenu.mainmenu(screen, FPS)

    # Call select character scene
    def select_character(self):
        pygame.mixer.music.load("Music\Medieval Theme #1.wav")
        pygame.mixer.music.play(-1)
        self.scene = choosecharacter.selectCharacter(screen, self.name_user, self.act_user)

    # Call game scene
    def game(self):
        pygame.mixer.music.load("Music\Medieval Theme #1.wav")
        pygame.mixer.music.play(-1)
        self.scene, self.result_player_list = gamePage.gameBoard(self.name_user, self.act_user,self.result_player_list)
    
    # Call rule scene
    def rule_book(self):
        pygame.mixer.music.load("Music\Mystical  Loop #1.wav")
        pygame.mixer.music.play(-1)
        self.scene = Rule.rulebook(screen, FPS)

    # Call setting scene
    def setting(self):
        pygame.mixer.music.load("Music\Mystical  Loop #1.wav")
        pygame.mixer.music.play(-1)
        self.scene, self.isFullscreen, self.volume   = Setting.setting(screen, FPS, res, self.isFullscreen, self.volume)

    # Call result scene
    def result(self):
        pygame.mixer.music.load("Music\Dreams of Glory.wav")
        pygame.mixer.music.play(-1)
        self.scene = result.result(screen,self.result_player_list)
    
    # Check current scene and call that scene
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

res = (1280, 720) # game resolution (width, height)
screen = pygame.display.set_mode(res)

# Open game
while True:
    game_state.scene_manager()
    
