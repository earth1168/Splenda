import pygame
import sys
import os

from pygame.constants import MOUSEMOTION

path = os.getcwd()
sys.path.insert(0, path)

from classButtonDirty import ButtonDirty
pygame.init()
#Set variable for window size
WIDTH, HEIGHT = 1280,720
res = (1280,720)
infoObj = pygame.display.Info()
screen = pygame.display.set_mode(res)
isFullscreen = False
volume = 1
#Set FPS of the game
FPS = 25

# change screen resolution. return new resolution
def change_resolution(screen, res_new, isFullscreen):
    if isFullscreen:
        # flags = pygame.FULLSCREEN | pygame.SCALED
        flags = pygame.FULLSCREEN
    else:
        flags = 0
    screen = pygame.display.set_mode(res_new, flags)
    return res_new

def setting(screen, FPS, res, isFullscreen, volume) :
    clock = pygame.time.Clock()
    #Set name of screen caption
    pygame.display.set_caption("Game setting")
    BACKGROUND = pygame.image.load("Image\Background\Setting720p.png").convert()
    #Text setting
    font = pygame.font.Font("Font\Roboto\Roboto-Regular.ttf",30)
    isFullscreen = isFullscreen
    window_mode = ['Window', 'Fullscreen']
    # Define buttons and their group (only use fullscreen/window button(b3))
    button_group = pygame.sprite.LayeredDirty()
    #Setting Text
    ScreenModeSurface = font.render('Screen Mode : ', True, 'Black')
    # button for changing window mode ##################################################################################
    if isFullscreen:
        Mode = ButtonDirty((570, 255), (180, 50), window_mode[1], 30, 'Image\Button\ButtonNewUnhover.png', 'black')
    else:
        Mode = ButtonDirty((570, 255), (180, 50), window_mode[0], 30, 'Image\Button\ButtonNewUnhover.png', 'black')
    # button for going back to mainmenu
    Back = ButtonDirty((1180,640), (130, 50), 'Menu', 30, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    button_group.add(Mode,Back)
    button_group.clear(screen, BACKGROUND)

    #Music slider ####################################################################################################
    change_volume = 0
    slide_rect = pygame.draw.rect(screen,(188, 186, 169, 0.77), [490,350,300,25],0)
    pygame.draw.rect(screen,(250, 162, 30, 1), [490,350,300*(volume/1),25],0)
    MusicSurface = font.render('Music volume : ', True, 'Black')
    volumeSurface = font.render("%.0f %%" % (volume*100), True, 'Black')

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
                    if Mode.rect.collidepoint(pygame.mouse.get_pos()):
                        isFullscreen = not isFullscreen
                        # change text on the button
                        if isFullscreen:
                            Mode.update_text(window_mode[1])
                        else:
                            Mode.update_text(window_mode[0])
                        res = change_resolution(screen, res, isFullscreen)  
                    if Back.rect.collidepoint(pygame.mouse.get_pos()):
                        return 'menu', isFullscreen, volume  
                    if slide_rect.collidepoint(pygame.mouse.get_pos()):
                        volume = (pygame.mouse.get_pos()[0]-490)/300  
                        change_volume = 1

            if event.type == pygame.MOUSEMOTION:
                if change_volume == 1 :
                    volume = (pygame.mouse.get_pos()[0]-490)/300
                    if volume > 1 :
                        volume = 1
                    elif volume < 0 :
                        volume = 0
            
            if event.type == pygame.MOUSEBUTTONUP:
                change_volume = 0

        if Mode.rect.collidepoint(pygame.mouse.get_pos()):
            Mode.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
        else : 
            Mode.unhover()
        
        if Back.rect.collidepoint(pygame.mouse.get_pos()):
            Back.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
        else : 
            Back.unhover()

        #FPS of the game
        clock.tick(FPS)
        screen.blit(BACKGROUND,(0,0))
        screen.blit(ScreenModeSurface,(275,235))
        screen.blit(MusicSurface,(275,345))
        volumeSurface = font.render("%.0f %%" % (volume*100), True, 'Black')
        screen.blit(volumeSurface,(800,345))
        #Music update
        #pygame.draw.rect(surface,color(RGB,RGBA),[position_x,position_y,size_x,size_y,radious_outline,rightbtt,lefttop,righttop,leftbtt]
        pygame.draw.rect(screen,(188, 186, 169, 0.77), [490,350,300,25],0)
        pygame.draw.rect(screen,(250, 162, 30, 1), [490,350,300*(volume/1),25],0)
        pygame.mixer.music.set_volume(volume)

        Mode.dirty = Back.dirty = 1
        # draw button
        button_group.draw(screen)
        #Update screen
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":
   setting(screen, FPS, res, isFullscreen, volume)