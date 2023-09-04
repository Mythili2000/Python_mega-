#Write a program that takes a year as input and prints whether it's a leap year or not.
year = int(input("Enter a year:"))

if(year % 400 ==0) and (year % 100 ==0):
    print(year,"is a leap year")

elif(year % 4 ==0) and (year % 100 !=0):
    print(year, "is a leap year")

else:
    print(year,"is not a leap year")
