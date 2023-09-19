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
The assign value  if - else function adds numerical values to the rank of the cards 

""""

def assign_value(self, rank):
    if rank in ["Jack", "Queen", "King"]:
      return 10
    elif rank == "Ace":
      return 11
    else:
      return int(rank)



class Deck:
    def __init__(self):
        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
                {"rank": "A", "value": 11},
                {"rank": "2", "value": 2},
                {"rank": "3", "value": 3},
                {"rank": "4", "value": 4},
                {"rank": "5", "value": 5},
                {"rank": "6", "value": 6},
                {"rank": "7", "value": 7},
                {"rank": "8", "value": 8},
                {"rank": "9", "value": 9},
                {"rank": "10", "value": 10},
                {"rank": "J", "value": 10},
                {"rank": "Q", "value": 10},
                {"rank": "K", "value": 10},
            ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
    
    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt               

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10
            
    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21

    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand is shown in the cards below:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
            and not show_all_dealer_cards and not self.is_blackjack():
                print("hidden")
            else:
                print(card)

        if not self.dealer:
            print("Value:", self.get_value())
        print()            

class Game:

  def play(self):
    game_number = 0
    games_to_play = 3
    

    while game_number < games_to_play:
      game_number += 1

      deck = Deck()
      deck.shuffle()

      player_hand = Hand()
      dealer_hand = Hand(dealer=True)

      for i in range(2):
        player_hand.add_card(deck.deal(1))
        dealer_hand.add_card(deck.deal(1))

      print()
      print("🃏 !!WELCOME TO BLACKJACK ONLINE!! 🃏")
      print()
      print("YOU HAVE 3 TURNS TO PLAY! GOOD LUCK!")
      print()
      print("🤑 !!PLAY RIGHT AND WIN BIG!! 🤑")
      print()
      print(get_player_name)
      player_hand.display()
      dealer_hand.display()

      if self.check_winner(player_hand, dealer_hand):
        continue

      choice = ""
      while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
        choice = input("Please type your choice of 'Hit' or 'Stand' to continue!:\n ").lower()
        print()
        while choice not in ["h", "s", "hit", "stand"]:
          choice = input("Please enter 'Hit' or 'Stand' (or H/S)\n").lower()
          print()
        if choice in ["hit", "h"]:
          player_hand.add_card(deck.deal(1))
          player_hand.display()

      if self.check_winner(player_hand, dealer_hand):
        continue

      player_hand_value = player_hand.get_value()
      dealer_hand_value = dealer_hand.get_value()

      while dealer_hand_value < 17:
        dealer_hand.add_card(deck.deal(1))
        dealer_hand_value = dealer_hand.get_value()

      dealer_hand.display(show_all_dealer_cards=True)

      if self.check_winner(player_hand, dealer_hand):
        continue

      print("Final Results")
      print("Your hand:", player_hand_value)
      print("Dealer's hand:", dealer_hand_value)

      self.check_winner(player_hand, dealer_hand, True)

    print("\nThanks for playing!")
    print("\nRun the program again to keep playing!")
    print()
    print()
    


  def check_winner(self, player_hand, dealer_hand, game_over=False):
    if not game_over:
      if player_hand.get_value() > 21:
        print("You busted. Dealer wins! Maybe Next Time! 😭")
        return True
      elif dealer_hand.get_value() > 21:
        print("Dealer busted. You win! WINNER WINNER CHICKEN DINNER! 😀 🏆 ")
        return True
      elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
        print("Both players have blackjack! Tie! 😑 👀")
        return True
      elif player_hand.is_blackjack():
        print("You have blackjack. You win!..WINNER WINNER CHICKEN DINNER! 😀 🏆 👑 ")
        return True
      elif dealer_hand.is_blackjack():
        print("Dealer has blackjack. Dealer wins! 😭 Maybe Next Time!")
        return True
    else:
      if player_hand.get_value() > dealer_hand.get_value():
        print("You win! ..WINNER WINNER CHICKEN DINNER! 😀 🏆 ")
      elif player_hand.get_value() == dealer_hand.get_value():
        print("Tie! 😑 😒 ")
      else:
        print("Dealer wins. 😭  Maybe Next Time!")
      return True
    return False

  
g = Game()
get_player_name()
g.play()
