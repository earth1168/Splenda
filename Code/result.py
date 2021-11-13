import pygame, sys
from classButtonDirty import ButtonDirty
from classPlayer import Player
pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPLENDA")
icon = pygame.image.load('Character/splenda.png')
pygame.display.set_icon(icon)

player1 = Player(0, 0, 't')
player2 = Player(0, 2, '0123456789')
player3 = Player(0, 4, 'testB0i3')
player4 = Player(0, 5, 'testB0i4saa')
result_player_list = [player1,player2]

def result(screen,result_player_list):
    print("In result")
    for player in result_player_list:
        print(f'{player.name}: {player.score}')
    char = []
    char_scale = [(200, 242), (200, 237), (200, 238), (180, 238), (197, 242), (185, 238)]
    #Text setting
    font = pygame.font.Font("Font\Roboto\Roboto-Bold.ttf",25)

    button = pygame.sprite.LayeredDirty()
    b_main = ButtonDirty((1160, 50), (130, 50), 'Main menu', 20, 'Image\Button\ButtonNewUnhover.png', 'black', 'Font/Roboto/Roboto-Regular.ttf')
    
    for i, player in enumerate(result_player_list):
        char.append(pygame.image.load(f'Character/character/character{player.chr_id+1}.png').convert_alpha())
        char[i] = pygame.transform.smoothscale(char[i], char_scale[player.chr_id])

    bg1 = pygame.image.load('Character/Result2player.png').convert_alpha()
    bg2 = pygame.image.load('Character/Result4&3player.png').convert_alpha()
    bg1 = pygame.transform.smoothscale(bg1, (1280, 720))
    bg2 = pygame.transform.smoothscale(bg2, (1280, 720))

    background = pygame.Surface(screen.get_size()).convert()

    if len(result_player_list) < 3:
        background.blit(bg1, (0, 0))

        background.blit(char[0], (260, 70))
        Player1Surface = font.render(f'{result_player_list[0].name}', True, 'White')
        Player1rect = Player1Surface.get_rect(center = (350,645))
        background.blit(Player1Surface,Player1rect)

        background.blit(char[1], (790, 190))
        Player2Surface = font.render(f'{result_player_list[1].name}', True, 'White')
        Player2rect = Player2Surface.get_rect(center = (895,645))
        background.blit(Player2Surface,Player2rect)
    else:
        background.blit(bg2, (0, 0))

        background.blit(char[0], (150, 80))
        Player1Surface = font.render(f'{result_player_list[0].name}', True, 'White')
        Player1rect = Player1Surface.get_rect(center = (250,635))
        background.blit(Player1Surface,Player1rect)

        background.blit(char[1], (520, 180))
        Player2Surface = font.render(f'{result_player_list[1].name}', True, 'White')
        Player2rect = Player2Surface.get_rect(center = (625,635))
        background.blit(Player2Surface,Player2rect)

        background.blit(char[2], (880, 260))
        Player3Surface = font.render(f'{result_player_list[2].name}', True, 'White')
        Player3rect = Player3Surface.get_rect(center = (1000,675))
        background.blit(Player3Surface,Player3rect)
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
            if event.type == pygame.MOUSEMOTION:
                if b_main.is_collide_mouse(event.pos):
                    b_main.hover((153,0,0), 'Image\Button\ButtonNewhover.png')
                else:
                    b_main.unhover()


        mouse_pos = pygame.mouse.get_pos()
        if b_main.rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    return 'menu'
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        rect = button.draw(screen)
        pygame.display.update(rect)

if __name__ == "__main__":
    result(screen, result_player_list)