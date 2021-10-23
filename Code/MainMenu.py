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
    #Set name of screen caption
    pygame.display.set_caption("MainMenu")
    #Text setting
    text_font = pygame.font.Font("Font\Roboto\Roboto-Regular.ttf",50)
    #Set path of background image file
    BACKGROUND = pygame.image.load("Image\Background\MainMenu720p.png").convert()
    #Set path of pause background image file
    PAUSEBG = pygame.image.load("Image\Popup\Popup720p.png").convert_alpha()
    #define variable for state of the game 
    Pause = 0
    #Define variable to monitor if mouse hover over button
    Bhover = [0,0,0,0,0,0]
    #Create Text button objects for mainmenu option
    button_group = pygame.sprite.Group()
    StartGame = TButton((50,250),'StartGame',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    Rule = TButton((50,320),'Rule',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    Setting = TButton((50,390),'Setting',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    Exit = TButton((50,460),'Exit',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    #Create Text button objects and Text rectangle for when the game is pause
    pause_button_group = pygame.sprite.Group()
    Text_QExit_surface = text_font.render('Are you sure you want to exit?',True,'White').convert_alpha()
    Text_QExit_rect = Text_QExit_surface.get_rect(topleft = (326,244))
    Yes = TButton((436,420),'Yes',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    No = TButton((818,420),'No',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    button_group.add(StartGame,Rule,Setting,Exit)
    pause_button_group.add(Yes,No)
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
                            print('3')
                        if Exit.rect.collidepoint(pygame.mouse.get_pos()) :
                            Pause = 1
                    else :
                        if Yes.rect.collidepoint(pygame.mouse.get_pos()):
                            run = False
                        if No.rect.collidepoint(pygame.mouse.get_pos()):
                            Pause = 0

        #Change the color of text when mouse cusor hover above the text
        if Pause == 0 :
            Bhover[4] = 0
            Bhover[5] = 0
            if StartGame.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[0] = 1
                StartGame.hover('Gold')
            else : 
                Bhover[0] = 0
                StartGame.hover('White')

            if Rule.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[1] = 1
                Rule.hover('Gold')
            else : 
                Bhover[1] = 0
                Rule.hover('White')

            if Setting.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[2] = 1
                Setting.hover('Gold')
            else : 
                Bhover[2] = 0
                Setting.hover('White')

            if Exit.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[3] = 1    
                Exit.hover('Gold')
            else :
                Bhover[3] = 0
                Exit.hover('White')
        else :
            Bhover[3] = 0
            if Yes.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[4] = 1
                Yes.hover('Gold')
            else : 
                Bhover[4] = 0
                Yes.hover('White')
            if No.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[5] = 1
                No.hover('Gold')
            else : 
                Bhover[5] = 0
                No.hover('White')

        #if any button are hover, mouse cursor will turn to hand 
        if 1 in Bhover :
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else :
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

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
            screen.blit(Text_QExit_surface,Text_QExit_rect)
            pause_button_group.draw(screen)
            pause_button_group.update()
        #Update screen
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":
   mainmenu(screen, FPS)