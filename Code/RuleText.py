from typing import Optional, Tuple, Union
import pygame
#Input with a paragraph of text and render it on screen within block size
# Argument:
#   font        -- pygame.font that will use to render text
#   text        -- String of text
#   color       -- color of text
#   pos         -- start position of text
#   block_width -- width of block that contain text in screen' surface
#   screen      -- screen surface 
#   row_height  -- space between row of text
def text_block(font: pygame.font, 
                text: str, 
                color: Union[str, Tuple[int, int, int]], 
                pos: Tuple[int, int], 
                block_width: Tuple[int, int], 
                screen: pygame.surface, 
                row_height: int) :
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

#Contain body of text and return the information in the page number
# Argument:
#   page      -- page number
# Return
#   str         -- string of body text corresponding to that page number
def Textpage (page) :
    #Body text
    components = "7 \b green tokens\n" \
        "7 \b white tokens\n" \
        "7 \b blue tokens\n" \
        "7 \b black tokens\n" \
        "7 \b red tokens\n" \
        "5 \b Gold tokens\n" \
        "90 Development cards\n" \
        "10 Noble tiles"
    
    EndGame = "- \t When a player reaches 15 points," \
        " complete the current round so that each player has played the same number of turns.\n" \
        "- \t The player who then has the highest number of points is declared the winner.\n" \
        "- \t In case of a tie, the player who has purchased the fewest development cards wins."
    
    Game2Player = "- \t Remove 3 tokens of each gem color \n \t (there should be only 4 of each remaining).\n" \
        "- \t Reveal 3 noble tiles."

    Game3Player = "- \t Remove 2 tokens of each gem color \n \t (there should be only 5 of each remaining).\n" \
        "- \t Reveal 4 noble tiles."

    Setup1 = "- \t Development card decks are place in a column in the middle of the screen in increasing order from bottom to top.\n" \
        "- \t 4 cards from each development card deck level are reveal next to the decks at right.\n" \
        "- \t the noble tiles are reveal as many of them as there are players plus one.\n"
    
    Setup2 = "- \t The tokens are place in 6 distinct piles next to the decks at left."

    DevCard = "- \t To win points, the players must purchase development cards.\n" \
        "- \t These cards are visible in the middle-right of the screen and may be purchased by all players during the game.\n" \
        "- \t The developments in hold slot are the cards which the players reserve throughout the game.\n" \
        "- \t Developments in hold slot may only be purchased by the players holding them."

    NobleCard = "- \t The noble tiles are visible in the top of the screen.\n" \
        "- \t At the end of their turn, a player automatically receives the visit from a noble if that player has the amount of bonuses (and only bonuses) required, and they get the corresponding tile.\n" \
        "- \t A player cannot refuse a visit from a noble.\n" \
        "- \t Receiving a noble isn't considered to be an action. Each noble tile is worth 3 points, but players can only get a single one per turn."

    Gameplay1 = "The turn order is chosen from order when players choose character.\n" \
        "On their turn, a player must choose to perform only one of the following four actions:\n" \
        "\t - \t Take 3 tokens of different colors.\n" \
        "\t - \t Take 2 tokens of the same color.\n" \
        "\t This action is only possible if there are at least 4 tokens of the chosen color left when the player takes them."
    
    Gameplay2 = "\t - \t Reserve 1 development card and take 1 gold token.\n" \
        "\t - \t Purchase 1 face-up development card from the middle-right of the screen or a previously reserved one."

    Selecttoken = "- \t A player can never have more than 10 tokens at the end of their turn (including golds).\n" \
        "- \t If this happens, they must return tokens until they only have 10 left.\n \n" \
        "Note : players may not take 2 tokens of the same color if there are less than 4 tokens available of that color."

    Reserve1 = "- \t To reserve a card, a player simply needs to click 'hold' the development card from the middle-right of the screen.\n" \
        "- \t The reserved cards are kept in hold slot and cannot be discarded.\n" \
    
    Reserve2 = "- \t Players may not have more than three reserved cards in hold slot, and the only way to get rid of a card is to buy it.\n" \
        "- \t Reserving a card is also the only way to get a gold token.\n" \
        "- \t If there is no gold left, you can still reserve a card, but you won't get any gold."

    Buying1 = "- \t To purchase a card, a player must spend the number of tokens indicated on the card.\n"\
        "- \t A gold token can replace any color.\n" \
        "- \t The spent tokens are returned to the middle of the screen.\n" \
        "- \t A player may purchase one of the face-up development cards in the middle-right of the screen or a card in their hold slot that was reserved on a previous turn.\n" \

    Buying2 = "- \t Each player makes distinct columns with the acquired development cards by sorting them by color and their bonuses are visible.\n" \
        "- \t The bonuses and points granted by each card must be visible to all at all times.\n" \

    Buying3 =  "Note: when a development card from the middle-right of the screen is acquired or reserved, it must immediately be replaced by a card of the same level.\n" \
    "\t At all times during the game, there must be 4 face-up cards of each level (unless the deck in question is empty, in which case the empty spaces also remain empty)."

    Bonus1 = "- \t The bonuses a player has from development cards acquired on previous turns provide discounts on the purchase of new cards.\n" \
        "- \t Each bonus of a given color is equal to a token of that color.\n" \
        "- \t Thus, if a player has 2 blue bonuses and wants to purchase a card which costs 2 blue tokens and 1 green token, the player must only spend 1 green token.\n" \
    
    Bonus2 = "- \t If a player has enough development cards (and therefore bonuses), they can even purchase a card without spending any tokens."

    Noble1 = "- \t At the end of their turn, each player checks the noble tiles in order to determine if they're receiving a visit from one of them. A player can be visited if they have (at least) the quantity and type of bonuses indicated on the noble tile.\n" \
        "- \t It is impossible to refuse the visit from a noble, which is not considered to be an action.\n" \

    Noble2 = "- \t If a player has enough bonuses to be visited by more than one noble at the end of their turn, that player chooses the noble to be received.\n" \
        "- \t The tile obtained is placed to the player in question."

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
        return Gameplay1
    if page == 9 :
        return Gameplay2
    if page == 10 :
        return Selecttoken
    if page == 11 :
        return Reserve1
    if page == 12 :
        return Reserve2
    if page == 13 :
        return Buying1
    if page == 14 :
        return Buying2
    if page == 15 :
        return Buying3
    if page == 16 :
        return Bonus1
    if page == 17 :
        return Bonus2
    if page == 18 :
        return Noble1
    if page == 19 :
        return Noble2
    if page == 20 :
        return EndGame
    
