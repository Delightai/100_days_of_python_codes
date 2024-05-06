

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

def cal():

    from art3 import logo 

    print (logo)

    first_number = float(input('Please input the first number\n'))
    for love in operator_list:
        print (love)

    repetition = True 

    while repetition:
        operator = input('Pick an operator\n')
        second_number = float(input('Please input the next number\n'))
        calculation_function = operator_list[operator]
        answer1 = calculation_function(first_number, second_number)

        print(f"{first_number}{operator}{second_number} = {answer1}") 
        
        if input(f"Type 'y' to continue with {answer1}, or type 'n' to start calculating all again:, or type 'e' to end the program\n ") == 'y':
            first_number = answer1
        elif input(f"Type 'y' to continue with {answer1}, or type 'n' to start calculating all again:, or type 'E' to end the program \n") == 'n' :
            repetition = False
            cal()
        else:
            repetition = False
            print("Thank you for using oor calculator app")
cal()

 


    


