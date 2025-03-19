def get_student_score() -> float:
    """
    Handles user input to obtain the student's score.
    Ensures valid numerical input (integer or float).
    Returns:
        float: The student's score.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score and grading scale.
    
    Args:
        score (float): The student's numerical score.
    
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

# Main program flow
if __name__ == "__main__":
    student_score = get_student_score()
    grade = calculate_grade(student_score)
    print(f"Your Grade is: {grade}")
