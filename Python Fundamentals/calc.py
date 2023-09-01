# basic calc

def add(num1, num2):
    return num1 + num2
def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

choice = int(input('\n Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: '))

num1 = int(input('\n input your first number'))
num2 = int(input('\n input your second number'))

if choice == 1:
    print(num1, '+', num2, '=', add(num1, num2))
elif choice == 2:
    print(num1, '-', num2, '=', substract(num1, num2))
elif choice == 3:
    print(num1, '*', num2, '=', multiply(num1, num2))
elif choice == 4:
    print(num1, '/', num2, '=', divide(num1, num2))
else:
    print('invalid option')