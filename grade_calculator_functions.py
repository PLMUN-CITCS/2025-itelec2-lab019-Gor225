def prompt_user_score() -> float:
    """
    Prompts the user for their score, ensuring a valid input.
    Returns:
        float: The user's validated score.
    """
    while True:
        try:
            score = float(input("Enter your score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input. Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def assign_grade(score: float) -> str:
    """
    Assigns a grade based on the provided score.
    Parameters:
        score (float): The numerical score of the user.
    Returns:
        str: The assigned grade ('A', 'B', 'C', 'D', or 'F').
    """
    grading_scale = {
        'A': score >= 90,
        'B': 80 <= score < 90,
        'C': 70 <= score < 80,
        'D': 60 <= score < 70,
        'F': score < 60
    }
    for grade, condition in grading_scale.items():
        if condition:
            return grade

def execute_grading_process():
    """
    Facilitates the flow of the program, from input to output.
    """
    score = prompt_user_score()
    grade = assign_grade(score)
    print(f"\nYour Grade is: {grade}")

if __name__ == "__main__":
    execute_grading_process()
