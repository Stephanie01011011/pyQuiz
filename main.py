from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_q = Question(text, answer)
    question_bank.append(new_q)


new_quiz = QuizBrain(question_bank)
while new_quiz.still_has_questions():
    new_quiz.next_question()
print("You've completed the quiz! Congratulations :)")
print(f"Your final score was {new_quiz.score}/{len(question_bank)}")