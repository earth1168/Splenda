import pygame
pygame.init()


screen = pygame.display.set_mode([1280, 720])
bgimage = pygame.image.load("../Image/Card/bg-01.png")
bgimage = pygame.transform.scale(bgimage, (1280, 720))

lv101 = pygame.image.load('../Image/Card/R101T-01.png')
lv101 = pygame.transform.scale(lv101, (122, 167))
lv102 = pygame.image.load('../Image/Card/101.png')
lv102 = pygame.transform.scale(lv102, (122, 167))
lv103 = pygame.image.load('../Image/Card/101.png')
lv103 = pygame.transform.scale(lv103, (122, 167))
lv104 = pygame.image.load('../Image/Card/K101T-01.png')
lv104 = pygame.transform.scale(lv104, (122, 167))

lv201 = pygame.image.load('../Image/Card/201.png')
lv201 = pygame.transform.scale(lv201, (122, 167))
lv202 = pygame.image.load('../Image/Card/202.png')
lv202 = pygame.transform.scale(lv202, (122, 167))
lv203 = pygame.image.load('../Image/Card/203.png')
lv203 = pygame.transform.scale(lv203, (122, 167))
lv204 = pygame.image.load('../Image/Card/204.png')
lv204 = pygame.transform.scale(lv204, (122, 167))

Noble1 = pygame.image.load('../Image/Card/Noble/noble01.png')
Noble1 = pygame.transform.scale(Noble1, (122, 122))
Noble2 = pygame.image.load('../Image/Card/Noble/noble02.png')
Noble2 = pygame.transform.scale(Noble2, (122, 122))
Noble3 = pygame.image.load('../Image/Card/Noble/noble03.png')
Noble3 = pygame.transform.scale(Noble3, (122, 122))
Noble4 = pygame.image.load('../Image/Card/Noble/noble04.png')
Noble4 = pygame.transform.scale(Noble4, (122, 122))
Noble5 = pygame.image.load('../Image/Card/Noble/noble05.png')
Noble5 = pygame.transform.scale(Noble5, (122, 122))


Deck1 = pygame.image.load('../Image/Card/D01.png')
Deck1 = pygame.transform.scale(Deck1, (122, 167))
Deck2 = pygame.image.load('../Image/Card/D02.png')
Deck2 = pygame.transform.scale(Deck2, (122, 167))
Deck3 = pygame.image.load('../Image/Card/D03.png')
Deck3 = pygame.transform.scale(Deck3, (122, 167))
test_font = pygame.font.Font(None,30)
RemainingCard = test_font.render('25',False,'White')

RedCoin = pygame.image.load('../Image/Coin/RedCoin-01.png')
RedCoin = pygame.transform.scale(RedCoin, (108, 108))
BlueCoin = pygame.image.load('../Image/Coin/BlueCoin-01.png')
BlueCoin = pygame.transform.scale(BlueCoin, (108, 108))
GreenCoin = pygame.image.load('../Image/Coin/GreenCoin-01.png')
GreenCoin = pygame.transform.scale(GreenCoin, (108, 108))
BlackCoin = pygame.image.load('../Image/Coin/BlackCoin-01.png')
BlackCoin = pygame.transform.scale(BlackCoin, (108, 108))
WhiteCoin = pygame.image.load('../Image/Coin/WhiteCoin-01.png')
WhiteCoin = pygame.transform.scale(WhiteCoin, (108, 108))
GoldCoin = pygame.image.load('../Image/Coin/GoldCoin-01.png')
GoldCoin = pygame.transform.scale(GoldCoin, (108, 108))


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bgimage,(0,0))
    screen.blit(lv101,(1086,533))
    screen.blit(lv102,(954,533))
    screen.blit(lv103,(822,533))
    screen.blit(lv104,(690,533))
    screen.blit(Deck1,(558,533))
    screen.blit(RemainingCard,(611,675))

    screen.blit(lv201,(1086,356))
    screen.blit(lv202,(954,356))
    screen.blit(lv203,(822,356))
    screen.blit(lv204,(690,356))
    screen.blit(Deck2,(558,356))

    screen.blit(lv101,(1086,179))
    screen.blit(lv102,(954,179))
    screen.blit(lv103,(822,179))
    screen.blit(lv104,(690,179))
    screen.blit(Deck3,(558,179))

    screen.blit(Noble1,(1086,29))
    screen.blit(Noble2,(954,29))
    screen.blit(Noble3,(822,29))
    screen.blit(Noble4,(690,29))
    screen.blit(Noble5,(558,29))
    


    screen.blit(BlackCoin,(440,602))
    screen.blit(RedCoin,(440,484))
    screen.blit(GreenCoin,(440,366))
    screen.blit(BlueCoin,(440,248))
    screen.blit(WhiteCoin,(440,130))
    screen.blit(GoldCoin,(440,12))


    pygame.display.update()
# Done! Time to quit.
pygame.quit()