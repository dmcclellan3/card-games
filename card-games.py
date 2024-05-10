import random

Deck_Value = list(range(1, 52))
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
suits_values = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
number_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# Card_Hand = ['1']
# Score = [0]
Face_Value_Cards = {'J': 11, 
                    'Q': 12, 
                    'K': 13,  
                    'A': 14,}

##Todo list: 
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
    def __init__(self, name_param, score=0):
        self.name = name_param
        self.card = None
        self.score = score

    def increment_score(self):
        self.score += 1
        print("Player 1 Score: ", player1.score)
        print("Dealer Score: ", dealer.score)

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
            # player1.increment_score()
        elif dealer.card.numbervalue > player1.card.numbervalue:
            print('Dealer Wins!')
            return False 
            # print('Dealer Score :')
            # dealer.increment_score()
        else: return True 
        
        # self.check_winner()
        
        ##player1.card.numbervalue == dealer.card.numbervalue:
            ##print("It's a tie!")

new_game = StartGame(1) 




class Card:
    def __init__(self, Value, Suit, NumberValue):
        self.value = Value
        self.suit = Suit
        self.numbervalue = NumberValue
        
def generate_cards(values, suits):
    cards = []
    for index, value in enumerate(values):
        for suit in suits:                  ##This section takes cards values and suits from the array 
            cards.append(Card(value, suit, NumberValue=number_values[index])) ##and appends the card object to the value and suit
    random.shuffle(cards)                   ##Then we can use the random function that was imported and shuffle the cards list 
    return cards
            # if value in Face_Value_Cards:   
            #     face_card = Face_Value_Cards[value]
            #     # cards.append((face_card, suit))
            # else:
            #     cards.append((value, suit))

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
        
current_game_deck = Deck(suits, values, Deck_Value, len(Deck_Value)) 

def play_loop():
    current_game_deck.deal()
    print('player value:', player1.card.value, player1.card.suit)
    print('dealer value:', dealer.card.value, dealer.card.suit)
    restart_game = new_game.check_winner()  
    if restart_game == True:
        play_loop()

play_loop()