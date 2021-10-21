import pygame
from sys import exit
pygame.init()
#Set variable for window size
WIDTH, HEIGHT = 1280,720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#Set FPS of the game
FPS = 60

def text_block(font, text, color, pos, block_width, screen, row_height) :
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
                y += word_height+row_height
            #if the word '\t' is the word, make a empty space in paragraph
            if word != '\b' and word != '\t' :
                #render on screen
                screen.blit(word_surface, (x, y))
            if word == '\t' :
                x += space+space+space
            #add space(' ') between words
            x += word_width + space
        # Reset the x
        x = pos[0]
        # Start on new row
        y += word_height+row_height

def Textpage (page) :
    components = "7 \b Emerald tokens (green)\n" \
        "7 \b Diamond tokens (white)\n" \
        "7 \b Sapphire tokens (blue)\n" \
        "7 \b Onyx tokens(black)\n" \
        "7 \b Ruby tokens (red)\n" \
        "5 \b Gold Joker tokens (yellow)\n" \
        "90 Development cards\n" \
        "10 Noble tiles"
    
    EndGame = "\t When a player reaches 15 prestige points," \
        " complete the current round so that each player has played the same number of turns.\n" \
        " \t The player who then has the highest number of prestige points is declared the winner (don't forget to count your nobles).\n" \
        " \t In case of a tie, the player who has purchased the fewest development cards wins."
    
    Game2Player = "- \t Remove 3 tokens of each gem color \n \t (there should be only 4 of each remaining).\n" \
        "- \t Don't touch the gold.\n" \
        "- \t Reveal 3 noble tiles."

    Game3Player = "- \t Remove 2 tokens of each gem color \n \t (there should be only 5 of each remaining).\n" \
        "- \t Don't touch the gold.\n" \
        "- \t Reveal 4 noble tiles."

    Setup1 = "- \t Development card decks are place in a column in the middle of the screen in increasing order from bottom to top.\n" \
        "- \t 4 cards from each development card deck level are reveal next to the decks at right.\n" \
        "- \t the noble tiles are reveal as many of them as there are players plus one.\n"
    
    Setup2 = "- \t The tokens are place in 6 distinct piles (sort them by color) next to the decks at left."

    DevCard = "To win prestige points, the players must purchase development cards.\n" \
        "These cards are visible in the middle of the table and may be purchased by all players during the game.\n" \
        "The developments in hand are the cards which the players reserve throughout the game.\n" \
        "Developments in hand may only be purchased by the players holding them."

    NobleCard = "The noble tiles are visible in the middle of the table.\n" \
        "At the end of their turn, a player automatically receives the visit from a noble if that player has the amount of bonuses (and only bonuses) required, and they get the corresponding tile.\n" \
        "A player cannot refuse a visit from a noble.\n" \
        "Receiving a noble isn't considered to be an action. Each noble tile is worth 3 prestige points, but players can only get a single one per turn."

    Gameplay = "The turn order is chosen randomly at the start.\n" \
        "On their turn, a player must choose to perform only one of the following four actions:\n" \
        "\t - \t Take 3 gem tokens of different colors.\n" \
        "\t - \t Take 2 gem tokens of the same color. This action is only possible if there are at least 4 tokens of the chosen color left when the player takes them.\n" \
        "\t - \tReserve 1 development card and take 1 gold token (joker).\n" \
        "\t - \tPurchase 1 face-up development card from the middle of the table or a previously reserved one."

    Selecttoken = "A player can never have more than 10 tokens at the end of their turn (including jokers).\n" \
        "If this happens, they must return tokens until they only have 10 left.\n" \
        "Note: players may not take 2 tokens of the same color if there are less than 4 tokens available of that color."

    Reserve = "To reserve a card, a player simply needs to take a face-up development from the middle of the table or (if you're feeling lucky) draw the first card from one of the three decks (level 1; level 2 ; level 3) without showing it to the other players.\n" \
        "The reserved cards are kept in hand and cannot be discarded.\n" \
        "Players may not have more than three reserved cards in hand, and the only way to get rid of a card is to buy it.\n" \
        "Reserving a card is also the only way to get a gold token (joker).\n" \
        "If there is no gold left, you can still reserve a card, but you won't get any gold."

    Buying = "To purchase a card, a player must spend the number of tokens indicated on the card.\n"\
        "A joker token can replace any color.\n" \
        "The spent tokens (including any jokers) are returned to the middle of the table.\n" \
        "A player may purchase one of the face-up development cards in the middle of the table or a card in his hand that was reserved on a previous turn.\n" \
        "Each player makes distinct rows with the acquired development cards by sorting them by color, and staggering them vertically so that their bonuses and prestige point values are visible.\n" \
        "The bonuses and prestige points granted by each card must be visible to all at all times.\n" \
        "Note: when a development card from the middle of the table is acquired or reserved, it must immediately be replaced by a card of the same level.\n" \
        "At all times during the game, there must be 4 face-up cards of each level (unless the deck in question is empty, in which case the empty spaces also remain empty)."

    Bonus = "The bonuses a player has from development cards acquired on previous turns provide discounts on the purchase of new cards.\n" \
        "Each bonus of a given color is equal to a token of that color.\n" \
        "Thus, if a player has 2 blue bonuses and wants to purchase a card which costs 2 blue tokens and 1 green token, the player must only spend 1 green token.\n" \
        "If a player has enough development cards (and therefore bonuses), they can even purchase a card without spending any tokens."

    Noble = "At the end of their turn, each player checks the noble tiles in order to determine if they're receiving a visit from one of them. A player can be visited if they have (at least) the quantity and type of bonuses indicated on the noble tile.\n" \
        "It is impossible to refuse the visit from a noble, which is not considered to be an action.\n" \
        "If a player has enough bonuses to be visited by more than one noble at the end of their turn, that player chooses the noble to be received.\n" \
        "The tile obtained is placed face-up in front of the player in question."

    #return text for the page
    if page == 1 :
        return components
    if page == 2 :
        return Setup1
    if page == 3 :
        return Setup2
    if page == 4 :
        return Game2Player
    if page == 5 :
        return Game3Player
    if page == 6 :
        return DevCard
    if page == 7 :
        return NobleCard
    if page == 8 :
        return Gameplay
    if page == 9 :
        return Selecttoken
    if page == 10 :
        return Reserve
    if page == 11 :
        return Buying
    if page == 12 :
        return Bonus
    if page == 13 :
        return Noble
    if page == 14 :
        return EndGame

