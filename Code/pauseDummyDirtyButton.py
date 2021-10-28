#Written by Pojnarin 62070501041
import pygame
import Rule
from sys import exit

from pygame.mixer import pause
from classButtonDirty import ButtonDirty

pygame.init()
#Set variable for window size
WIDTH, HEIGHT = 1280,720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#Set FPS of the game
FPS = 30

def mainmenu(screen, FPS) :
    clock = pygame.time.Clock()
    #Set name of screen caption
    pygame.display.set_caption("MainMenu")
    #Set path of background image file
    BACKGROUND = pygame.image.load("Image\Background\MainMenu720p.png").convert()
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

    #DirtyButton Start Here ################################### NNNNNNNNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEEEEWWWWWWWWWWWWWWWWWWWWWWWWWWW
    
    btn_pause = ButtonDirty((100,550), (130, 50), 'Pause', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    #Pop up button
    btn_Rule = ButtonDirty((670,300), (140, 70), 'Rule', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    btn_Resume = ButtonDirty((670,400), (140, 70), 'Resume', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    btn_Back = ButtonDirty((670,520), (250, 70), 'Back to Menu', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    #Rule Button
    Next = ButtonDirty((1180,140), (130, 50), 'Next', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    Prev = ButtonDirty((85,140), (140, 50), 'Previous', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    Back = ButtonDirty((1180,640), (130, 50), 'Menu', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    #Set visibility
    btn_pause.visible = 1
    btn_Rule.visible = btn_Resume.visible = btn_Back.visible = Next.visible = Prev.visible = Back.visible = 0
    #Add button in group
    Menusprites = pygame.sprite.LayeredDirty()
    Menusprites.add(btn_pause)
    Popupsprites = pygame.sprite.LayeredDirty()
    Popupsprites.add(btn_Rule, btn_Resume, btn_Back)
    Rulesprites = pygame.sprite.LayeredDirty()
    Rulesprites.add(Next, Prev, Back)
    #SetBackGround
    Menusprites.clear(screen, BACKGROUND)
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
                        ##########################################v
                        #New Button
                        if btn_pause.rect.collidepoint(pygame.mouse.get_pos()):
                            Pause = 1
                        ##########################################^
                    elif Pause == 1 :
                        if btn_Back.rect.collidepoint(pygame.mouse.get_pos()):
                            print("return 'menu' ")
                            Pause = 0
                        if btn_Resume.rect.collidepoint(pygame.mouse.get_pos()):
                            Pause = 0
                        if btn_Rule.rect.collidepoint(pygame.mouse.get_pos()):
                            Pause = 2
                            print(Pause)
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

            #New Button
            if btn_pause.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[6] = 1    
                btn_pause.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            else :
                Bhover[6] = 0
                btn_pause.hover('black', 'Image\Button\ButtonNewUnhover.png')
                

        elif Pause == 1 :
            Bhover[3] = 0
            ########################################## Hover effect of Pause Button on menu
            #New Button
            Bhover[10] = 0
            Bhover[11] = 0
            Bhover[12] = 0
            Bhover[6] = 0
            btn_pause.hover('black', 'Image\Button\ButtonNewUnhover.png')

            ########################################### Hover effect of Pause Menu Option
            if btn_Rule.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[7] = 1    
                btn_Rule.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            else :
                Bhover[7] = 0
                btn_Rule.hover('black', 'Image\Button\ButtonNewUnhover.png')

            if btn_Resume.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[8] = 1    
                btn_Resume.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            else :
                Bhover[8] = 0
                btn_Resume.hover('black', 'Image\Button\ButtonNewUnhover.png')

            if btn_Back.rect.collidepoint(pygame.mouse.get_pos()):
                Bhover[9] = 1    
                btn_Back.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            else :
                Bhover[9] = 0
                btn_Back.hover('black', 'Image\Button\ButtonNewUnhover.png')
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

        Menusprites.draw(screen)
        btn_pause.visible = 1
        ########################################## After Pause : Render Pause Menu option 
        if Pause == 1 :
            page = 1
            screen.blit(POPINBG,(0,0))

            btn_Back.visible = btn_Resume.visible = btn_Rule.visible = 1
            Popupsprites.draw(screen)
        ##########################################
        ########################################## If Click on Rule while Pause, Render Rule scene
        elif Pause == 2 :
            screen.blit(RULEPBG,(0,0))

            Page_surface = text_font_regular.render('Page '+str(page)+'/'+str(allpage),True,'Black')
            screen.blit(Page_surface,(25,640))

            Rule.ruletext (page,text_font_bold,text_font_regular)

            Next.visible = Prev.visible = Back.visible = 1

            Rulesprites.draw(screen)
        ##########################################
        #Update screen
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":
   mainmenu(screen, FPS)