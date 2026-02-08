from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from random import shuffle

# Create and append Question objects to a list
question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

shuffle(question_bank)

# Create QuizBrain object
quiz = QuizBrain(question_bank)

# Main loop
while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}.")