list = input("Enter your favorite color:")
lists = []
lists.append(list)
print("Initial List of Colors")
print(lists)
while True:
    list_manipulation = input("Pick any one to_do with list add, remove, exit: ")
    list_manipulation= list_manipulation.strip()

    if list_manipulation == 'add':
        new = input("Enter your favorite color:")
        lists.append(new)
        print("Updated List of Colors",new)
        print(lists)

    elif list_manipulation == 'remove':
        delete_item = input("Enter color that remove from list:")
        if delete_item in lists:
            lists.remove(delete_item)
            print("Final List of Colors")
            print(lists)

    elif list_manipulation == 'exit':
        break
    else:
        print("Oops...You have choosen unknown operation")
