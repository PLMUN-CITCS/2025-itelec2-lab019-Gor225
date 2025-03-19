def get_student_score() -> float:
    """
    Handles user input to obtain the student's score.
    Ensures the input is a valid numerical value.
    Returns:
        float: The numerical score entered by the user.
    """
    while True:
        try:
            score = float(input("Please enter your score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Enter a numeric value.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score and grading scale.
    
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

def display_grade(score: float, grade: str) -> None:
    """
    Displays the student's score and corresponding letter grade.
    
    Args:
        score (float): The student's numerical score.
        grade (str): The corresponding letter grade.
    """
    print(f"Your score: {score}")
    print(f"Your Grade is: {grade}")

def main():
    """Main program flow to get the student's score and display the corresponding grade."""
    score = get_student_score()
    grade = calculate_grade(score)
    display_grade(score, grade)

if __name__ == "__main__":
    main()