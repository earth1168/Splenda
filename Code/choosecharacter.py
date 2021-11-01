import pygame, sys
from classButton import Button

pygame.init()

WIDTH, HEIGHT = 1280,720
name_user = []
act_user = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPLENDA")
icon = pygame.image.load('choose/splenda.png')
pygame.display.set_icon(icon)

def character(profile, profile_rect, bg, text_white):
    screen.blit(bg, (0, 0))
    screen.blit(text_white, (40, 10))
    for count, value in enumerate(profile):
        screen.blit(value, profile_rect[count])

def showFullActer(act_id, full_profile, button):
    if act_id != -1:
        screen.blit(full_profile[act_id], (800, 90))
    button.draw(screen)
    button.update()

def showFaceActer(face, name_user, base_font):
    for x, y in enumerate(face):
        screen.blit(y, y.get_rect(topleft = ((x * 120) + 150, 550)))
        text_name3 = base_font.render(name_user[x], True, (255, 255, 255))
        screen.blit(text_name3, y.get_rect(topleft = ((x * 120) + 150, 670)))

def graycharacter(profile_gray, profile_rect):
    for x, y in enumerate(profile_gray):
        if y != None:
            screen.blit(y, profile_rect[x])

def selectCharacter(screen, name_user, act_user):
    clock = pygame.time.Clock()
    face = []
    face_scale = [(128, 100), (110, 100), (100, 108), (100, 132), (100, 119), (100, 107)]

    profile = []
    profile_scale = [(200, 242), (200, 237), (200, 238), (180, 238), (197, 242), (185, 238)]
    profile_rect = []

    full_profile = []
    full_profile_scale = [(330, 400), (339, 400), (371, 400), (302, 400), (322, 400), (307, 400)]

    profile_gray = [None, None, None, None, None, None, None]

    active = False
    user_text = ''
    act_id = -1
    FPS = 15
    text_font = pygame.font.Font("Font\Roboto\Roboto-BlackItalic.ttf", 50)
    base_font = pygame.font.Font(None, 32)

    # input
    frametext = pygame.Rect(815, 491, 160, 50)
    text_rect = pygame.Rect(820, 500, 140, 32)
    color_active = pygame.Color(195, 155, 211)
    color_passive = pygame.Color('white')
    colortext = color_passive

    # button
    button = pygame.sprite.Group()
    b_confirm = Button((1100, 580), (200, 80), 'Confirm', 40, 'Image/Button/testButton-01.png', 'white')
    b_start = Button((850, 580), (200, 80), 'Start', 40, 'Image/Button/testButton-01.png', 'white')

    # load image
    bg = pygame.image.load('Character/bg.png')
    bg = pygame.transform.scale(bg, (1280, 720))
    text_white = text_font.render('CHOOSE YOUR CHARACTER', True, 'white').convert_alpha()

    for p in range(6):
        profile.append(pygame.image.load(f'Character/character/character{p + 1}.png').convert_alpha())
        profile[p] = pygame.transform.scale(profile[p], profile_scale[p])
        profile_rect.append(profile[p].get_rect(midbottom=((p % 3) * 220 + 160, int(p / 3) * 240 + 300)))

    # show full
    for i in range(6):
        full_profile.append(pygame.image.load(f'Character/characterfull/fullacter{i + 1}.png').convert_alpha())
        full_profile[i] = pygame.transform.scale(full_profile[i], full_profile_scale[i])

    run = True
    while run:
        clock.tick(FPS)
        if not button.has(b_confirm):
            button.add(b_confirm)
        #input text user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
            if active:
                colortext = color_active
            else:
                colortext = color_passive

        #show all character
        character(profile, profile_rect, bg, text_white)

        #check mouse click
        mouse_pos = pygame.mouse.get_pos()
        if profile_rect[0].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 0
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if profile_rect[1].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 1

        if profile_rect[2].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 2

        if profile_rect[3].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 3

        if profile_rect[4].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 4

        if profile_rect[5].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 5

        if len(act_user) > 1:
            if b_start.rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_presses = pygame.mouse.get_pressed()
                    if mouse_presses[0]:
                        return 'game'

        if act_id not in act_user and len(act_user) < 4:
            if b_confirm.rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        act_user.append(act_id)
                        name_user.append(user_text)
                        user_text = ''
                        face.append(pygame.image.load(f'Character/face/face{act_id + 1}.png').convert_alpha())
                        face[-1] = pygame.transform.scale(face[-1], face_scale[-1])
                        profile_gray[act_id] = pygame.image.load(f'Character/gray/cha{act_id + 1}.png').convert_alpha()
                        profile_gray[act_id] = pygame.transform.scale(profile_gray[act_id], profile_scale[act_id])

        if act_id != -1:
            pygame.draw.rect(screen, 'black', frametext)
            pygame.draw.rect(screen, colortext, text_rect)
            text_surface = base_font.render(user_text, True, (0, 0, 0))
            screen.blit(text_surface, (text_rect.x + 5, text_rect.y + 5))
            text_rect.w = max(90, text_surface.get_width() + 10)
            frametext.w = max(100, text_surface.get_width() + 20)

        if len(act_user) > 1 and not button.has(b_start):
            button.add(b_start)

        showFullActer(act_id, full_profile, button)
        showFaceActer(face, name_user, base_font)
        graycharacter(profile_gray, profile_rect)
        pygame.display.update()

if __name__ == "__main__":
    selectCharacter(screen, name_user, act_user)