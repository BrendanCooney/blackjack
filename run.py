import random

""""
This function requests the players name before they play.
The player name can be printed out after the game.
""""

def get_player_name():
  player_name = input("Enter your name:")
  return player_name
  print(get_player_name)

""""
This is the Class called Card
It has the attributes of suit (Clubs, Diamonds, Heards, Spades)
It also has the attributes of rank (Ace,2..Jack,Queen,King)

""""

class Card:

def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = self.assign_value(rank)

""""
This function returns the values of the rank and suit of the card.

""""
def __str__(self):
    return f"{self.rank} of {self.suit}"

""""
The assign_value  if - else function adds numerical values to the rank of the cards 

""""

def assign_value(self, rank):
    if rank in ["Jack", "Queen", "King"]:
      return 10
    elif rank == "Ace":
      return 11
    else:
      return int(rank)

""""
This Class is for the deck of Cards.

The first function defines the deck of cards and generates it.

The  generate_deck function generates cards  in each deck with various values.

The shuffle function shuffles cards using random 

The deal function deals the cards. 

""""

Class Deck: 

def__init__(self):
self.cards = self.generate_deck()


  def generate_deck(self):
      suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
      ranks = [str(i) for i in range(2, 11)] + ["Ace", "Jack", "Queen", "King"]
      return [Card(suit, rank) for suit in suits for rank in ranks]

  def shuffle(self):
      random.shuffle(self.cards)

  def deal(self):
    return self.cards.pop()

""""
The Player Class is for the player in the card game.
The attributes are the players name and the players hand. 
The cards in the players hand must be printed to the console

""""
class Player:

  def __init__(self, name):
      self.name = name
      self.hand = []

  def receive_card(self, card):
      self.hand.append(card)
      self.adjust_for_ace()

  def adjust_for_ace(self):
      total_value = sum(card.value for card in self.hand)
      num_aces = sum(1 for card in self.hand if card.rank == 'A')
      while total_value > 21 and num_aces:
        total_value -= 10
        num_aces -= 1

  def hand_value(self):
      return sum(card.value for card in self.hand)

  def display_hand(self):
      for card in self.hand:
        print(card)

""""
This is a class that represents the blackjack game.
it involves the dealer dealing the player and dealers hands and then it checks for a win. 

""""
class Game:

  def __init__(self):
      self.deck = Deck()
      self.player = Player("Player")
      self.dealer = Player("Dealer")

""""
This function works on validating input 
If the input is incorrect the function asks for "Hit" or "Stand"
""""