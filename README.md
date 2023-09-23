
![BlackJack Logo](/assets/images/blackjack1.PNG)

# Blackjack 
----
Blackjack is a card game with the aim of getting to the number 21 which is Blackjack.

There are four suits of cards in the game when playing with a normal deck. Diamonds, Clubs, Hearts and Spades.
The Ace in each suit can either be valued at 11 or 1. This is where the trick comes in. 

In this card game there is one player who is playing against the dealer. The aim is to get to 21 or closest to it each playr gets a turn to play.

The dealer shuffles the deck and deals cards in their suits and values. The player can choose to either 'Hit' or 'Stand' hit means they request another card to get closer to the total of 21. Stand means they feel they are too close to the total and will not take a card this round. There is risk either way in the choice. That is the game. 

Here is the live version of my project:

https://pythonblackjack.herokuapp.com/


![Python Responsive](/assets/images/responsive.PNG)

## How to Play
----

When playing the Game follow the prompts of the messages in the console.
Choose either "Hit" or "Stand" to get the closest to 21. The aim is 21 but the closest wins.
If you get 21 you have scored Blackjack and will win or tie. 


## Features
----
Existing Features:

* This is the opening console screen of the application.
* The player is asked for their name. 


![BlackJackimage](/assets/images/welcome_pic.PNG)


* The player must type "Hit","Stand" to play. All other Enntries will ask for the correct data.


![BlackJackPlay](/assets/images/name_entered.PNG)

In the next example you see the player asking the dealer for a hit and subsequently loosing the game:

![BlackJackPlay2](/assets/images/game_play.PNG)

The Final scores are shown and the player is able to play the game again if the want to. 


## Testing
----
All testing was done by myself during game play and running the program.

Input validation and Pep8 compliance have been included in the testing the Code Institute https://pep8ci.herokuapp.com/
was the application used for the Pep8 tests. 
 
## Bugs
----
The Pep8 Linter has indicated these bugs. Some lines of code are too long:

Results:
62: E501 line too long (81 > 79 characters)
163: E127 continuation line over-indented for visual indent
200: W292 no newline at end of file


## Deployment
______
This project has been deployed from Git Hub to Heroku at the link above. 
The project was deployed using code Institutes mockterminal for Heroku. Github has been conected to Heroku for all commits. 

### Steps for Deployment:
* Fork or clone this repository
* Create a new Heroku app
* Set the buildbacks to Python and NodeJs in that order
* Link the Heroku app to the repository 
* Click on Deploy
* This project selected the auto update option on Heroku as there was no API used


## References
______

### Information that helped me build this game is listed below: 
* https://www.w3schools.com/python/python_functions.asp
* https://www.w3schools.com/python/python_classes.asp
* https://www.youtube.com/watch?v=eWRfhZUzrAc&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&index=6
* https://bicyclecards.com/how-to-play/blackjack/
* https://www.geeksforgeeks.org/blackjack-console-game-using-python/
* https://www.geeksforgeeks.org/python-list-pop-method/
* https://peps.python.org/pep-0008/#:~:text=Long%20lines%20can%20be%20broken,a%20backslash%20for%20line%20continuation.




