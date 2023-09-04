#mini calculator

a = int(input("Enter a number1:"))
b = int(input("Enter a number2:"))
calculator = input("Choose any operation add/sub/mul/div:")
if calculator == 'add':
    print("The value is",a + b)

elif calculator == 'sub':
    print("The value is", a - b)

elif calculator == 'mul':
    print("The value is", a * b)

elif calculator == 'div':
    print("The value is", a / b)

else:
    print("Invalid operation....Try again!")
