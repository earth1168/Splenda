#Written by Pojnarin 62070501041
import pygame
from sys import exit
from classText import TButton
pygame.init()
#Set variable for window size
WIDTH, HEIGHT = 1280,720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#Set FPS of the game
FPS = 60

def mainmenu(screen, FPS) :
    clock = pygame.time.Clock()
    #Set path of background image file
    BACKGROUND = pygame.image.load("Image\Background\MainMenu720p.png").convert()
    #Set path of pause background image file
    PAUSEBG = pygame.image.load("Image\Popup\Popup720p.png").convert_alpha()
    #define variable for state of the game 
    Pause = 0
    #Create Text button objects for mainmenu option
    button_group = pygame.sprite.Group()
    StartGame = TButton((50,250),'StartGame',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    Rule = TButton((50,320),'Rule',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    Setting = TButton((50,390),'Setting',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    Exit = TButton((50,460),'Exit',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    #Create Text button objects and Text rectangle for when the game is pause
    pause_button_group = pygame.sprite.Group()
    QExit = TButton((326,244),'Are you sure you want to exit?',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    Yes = TButton((436,420),'Yes',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    No = TButton((818,420),'No',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    button_group.add(StartGame,Rule,Setting,Exit)
    pause_button_group.add(QExit,Yes,No)
    #Game loop
    run = True
    while run:
        #Handle user-input
        for event in pygame.event.get():
            #Exit game when press X button on window
            if event.type == pygame.QUIT :
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 :
                    if Pause == 0 :
                        if StartGame.rect.collidepoint(pygame.mouse.get_pos()):
                            return "select_character"
                        if Rule.rect.collidepoint(pygame.mouse.get_pos()):
                            return "rule_book"
                        if Setting.rect.collidepoint(pygame.mouse.get_pos()):
                            return "setting"
                        if Exit.rect.collidepoint(pygame.mouse.get_pos()) :
                            Pause = 1
                    else :
                        if Yes.rect.collidepoint(pygame.mouse.get_pos()):
                            run = False
                        if No.rect.collidepoint(pygame.mouse.get_pos()):
                            Pause = 0

        #Change the color of text when mouse cusor hover above the text
        if Pause == 0 :
            if StartGame.rect.collidepoint(pygame.mouse.get_pos()):
                StartGame.hover('Gold')
            else : 
                StartGame.hover('White')

            if Rule.rect.collidepoint(pygame.mouse.get_pos()):
                Rule.hover('Gold')
            else : 
                Rule.hover('White')

            if Setting.rect.collidepoint(pygame.mouse.get_pos()):
                Setting.hover('Gold')
            else : 
                Setting.hover('White')

            if Exit.rect.collidepoint(pygame.mouse.get_pos()):  
                Exit.hover('Gold')
            else :
                Exit.hover('White')
        else :
            if Yes.rect.collidepoint(pygame.mouse.get_pos()):
                Yes.hover('Gold')
            else : 
                Yes.hover('White')
            if No.rect.collidepoint(pygame.mouse.get_pos()):
                No.hover('Gold')
            else : 
                No.hover('White')

        #FPS of the game
        clock.tick(FPS)
        #Background image
        screen.blit(BACKGROUND,(0,0))
        #Render Text on mainmenu
        button_group.draw(screen)
        button_group.update()
        if Pause == 1 :
            #Render when popup
            screen.blit(PAUSEBG,(0,0))
            pause_button_group.draw(screen)
            pause_button_group.update()
        #Update screen
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":
   mainmenu(screen, FPS)