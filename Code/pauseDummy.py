#Written by Pojnarin 62070501041
import pygame
import Rule
from sys import exit

from pygame.mixer import pause
from classText import TButton
from classButton import Button 
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
    #Set path of background image file
    BACKGROUND = pygame.image.load("Image\Background\MainMenu720p.png").convert()
    #Set path of pause background image file
    PAUSEBG = pygame.image.load("Image\Popup\Popup720p.png").convert_alpha()
    #define variable for state of the game 0 = No pause , 1 = Pause
    Pause = 0
    ########################################## VVVVVVVVVVVVVVVVVVVVV
    #When open rule, set Pause = 2
    POPINBG = pygame.image.load("Image\Background\PauseGame720p.png").convert_alpha()
    RULEPBG = pygame.image.load("Image\Background\RuleInGame720p.png").convert_alpha()
    ##########################################
    #Define variable to monitor if mouse hover over button
    Bhover = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    ########################################## ^^^^^^^^^^^^^^^^^^

    #Create Text button objects for mainmenu option
    button_group = pygame.sprite.Group()
    StartGame = TButton((50,250),'StartGame',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    RuleB = TButton((50,320),'Rule',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    Setting = TButton((50,390),'Setting',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    Exit = TButton((50,460),'Exit',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    #Create Text button objects and Text rectangle for when the game is pause
    pause_button_group = pygame.sprite.Group()
    QExit = TButton((326,244),'Are you sure you want to exit?',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    Yes = TButton((436,420),'Yes',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    No = TButton((818,420),'No',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    button_group.add(StartGame,RuleB,Setting,Exit)
    pause_button_group.add(QExit,Yes,No)
    ##########################################
    #New Button Group
    newpausebutton_group = pygame.sprite.Group()
    popinbutton_group = pygame.sprite.Group()
    #Test Pause Button
    PauseButton = Button((100,550), (130, 50), 'Pause', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    RuleButton = Button((670,300), (140, 70), 'Rule', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    ResumeButton = Button((670,400), (140, 70), 'Resume', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    BackBotton = Button((670,520), (250, 70), 'Back to Menu', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    #Rule Button
    #######################################################
    rulebutton_group = pygame.sprite.Group()
    # button with 'start' text, button's background image, set colors, and set font 
    Next = Button((1180,140), (130, 50), 'Next', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    # button with 'exit' text, button's background image, set colors, and default font 
    Prev = Button((85,140), (140, 50), 'Previous', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    # button with 'Menu' text, button's background image, set colors, and default font 
    Back = Button((1180,640), (130, 50), 'Menu', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    # add button to group
    rulebutton_group.add(Next, Prev,Back)
    ##############################################################
    #Add new button to group
    newpausebutton_group.add(PauseButton)
    popinbutton_group.add(RuleButton,ResumeButton,BackBotton)
    ###########################################################
    text_font_bold = pygame.font.Font("Font\Roboto\Roboto-Bold.ttf",40)
    text_font_regular = pygame.font.Font("Font\Roboto\Roboto-Regular.ttf",30)
    page = 1
    allpage = 20
    #Game loop
    run = True
    while run:
        #Handle user-input
        for event in pygame.event.get():
            #Exit game when press X button on window
            if event.type == pygame.QUIT :
                run = False

            ########################################## vvvvvvvvv When press key 'ESC'
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    if Pause == 1 : Pause = 0
                    elif Pause == 0 : Pause = 1
                    else : Pause = 0
            ########################################## ^^^^^^^^^^
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 :
                    print(event.pos)
                    if Pause == 0 :
                        if StartGame.rect.collidepoint(pygame.mouse.get_pos()):
                            return "select_character"
                        if RuleButton.rect.collidepoint(pygame.mouse.get_pos()):
                            return "rule_book"
                        if Setting.rect.collidepoint(pygame.mouse.get_pos()):
                            return "setting"
                        if Exit.rect.collidepoint(pygame.mouse.get_pos()) :
                            run = False
                        ##########################################v
                        #New Button
                        if PauseButton.rect.collidepoint(pygame.mouse.get_pos()):
                            Pause = 1
                        ##########################################^
                    elif Pause == 1 :
                        if Yes.rect.collidepoint(pygame.mouse.get_pos()):
                            run = False
                        if No.rect.collidepoint(pygame.mouse.get_pos()):
                            Pause = 0
                        ##########################################V
                        if BackBotton.rect.collidepoint(pygame.mouse.get_pos()):
                            print("return 'menu' ")
                            Pause = 0
                        if ResumeButton.rect.collidepoint(pygame.mouse.get_pos()):
                            Pause = 0
                        if RuleButton.rect.collidepoint(pygame.mouse.get_pos()):
                            Pause = 2
                        ##########################################^
                    else :
                        if Next.rect.collidepoint(pygame.mouse.get_pos()):
                            if page != allpage :
                                page += 1
                        if Prev.rect.collidepoint(pygame.mouse.get_pos()):
                            if page != 1 :
                                page -= 1
                        if Back.rect.collidepoint(pygame.mouse.get_pos()):
                            Pause = 1

        #Change the color of text when mouse cusor hover above the text
        if Pause == 0 :
            Bhover[4] = 0
            Bhover[5] = 0
            ################################# Reset hover after Unpause
            Bhover[10] = 0
            Bhover[11] = 0
            Bhover[12] = 0
            Bhover[8] = 0
            Bhover[9] = 0
            #################################
            if StartGame.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[0] = 1
                StartGame.hover('Gold')
            else : 
                Bhover[0] = 0
                StartGame.hover('White')

            if RuleButton.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[1] = 1
                RuleButton.hover('Gold')
            else : 
                Bhover[1] = 0
                RuleButton.hover('White')

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
            ##########################################
            #New Button
            if PauseButton.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[6] = 1    
                PauseButton.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            else :
                Bhover[6] = 0
                PauseButton.hover('black', 'Image\Button\ButtonNewUnhover.png')

        elif Pause == 1 :
            Bhover[3] = 0
            ########################################## Hover effect of Pause Button on menu
            #New Button
            Bhover[10] = 0
            Bhover[11] = 0
            Bhover[12] = 0
            Bhover[6] = 0
            PauseButton.hover('black', 'Image\Button\ButtonNewUnhover.png')
            ##########################################
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
            ########################################### Hover effect of Pause Menu Option
            if RuleButton.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[7] = 1    
                RuleButton.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            else :
                Bhover[7] = 0
                RuleButton.hover('black', 'Image\Button\ButtonNewUnhover.png')

            if ResumeButton.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[8] = 1    
                ResumeButton.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            else :
                Bhover[8] = 0
                ResumeButton.hover('black', 'Image\Button\ButtonNewUnhover.png')

            if BackBotton.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[9] = 1    
                BackBotton.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            else :
                Bhover[9] = 0
                BackBotton.hover('black', 'Image\Button\ButtonNewUnhover.png')
            ###########################################
        else :
            Bhover[7] = 0
            if Next.rect.collidepoint(pygame.mouse.get_pos()) and page != allpage :
                Bhover[10] = 1    
                Next.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            elif page == allpage :
                Next.hover((68,68,68), 'Image\Button\ButtonNewGray.png')
                Bhover[10] = 0
            else :
                Bhover[10] = 0
                Next.hover('black', 'Image\Button\ButtonNewUnhover.png')

            if Prev.rect.collidepoint(pygame.mouse.get_pos()) and page != 1 :
                Bhover[11] = 1    
                Prev.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            elif page == 1 : 
                Prev.hover((68,68,68), 'Image\Button\ButtonNewGray.png')
                Bhover[11] = 0
            else :
                Bhover[11] = 0
                Prev.hover('black', 'Image\Button\ButtonNewUnhover.png')

            if Back.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[12] = 1    
                Back.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            else :
                Bhover[12] = 0
                Back.hover('black', 'Image\Button\ButtonNewUnhover.png')
        #############################################################################^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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

        ########################################## Before Pause : Render Pause Button to pause from menu
        newpausebutton_group.draw(screen)
        newpausebutton_group.update() 
        ##########################################
        ########################################## After Pause : Render Pause Menu option 
        if Pause == 1 :
            page = 1
            screen.blit(POPINBG,(0,0))
            popinbutton_group.draw(screen)
            popinbutton_group.update() 
        ##########################################
        ########################################## If Click on Rule while Pause, Render Rule scene
        elif Pause == 2 :
            screen.blit(RULEPBG,(0,0))
            Page_surface = text_font_regular.render('Page '+str(page)+'/'+str(allpage),True,'Black')
            screen.blit(Page_surface,(25,640))
            # draw all button on the screen
            rulebutton_group.draw(screen)
            rulebutton_group.update() 
            #render text body
            Rule.ruletext (page,text_font_bold,text_font_regular)
        ##########################################
        
        #Update screen
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":
   mainmenu(screen, FPS)