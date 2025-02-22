def get_student_score():
    """Prompts the user to enter a numeric score and returns it as an integer."""
    while True:
        try:
            score = float(input("Enter your score: "))
            return score
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(score):
    """Determines and returns the letter grade based on the grading scale."""
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
    """Main function to run the Grade Calculator program."""
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()
