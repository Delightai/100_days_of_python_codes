import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


user_output = []
computer_output = []

for i in range(2):
    user = random.choice(cards) 
    user_choice = user_output.append(user)
    print (user_output)
    total = sum(user_output)

print(f'Your cards: {user_output}, current score: {total}')

computer = random.choice(cards)
print(f"Computer's First card: {computer}")
computer_choice = computer_output.append(computer)

choice = input("Type 'y' to get another card, type 'n' to pass\n")

if choice == 'y':

    user1 = random.choice(cards)
    print(f'the new choice is {user1}')
    user_choice1 = user_output.append(user1)
    print(user_output)
    total1 = sum(user_output)

    
print(f"Your cards: {user_output}, current score: {total1}")

computer1 = random.choice(cards)
computer_second = computer_output.append(computer1)
print(f"The computers choice : {computer_output}")
computer_total = sum(computer_output)

if total1 > 21:
    print('You went over you lose')
elif total1 > computer_total :
    print('You win!')
else:
    print("computer won")
