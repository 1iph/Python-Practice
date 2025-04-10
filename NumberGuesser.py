import random
import time
print("Number Guessing Game")
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print("\nI'm going to pick a number from 1-10, Try and guess it!")
counter = 0
while True:
 ready = input("\nHere we go! Are you Ready? (y/n): ")
 if ready == "n":
     
    print("Ok, You have 5 seconds!")
    counter += 1
    time.sleep(5)
    
 original_number = random.choice(number)

 guess = input("\nWhat is your guess?: ")
 if guess == (original_number):
    print("Horray, you guessed it!")
 else:
    print("Sorry, that number is incorect")   
    print(f"\nThe correct number was {original_number}")

 proceed = input("Try again? (y/n): ")
 if proceed != "y":
    print("Goodbye")
    break