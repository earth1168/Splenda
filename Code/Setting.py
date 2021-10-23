import pygame
import sys
import os

path = os.getcwd()
sys.path.insert(0, path)

from Code.classButton import Button
from Code.classText import TButton

pygame.init()
#Set variable for window size
WIDTH, HEIGHT = 1280,720
res = (1280,720)
infoObj = pygame.display.Info()
screen = pygame.display.set_mode(res)
isFullscreen = False
#Set FPS of the game
FPS = 60

# change screen resolution. return new resolution
def change_resolution(screen, res_new, isFullscreen):
    if isFullscreen:
        # flags = pygame.FULLSCREEN | pygame.SCALED
        flags = pygame.FULLSCREEN
    else:
        flags = 0
    screen = pygame.display.set_mode(res_new, flags)
    return res_new

def setting(screen, FPS, res , isFullscreen) :
    clock = pygame.time.Clock()
    #Set name of screen caption
    pygame.display.set_caption("Game setting")
    BACKGROUND = pygame.image.load("Image\Background\Setting720p.png").convert()
    #Text setting
    text_font = pygame.font.Font("Font\Roboto\Roboto-Regular.ttf",50)
    isFullscreen = isFullscreen
    old_option = -1
    window_mode = ['Window', 'Fullscreen']

    # Define buttons and their group (only use fullscreen/window button(b3))
    button_group = pygame.sprite.Group()
    #Setting Text
    ScreenMode = TButton((275,235),'Screen Mode : ',30,'Black',"Font\Roboto\Roboto-Regular.ttf")    
    # button for changing window mode
    Mode = Button((570, 255), (180, 50), window_mode[1], 30, 'Image\Button\ButtonNewUnhover.png', 'black')
    # button for going back to mainmenu
    Back = Button((1180,640), (130, 50), 'Menu', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    button_group.add(ScreenMode,Mode,Back)
    Bhover = [0,0]

    #Game loop
    run = True
    while run:
        event_list = pygame.event.get()
        #Handle user-input
        for event in event_list :
            #Exit game when press X button on window
            if event.type == pygame.QUIT :
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 :
                    print(event.pos)
                    if Mode.rect.collidepoint(pygame.mouse.get_pos()):
                        isFullscreen = not isFullscreen
                        # change text on the button
                        if isFullscreen:
                            Mode.text = window_mode[0]
                        else:
                            Mode.text = window_mode[1]
                        res = change_resolution(screen, res, isFullscreen)  
                    if Back.rect.collidepoint(pygame.mouse.get_pos()):
                        return "menu"

        if Mode.rect.collidepoint(pygame.mouse.get_pos()):
            Mode.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            Bhover[0] = 1
        else : 
            Mode.hover('black', 'Image\Button\ButtonNewUnhover.png')
            Bhover[0] = 0
        
        if Back.rect.collidepoint(pygame.mouse.get_pos()):
            Back.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
            Bhover[1] = 1
        else : 
            Back.hover('black', 'Image\Button\ButtonNewUnhover.png')
            Bhover[1] = 0
        
        #if any button are hover, mouse cursor will turn to hand 
        if 1 in Bhover :
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else :
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        #FPS of the game
        clock.tick(FPS)
        screen.blit(BACKGROUND,(0,0))
        # draw button
        button_group.draw(screen)
        button_group.update()
        #Update screen
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":
   setting(screen, FPS, res, isFullscreen)