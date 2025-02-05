from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]


for i in question_data:
    datas=[i['question'],i['correct_answer']]
    question=Question(datas[0],datas[1])
    question_bank.append(question)





quiz=QuizBrain(question_bank)

while quiz.still_has_ques():
    quiz.nextques()

