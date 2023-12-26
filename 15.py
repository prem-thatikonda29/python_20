class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def display_question(self):
        print(self.text)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def check_answer(self, user_answer):
        return user_answer == self.correct_option


class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def take_quiz(self, user):
        print(f"Welcome, {user.name}, to the {self.name} quiz!")
        score = 0

        for question in self.questions:
            question.display_question()
            user_answer = int(input("Your answer (enter the option number): "))

            if question.check_answer(user_answer):
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was option {question.correct_option}.\n")

        print(f"Quiz completed! Your score: {score}/{len(self.questions)}")
        return score


class User:
    def __init__(self, name):
        self.name = name


def main():
    # Sample questions for a quiz
    # question1 = Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], 2)
    # question2 = Question("What is the largest mammal?", ["Elephant", "Whale", "Giraffe", "Lion"], 2)
    # question3 = Question("Which programming language is this quiz written in?", ["Java", "Python", "C++", "JavaScript"], 2)

    question1 = Question("What is the result of 5 + 7?", ['12', '14', '10', '16'],1)
    question2 = Question("What is the square of 4?", ['14', '15', '16', '17'],3)
    question3 = Question("If x = 3 and y = 2, what is x + y?", ['3', '5', '6', '7'],2)
    question4 = Question("What is the product of 6 and 9?", ['50', '52', '54', '56'],3)
    
    quiz = Quiz("Mathematics", [question1, question2, question3, question4])

    # Get user's name
    user_name = input("Enter your name: ")
    user = User(user_name)

    # Take the quiz
    user_score = quiz.take_quiz(user)

    # Display results
    print(f"Thank you, {user.name}, for taking the quiz! Your final score is: {user_score}/{len(quiz.questions)}")


if __name__ == "__main__":
    main()
