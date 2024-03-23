import random

#assigning the list of options to chose from into the variable words
words = ["SEUN", "FUNMI", "BOLAJI", "BREAD", "MUSIC", "TEACHER", "ANIBE"]

#this is assigning the variable chosen_word into the random word chosen by the computer
chosen_word = random.choice(words).lower()
chosen_word_list = list(chosen_word) # this converts the chosen word into a list of character 

display = ["_"] * len(chosen_word) # this multiplies the length of word by the string "_" and save into the variable display
 
print(display)

max_attempts = 6  # Maximum number of attempts
attempts_left = max_attempts  # Initialize attempts left counter

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


while "_" in display and attempts_left > 0:
    guess = input("Guess an alphabet: ").lower()

    correct_guess = False
    for i in range(len(chosen_word_list)):
        if guess == chosen_word_list[i]:
            display[i] = guess
            correct_guess = True

    print("Current state:", ''.join(display))
    
    if not correct_guess:
        attempts_left -= 1
        print("Incorrect guess. Attempts left:", attempts_left)

if "_" not in display:
    print("Congratulations! You guessed the word.")
else:
    print("Out of attempts. The word was:", chosen_word)


print(stages[attempts_left]) 



