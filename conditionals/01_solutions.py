# Classify a person's age group: Child(<13), Teenager(13-19), Adult(20-59), Senior Citizen(60+).

age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")  
else:
    print("You are a senior citizen.")