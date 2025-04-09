import random
print("Coin Flip Game")

print("Guess heads or tails")

while True:
    guess = input("\nEnter your guess: ").lower()
    if guess != "heads" and guess != "tails":
        print("Please enter 'heads' or 'tails'")
        continue 
    flip = random.choice(["heads", "tails"])
    print(f"Coin shows {flip}")

    if guess == flip:
        print("You guessed correctly!")
    else:
        print("You were unsucsessful")

    proceed = input("would you like to continue? (y/n): ")
    if proceed != "y":
        print("Thanks for playing!")
        break