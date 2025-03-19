def get_student_score() -> float:
    """
    Prompts the user to enter their score and ensures valid numerical input.
    Returns:
        float: The student's score.
    """
    while True:
        try:
            score = float(input("Enter your score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score.
    Args:
        score (float): The student's numerical score.
    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
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
    """Main function to execute the grade calculator."""
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()