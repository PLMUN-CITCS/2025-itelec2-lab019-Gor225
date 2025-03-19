def get_student_score() -> float:
    """Handles user input to obtain the student's score.
    
    Returns:
        float: The numerical score entered by the user.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(score: float) -> str:
    """Determines the letter grade based on the given score.
    
    Args:
        score (float): The numerical score to be evaluated.
    
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
    """Main function to execute the grade calculation program."""
    print("\nEnhanced Grade Calculator")
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")
    print("Thank you for using the Grade Calculator!")

if __name__ == "__main__":
    main()
