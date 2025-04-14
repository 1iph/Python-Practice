import random
import time

player_score = 0
computer_score = 0
round_number = 1
print("\n==== Rock Paper Scissors ====")
print("\nRules:")
print("-Rock crushes Scissors")
print("-Scissors cuts Paper")
print("-Paper covers Rock")
print("-First to win 3 rounds is the champion!")

while True:
   
    print("\n -------------------------------")
    print(f"\n==== Round {round_number} ====")

    print("Make your choice: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choices = ["Rock", "Paper", "Scissors"]

    player_input = int(input("Enter your choice (1-3): "))
    player_choice = choices[player_input - 1]
    computer_choice = random.choice(choices)

    print(f"You chose: {player_choice}")
    print("Computer is choosing...")
    time.sleep(2)
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")

    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        player_score += 1
        print("You win this round!")

    else:
        computer_score += 1
        print("Computer wins this round!")

    print(f"Score: You {player_score} - {computer_score} Computer")
    round_number += 1

    if player_score == 3 or computer_score == 3:
        break

if player_score == 3:
    print("Congrats, you're the champion!")
else:
    print("Computer is the champion! Better luck next time.")
