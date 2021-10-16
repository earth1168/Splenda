import pygame,sys
pygame.init()

WIDTH, HEIGHT = 1280,720
FPS = 60
color = ['White']
text_font = pygame.font.Font("Font\Roboto\Roboto-Regular.ttf",50)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPLENDA")
icon = pygame.image.load('choose/splenda.png')
pygame.display.set_icon(icon)

act_id = -1

#load image
profile_width, profile_height = 400,225
bg = pygame.image.load('choose/bg.png')
bg = pygame.transform.scale(bg, (1280,720))
text_player = text_font.render('CHOOSE YOUR CHARACTER',True,color[0]).convert_alpha()
profile1 = pygame.image.load('choose/character/character1.png')
profile1 = pygame.transform.scale(profile1,(200,242))
profile1_rect = profile1.get_rect(midbottom= (160,350))
profile2 = pygame.image.load('choose/character/character2.png')
profile2 = pygame.transform.scale(profile2,(200, 237))
profile2_rect = profile2.get_rect(midbottom= (400,350))
profile3 = pygame.image.load('choose/character/character3.png')
profile3 = pygame.transform.scale(profile3,(200,238))
profile3_rect = profile3.get_rect(midbottom= (640,350))
profile4 = pygame.image.load('choose/character/character4.png')
profile4 = pygame.transform.scale(profile4,(180,238))
profile4_rect = profile4.get_rect(midbottom= (160,600))
profile5 = pygame.image.load('choose/character/character5.png')
profile5 = pygame.transform.scale(profile5,(197,242))
profile5_rect = profile5.get_rect(midbottom= (390,600))
profile6 = pygame.image.load('choose/character/character7.png')
profile6 = pygame.transform.scale(profile6,(185,238))
profile6_rect = profile6.get_rect(midbottom= (640,600))
#show full
fullacter1 = pygame.image.load('choose/characterfull/fullacter1.png')
fullacter1 = pygame.transform.scale(fullacter1,(412,500))
fullacter2 = pygame.image.load('choose/characterfull/fullacter2.png')
fullacter2 = pygame.transform.scale(fullacter2, (422, 500))
fullacter3 = pygame.image.load('choose/characterfull/fullacter3.png')
fullacter3 = pygame.transform.scale(fullacter3,(463,500))
fullacter4 = pygame.image.load('choose/characterfull/fullacter4.png')
fullacter4 = pygame.transform.scale(fullacter4,(378,500))
fullacter5 = pygame.image.load('choose/characterfull/fullacter5.png')
fullacter5 = pygame.transform.scale(fullacter5,(403,500))
fullacter6 = pygame.image.load('choose/characterfull/fullacter6.png')
fullacter6 = pygame.transform.scale(fullacter6,(335,450))
#load bg character
bgacter1 = pygame.image.load('choose/backgroundacter/bgact1.png')
bgacter1 = pygame.transform.scale(bgacter1,(1280,720))
bgacter2 = pygame.image.load('choose/backgroundacter/bgact2.png')
bgacter2 = pygame.transform.scale(bgacter2,(1280,720))
bgacter3 = pygame.image.load('choose/backgroundacter/bgact3.png')
bgacter3 = pygame.transform.scale(bgacter3,(1280,720))
bgacter4 = pygame.image.load('choose/backgroundacter/bgact4.png')
bgacter4 = pygame.transform.scale(bgacter4,(1280,720))
bgacter5 = pygame.image.load('choose/backgroundacter/bgact5.png')
bgacter5 = pygame.transform.scale(bgacter5,(1280,720))
bgacter6 = pygame.image.load('choose/backgroundacter/bgact6.png')
bgacter6 = pygame.transform.scale(bgacter6,(1280,720))


def character():
    screen.blit(bg,(0,0))
    screen.blit(text_player, (100,30))
    screen.blit(profile1, profile1_rect)
    screen.blit(profile2, profile2_rect)
    screen.blit(profile3, profile3_rect)
    screen.blit(profile4, profile4_rect)
    screen.blit(profile5, profile5_rect)
    screen.blit(profile6, profile6_rect)

def showFullActer(acter_id):
    if acter_id == 1:
        screen.blit(bgacter1, (0, 0))
        screen.blit(fullacter1,(830,140))
        screen.blit(text_player, (100, 30))
        screen.blit(profile1, profile1_rect)
        screen.blit(profile2, profile2_rect)
        screen.blit(profile3, profile3_rect)
        screen.blit(profile4, profile4_rect)
        screen.blit(profile5, profile5_rect)
        screen.blit(profile6, profile6_rect)
    if acter_id == 2:
        screen.blit(bgacter2, (0, 0))
        screen.blit(fullacter2,(830,140))
        screen.blit(text_player, (100, 30))
        screen.blit(profile1, profile1_rect)
        screen.blit(profile2, profile2_rect)
        screen.blit(profile3, profile3_rect)
        screen.blit(profile4, profile4_rect)
        screen.blit(profile5, profile5_rect)
        screen.blit(profile6, profile6_rect)
    if acter_id == 3:
        screen.blit(bgacter3, (0, 0))
        screen.blit(fullacter3,(830,140))
        screen.blit(text_player, (100, 30))
        screen.blit(profile1, profile1_rect)
        screen.blit(profile2, profile2_rect)
        screen.blit(profile3, profile3_rect)
        screen.blit(profile4, profile4_rect)
        screen.blit(profile5, profile5_rect)
        screen.blit(profile6, profile6_rect)
    if acter_id == 4:
        screen.blit(bgacter4, (0, 0))
        screen.blit(fullacter4,(830,140))
        screen.blit(text_player, (100, 30))
        screen.blit(profile1, profile1_rect)
        screen.blit(profile2, profile2_rect)
        screen.blit(profile3, profile3_rect)
        screen.blit(profile4, profile4_rect)
        screen.blit(profile5, profile5_rect)
        screen.blit(profile6, profile6_rect)
    if acter_id == 5:
        screen.blit(bgacter5, (0, 0))
        screen.blit(fullacter5,(830,140))
        screen.blit(text_player, (100, 30))
        screen.blit(profile1, profile1_rect)
        screen.blit(profile2, profile2_rect)
        screen.blit(profile3, profile3_rect)
        screen.blit(profile4, profile4_rect)
        screen.blit(profile5, profile5_rect)
        screen.blit(profile6, profile6_rect)
    if acter_id == 6:
        screen.blit(bgacter6, (0, 0))
        screen.blit(fullacter6,(830,140))
        screen.blit(text_player, (100, 30))
        screen.blit(profile1, profile1_rect)
        screen.blit(profile2, profile2_rect)
        screen.blit(profile3, profile3_rect)
        screen.blit(profile4, profile4_rect)
        screen.blit(profile5, profile5_rect)
        screen.blit(profile6, profile6_rect)
    

def main(act_id):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        character()

        mouse_pos = pygame.mouse.get_pos()
        if profile1_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            # print(pygame.mouse.get_pressed())
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 1
                
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if profile2_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 2

        if profile3_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 3

        if profile4_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            print(pygame.mouse.get_pressed())
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_presses[0]:
                    act_id = 4

        if profile5_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 5

        if profile6_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 6
        
        print(act_id)
        showFullActer(act_id)
        pygame.display.update()

if __name__ == "__main__":
    main(act_id)