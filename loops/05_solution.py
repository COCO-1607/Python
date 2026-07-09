# Given a string, find the first non-repeated character.

str = input("Enter a string: ")

for char in str:
    print(char)
    if str.count(char) == 1:
        print(f"The first non-repeating character is: {char}")
        break