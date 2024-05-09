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

class Game:
    def __init__(self, NewGame, PlayerTurn, CardHand, WinningHand, Score):
        self.newgame = NewGame
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
        

class Card:
    def __init__(self, Random, Value, Draw):
        self.random = Random
        self.draw = Draw
        self.value = Value


def game():
    pass


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