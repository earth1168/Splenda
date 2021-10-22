#Written by Pojnarin 62070501041
import pygame
from sys import exit
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
    #Define color of text
    Color = ['White','White','White','White','White','White','White']
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
    #Frist time define text and create rectangle of all texts
    Text_StartGame_surface = text_font.render('StartGame',True,Color[0]).convert_alpha()
    Text_StartGame_rect = Text_StartGame_surface.get_rect(topleft = (50,250))
    Text_Rule_surface = text_font.render('Rule',True,Color[1]).convert_alpha()
    Text_Rule_rect = Text_StartGame_surface.get_rect(topleft = (50,320))
    Text_Setting_surface = text_font.render('Setting',True,Color[2]).convert_alpha()
    Text_Setting_rect = Text_StartGame_surface.get_rect(topleft = (50,390))
    Text_Exit_surface = text_font.render('Exit',True,Color[3]).convert_alpha()
    Text_Exit_rect = Text_Exit_surface.get_rect(topleft = (50,460))
    #Text for popup in exit
    Text_QExit_surface = text_font.render('Are you sure you want to exit?',True,Color[4]).convert_alpha()
    Text_QExit_rect = Text_Exit_surface.get_rect(topleft = (326,244))
    Text_Yes_surface = text_font.render('Yes',True,Color[5]).convert_alpha()
    Text_Yes_rect = Text_Exit_surface.get_rect(topleft = (436,420))
    Text_No_surface = text_font.render('No',True,Color[6]).convert_alpha()
    Text_No_rect = Text_Exit_surface.get_rect(topleft = (818,420))
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
                        if Text_StartGame_rect.collidepoint(pygame.mouse.get_pos()):
                            return "select_character"
                        if Text_Rule_rect.collidepoint(pygame.mouse.get_pos()):
                            return "rule_book"
                        if Text_Setting_rect.collidepoint(pygame.mouse.get_pos()):
                            print('3')
                        if Text_Exit_rect.collidepoint(pygame.mouse.get_pos()) :
                            Pause = 1
                    else :
                        if Text_Yes_rect.collidepoint(pygame.mouse.get_pos()):
                            run = False
                        if Text_No_rect.collidepoint(pygame.mouse.get_pos()):
                            Pause = 0

        #Change the color of text when mouse cusor hover above the text
        if Pause == 0 :
            Bhover[4] = 0
            Bhover[5] = 0
            if Text_StartGame_rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[0] = 1
                Color[0] = 'Gold'
            else : 
                Bhover[0] = 0
                Color[0] = 'White'

            if Text_Rule_rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[1] = 1
                Color[1] = 'Gold'
            else : 
                Bhover[1] = 0
                Color[1] = 'White'

            if Text_Setting_rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[2] = 1
                Color[2] = 'Gold'
            else : 
                Bhover[2] = 0
                Color[2] = 'White'

            if Text_Exit_rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[3] = 1    
                Color[3] = 'Gold'
            else :
                Bhover[3] = 0
                Color[3] = 'White'
        else :
            Bhover[3] = 0
            Color[3] = 'White'
            if Text_Yes_rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[4] = 1
                Color[5] = 'Gold'
            else : 
                Bhover[4] = 0
                Color[5] = 'White'
            if Text_No_rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[5] = 1
                Color[6] = 'Gold'
            else : 
                Bhover[5] = 0
                Color[6] = 'White'

        #if any button are hover, mouse cursor will turn to hand 
        if 1 in Bhover :
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else :
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        #FPS of the game
        clock.tick(FPS)
        #Background image
        screen.blit(BACKGROUND,(0,0))
        #Setting Text in loop because they need to change color when hover
        Text_StartGame_surface = text_font.render('StartGame',True,Color[0]).convert_alpha()
        Text_Rule_surface = text_font.render('Rule',True,Color[1]).convert_alpha()
        Text_Setting_surface = text_font.render('Setting',True,Color[2]).convert_alpha()
        Text_Exit_surface = text_font.render('Exit',True,Color[3]).convert_alpha()
        Text_Yes_surface = text_font.render('Yes',True,Color[5]).convert_alpha()
        Text_No_surface = text_font.render('No',True,Color[6]).convert_alpha()
        #Render Text on mainmenu
        screen.blit(Text_StartGame_surface,Text_StartGame_rect)
        screen.blit(Text_Rule_surface,Text_Rule_rect)
        screen.blit(Text_Setting_surface,Text_Setting_rect)
        screen.blit(Text_Exit_surface,Text_Exit_rect)
        if Pause == 1 :
            #Render when popup
            screen.blit(PAUSEBG,(0,0))
            screen.blit(Text_QExit_surface,Text_QExit_rect)
            screen.blit(Text_Yes_surface,Text_Yes_rect)
            screen.blit(Text_No_surface,Text_No_rect)
        #Update screen
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":
   mainmenu(screen, FPS)