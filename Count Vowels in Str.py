def count_vowels(word): #defining the count vowels
    vowels = "aeiouAEIOU" # mentioning what are the vowels in alphabets to understand the computer
    vowels_count = 0 # mentioning the count of vowels as 0 becoz it'll add in a loop

    for char in word: # using for loop to loop over the character in a word. so, that it'll iterate each character
        if char in vowels: # using in method to compare whether that character is present in vowels if it presents then it'll add to the count
            vowels_count += 1
    return vowels_count

user_input = input("Enter a string:")
vowels_count = count_vowels(user_input)

print("Number of vowels:",vowels_count)
