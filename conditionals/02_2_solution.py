# Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter your age: "))
# day = input("Enter the day of the week: ")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# 1. Print the menu options automatically
print("Please select a day:")
for index, day in enumerate(days, start=1):
    print(f"{index}. {day}")

# 2. Get the user's choice
choice = int(input("Enter the number of your selected day: "))
day = days[choice - 1]

price = 12 if age >= 18 else 8

if day.lower() == "wednesday":
    price -= 2

print(f"Your total is ${price}.")