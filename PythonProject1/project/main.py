from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    qt = Question(question["question"], question["correct_answer"])
    question_bank.append(qt)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"You 've completed the quiz\n"
      f"Your final score was: {quiz_brain.score}/{len(question_bank)}")