import random

def get_player_name():
    """
    This function requests the players name before they play.
    The player name can be printed out after the game.
    """
    while True:
        player_name = input("Enter your name:").strip().lower()
        if player_name == '':
            print('You must enter something that is not just a space')
        else:   
            print(f'Hey hi there {player_name}, lets play blackjack. Ready!')
            return player_name


"""
This is the Class called Card
It has the attributes of suit (Clubs, Diamonds, Heards, Spades)
It also has the attributes of rank (Ace,2..Jack,Queen,King)
"""


class Card:
    """
    This is the Class called Card
    It has the attributes of suit (Clubs, Diamonds, Heards, Spades)
    It also has the attributes of rank (Ace,2..Jack,Queen,King)
    """
    def __init__(self, suit, rank):
        """
        This initialises a card object
        """
        self.suit = suit
        self.rank = rank
        self.value = self.assign_value(rank)
      
    def __str__(self):
        """
        This function returns the values of the rank and suit of the card.
        """
        return f"{self.rank} of {self.suit}"

    def assign_value(self, rank):
        """
        The assign_value  if - else function adds numerical values to the 
        rank of the cards 
        """
        if rank in ["Jack", "Queen", "King"]:
            return 10
        elif rank == "Ace":
            return 11
        else:
            return int(rank)

class Deck:

  def __init__(self):
    self.cards = self.generate_deck()


  def generate_deck(self):
      suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
      ranks = [str(i) for i in range(2, 11)] + ["Ace", "Jack", "Queen", "King"]
      return [Card(suit, rank) for suit in suits for rank in ranks]

  def shuffle(self):
      random.shuffle(self.cards)

  def deal(self):
    return self.cards.pop()

"""
The Player Class is for the player in the card game.
The attributes are the players name and the players hand. 
The cards in the players hand must be printed to the console
"""
class Player:


  """
  This function defines the player and the hand.
  """

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

"""
This is a class that represents the blackjack game.
it involves the dealer dealing the player and dealers hands and then it checks for a win. 
"""

class Game:

  def __init__(self):
      self.deck = Deck()
      self.player = Player("Player")
      self.dealer = Player("Dealer")

"""
This function works on validating input 
If the input is incorrect the function asks for "Hit" or "Stand"
"""

def input_with_validation(self, prompt, valid_inputs):
  while True:
    user_input = input(prompt).lower().strip()
    if user_input in valid_inputs:
      return user_input
      print("Invalid choice. Please enter Hit or Stand.")

""""
This function starts the game play of blackjack.
It lists other functions, shuffle, recieveing cards, players turn, dealers turn, evaluating values and 
checking for the winner. 
"""

def play(self):
    self.deck.shuffle()
    for _ in range(2):
      self.player.receive_card(self.deck.deal())
      self.dealer.receive_card(self.deck.deal())
    self.player_turn()
    if self.player.hand_value() <= 21:
      self.dealer_turn()
    self.check_winner()

"""
The players turn function 
This function allows the player to hit or stand. If the player hits they are dealt a card if they stand it is the dealers turn. 
"""

def player_turn(self):
  while True:
    print("Your Hand:")
    self.player.display_hand()
    if self.player.hand_value() > 21:
      print ("Busted!")
      return
    action = self.input_with_validation("Do you want to 'hit' or 'stand'?",
                                            ['hit', 'stand'])
    if action == 'hit':
      self.player.receive_card(self.deck.deal())
    elif action == 'stand':
      return

"""
This function is the dealers turn in the game.
This method deals cards to the dealer until their hand value is at least 17.
"""

def dealer_turn(self):
  print("\nDealer's turn:")
  while self.dealer.hand_value() < 17:
    self.dealer.receive_card(self.deck.deal())


"""
This function checks who won the game.
It compares the hand values of the player and dealer and prints the result
"""

def check_winner(self): 
  player_val = self.player.hand_value()
  dealer_val = self.dealer.hand_vale()

  print(f"\nYour hand value: {player_val}")
  print(f"Dealer's hand value: {dealer_val}")

  if dealer_val > 21 or (player_val <=21 and player_val > dealer_val):
    print("You win!")
  elif player_val == dealer_val:
    print("It's a tie!")
  else:
    print("Dealer wins!")
    print("")


if __name__ == "__main__":
  game = Game()
  game.play()