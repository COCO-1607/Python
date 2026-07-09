# Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), E (40-59), F (below 40).

marks = int(input("Enter your marks: "))

if marks >100 or marks <= 0:
    print("Invalid marks. Please enter a value between 0 and 100.")
    exit()

if marks >= 90:
    Grade = ("You got an A grade.")
elif marks >= 80:
    Grade = ("You got a B grade.")
elif marks >= 70:
    Grade = ("You got a C grade.")
elif marks >= 60:
    Grade = ("You got a D grade.")
elif marks >= 40 :
    Grade = ("You got an E grade.")
else:
    Grade = ("You got an F grade.")
    
print("Grade:", Grade)
