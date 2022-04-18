# day17: main.py
from quiz_brain import QuizBrain
from data import question_data
from question_model import Question

questions = []
for x in question_data:
    questions.append(Question(x["text"], x["answer"]))

quiz = QuizBrain(questions)
quiz.run()
