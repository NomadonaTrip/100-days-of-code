# Ask the user for input
# Save data into dictionary {name: price}
# Whether if new bids need to be added
# Compare bids in dictionary

from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

# intro section
print(logo)
print("Welcome to the Secret Auction app")
# collect the first bidder's information

# buyer_name = input("What is your name? ")
# buyer_bid = input("How much are you bidding for the artwork? $")
your_name = ""
your_bid = ""
bid_set = {}
next_bid = "yes"
win_bid = {}


# create a function to add new bids
def add_bid(buyer_name, buyer_bid):
    your_name = input("What is your name? ")
    your_bid = input("How much are you bidding for the artwork? $")
    bid_set[your_name] = your_bid
    # if int(bid_set[your_name]) > int(win_bid[your_name]):
    #    win_bid[your_name] = your_bid}
    clear()


while next_bid == "yes":
    add_bid(buyer_name=your_name, buyer_bid=your_bid)
    next_bid = input("Are there other bidders, yes or no? ")
print(bid_set)

# identify the winning bid
winner = 0
for bid_name in bid_set:
    bid = bid_set[bid_name]
    if int(bid) > winner:
        winner = int(bid)
        win_bid[bid_name] = winner

print(win_bid)




