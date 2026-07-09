fruit = input("Enter a fruit name: ")
color = input("Enter the color of the fruit: ")

if fruit.lower() == "banana" :
    if color == "green":
        print("unripe fruit")
    elif color == "yellow": 
        print("ripe fruit")
    elif color == "brown":
        print("overripe fruit")
else: 
    print("Fruit not recognized.")