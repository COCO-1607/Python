str = input("Enter a string: ")

reverse_str = ""

for char in str:
    reverse_str = char + reverse_str

print("Reversed string:", reverse_str)