from art1 import logo
import os

print(logo)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initialize the highest bid variable and the highest bidder's name variable
highest_bid = 0
highest_bidder = ''

my_dictionary = {}

more_bidder = True

while more_bidder:
    user_name = input("What is your name?\n").lower()
    current_bid = int(input("What is your bid?\n"))

    # Check if the current bid is higher than the highest bid so far
    if current_bid > highest_bid:
        highest_bid = current_bid
        highest_bidder = user_name

    # Add user input to the dictionary
    my_dictionary[user_name] = current_bid

    more_bidder = input('Are there still more bidders? (yes/no)\n').lower()
    if more_bidder != 'yes':
        break
    else:
        clear_console()

print(my_dictionary)

# Print the highest bidder
print(f"The highest bidder is {highest_bidder} with a bid of {highest_bid}.")
