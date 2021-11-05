#Written by Pimanus 62070501039
import pygame
pygame.init()


screen = pygame.display.set_mode([1280, 720])
bgimage = pygame.image.load("../Image/Card/bg-01.png")
bgimage = pygame.transform.scale(bgimage, (1280, 720))

lv101 = pygame.image.load('../Image/Card/Lv1/101.png')
lv101 = pygame.transform.smoothscale (lv101, (122, 167))
lv102 = pygame.image.load('../Image/Card/Lv1/102.png')
lv102 = pygame.transform.smoothscale (lv102, (122, 167))
lv103 = pygame.image.load('../Image/Card/Lv1/103.png')
lv103 = pygame.transform.smoothscale (lv103, (122, 167))
lv104 = pygame.image.load('../Image/Card/Lv1/104.png')
lv104 = pygame.transform.smoothscale (lv104, (122, 167))

lv201 = pygame.image.load('../Image/Card/Lv2/201.png')
lv201 = pygame.transform.smoothscale (lv201, (122, 167))
lv202 = pygame.image.load('../Image/Card/Lv2/202.png')
lv202 = pygame.transform.smoothscale (lv202, (122, 167))
lv203 = pygame.image.load('../Image/Card/Lv2/203.png')
lv203 = pygame.transform.smoothscale (lv203, (122, 167))
lv204 = pygame.image.load('../Image/Card/Lv2/204.png')
lv204 = pygame.transform.smoothscale (lv204, (122, 167))

lv301 = pygame.image.load('../Image/Card/Lv3/301.png')
lv301 = pygame.transform.smoothscale (lv301, (122, 167))
lv302 = pygame.image.load('../Image/Card/Lv3/302.png')
lv302 = pygame.transform.smoothscale (lv302, (122, 167))
lv303 = pygame.image.load('../Image/Card/Lv3/303.png')
lv303 = pygame.transform.smoothscale (lv303, (122, 167))
lv304 = pygame.image.load('../Image/Card/Lv3/304.png')
lv304 = pygame.transform.smoothscale (lv304, (122, 167))


Noble1 = pygame.image.load('../Image/Card/Noble/N01.png')
Noble1 = pygame.transform.smoothscale (Noble1, (122, 122))
Noble2 = pygame.image.load('../Image/Card/Noble/N02.png')
Noble2 = pygame.transform.smoothscale (Noble2, (122, 122))
Noble3 = pygame.image.load('../Image/Card/Noble/N03.png')
Noble3 = pygame.transform.smoothscale (Noble3, (122, 122))
Noble4 = pygame.image.load('../Image/Card/Noble/N04.png')
Noble4 = pygame.transform.smoothscale (Noble4, (122, 122))
Noble5 = pygame.image.load('../Image/Card/Noble/N05.png')
Noble5 = pygame.transform.smoothscale (Noble5, (122, 122))


Deck1 = pygame.image.load('../Image/Card/D01.png')
Deck1 = pygame.transform.smoothscale (Deck1, (122, 167))
Deck2 = pygame.image.load('../Image/Card/D02.png')
Deck2 = pygame.transform.smoothscale (Deck2, (122, 167))
Deck3 = pygame.image.load('../Image/Card/D03.png')
Deck3 = pygame.transform.smoothscale (Deck3, (122, 167))
test_font = pygame.font.Font(None,30)
RemainingCard = test_font.render('25','AA','White')

RedCoin = pygame.image.load('../Image/Coin/RedCoin-01.png')
RedCoin = pygame.transform.smoothscale (RedCoin, (108, 108))
BlueCoin = pygame.image.load('../Image/Coin/BlueCoin-01.png')
BlueCoin = pygame.transform.smoothscale (BlueCoin, (108, 108))
GreenCoin = pygame.image.load('../Image/Coin/GreenCoin-01.png')
GreenCoin = pygame.transform.smoothscale (GreenCoin, (108, 108))
BlackCoin = pygame.image.load('../Image/Coin/BlackCoin-01.png')
BlackCoin = pygame.transform.smoothscale (BlackCoin, (108, 108))
WhiteCoin = pygame.image.load('../Image/Coin/WhiteCoin-01.png')
WhiteCoin = pygame.transform.smoothscale (WhiteCoin, (108, 108))
GoldCoin = pygame.image.load('../Image/Coin/GoldCoin-01.png')
GoldCoin = pygame.transform.smoothscale (GoldCoin, (108, 108))

name_user = 1
act_user = 1

def getPlayer(name_user, act_user):
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

        screen.blit(lv301,(1086,179))
        screen.blit(lv302,(954,179))
        screen.blit(lv303,(822,179))
        screen.blit(lv304,(690,179))
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
    exit()
if __name__ == "__main__":
    getPlayer(name_user, act_user)