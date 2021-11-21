import pygame
import RuleText
from sys import exit
from classButtonDirty import ButtonDirty

# rule scene from main menu
# Argument:
#   screen      -- screen surface 
#   FPS         -- Game Fps
# Return
#   'menu'      -- return to change scene to menu
def rulebook(screen: pygame.surface, FPS: int) :
    clock = pygame.time.Clock()
    #Define default color of button 
    Color = ['White','White','White']
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
    #Set variable to remember if button is hover before change to gray to unhover it
    #Set 0 when unhover and 1 when hover
    hover = [0,0]

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
                    #if click next button change page by +1 until at the end of allpage
                    if Next.rect.collidepoint(pygame.mouse.get_pos()):
                        if page != allpage :
                            page += 1
                    #if click previous button change page by -1 until at the first of allpage
                    if Prev.rect.collidepoint(pygame.mouse.get_pos()):
                        if page != 1 :
                            page -= 1
                    #if click back return 'menu' to change scene
                    if Back.rect.collidepoint(pygame.mouse.get_pos()):
                       return "menu"

        #Change the color of Button when mouse cusor hover above the text
        if Next.rect.collidepoint(pygame.mouse.get_pos()) and page != allpage :
            Next.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            #if button was not hover before, then hover[0] = 1 to indicate that it is hover now
            if hover[0] == 0 :
                hover[0] = 1
        #if page is at the end of allpage change color of button to gray
        elif page == allpage :
            #if button was hover before, then hover[0] = 0 and unhover it to hover it again with different color
            if hover[0] == 1 :
                Next.unhover()
                hover[0] = 0
            Next.hover((68,68,68), 'Image\Button\ButtonNewGray.png')
        else :
            #if button was hover before, then hover[0] = 0 and unhover it
            Next.unhover()
            if hover[0] == 1 :
                hover[0] = 0

        if Prev.rect.collidepoint(pygame.mouse.get_pos()) and page != 1 :
            Prev.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            #if button was not hover before, then hover[0] = 1 to indicate that it is hover now
            if hover[1] == 0 :
                hover[1] = 1
        #if page is the first page change color of button to gray
        elif page == 1 :
            #if button was hover before, then hover[0] = 0 and unhover it to hover it again with different color
            if hover[1] == 1 :
                Prev.unhover()
                hover[1] = 0 
            Prev.hover((68,68,68), 'Image\Button\ButtonNewGray.png')
        else :
            #if button was hover before, then hover[0] = 0 and unhover it
            Prev.unhover()
            if hover[1] == 1 :
                hover[1] = 0

        if Back.rect.collidepoint(pygame.mouse.get_pos()):
            Back.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
        else : 
            Back.unhover()

        #FPS of the game
        clock.tick(FPS)
        #Background image
        screen.blit(BACKGROUND,(0,0))
        #Text page set up and render
        Page_surface = text_font_regular.render('Page '+str(page)+'/'+str(allpage),True,'White')
        screen.blit(Page_surface,(25,640))
        #Render Text for coressponding to page number
        RuleText.ruletext (page,text_font_bold,text_font_regular,screen)
        Next.visible = Prev.visible = Back.visible = 1
        # draw all button on the screen
        button_group.draw(screen)
        #Update screen
        pygame.display.update()

    pygame.quit()
    exit()