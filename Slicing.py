#Name Slicer
#Write a Python program that takes a full name as input (first name and last name separated by a space)
#and prints the initials of the first and last names.'''

name = input("Enter your full name:")
first_name,last_name = name.split() #spliting the full name into two has first name and last name
initials = first_name[0] + last_name[0] #creating a variable and assigning the slicing to get an initials of the full name
print("Initials:",initials)

