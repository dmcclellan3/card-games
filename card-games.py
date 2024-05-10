import random

Deck_Value = list(range(1, 53))
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
# values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
Card_Hand = ['1']
Score = [0]
Face_Value_Cards = {'J': 11, 
                    'Q': 12, 
                    'K': 13, ## Card needs to be written as J then the value 
                    'A': 14,
                    11 : 'J',
                    12 : 'Q',
                    13 : 'K',
                    14 : 'A'}

# Spades = list(range(2,15))
# Hearts = list(range(2,15))
# Diamonds = list(range(2,15))
# Clubs = list(range(2,15))

##Todo list: In winner who won -assign a number value to J,Q,K,A value(referencing what I have in FVC)
## number of decks needs to ask for user input 
##How does one suit beat another or tie? 




# class Game:
#     def __init__(self, PlayerTurn, CardHand, WinningHand, Score, Suits, Deck_Value, players):
#         self.playerturn = PlayerTurn
#         self.cardhand = CardHand
#         self.score = Score
#         self.winninghand = WinningHand
#         self.suits = Suits['Spades', 'Hearts', 'Clubs', 'Diamonds']
#         self.deckvalue = Deck_Value
#         self.players = players  


        
class Player:
    def __init__(self, name_param):
        self.name = name_param
        self.card = None
player1 = Player('Duke')
print('Player 1: ', player1.name)

dealer = Player('Dealer')
print('Dealer: ', dealer.name)

new_game = input("Play a game of High Card? Y/N")

class StartGame: 
    def __init__(self, decks):
        self.decks = decks

    def check_winner(self):
        if player1.card.value > dealer.card.value:
            print('Player 1 Wins!')
        if dealer.card.value > player1.card.value:
            print('Dealer Wins!')

new_game = StartGame(1)




class Card:
    def __init__(self, Value, Suit):
        self.value = Value
        self.suit = Suit
        
def generate_cards(values, suits):
    cards = []
    for value in values:
        for suit in suits:                  ##This section takes cards values and suits from the array 
            cards.append(Card(value, suit)) ##and appends the card object to the value and suit
            if value in Face_Value_Cards:   
                face_card = Face_Value_Cards[value]
                cards.append((face_card, suit))
            else:
                cards.append((value, suit))
    random.shuffle(cards)                   ##Then we can use the random function that was imported and shuffle the cards list 
    return cards

class Deck:
    def __init__(self, Suits, CardNumbers, DeckValue, CardCount): 
        self.suits = Suits
        self.cardnumbers = CardNumbers
        self.deckvalue = DeckValue
        self.cardcount = CardCount
        self.cards = generate_cards(values, suits)        
        

    def deal(self):
        player1.card = self.cards.pop()
        dealer.card = self.cards.pop()
        # self.cards = Cards
        # temp_list_of_cards = generate_cards(values, suits)
        
current_game_deck = Deck(suits, values, Deck_Value, len(Deck_Value))  ##Why does 'True' work here? It breaks otherwise.
current_game_deck.deal()
print('player value:', player1.card.value, player1.card.suit)
print('dealer value:', dealer.card.value, dealer.card.suit)

new_game.check_winner() 

# for card_obj in current_game_deck.cards:
#     print('Card', card_obj.value, card_obj.suit)
    
    # while game_running == True:
        # suits = random.choice(suits)
        # values = random.choice(values)
        # Face_Value_Cards = random.choice()
        # game_running = False


        














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