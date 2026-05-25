#print("What's your name?")
#name = input()
#print(f"Hello, {name}!")

# Ask user for their name and store it in a variable
name = input("What's your name? ").strip().title()

# Remove whitespace from the str and capitalize user's name
#name = name.strip().title()

# Split user's name into first and last name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}")
