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
    """
    This Class is for the deck of Cards.
    """
    def __init__(self):
        """ This initialises a deck of cards """
        self.cards = self.generate_deck()
      
    def generate_deck(self):
        """ This returns an array of a deck of cards """
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        ranks = [str(i) for i in range(2, 11)] + ["Ace", "Jack", "Queen", "King"]
        return [Card(suit, rank) for suit in suits for rank in ranks]
      
    def shuffle(self):
        """ This returns a shuffled deck of cards """
        random.shuffle(self.cards)
      
    def deal(self):
        """ This returns a card popped off the Card array"""
        return self.cards.pop()

class Player:
    """
    The Player Class is for the player in the card game.
    The attributes are the players name and the players hand. 
    The cards in the players hand must be printed to the console
    """
    def __init__(self, name):
        """
        This function defines the player and the hand
        """
        self.name = name
        self.hand = []

  def receive_card(self, card):
        """ This appends a card to the player """
        self.hand.append(card)
        self.adjust_for_ace()
      
    def adjust_for_ace(self):
        """ This handles whether the ace is a ten or one """
        total_value = sum(card.value for card in self.hand)
        num_aces = sum(1 for card in self.hand if card.rank == 'A')
        while total_value > 21 and num_aces:
          total_value -= 10
          num_aces -= 1
          
    def hand_value(self):
        """ This returns the value of the hand """
        return sum(card.value for card in self.hand)
      
    def display_hand(self):
        """ This prints the players hand """
        for card in self.hand:
          print(card)


class Game:
    """"
    This is a class that represents the blackjack game.
    it involves the dealer dealing the player and dealers hands and 
    then it checks for a win. 
    """
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def input_with_validation(self, prompt, valid_inputs):
        """"
        This function works on validating input 
        If the input is incorrect the function asks for "Hit" or "Stand"
        """
        while True:
            user_input = input(prompt).lower().strip()
            if user_input not in valid_inputs:
                print("Invalid choice. Please enter Hit or Stand.")
            if user_input in valid_inputs:
                return user_input

def play(self):
        """"
        This function starts the game play of blackjack.
        It lists other functions, shuffle, recieveing cards, players turn, 
        dealers turn, evaluating values and checking for the winner. 
        """
        self.deck.shuffle()
        for _ in range(2):
            self.player.receive_card(self.deck.deal())
            self.dealer.receive_card(self.deck.deal())
        self.player_turn()
        if self.player.hand_value() <= 21:
            self.dealer_turn()
        self.check_winner()

 def player_turn(self):
        """"
        The players turn function 
        This function allows the player to hit or stand. If the player hits 
        they are dealt a card if they stand it is the dealers turn. 
        """
        while True:
            print("Your Hand:")
            self.player.display_hand()
            print(f'The value of your hand is: {self.player.hand_value()}')
            if self.player.hand_value() > 21:
                print ("Busted!")
                return
            action = self.input_with_validation("Want to 'hit' or 'stand'?",
                                                    ['hit', 'stand'])
            if action == 'hit':
                self.player.receive_card(self.deck.deal())
            elif action == 'stand':
                return

  def dealer_turn(self):
        """
        This function is the dealers turn in the game.  This method deals cards 
        to the dealer until their hand value is at least 17.
        """
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