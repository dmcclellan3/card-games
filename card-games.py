import random

Deck_Value = list(range(1, 52))
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
number_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]



        
class Player:
    def __init__(self, name_param):
        self.name = name_param
        self.card = None
        

player1 = Player('Duke')
print('Player 1: ', player1.name)

dealer = Player('Dealer')
print('Dealer: ', dealer.name)


    

new_game = input("Play a round of High Card? Y/N")

class StartGame: 
    def __init__(self, decks):
        self.decks = decks

    def check_winner(self):
        if player1.card.numbervalue > dealer.card.numbervalue:
            print('Player 1 Wins!')
            return False
        elif dealer.card.numbervalue > player1.card.numbervalue:
            print('Dealer Wins!')
            return False 
            
        else: return True 

new_game = StartGame(1) 




class Card:
    def __init__(self, Value, Suit, NumberValue):
        self.value = Value
        self.suit = Suit
        self.numbervalue = NumberValue
        
def generate_cards(values, suits):
    cards = []
    for index, value in enumerate(values):  ## yields pairs 
        for suit in suits:                  ##This section takes cards values and suits from the array 
            cards.append(Card(value, suit, NumberValue=number_values[index])) ##and appends the card object to the value and suit
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
        
current_game_deck = Deck(suits, values, Deck_Value, len(Deck_Value)) 

def play_loop():
    current_game_deck.deal()
    print('player value:', player1.card.value, player1.card.suit)
    print('dealer value:', dealer.card.value, dealer.card.suit)
    restart_game = new_game.check_winner()  
    if restart_game == True:
        play_loop()

play_loop()