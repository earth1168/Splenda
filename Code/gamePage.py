# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1280, 720])
bgimage = pygame.image.load('Test/bg-01.png')
bgimage = pygame.transform.scale(bgimage, (1280, 720))

lv101 = pygame.image.load('Test/R101T-01.png')
lv101 = pygame.transform.scale(lv101, (122, 167))
lv102 = pygame.image.load('Test/101.png')
lv102 = pygame.transform.scale(lv102, (122, 167))
lv103 = pygame.image.load('Test/101.png')
lv103 = pygame.transform.scale(lv103, (122, 167))
lv104 = pygame.image.load('Test/K101T-01.png')
lv104 = pygame.transform.scale(lv104, (122, 167))

Deck1 = pygame.image.load('Test/D01.png')
Deck1 = pygame.transform.scale(Deck1, (122, 167))
Deck2 = pygame.image.load('Test/D02.png')
Deck2 = pygame.transform.scale(Deck2, (122, 167))
Deck3 = pygame.image.load('Test/D03.png')
Deck3 = pygame.transform.scale(Deck3, (122, 167))
test_font = pygame.font.Font(None,30)
RemainingCard = test_font.render('25',False,'White')

RedCoin = pygame.image.load('Test/RedCoin-01.png')
RedCoin = pygame.transform.scale(RedCoin, (108, 108))
BlueCoin = pygame.image.load('Test/BlueCoin-01.png')
BlueCoin = pygame.transform.scale(BlueCoin, (108, 108))
GreenCoin = pygame.image.load('Test/GreenCoin-01.png')
GreenCoin = pygame.transform.scale(GreenCoin, (108, 108))
BlackCoin = pygame.image.load('Test/BlackCoin-01.png')
BlackCoin = pygame.transform.scale(BlackCoin, (108, 108))
WhiteCoin = pygame.image.load('Test/WhiteCoin-01.png')
WhiteCoin = pygame.transform.scale(WhiteCoin, (108, 108))
GoldCoin = pygame.image.load('Test/GoldCoin-01.png')
GoldCoin = pygame.transform.scale(GoldCoin, (108, 108))


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bgimage,(0,0))
    screen.blit(lv101,(1036,533))
    screen.blit(lv102,(904,533))
    screen.blit(lv103,(772,533))
    screen.blit(lv104,(640,533))
    screen.blit(Deck1,(508,533))
    screen.blit(RemainingCard,(561,675))

    screen.blit(lv101,(1036,356))
    screen.blit(lv102,(904,356))
    screen.blit(lv103,(772,356))
    screen.blit(lv104,(640,356))
    screen.blit(Deck2,(508,356))

    screen.blit(lv101,(1036,179))
    screen.blit(lv102,(904,179))
    screen.blit(lv103,(772,179))
    screen.blit(lv104,(640,179))
    screen.blit(Deck3,(508,179))

    screen.blit(BlackCoin,(390,602))
    screen.blit(RedCoin,(390,484))
    screen.blit(GreenCoin,(390,366))
    screen.blit(BlueCoin,(390,248))
    screen.blit(WhiteCoin,(390,130))
    screen.blit(GoldCoin,(390,12))


    pygame.display.update()
# Done! Time to quit.
pygame.quit()