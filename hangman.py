import random 
#This me giving the system a random set of data to choose from 
words = ["SEUN","FUNMI","BOLAJI","BREAD","MUSIC","TEACHER", "ANIBE"]

chosen_word = random.choice(words).lower() #This changes the chosen word to a lower case letter after the computer has randomly picked a word
chosen_word_list = list(chosen_word) #This turns each word chosen into a set of data

display = []  #this is creating an empty list

#length_of_word = 0  #this is to initiate the length of word
#length_of_word += len(chosen_word) #this is to iterate over the lenght of words and store above accordingly

#print (length_of_word)


display = ["_"] * len(chosen_word) #this is to multiply the length of word by the number of underscore expected

print(display) 

while "_" in display: 
    guess = input("Guess an alphabet\n").lower() #this asks the user for an input and converts it into a lower case letter
    #print(guess)

    guess_count = {}
    for char in guess:
        guess_count[char] = guess_count.get(char, 0) + 1
    total_guess_count = sum(guess_count.values())

    print (total_guess_count)
    for i in range(len(chosen_word_list)):
        if guess == chosen_word_list[i]:
            display[i] = guess
        print("Current state:", ''.join(display))    
