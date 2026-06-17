# Initial score for the user
score = 0

# Storing All the questions in a list
quiz = [
    {
	'question': "What is the capital city of Kenya?",
	'options': ["A. Kampala", "B. Cairo", "C.Arusha", "D. Nairobi"],
	'answer': "D"
    },
    {
	'question': "Which language is used for web development?",
	'options': ["A. Python", "B. HTML", "C. C++", "D. Java"],
	'answer': "B",
    },
	{
		# More questions to be added 
	}
]
# Loop throw the quiz list and manipulate it
for index, data in enumerate(quiz, 1):
    print(f"Question {index}. {data['question']}")
    for option in data['options']:
        print(option)

    # prompt the user for an answer
    answer = input("Enter your answer using (A/B/C/D): ").strip().upper()

    # Evaluate the answer
    if answer == data['answer']:
        print("Correct\n")
        score += 2
    else:
        print(f"Wrong answer, the correct answer is {data['answer']}\n")

    continue_choice = input("Do you want to continue (yes/no): ").lower()
    if continue_choice != "yes":
        print("Thanks for Participating!")
        break


# display Final score
print(f"Your Overall score is {score} points")