def get_student_score():
    """Prompts the user to enter a numeric score and handles invalid input."""
    while True:
        try:
            score = float(input("Enter your score: "))
            return score
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def calculate_grade(score):
    """Determines the letter grade based on the given score and grading scale."""
    if 90 <= score <= 100:
        return 'A'
    if 80 <= score < 90:
        return 'B'
    if 70 <= score < 80:
        return 'C'
    if 60 <= score < 70:
        return 'D'
    return 'F'


def main():
    """Main program flow."""
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")


if _name_ == "_main_":
    main()