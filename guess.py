guess_taken = 0
while True:
    print('take a guess')
    number = int(input("Enter a number from 1 to 20:"))
    guess_taken = guess_taken + 1
    if number < guess_taken:
        print("Guess is too low")
    elif number > guess_taken:
        print("Guess is too high")
    elif number==guess_taken:
        print("congratulations")
        break