#setup and render title and body text of that page
# Argument:
#   page      -- page number
#   text_font_bold    -- pygame.font for bold text
#   text_font_regular -- pygame.font for regular text
#   screen    -- screen surface 
def ruletext (page: int, text_font_bold: pygame.font, text_font_regular: pygame.font, screen: pygame.surface) :
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
            text_block(text_font_bold , "Game With 2 Players", 'Black', (460,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Game with 3 players 
        if page == 5 :
            text_block(text_font_bold , "Game With 3 Players", 'Black', (460,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #The Development Cards
        if page == 6 :
            text_block(text_font_bold , "The Development Cards", 'Black', (440,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #The Noble Tiles
        if page == 7 :
            text_block(text_font_bold , "The Noble Tiles", 'Black', (480,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Game Play 1 / 2
        if page == 8 :
            text_block(text_font_bold , "Game Play 1/2", 'Black', (480,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Game Play 2 / 2
        if page == 9 :
            text_block(text_font_bold , "Game Play 2/2", 'Black', (480,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Selecting Tokens
        if page == 10 :
            text_block(text_font_bold , "Selecting Tokens", 'Black', (480,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Reserve a development card 1 / 2
        if page == 11 :
            text_block(text_font_bold , "Reserve a development card 1/2", 'Black', (370,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Reserve a development card 2 / 2
        if page == 12 :
            text_block(text_font_bold , "Reserve a development card 2/2", 'Black', (370,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Buying a development card 1 / 3
        if page == 13 :
            text_block(text_font_bold , "Buying a development card 1/3", 'Black', (370,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Buying a development card 2 / 3
        if page == 14 :
            text_block(text_font_bold , "Buying a development card 2/3", 'Black', (370,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #Buying a development card 3 / 3
        if page == 15 :
            text_block(text_font_bold , "Buying a development card 3/3", 'Black', (370,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #The Bonuses 1 / 2
        if page == 16 :
            text_block(text_font_bold , "The Bonuses 1/2", 'Black', (480,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #The Bonuses 2 / 2
        if page == 17 :
            text_block(text_font_bold , "The Bonuses 2/2", 'Black', (480,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #The Nobles 1 / 2
        if page == 18 :
            text_block(text_font_bold , "The Nobles 1/2", 'Black', (480,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #The Nobles 2 / 2
        if page == 19 :
            text_block(text_font_bold , "The Nobles 2/2", 'Black', (480,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)
        #End of the Game 
        if page == 20 :
            text_block(text_font_bold , "End of the Game", 'Black', (480,150), 1030, screen, 10)
            text_block(text_font_regular, Textpage (page), 'Black', (270,230), 1030, screen, 15)