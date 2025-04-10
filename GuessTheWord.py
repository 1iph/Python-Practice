import random
print("Word Scramble Game")
print("Unscramble the letters to find the word!")

words = ["earth", "bottle", "computer", "book", "lamp", "plant", "violin", "water", "window"]


while True:
    original_word = random.choice(words)
    letters = list(original_word)
    random.shuffle(letters)
    scrambled = "".join(letters)

    print(f"\n Here is your scrambled word: {scrambled}")
    guess = input("What's the word?: ").lower()
    if guess == original_word:
        print("You Guess correctly!")
    else: 
       print("Sorry, that was inccorect")
    proceed = input("Would you like to continue? (y/n): ")
    if proceed != 'y':
        print("Goodbye")
        break