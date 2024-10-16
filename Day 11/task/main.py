#TODO 1: import the logo art
from art import logo

import random


#TODO 4: Ask player whether they want to play the game

willplay = input("Do you want to play a game of BlackJack? Type 'y' or 'N'. \n")

cardlist = [11,2,3,4,5,6,7,8,9,10,10,10,10]



#TODO 2: create a dictionary to hold player cards and scores

player = {}
dealer = {}

player["cards"] = []
player["score"] = 0
player = {"cards": [], "score": 0}

#TODO 3: create a dictionary to hold dealer cards and scores
dealer["cards"] = []
dealer["score"] = 0

dealer = {"cards": [], "score": 0}



#TODO 5: Deal two cards to both player and dealer, exposing both player cards and score; but only the first dealer card
#TODO 5.1: Create a function to deal cards to both player and dealer
def deal():
    cardselect = random.choice(cardlist)
    return cardselect
def dealplayer():
    deal()
    player["cards"].append(deal())
    player["score"] += int(player["cards"][turn])
    # TODO 5.2: If playerscore is greater than 21, check if any of player's cards are 11. If this is the case, change its value to 1
    if player["cards"][turn] == 11 and player["score"] > 21:
        player["score"] = player["score"] - 10

def dealcomputer():
    deal()
    dealer["cards"].append(deal())
    dealer["score"] += int(dealer["cards"][turn])
    if dealer["cards"][turn] == 11 and dealer["score"] > 21:
        dealer["score"] = dealer["score"]- 10

def playturn():
    dealplayer()
    dealcomputer()

    print(f"Your cards: {player["cards"]}, current score: {player["score"]}")
    print(f"Computer's first card: {dealer["cards"][0]}")
    #print(f"Computer score: {dealer["score"]}")

#TODO 5.2: Deal the first two cards and calculate player and dealer scores
def result():

    if player["score"] == 21:
        print("You have Blackjack, you win!")

    elif player["score"] > 21:
        print("You lose. Your score is higher than 21")

    elif dealer["score"] == 21:
        print("Lose. Opponent has Blackjack")


    elif dealer["score"] > 21:
        print("You win!")


    elif player["score"] == dealer["score"]:
        print("There's a draw")


    elif player["score"] < dealer["score"]:
        print("Lose, opponent has a higher score")


    else:
        print("You win")

while willplay == "Y" or willplay == "y":
    print(logo)

    for turn in range(0,2):
        dealplayer()
        dealcomputer()

    print(f"Your cards: {player["cards"]}, current score: {player["score"]}")
    print(f"Computer's first card: [{dealer["cards"][0]}]")
    #print(f"Computer score: {dealer["score"]}")



    #TODO 6: Check if player score is equal to 21
    if player["score"] == 21:
        print("You have BlackJack, You win!")

# TODO 6_1: Check if player score is above 21

#TODO 7: Ask if player wants to deal again or pass

    playagain = input("Type 'y' to get another card, type 'n' to pass \n")

    while playagain == "Y" or playagain == "y":
        turn += 1

        playturn()
        if player["score"] > 21:
            playagain = "n"
        else:
            playagain = input("Type 'y' to get another card, type 'n' to pass \n")

    else:
        result()
        print(f"Player's final score: {player["score"]}")
        print(f"Dealer's final score: {dealer["score"]}")


        player["cards"] = []
        player["score"] = 0
        dealer["cards"] = []
        dealer["score"] = 0

        willplay = input("Do you want to play blackjack? Type 'Y' or 'N'\n")


















#TODO 8: If player chooses to pass, compare player score with dealer score and announce player status based on BlackJack rules
#TODO 9: If player chooses to deal again, add a card to player cards and its value to player score
#TODO 10: If player chooses to pass, check if dealer score is less than 17
#TODO 11: If dealer score < 17, deal another card to dealer.
#TODO 12: Evaluate and announce player outcome based on BlackJack rules.

