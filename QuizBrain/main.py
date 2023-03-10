from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

data_bank = list()
for i in question_data:
    data_bank.append(Question(i["text"], i["answer"]))
print(data_bank[0].GetAnswer())
quiz = QuizBrain(data_bank)
while quiz.still_has_question():
    quiz.next_question()
