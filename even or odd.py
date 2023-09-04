def findevenorodd(number):
    if number % 2 == 0:
        print("The number",number," is even")
    else:
        print("The number",number,"is odd")

value = int(input("Enter an integer to check even or add:"))
findevenorodd(value)