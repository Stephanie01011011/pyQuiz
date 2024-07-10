# asking the questions
# check if answer is correct
# check if were at the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        question_number = self.question_number
        current_question = self.questions_list[question_number]
        self.question_number +=1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True or False): \n")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        question_number = self.question_number
        q_list = self.questions_list
        return question_number < len(q_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You're right!")
            self.score += 1

        else:
            print("That is wrong.")
            print(f"The correct answer was {correct_answer}")

        print(f"Your current score is: {self.score}/{self.question_number}.\n\n")