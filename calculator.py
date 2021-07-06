'''
Collaborators: Megan helped me

'''

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b 

x = int(input("Please enter a number: "))
y = int(input("Please enter a number: "))

opperation = int(input("If addition enter 1, if subtraction enter 2, if multiplication enter 3, if division enter 4: "))

if opperation == 1:
    print("The sum is " + str(addition(x,y)))
elif opperation == 2:
    print("The difference is " + str(subtraction(x,y)))
elif opperation == 3:
    print("The product is " + str(multiplication(x,y)))
elif opperation == 4:
    print("The quotient is " + str(division(x,y)))
else:
    print("You did not enter 1,2,3 or 4. Try again...")