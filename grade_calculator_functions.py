def get_student_score() -> float:
    """
    Prompts the user to enter their score and ensures valid input.
    Returns:
        float: The validated student score.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score: float) -> str:
    """
    Determines the grade based on the given score.
    
    Args:
        score (float): The student's score.
    
    Returns:
        str: The corresponding letter grade.
    """
    grades = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D')]
    for threshold, grade in grades:
        if score >= threshold:
            return grade
    return 'F'

if __name__ == "__main__":
    student_score = get_student_score()
    grade = calculate_grade(student_score)
    print(f"Your Grade is: {grade}")
