import pygame
from sys import exit
pygame.init()
#Set variable for window size
WIDTH, HEIGHT = 1280,720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#Set FPS of the game
FPS = 60

def text_block(font, text, color, pos, block_width, screen) :
    # 2D array where each row is a list of words
    words = [word.split(' ') for word in text.splitlines()]
    # The width of a space
    space = font.size(' ')[0]
    x, y = pos
    #loop for each line in all the text
    for line in words :
        #loop for each word in one line
        for word in line :
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            #if this word in this line of text exceed block_width, put this word on the next line
            if x + word_width >= block_width :
                # Reset the x.
                x = pos[0]
                # Start on new row
                y += word_height
            #render on screen
            screen.blit(word_surface, (x, y))
            #add space(' ') between words
            x += word_width + space
        # Reset the x
        x = pos[0]
        # Start on new row
        y += word_height

def rulebook(screen, FPS) :
    clock = pygame.time.Clock()
    #Set name of screen caption
    pygame.display.set_caption("Rule of the game")
    #Define color of text
    Color = ['White','White','White','White','White','White','White']
    #Text setting
    text_font = pygame.font.Font("Font\Roboto\Roboto-Regular.ttf",30)
    #Set path of background image file
    BACKGROUND = pygame.image.load("Image\Background\MainMenu720p.png").convert()
    
    text = "This is a really long sentence with a couple of breaks.\nSometimes it will break even if there isn't a break " \
       "in the sentence, but that's because the text is too long to fit the screen.\nIt can look strange sometimes.\n" \
       "This function doesn't check if the text is too high to fit on the height of the surface though, so sometimes " \
       "text will disappear underneath the surface"

    #Game loop
    run = True
    while run:
        #Handle user-input
        for event in pygame.event.get():
            #Exit game when press X button on window
            if event.type == pygame.QUIT :
                run = False
                
        #FPS of the game
        clock.tick(FPS)
        #Background image
        screen.blit(BACKGROUND,(0,0))
        text_block(text_font, text, 'White', (10,20), 800, screen)
        #Update screen
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":
   rulebook(screen, FPS)