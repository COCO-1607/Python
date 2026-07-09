#  Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

print("What is the weather like today?:")
print("1. Sunny")
print("2. Rainy")
print("3. Snowy")

choice = input("Enter the number corresponding to the weather: ")

if choice == "1":
    print("It's a sunny day! Go for a walk. Don't forget your sunglasses.")
elif choice == "2":
    print("It's raining outside. Read a book with a nice cup of coffee.")
elif choice == "3":
    print("It's snowing! Go build a snowman. Don't forget your coat.") 