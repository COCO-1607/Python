print("Please select what type of pet you have")
print("1.Dog")
print("2.Cat")

Pet = int(input("Enter your choice (1 or 2): "))

age = int(input("Enter your pet's age: "))

if Pet == 1:
    if age < 2:
        print("Your dog is a puppy. Use puppy food.")
    else:
        print("Your dog is an adult. Use adult dog food.")
else:
    if age > 5:
        print("Your cat is an adult. Use adult cat food.") 
    else:
        print("Your cat is a kitten. Use kitten food.")