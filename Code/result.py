import pygame, sys
from classButtonDirty import ButtonDirty
pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPLENDA")
icon = pygame.image.load('Character/splenda.png')
pygame.display.set_icon(icon)

def result(screen):
    act_user = []
    button = pygame.sprite.LayeredDirty()
    b_main = ButtonDirty((1160, 50), (200, 80), 'Main menu', 40, 'Image/Button/testButton-01.png', 'purple')
    bg1 = pygame.image.load('Character/Result2player.png').convert_alpha()
    bg2 = pygame.image.load('Character/Result4&3player.png').convert_alpha()
    bg1 = pygame.transform.smoothscale(bg1, (1280, 720))
    bg2 = pygame.transform.smoothscale(bg2, (1280, 720))

    background = pygame.Surface(screen.get_size()).convert()

    if len(act_user) < 3:
        background.blit(bg1, (0, 0))
    else:
        background.blit(bg2, (0, 0))
    button.add(b_main)
    button.clear(screen, background)

    clock = pygame.time.Clock()
    FPS = 10
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        mouse_pos = pygame.mouse.get_pos()
        if b_main.rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    return 'main menu'
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        rect = button.draw(screen)
        pygame.display.update(rect)

if __name__ == "__main__":
    result(screen)