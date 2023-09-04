#get i/p from user for salary and age. if salary is greater than 20000 or age is less than 25 then it'll ask for loan amount if not it will print you are not eligible
salary = int(input("Enter your salary:"))
age = int(input("Enter your age:"))

if (salary >= 20000 or age <= 25):
    loan_amount = int(input("Enter your loan amount:"))
    if loan_amount <= 50000:
        print("you are eligible for loan")
    else:
        print("Maximum loan amount is 50000")

else:
    print("you are not eligible for loan")