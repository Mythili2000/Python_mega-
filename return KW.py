s_username = "Mythili"
s_password = 123
uname = input("Enter user name:")
password = int(input("Enter your password:"))
def validate():
    if (s_username == uname) and (s_password == password):
        return True
    else:
        return False
result = validate()
print(result)
