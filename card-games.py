import random

Deck_Value = list(range(1, 53))
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
Card_Hand = ['1']
Score = [0]
Face_Value_Cards = {11: 'J', 
                    12: 'Q', 
                    13: 'K', 
                    14: 'A'}

Spades = list(range(2,15))
Hearts = list(range(2,15))
Diamonds = list(range(2,15))
Clubs = list(range(2,15))

##game class
##who's turn is it and who won the hand 
##reshuffle the deck and start over if theres not enough cards 
##alerting new shuffle

class StartGame: 
    def __init__(self, NewGame, Decks, Players):
        self.newgame = NewGame 
        self.decks = Decks
        self.players = Players  ##one player and dealer

class Game:
    def __init__(self, PlayerTurn, CardHand, WinningHand, Score):
        self.playerturn = PlayerTurn
        self.cardhand = CardHand
        self.score = Score
        self.winninghand = WinningHand
        

class Player:
    def __init__(self, Player, Dealer, CardHand):
        self.player = Player
        self.dealer = Dealer
        self.cardhand = CardHand
        
        

class Deck:
    def __init__(self, Suits, CardNumbers, DeckValue, CardCount, Shuffle): 
        self.suits = Suits
        self.cardnumbers = CardNumbers
        self.deckvalue = DeckValue
        self.cardcount = CardCount
        self.shuffle = Shuffle
        # temp_list_of_cards = generate_cards(values, suits)
        # self.cards = temp_list_of_cards
        
current_game_deck = Deck()
game_running = True
for card_obj in current_game_deck.cards:
    while game_running == True:
        suits = random.choice()
        values = random.choice()
        Face_Value_Cards = random.choice()
        suits = random.choice()
        shuffle = random.choice()
        print('A card!')

class Card:
    def __init__(self, Random, Value, Draw):
        self.random = Random
        self.draw = Draw
        self.value = Value


def start_game():
    pass
    ##start the game(adding an input for if they want to play Y/N)
    ##generating the cards 


def generate_cards(values, suits):
    cards = []
    for value in values:
        for suit in suits:                  ##This section checks what the value is of a card
            if value in Face_Value_Cards:   ##It will determine if a card has a face value or not.
                face_card = Face_Value_Cards[value]
                cards.append((face_card, suit))
            else:
                cards.append((value, suit))
    return cards









##init 
##shuffle
##how many decks are there?

##

##Card class
##Random card function
##Removing a card from the deck and keeping track of the current amount in the deck. 

##player
## how many cards they get
##dealer

##score class ##scoreboard