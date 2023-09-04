# get score percentage if the score is greater than 70% then we can get i/p from user for name,dept,loc and we need to print you are eligible if not we can print yoy are not eligible
score_percentage = int(input("Enter your score percentage:"))
if score_percentage > 70:
    name = input("Enter your name:")
    department = input("Enter your department:")
    location = input("Enter your location:")
    print("You are eligible")

else:
    print("you are not eligible")