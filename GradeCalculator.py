print("Grade Calculator")

def get_grade(score):
    if score > 95:
        return "A+"
    elif score == 95:
        return "A"
    elif score >= 90:
        return "A-"
    elif score > 85:
        return "B+"
    elif score == 85:
        return "B"
    elif score >= 80:
        return "B-"
    elif score > 75:
        return "C+"
    elif score == 75:
        return "C"
    elif score >= 70:
        return "C-"
    elif score > 65:
        return "D+"
    elif score == 65:
        return "D"
    elif score >= 60:
        return "D-"
    else:
        return "F"

scores = []
while True:
    score_input = input("Enter your score (or 'done' to finish): ")
    if score_input.lower() == 'done':
        break

    try:
        score = float(score_input)
        scores.append(score)
        average = sum(scores) / len(scores)
        print(f"Your average score so far is: {average:.1f}")
        print(f"Grade for {score}: {get_grade(score)}")
    except ValueError:
        print("Please enter a valid number.")

if scores:
    final_average = sum(scores) / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)
    
    print("\nFinal Results:")
    print(f"Average Score: {final_average:.1f}")
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")
    print(f"Final Grade: {get_grade(final_average)}")
else:
    print("No scores were entered.")
