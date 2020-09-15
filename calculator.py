'''
Collaborators: Megan helped me

'''

def addition():
    return x + y

def subtraction():
    return x - y

def multiplication():
    return x * y

def division():
    return x / y 

x = int(input("Please enter a number: "))
y = int(input("Please enter a number: "))

opperation = int(input("If addition enter 1, if subtraction enter 2, if multiplication enter 3, if division enter 4: "))

if opperation == 1:
    print("The sum is " + str(addition()))
elif opperation == 2:
    print("The difference is " + str(subtraction()))
elif opperation == 3:
    print("The product is " + str(multiplication()))
elif opperation == 4:
    print("The quotient is " + str(division()))
else:
    print("You did not enter 1,2,3 or 4. Try again...")