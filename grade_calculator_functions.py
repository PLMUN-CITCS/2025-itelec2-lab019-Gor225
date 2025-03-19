def get_student_score() -> float:
    """
    Prompts the user to enter their score and ensures valid numerical input.
    Returns:
        float: The validated numerical score.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Please enter a score between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score.
    Args:
        score (float): The numerical score to evaluate.
    Returns:
        str: The corresponding letter grade.
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    """
    Main function to execute the grade calculator program.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()