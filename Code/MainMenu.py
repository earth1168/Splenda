import pygame
pygame.init()
#Set name of screen caption
pygame.display.set_caption("MainMenu")
#Set variable for window size
WIDTH, HEIGHT = 1280,720
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

#Set FPS of the game
FPS = 60
#Text setting
text_font = pygame.font.Font("Font\Roboto\Roboto-Regular.ttf",50)
text_surface = text_font.render('Test',True,'White')
#Set path of background image file
BACKGROUND = pygame.image.load("Image\Background\MainMenu720p.png").convert()


def mainmenu() :
    clock = pygame.time.Clock()
    #Game loop
    run = True
    while run:
        #Background image
        SCREEN.blit(BACKGROUND,(0,0))
        #Test text
        SCREEN.blit(text_surface,(50,250))

        #Handle user-input
        for event in pygame.event.get():
            #Exit game when press X button on window
            if event.type == pygame.QUIT :
                run = False
        
        #FPS of the game
        clock.tick(FPS)
        #Update screen
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
   mainmenu()