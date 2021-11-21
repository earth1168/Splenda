#Written by Pojnarin 62070501041
import pygame
import RuleText
from sys import exit
from classButtonDirty import ButtonDirty
pygame.init()
#Set variable for window size
WIDTH, HEIGHT = 1280,720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#Set FPS of the game
FPS = 25

def rulebook(screen, FPS) :
    clock = pygame.time.Clock()
    #Set name of screen caption
    pygame.display.set_caption("Rule of the game")
    #Define default color of button 
    Color = ['White','White','White']
    #Define variable to monitor if mouse hover over button
    Bhover = [0,0,0]
    # group of buttons. work with sprite (Button class in this context)
    button_group = pygame.sprite.LayeredDirty()
    # button with 'start' text, button's background image, set colors, and set font 
    Next = ButtonDirty((1180,140), (130, 50), 'Next', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    # button with 'exit' text, button's background image, set colors, and default font 
    Prev = ButtonDirty((85,140), (140, 50), 'Previous', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    # button with 'Menu' text, button's background image, set colors, and default font 
    Back = ButtonDirty((1180,640), (130, 50), 'Menu', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    #Set path of background image file
    BACKGROUND = pygame.image.load("Image\Background\Rule720p.png").convert()
    #Text setting
    text_font_bold = pygame.font.Font("Font\Roboto\Roboto-Bold.ttf",40)
    text_font_regular = pygame.font.Font("Font\Roboto\Roboto-Regular.ttf",30)

    # add button to group
    button_group.add(Next, Prev,Back)
    button_group.clear(screen, BACKGROUND)
    #Set page of text. Default is page 1
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 :
                    print(event.pos)
                    if Next.rect.collidepoint(pygame.mouse.get_pos()):
                        if page != allpage :
                            page += 1
                    if Prev.rect.collidepoint(pygame.mouse.get_pos()):
                        if page != 1 :
                            page -= 1
                    if Back.rect.collidepoint(pygame.mouse.get_pos()):
                       return "menu"

        #Change the color of Button when mouse cusor hover above the text
        if Next.rect.collidepoint(pygame.mouse.get_pos()) and page != allpage :
            Next.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            Bhover[0] = 1
        elif page == allpage :
            Next.hover((68,68,68), 'Image\Button\ButtonNewGray.png')
            Bhover[0] = 0
        else :
            Next.unhover()
            Bhover[0] = 0

        if Prev.rect.collidepoint(pygame.mouse.get_pos()) and page != 1 :
            Prev.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            Bhover[1] = 1
        elif page == 1 : 
            Prev.hover((68,68,68), 'Image\Button\ButtonNewGray.png')
            Bhover[1] = 0
        else :
            Prev.unhover()
            Bhover[1] = 0


        if Back.rect.collidepoint(pygame.mouse.get_pos()):
            Back.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            Bhover[2] = 1
        else : 
            Back.unhover()
            Bhover[2] = 0

        #if any button are hover, mouse cursor will turn to hand 
        if 1 in Bhover :
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else :
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        #FPS of the game
        clock.tick(FPS)
        #Background image
        screen.blit(BACKGROUND,(0,0))
        #Text page set up and render
        Page_surface = text_font_regular.render('Page '+str(page)+'/'+str(allpage),True,'White')
        screen.blit(Page_surface,(25,640))
        RuleText.ruletext (page,text_font_bold,text_font_regular,screen)
        Next.visible = Prev.visible = Back.visible = 1
        # draw all button on the screen
        button_group.draw(screen)
        #render text body
        #Update screen
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":
   rulebook(screen, FPS)