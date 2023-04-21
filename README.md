
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


![Python Responsive](/assets/images/python-responsive.PNG)

## How to Play
----

When playing the Game follow the prompts of the messages in the console.
Choose either "Hit" or "Stand" to get the closest to 21. The aim is 21 but the closest wins.
If you get 21 you have scored Blackjack and will win. 


## Features
----
Existing Features:

* This is the opening console screen of the application.
* I have not used any libraries but just emojies in the text of the game. 
* I have allocated three games per session with the dealer. 
  After these sessions the player can choose to run the program again and repeat. 
* The player must type "Hit","Stand" or "h","s" to play. All other Enntries will ask for the correct data. 


![BlackJackimage](/assets/images/blackjack-start.PNG)


In the example below you can see the player has chosen hit meaning asking the dealer for another card. The result is Blackjack!
the player wins. 


![BlackJackPlay](/assets/images/blackjack-play.PNG)

In the next example you see the player asking the dealer for two hits and subsequently loosing the game:

![BlackJackPlay2](/assets/images/blackjack-play2.PNG)

On the Final play run you can see the player has asked for two hits and lost the game. The game asks the player to run the program again to start again.

![blackJackPlay3](/assets/images/blackjack-play3.PNG)

## Testing
----
All testing was done by myself and my sons on game play. 

Testing invloved entering incorrect inforamtion for example numbers and text into the game. The continue prompts keep asking for valid data.
 
## Bugs
----

Although there are no apparent bugs in the code there are bugs in the syntax. ( I used my sons as bug testers and asked them to break the game.) There are syntax errors in the code which I was still working on a the time of submission.

While the syntax spacing is not 100% the application does run and work. 

* When putting the code through the PEP8 Phyton Linter I was able to reduce the syntax and spacing errors considerably (Down to 4 lines)
However when running the code after this the program would not run. This is the reason I have left the code as it is as the program runs.


## Deployment
______
This project has been deployed from Git Hub to Heroku at the link above. 
The project was deployed using code Institutes mockterminal for Heroku.

### Steps for Deployment:
* Fork or clone this repository
* Create a new Heroku app
* Set the buildbacks to Python and NodeJs in that order
* Link the Heroku app to the repository 
* Click on Deploy
* This project selected the auto update option on Heroku as there was no API used




## Credits
______

All credit goes to The Code Institute and Beau Carnes of Free Code Camp. I followed the Blackjack game tutorial online.
I looked at a number of other games whne choosing the project. This one produced a simple, effective and fun result even though there were complex learning steps in the code.  

https://www.youtube.com/watch?v=eWRfhZUzrAc&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&index=6

