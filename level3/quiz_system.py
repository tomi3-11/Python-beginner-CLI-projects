def run_quiz():
    score = 0

    quiz = [
        {
            "question": "What is the capital city of Kenya?",
            "options": [
                "A. Kampala",
                "B. Cairo",
                "C. Arusha",
                "D. Nairobi"
            ],
            "answer": "D"
        },
        {
            "question": "Which language is primarily used to structure web pages?",
            "options": [
                "A. Python",
                "B. HTML",
                "C. C++",
                "D. Java"
            ],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": [
                "A. Earth",
                "B. Venus",
                "C. Mars",
                "D. Jupiter"
            ],
            "answer": "C"
        },
        {
            "question": "What does CPU stand for?",
            "options": [
                "A. Central Processing Unit",
                "B. Computer Personal Unit",
                "C. Central Program Utility",
                "D. Control Processing User"
            ],
            "answer": "A"
        },
        {
            "question": "Which of these is a Python data type?",
            "options": [
                "A. Integer",
                "B. Paragraph",
                "C. Browser",
                "D. Website"
            ],
            "answer": "A"
        },
        {
            "question": "Which ocean is the largest?",
            "options": [
                "A. Atlantic Ocean",
                "B. Indian Ocean",
                "C. Pacific Ocean",
                "D. Arctic Ocean"
            ],
            "answer": "C"
        },
        {
            "question": "What symbol is used for comments in Python?",
            "options": [
                "A. //",
                "B. #",
                "C. <!-- -->",
                "D. **"
            ],
            "answer": "B"
        },
        {
            "question": "How many days are there in a leap year?",
            "options": [
                "A. 365",
                "B. 364",
                "C. 366",
                "D. 360"
            ],
            "answer": "C"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": [
                "A. function",
                "B. func",
                "C. define",
                "D. def"
            ],
            "answer": "D"
        },
        {
            "question": "Which device is used to enter text into a computer?",
            "options": [
                "A. Monitor",
                "B. Keyboard",
                "C. Printer",
                "D. Speaker"
            ],
            "answer": "B"
        }
    ]

    print("\n" + "=" * 45)
    print("         WELCOME TO THE QUIZ SYSTEM")
    print("=" * 45)

    for index, data in enumerate(quiz, 1):

        print(f"\nQuestion {index} of {len(quiz)}")
        print(data["question"])

        for option in data["options"]:
            print(option)

        while True:
            answer = input(
                "\nEnter your answer (A/B/C/D): "
            ).strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("Invalid input! Please enter A, B, C, or D.")

        if answer == data["answer"]:
            print("Correct! ✓")
            score += 1
        else:
            print(
                f"Wrong! The correct answer is {data['answer']}."
            )

    percentage = (score / len(quiz)) * 100

    print("\n" + "=" * 45)
    print("              QUIZ RESULTS")
    print("=" * 45)

    print(f"Correct Answers: {score}/{len(quiz)}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage >= 80:
        print("Excellent work! Outstanding performance!")
    elif percentage >= 60:
        print("Good job! Keep improving!")
    elif percentage >= 40:
        print("Not bad! Keep practicing!")
    else:
        print("Keep studying and try again!")


def main():

    while True:

        run_quiz()

        play_again = input(
            "\nDo you want to play again? (yes/no): "
        ).strip().lower()

        if play_again != "yes":
            print("\nThank you for participating!")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()