Number = 0
for player in range(1,101):
    Number = player
    if player % 3 == 0 and player % 5 == 0 :
        print("FizzBuzz")
    elif player % 3 == 0 :
        print("Fizz")
    elif player % 5 == 0 :
        print ("Buzz")
        
    else:
        print (Number)