'''Please code this exercise in your computer IDE. For this exercise, download the members.txt file attached to the resources. Then, create a program that:

1. prompts the user to enter a new member.

2. adds that member to members.txt at the end of the existing members. For example, the user here has entered the member Solomon Right.


In the above example, Solomon Right will be added to members.txt updating the content of the file to:

John Smith

Sen Lakmi

Sono Octonot

Solomon Right'''

user_prompts = input("Enter a new member") + "\n"
file = open('members.txt', 'r')
members = file.readlines()
file.close()

members.append(user_prompts)

file = open('members.txt', 'w')
members = file.writelines(members)
file.close()

''' Extend the given code (in the exercise area) so the code capitalizes all the names and surnames of the list and then prints the new list. The output of your code should be as below:
['John Smith', 'Jay Santi', 'Eva Kuki']'''

'''names = ["john smith", "jay santi", "eva kuki"]

names = [name.title() for name in names]
print(names)'''
user_prompt = input("Enter a password:")

if len(user_prompt) > 7:
    print("Great password there")

elif len(user_prompt) == 7:
    print("Password is OK, but not too strong")

elif len(user_prompt) <= 7:
    print("Your password is weak")

