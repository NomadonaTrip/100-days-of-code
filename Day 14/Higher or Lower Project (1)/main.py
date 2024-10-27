#import the logo
from random import randint

from art import logo

#import the data
from game_data import data

#import the random module
import random

#import the versus ASCII art
from art import vs

#Print the welcome ASCII art
print(logo)

options = []

a_choice = int(randint(0,len(data)))
options.append(a_choice)
    #randomize the contents of the data
b_choice = int(randint(0,len(data)))
options.append(b_choice)


#Call two contents of the data and compare them one to the other




score = 0
guess = ""
def iscorrect(options, score):

    # randomize the contents of the data

    print(f"Compare A: {data[options[0]]['name']}, {data[options[0]]['description']}, {data[options[0]]['country']} \n")
    print(vs)

    if options[0] == options[1]:
        options[1] = int(randint(0, len(data)))
        print(
            f"""Against B: {data[options[1]]['name']}, {data[options[1]]['description']}, {data[options[1]]['country']}""")
    else:
        print(f"Against B: {data[options[1]]['name']}, {data[options[1]]['description']}, {data[options[1]]['country']}")

    guess = input("Who has more social media followers, A or B? ")



    if guess == "A" and data[options[0]]['follower_count'] > data[options[1]]['follower_count']:
        return True
    elif guess == "A" and data[options[0]]['follower_count'] < data[options[1]]['follower_count']:

        return False
    elif guess == "B" and data[options[1]]['follower_count'] > data[options[0]]['follower_count']:

        return True
    else:

        return False

while iscorrect(options, score):
    score += 1
    print(f"You're right, current score: {score}")
    options[0] = options[1]
    options[1] = int(randint(0, len(data)))



else:
    print(f"Sorry, you're wrong. Final score: {score}")



#A function that takes the response, compares the associated social media following with the other, and returns an answer





#Create a loop of continuous comparisons and a condition under which the loop ends
