#
subject1 = int(input("Enter your subject1 mark:"))
subject2 = int(input("Enter your subject2 mark:"))
subject3 = int(input("Enter your subject3 mark:"))
subject4 = int(input("Enter your subject4 mark:"))
subject5 = int(input("Enter your subject5 mark:"))
average = (subject1 + subject2 + subject3 + subject4 + subject5)/5
print("Your average mark is:",average)
if average < 35:
    print("Additional is required")

else:
    print("you are good to go..!")




