import time

print("Count down timer")

countdown_from = int (input("What do you want to start at?: ")) # sets the number

print("Countdown timer starting!")
while countdown_from > 0: # makes it repeat until 0
 print(f"{countdown_from} seconds remaining") # starts at whatever time was input
 time.sleep(1) # waits 1 second
 countdown_from -= 1 # Decreases the timer by 1 
print("Time's up!")

