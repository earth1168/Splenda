import pygame
from sys import exit
from classText import TButton
pygame.init()

# main menu scene
# Argument:
#   screen      -- screen surface 
#   FPS         -- Game Fps
# Return
#   str         -- name's string for next scene
def mainmenu(screen: pygame.surface, FPS: int) :
    clock = pygame.time.Clock()
    #Set path of background image file
    BACKGROUND = pygame.image.load("Image\Background\MainMenu720p.png").convert()
    #Set path of pause background image file
    PAUSEBG = pygame.image.load("Image\Popup\Popup720p.png").convert_alpha()
    #define variable for state of the game, 0 = unpause and 1 = pause
    Pause = 0
    #Create group of text button objects for mainmenu option
    button_group = pygame.sprite.Group()
    StartGame = TButton((50,250),'StartGame',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    Rule = TButton((50,320),'Rule',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    Setting = TButton((50,390),'Setting',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    Exit = TButton((50,460),'Exit',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    button_group.add(StartGame,Rule,Setting,Exit)
    #Create group of text button objects for when the game is pause
    pause_button_group = pygame.sprite.Group()
    QExit = TButton((326,244),'Are you sure you want to exit?',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    Yes = TButton((436,420),'Yes',50,'White',"Font\Roboto\Roboto-Regular.ttf")
    No = TButton((818,420),'No',50,'White',"Font\Roboto\Roboto-Regular.ttf")
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
                    #When no popup on the scene, clicked text button return scene name to change scene to that page 
                    if Pause == 0 :
                        #if click star game button, return "select_character"
                        if StartGame.rect.collidepoint(pygame.mouse.get_pos()):
                            return "select_character"
                        #if click rule button, return "rule_book"
                        if Rule.rect.collidepoint(pygame.mouse.get_pos()):
                            return "rule_book"
                        #if click Setting button, return "setting"
                        if Setting.rect.collidepoint(pygame.mouse.get_pos()):
                            return "setting"
                        #if click exit button, pause the scene and show popup
                        if Exit.rect.collidepoint(pygame.mouse.get_pos()) :
                            Pause = 1
                    #When there is popup on the scene
                    else :
                        if Yes.rect.collidepoint(pygame.mouse.get_pos()):
                            run = False
                        if No.rect.collidepoint(pygame.mouse.get_pos()):
                            Pause = 0

        #Change the color of text when mouse cusor hover above the text from white to gold
        #When no popup on the scene
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
        #When there is popup on the scene
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
        #When there is popup on the scene
        if Pause == 1 :
            #Render pause background and text when popup
            screen.blit(PAUSEBG,(0,0))
            pause_button_group.draw(screen)
            pause_button_group.update()
        #Update screen
        pygame.display.update()

    pygame.quit()
    exit()