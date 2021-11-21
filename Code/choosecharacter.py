import pygame, sys
from classButtonDirty import ButtonDirty

pygame.init()

# Set resolution
WIDTH, HEIGHT = 1280,720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

name_user = []
act_user = []

# Show all characters for player choose
def character(profile, profile_rect, bg, text_white):
    screen.blit(bg, (0, 0))
    screen.blit(text_white, (40, 10))
    for count, value in enumerate(profile):
        screen.blit(value, profile_rect[count])

# Show large characters 
def showFullActer(act_id, full_profile, button):
    if act_id != -1:
        screen.blit(full_profile[act_id], (800, 90))
    button.draw(screen) #draw button

# Show face character and name player
def showFaceActer(face, name_user, base_font, text_max):
    for x, y in enumerate(face):
        screen.blit(y, y.get_rect(topleft = ((x * 120) + 150, 550)))
        text_name3 = base_font.render(name_user[x], True, (255, 255, 255))
        screen.blit(text_name3, y.get_rect(topleft = ((x * 120) + 150, 670)))

# Change the character's appearance to gray 
def graycharacter(profile_gray, profile_rect):
    for x, y in enumerate(profile_gray):
        if y != None:
            screen.blit(y, profile_rect[x])

def selectCharacter(screen, name_user, act_user):
    clock = pygame.time.Clock()

    # Set size of each image
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
    # Set FPS
    FPS = 15
    # Set text font
    text_font = pygame.font.Font("Font\Roboto\Roboto-BlackItalic.ttf", 50)
    text_max = pygame.font.Font("Font\Roboto\Roboto-BlackItalic.ttf", 35)
    text = pygame.font.Font("Font\Roboto\Roboto-BlackItalic.ttf", 25)
    base_font = pygame.font.Font(None, 32)

    # Create rect for player name field
    frametext = pygame.Rect(970, 491, 160, 50)
    text_rect = pygame.Rect(975, 500, 140, 32)
    color_active = pygame.Color(195, 155, 211)
    color_passive = pygame.Color('white')
    colortext = color_passive

    # Create button
    button = pygame.sprite.LayeredDirty()
    b_confirm = ButtonDirty((1100, 580), (130, 50), 'Confirm', 20, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    b_start = ButtonDirty((850, 580), (130, 50), 'Start', 20, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    b_confirm.visible = b_start.visible = 0
    button.add(b_confirm, b_start)

    # Load image
    bg = pygame.image.load('Character/bg.png')
    bg = pygame.transform.smoothscale(bg, (1280, 720))
    text_white = text_font.render('CHOOSE YOUR CHARACTER', True, 'white').convert_alpha()

    for p in range(6):
        profile.append(pygame.image.load(f'Character/character/character{p + 1}.png').convert_alpha())
        profile[p] = pygame.transform.smoothscale(profile[p], profile_scale[p])
        profile_rect.append(profile[p].get_rect(midbottom=((p % 3) * 220 + 160, int(p / 3) * 240 + 300)))

    # Load image
    for i in range(6):
        full_profile.append(pygame.image.load(f'Character/characterfull/fullacter{i + 1}.png').convert_alpha())
        full_profile[i] = pygame.transform.smoothscale(full_profile[i], full_profile_scale[i])

    run = True
    while run:
        clock.tick(FPS)
        if act_id != -1:
            b_confirm.visible = 1
        else:
            b_confirm.visible = 0

        # Receive text from player/user
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
                    elif len(user_text) < 6 :   # max name player is 6
                        user_text += event.unicode
            if active:
                colortext = color_active
            else:
                colortext = color_passive

        # Show all character
        character(profile, profile_rect, bg, text_white)

        # Check mouse click and stores the value selected by the player
        mouse_pos = pygame.mouse.get_pos()
        if profile_rect[0].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0]:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 0
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if profile_rect[1].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0]:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 1

        if profile_rect[2].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0]:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 2

        if profile_rect[3].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0]:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 3

        if profile_rect[4].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0]:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 4

        if profile_rect[5].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0]:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    act_id = 5

        # Check start button : show start button when player more than 1
        if len(act_user) > 1:
            if b_start.rect.collidepoint(mouse_pos):
                b_start.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                if pygame.mouse.get_pressed()[0]:
                    mouse_presses = pygame.mouse.get_pressed()
                    if mouse_presses[0]:
                        return 'game'
            else:
                b_start.unhover()
                
        # Check confirm button : select character first ,button will be display  
        if act_id not in act_user and len(act_user) < 4 and act_id != -1:         
            if b_confirm.rect.collidepoint(mouse_pos):
                b_confirm.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                if pygame.mouse.get_pressed()[0]:
                    b_confirm.unhover()
                    b_confirm.hover((68,68,68), 'Image\Button\ButtonNewGray.png')
                    act_user.append(act_id)
                    name_user.append(user_text)
                    user_text = ''
                    face.append(pygame.image.load(f'Character/face/face{act_id + 1}.png').convert_alpha())
                    face[-1] = pygame.transform.smoothscale(face[-1], face_scale[-1])
                    # Load image
                    profile_gray[act_id] = pygame.image.load(f'Character/gray/cha{act_id + 1}.png').convert_alpha()
                    profile_gray[act_id] = pygame.transform.smoothscale(profile_gray[act_id], profile_scale[act_id])
            else:
                b_confirm.unhover()
        elif act_id in act_user :
            b_confirm.hover((68,68,68), 'Image\Button\ButtonNewGray.png')

        # Create a name player box
        if act_id != -1:
            pygame.draw.rect(screen, 'black', frametext)     
            pygame.draw.rect(screen, colortext, text_rect)
            text_surface = base_font.render(user_text, True, (0, 0, 0))
            screen.blit(text_surface, (text_rect.x + 5, text_rect.y + 5))
            text_rect.w = max(90, text_surface.get_width() + 10)
            frametext.w = max(100, text_surface.get_width() + 20)
            textname = text.render('Enter your name :', True, 'white').convert_alpha()
            screen.blit(textname, (770, 500))

        if len(act_user) > 1:
            b_start.visible = 1

        # Displays a warning message when the player selects all 4 characters 
        if len(act_user) > 3:
            textmax = text_max.render('Max player is 4', True, 'white').convert_alpha()         
            screen.blit(textmax, (850, 630))

        showFullActer(act_id, full_profile, button)
        showFaceActer(face, name_user, base_font, text_max)
        graycharacter(profile_gray, profile_rect)
        pygame.display.update()

if __name__ == "__main__":
    selectCharacter(screen, name_user, act_user)