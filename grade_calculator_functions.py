# grade_calculator_functions.py

def get_student_score() -> float:
    """
    Prompts the user to enter a student's score and returns it as a numerical value.

    Returns:
        float: The numerical score entered by the user.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid numerical score.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the provided score.

    Parameters:
        score (float): The numerical score.

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
    """
    Main program flow to obtain the student's score and display the calculated grade.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()

