print("STEP COUNTER")
goal = int (input("What is your step goal today? "))
total_steps = int (input("How many steps are you at currently? "))

remaining = goal - total_steps
if remaining > 0:
    print(f"You need {remaining} more steps to reach your goal!")
if remaining < 0:
    print(f"Congratulations! You've exceeded your goal by {-remaining} steps!")  
if remaining == 0:
    print("Congratulations! You've reached your goal!")