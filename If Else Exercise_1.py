# get input for variable number and check whether the number is divisible by 3 and 5. If yes print it is divisible by 3 and 5 or not divisible by 3 and 5
a = int(input("Enter a number:"))
if (a % 3 == 0):
    print("The number is divisible by 3 and 5")
elif(a %5 ==0):
    print("The number is divisible by 3 and 5")
else:
    print("The number is not divisible by 3 and 5")