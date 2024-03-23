import random 

# This is me giving the system a random set of data to choose from 
words = ["SEUN", "FUNMI", "BOLAJI", "BREAD", "MUSIC", "TEACHER", "ANIBE"]

# Randomly choose a word and convert it to lowercase
chosen_word = random.choice(words).lower()
chosen_word_list = list(chosen_word) # This turns each word chosen into a set of data

display = []
# Initialize an empty list to store the display
display = ["_"] * len(chosen_word) # This is to multiply the length of word by the number of underscore expected


# Print the initial display
print(display) 

# This loop continues until all underscores are replaced
while "_" in display:
    guess = input("Guess an alphabet\n").lower() # This asks the user for an input and converts it into a lower case letter
    # print(guess)

    guess_count = {}
    for char in guess:
        guess_count[char] = guess_count.get(char, 0) + 1
    total_guess_count = sum(guess_count.values())

    print (total_guess_count)
    
    # Check if the guessed alphabet is present in the chosen word
    for i in range(len(chosen_word_list)):
        if guess == chosen_word_list[i]:
            display[i] = guess
    
    # Print the current state of the word
    print("Current state:", ''.join(display))
