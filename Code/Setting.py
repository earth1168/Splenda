import pygame
from sys import exit
pygame.init()
#Set variable for window size
WIDTH, HEIGHT = 1280,720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#Set FPS of the game
FPS = 60

def setting(screen, FPS) :
    clock = pygame.time.Clock()
    #Set name of screen caption
    pygame.display.set_caption("Game setting")
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
                    print(event.pos)
                    if Pause == 0 :
                        if Text_StartGame_rect.collidepoint(pygame.mouse.get_pos()):
                            print('1')
                            return "select_character"
                        if Text_Rule_rect.collidepoint(pygame.mouse.get_pos()):
                            print('2')
                        if Text_Setting_rect.collidepoint(pygame.mouse.get_pos()):
                            print('3')
                        if Text_Exit_rect.collidepoint(pygame.mouse.get_pos()) :
                            Pause = 1
                    else :
                        if Text_Yes_rect.collidepoint(pygame.mouse.get_pos()):
                            print('Yes')
                            run = False
                        if Text_No_rect.collidepoint(pygame.mouse.get_pos()):
                            Pause = 0
                            print('No')

        #Change the color of text when mouse cusor hover above the text
        if Pause == 0 :
            if Text_StartGame_rect.collidepoint(pygame.mouse.get_pos()):
                    Color[0] = 'Gold'
            else : Color[0] = 'White'

            if Text_Rule_rect.collidepoint(pygame.mouse.get_pos()):
                    Color[1] = 'Gold'
            else : Color[1] = 'White'

            if Text_Setting_rect.collidepoint(pygame.mouse.get_pos()):
                    Color[2] = 'Gold'
            else : Color[2] = 'White'

            if Text_Exit_rect.collidepoint(pygame.mouse.get_pos()):
                    Color[3] = 'Gold'
            else : Color[3] = 'White'
        else :
            Color[3] = 'White'
            if Text_Yes_rect.collidepoint(pygame.mouse.get_pos()):
                    Color[5] = 'Gold'
            else : Color[5] = 'White'
            if Text_No_rect.collidepoint(pygame.mouse.get_pos()):
                    Color[6] = 'Gold'
            else : Color[6] = 'White'


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
   setting(screen, FPS)