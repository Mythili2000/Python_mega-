#Write a program that takes two numbers as input and prints the maximum of the two.
num1 = int(input("Enter a num1:"))
num2 = int(input("Enter a num2:"))
if num1 > num2:
    print(num1,"is maximum number")

elif num1 < num2:
    print(num2,"is maximum number")

elif num1 == num2:
    print(num1,num2,"both is maximum numbers")