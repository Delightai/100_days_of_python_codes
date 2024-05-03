

def add(n1, n2):
    return (n1 + n2)

def subtraction(n1 , n2):
    return (n1 - n2)

def division (n1 , n2):
    return (n1/n2)

def multiplication (n1, n2 ):
    return (n1 * n2)


operator_list = {
    "+" : add ,
    "-" : subtraction ,
    "/" : division ,
    "*" : multiplication,
}



from art3 import logo 

print (logo)
repetition = True


first_number = float(input("Put in the first number\n"))

for love in operator_list:
    print(love)
operator = input('Pick an operator\n')

while repetition:

    second_number = float(input("Put in the second number\n"))

    calculation_function = operator_list[operator]

    answer = calculation_function(first_number, second_number)

    print(f"{first_number}{operator}{second_number} = {answer}") 

    if input(f"Type 'y' to continue with {answer}, or type 'n' to exit: ") == 'y':
        answer == first_number
     
    else:
        repetition = False



    


