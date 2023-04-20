![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome BrendanCooney,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!


![BlackJack Logo](/assets/images/blackjack1.PNG)

# Blackjack 
----
Blackjack is a card game with the aim of getting to the number 21 which is Blackjack.

There are four suits of cards in the game when playing with a normal deck. Diamonds, Clubs, Hearts and Spades.
The Ace in each suit can either be valued at 11 or 1. This is where the trick come in. 

In this card game there is one player who is playing against the dealer. The aim is to get to 21 before the dealer.

The dealer deals cards in their suits and values. The player can choose to either 'Hit' or 'Stand' hit means they request another card to move get closer to the total. Stand means they feel they are too close to the total and will not take a card this round. 
There is risk either way in the choice. That is the game. 