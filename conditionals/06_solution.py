distance = int(input("Enter the distance: "))

if distance < 3:
    transport = ("You can walk to your destination.")
elif distance <= 15:
    transport = ("You can take a bike to your destination.")
else:
    transport = ("You should take a bus or drive to your destination.")

print("AI recommends you the Mode of transport: " + transport)