def ruletext (page,text_font_bold,text_font_regular) :
    #Components Text render 
        if page == 1 :
            text_block(text_font_bold , "Components", 'Black', (530,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (480,230), 1030, screen, 15)
        #Setup of the Game 1 / 2
        if page == 2 :
            text_block(text_font_bold , "Setup 1/2", 'Black', (550,150), 1040, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Setup of the Game 2 / 2
        if page == 3 :
            text_block(text_font_bold , "Setup 2/2", 'Black', (550,150), 1040, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Game with 2 players 
        if page == 4 :
            text_block(text_font_bold , "Game With 2 Players", 'Black', (480,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Game with 3 players 
        if page == 5 :
            text_block(text_font_bold , "Game With 3 Players", 'Black', (480,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #The Development Cards
        if page == 6 :
            text_block(text_font_bold , "The Development Cards", 'Black', (440,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #The Noble Tiles
        if page == 7 :
            text_block(text_font_bold , "The Noble Tiles", 'Black', (520,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Game Play
        if page == 8 :
            text_block(text_font_bold , "Game Play", 'Black', (550,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Selecting Tokens
        if page == 9 :
            text_block(text_font_bold , "Selecting Tokens", 'Black', (480,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Reserve a development card
        if page == 10 :
            text_block(text_font_bold , "Reserve a development card", 'Black', (370,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Buying a development card
        if page == 11 :
            text_block(text_font_bold , "Buying a development card", 'Black', (370,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #The Bonuses
        if page == 12 :
            text_block(text_font_bold , "The Bonuses", 'Black', (550,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #The Nobles
        if page == 13 :
            text_block(text_font_bold , "The Nobles", 'Black', (550,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #End of the Game 
        if page == 14 :
            text_block(text_font_bold , "End of the Game", 'Black', (480,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)

def rulebook(screen, FPS) :
    clock = pygame.time.Clock()
    #Set name of screen caption
    pygame.display.set_caption("Rule of the game")
    #Define default color of button 
    Color = ['White','White','White']
    #Set path of background image file
    BACKGROUND = pygame.image.load("Image\Background\Rule720p.png").convert()
    #Text setting
    text_font_bold = pygame.font.Font("Font\Roboto\Roboto-Bold.ttf",40)
    text_font_regular = pygame.font.Font("Font\Roboto\Roboto-Regular.ttf",30)
    text_font_Button = pygame.font.Font("Font\Roboto\Roboto-Regular.ttf",20)
    #Text Button set up
    Next_surface = text_font_regular.render('Next',True,Color[0]).convert_alpha()
    Next_rect = Next_surface.get_rect(topleft = (1150,140))
    Prev_surface = text_font_regular.render('Previous',True,Color[1]).convert_alpha()
    Prev_rect = Prev_surface.get_rect(topleft = (30,140))
    Back_surface = text_font_regular.render('Menu',True,Color[2]).convert_alpha()
    Back_rect = Back_surface.get_rect(topleft = (1150,640))
    #Set page of text. Default is page 1
    page = 1
    allpage = 14

    #Game loop
    run = True
    while run:
        #Handle user-input
        for event in pygame.event.get():
            #Exit game when press X button on window
            if event.type == pygame.QUIT :
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 :
                    print(event.pos)
                    if Next_rect.collidepoint(pygame.mouse.get_pos()):
                        if page != allpage :
                            page += 1
                    if Prev_rect.collidepoint(pygame.mouse.get_pos()):
                        if page != 1 :
                            page -= 1
                    if Back_rect.collidepoint(pygame.mouse.get_pos()):
                       return "menu"

        #Change the color of Button when mouse cusor hover above the text
        if Next_rect.collidepoint(pygame.mouse.get_pos()) and page != allpage :
            Color[0] = 'Gold'
        elif page == allpage : 
            Color[0] = 'Gray'
        else :
            Color[0] = 'White'

        if Prev_rect.collidepoint(pygame.mouse.get_pos()) and page != 1 :
            Color[1] = 'Gold'
        elif page == 1 : 
            Color[1] = 'Gray'
        else :
            Color[1] = 'White'

        if Back_rect.collidepoint(pygame.mouse.get_pos()):
            Color[2] = 'Gold'
        else : Color[2] = 'White'

        #FPS of the game
        clock.tick(FPS)
        #Background image
        screen.blit(BACKGROUND,(0,0))
        #Text page set up and render
        Page_surface = text_font_regular.render('Page '+str(page)+'/'+str(allpage),True,'White')
        screen.blit(Page_surface,(30,640))
        #Setting Button Text in loop because they need to change color when hover
        Next_surface = text_font_regular.render('Next',True,Color[0]).convert_alpha()
        Prev_surface = text_font_regular.render('Previous',True,Color[1]).convert_alpha()
        Back_surface = text_font_regular.render('Menu',True,Color[2]).convert_alpha()
        #Button render
        screen.blit(Next_surface,Next_rect)
        screen.blit(Prev_surface,Prev_rect)
        screen.blit(Back_surface,Back_rect)
        #render text body
        ruletext (page,text_font_bold,text_font_regular)
        #Update screen
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":
   rulebook(screen, FPS)