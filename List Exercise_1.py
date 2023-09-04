#Create a list of your favorite books and print it.
#Add a new book to the list and print the updated list.
#Remove a book from the list and print the final list.

books = ["ikigai", "the harry potter","The middle class","The love begins"]
print("List of Your Favorite books:")
print(books)
while True:
    option = input("Choose any one of the option add,remove:")

    if option == 'add':
        new_book = input("Enter new book to add in list:")
        books.append(new_book)
        print("Updated List of Your Favorite books:")
        print(books)

    elif option == 'remove':
        remove_book = input("Enter book name to remove from list:")
        books.remove(remove_book)
        print("Final List of Your Favorite books")
        print(books)