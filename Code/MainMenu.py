import pygame
pygame.init()

#Set variable for window size
WIDTH, HEIGHT = 1280,720
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#Set name of screen caption
pygame.display.set_caption("MainMenu")

#Set FPS of the game
FPS = 60
#Set path of background image file
BACKGROUND = pygame.image.load("Image\Background\MainMenu720p.png")


def main() :
    clock = pygame.time.Clock()
    run = True
    while run:
        #FPS of the game
        clock.tick(FPS)

        #Update screen
        pygame.display.flip()

        #Background image
        WIN.blit(BACKGROUND,(0,0))

        #Handle user-input
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False
                
    pygame.quit()

if __name__ == "__main__":
    main()