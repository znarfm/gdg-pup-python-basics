# declare a favorite foods list
faves: list[str] = [
    "Chicken Sandwich",
    "Pork Steak",
    "Chop Suey",
    "Pancit Palabok",
    "Fried Chicken",
]

# Iterating Through a List Using a for Loop
print("Here are my favorite foods:")
for food in faves:
    print(f"- {food}")

# Countdown Using a while Loop
try:
    # Ask for a starting number
    number: int = int(input("Enter a starting number to count down from: "))
    if number < 0:
        raise ValueError("Invalid input: Please enter a positive integer.")
    while number > 0:
        print(number)
        number -= 1  # decrement the number by 1
    print("Countdown complete!")
# catch if the input is negative
except ValueError as e:
    print(
        str(e)
        if "Invalid input: Please enter a positive integer." in str(e)
        else "Invalid input: Please enter a valid number."
    )
