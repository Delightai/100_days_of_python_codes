import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:
    user_output = []
    computer_output = []

    for _ in range(2):
        user = random.choice(cards)
        user_output.append(user)
    print(f'Your cards: {user_output}, current score: {sum(user_output)}')

    computer = random.choice(cards)
    print(f"Computer's First card: {computer}")

    choice = input("Type 'y' to get another card, type 'n' to pass\n")

    while choice == 'y':
        user = random.choice(cards)
        print(f'the new choice is {user}')
        user_output.append(user)
        print(f"Your cards: {user_output}, current score: {sum(user_output)}")
        if sum(user_output) > 21:
            print('You went over, you lose!')
            break
        choice = input("Type 'y' to get another card, type 'n' to pass\n")

    computer_output.append(computer)
    while sum(computer_output) < 17:
        computer = random.choice(cards)
        computer_output.append(computer)
    print(f"The computer's choice: {computer_output}, current score: {sum(computer_output)}")

    user_total = sum(user_output)
    computer_total = sum(computer_output)

    if user_total > 21:
        print('You went over, you lose!')
    elif computer_total > 21:
        print('Computer went over, you win!')
    elif user_total > computer_total:
        print('You win!')
    elif user_total < computer_total:
        print('Computer wins!')
    else:
        print('It\'s a draw!')

    play_again = input("Do you want to play again? Type 'y' for yes or 'n' for no: ")
    if play_again != 'y':
        break
