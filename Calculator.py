num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number: "))

c = input("Enter +, -, *, /, %, **, //:")

if c == '+':
    sum = num1 + num2
    print(sum)

elif c == '-':
    sum = num1 - num2
    print(sum)

elif c == '*':
    sum = num1 * num2
    print(sum)

elif c == '/':
    sum = num1 / num2
    print(sum)

elif c == '%':
    sum = num1 % num2
    print(sum)

elif c == '**':
    sum = num1 ** num2
    print(sum)

elif c == '//':
    sum = num1 // num2
    print(sum)

else:
    print("Oops....You have Entered an unknown Operator, Sorry Try again!")


