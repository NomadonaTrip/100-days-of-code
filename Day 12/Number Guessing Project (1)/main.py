from random import randint
from random import randint
from art import logo_new
print(logo_new)

print("WELCOME TO THE NUMBER GUESSING GAME!\n")

print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")



def play():
    number = randint(1,100)
    attempts = 0
    guess = 0
    if difficulty == "hard":
        attempts = 5
    else:
        attempts = 10
    print(f"You have {attempts} attempts remaining to guess the answer")

    while attempts > 0 and guess != number:

        guess = int(input("Make a guess: "))
        attempts -= 1
        if guess > number:
            print(f"Too high, you have {attempts} attempts remaining")
        else:
            print(f"Too low, you have {attempts} attempts remaining")
    else:
        if guess == number:
            print(f"You got it! The answer was {guess}.")
        else:
            print("You have run out of guesses. You lose")

play()
