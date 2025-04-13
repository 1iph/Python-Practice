import time
import random

print("Word Association Game")
print("Respond with a related word as fast as you can!")

random_words = [ "tree", "math", "water", "fruit", "pencil", "instrument", "sea", "beach"]

while True:
 prompt_word = random.choice(random_words)
 ready = input("Are you ready? (y): ")
 print(f"The random word is: {prompt_word}")
 print("Try to guess as fast as you can!")
 start_time = time.time()
 guess = input("> ")
 response_time = time.time() - start_time

 print("response time", response_time)
 proceed = input("Would you like to go again? (y/n): ")
 if proceed != "y":
    print("Goodbye")
    break