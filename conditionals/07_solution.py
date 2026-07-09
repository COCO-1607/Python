# Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

print("please select the size of your drink:")
print("1. Small")
print("2. Medium") 
print("3. Large")

size = int(input("Enter your choice (1-3): "))

print("Would you like to add any extra shot of espresso?")
extra_shot = input("Enter 'yes' or 'no': ")

if size == 1 :
    if extra_shot.lower() == 'yes':
        coffee = ("You have selected a Small coffee with an extra shot of espresso.")
    else:
        coffee = ("You have selected a Small coffee without an extra shot of espresso.")
elif size == 2:
    if extra_shot.lower() == 'yes':
        coffee = ("You have selected a Medium coffee with an extra shot of espresso.")
    else:
        coffee = ("You have selected a Medium coffee without an extra shot of espresso.")
elif size == 3:
    if extra_shot.lower() == 'yes':
        coffee = ("You have selected a Large coffee with an extra shot of espresso.")
    else:
        coffee = ("You have selected a Large coffee without an extra shot of espresso.")

print("Your Order: " + coffee)
