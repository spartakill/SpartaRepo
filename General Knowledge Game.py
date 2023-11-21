import random

class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer == self.correct_option

def ask_question(question_obj):
    print(question_obj.question)
    for i, option in enumerate(question_obj.options, start=1):
        print(f"{i}. {option}")
    user_answer = input("Your answer (enter the option number): ")
    return question_obj.is_correct(int(user_answer))

def main():
    questions = [
        Question("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2),
        Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], 1),
        Question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"], 3),
        # Add more questions as needed
    ]

    score = 0

    random.shuffle(questions)

    for question in questions:
        if ask_question(question):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question.options[question.correct_option - 1]}\n")

    print(f"You got {score} out of {len(questions)} questions correct.")

if __name__ == "__main__":
    main()
