def get_student_score() -> int:
    """
    Prompts the user to enter a valid numerical score between 0 and 100.
    Returns:
        int: The student's validated score.
    """
    while True:
        try:
            score = int(input("Enter your score (0-100): "))
            if 0 <= score <= 100:  # Check if score is within range
                return score
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a whole number.")

def calculate_grade(score: int) -> str:
    """
    Calculates the grade based on the provided score.
    Parameters:
        score (int): The student's score.
    Returns:
        str: The corresponding grade (A, B, C, D, or F).
    """
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def display_result():
    """
    Main function to coordinate getting the score, calculating the grade,
    and displaying the result.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"\nYour Grade is: {grade}")

if __name__ == "__main__":
    display_result()
