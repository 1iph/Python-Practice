import random

print("Recipe Generator")

while True:

 recipe = random.choice(["pasta", "Salad", "Grilled Cheese", "Noodle Soup", "Egg Sandwhich", "Chicken Salad Sandwhich"])

 print(f"\nYour random recipe: {recipe}")

 proceed = input("would you like to continue? (y/n): ")
 if proceed != "y":
        print("Goodbye")
        break