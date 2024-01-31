print("The Love Calculator is calculating your score...")
name1 = input("what is your name") # What is your name?
name2 = input("what is your babes name") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

combined_name = name1 + name2
capitalization = combined_name.lower()

T = capitalization.count("t")
R = capitalization.count("r")
U = capitalization.count("u")
E = capitalization.count("e")
L = capitalization.count("l")
O = capitalization.count("o")
V = capitalization.count("v")
E = capitalization.count("e")

first_digit = T + R + U + E
second_digit = L + O + V + E

Concantenate = str(first_digit) + str(second_digit)
Concantenate_number = int(Concantenate)

if Concantenate_number < 10 or Concantenate_number > 90 :
  print (f"Your score is {Concantenate_number}, you go together like coke and mentos.")
elif Concantenate_number >= 40 and Concantenate_number <= 50:
  print (f"Your score is {Concantenate_number}, you are alright together.")
else: 
  print(f"Your score is {Concantenate_number}.")