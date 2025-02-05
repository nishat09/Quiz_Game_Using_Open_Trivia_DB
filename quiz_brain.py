class QuizBrain:
    def __init__(self,q_bank):
        self.q_number=0
        self.score=0
        self.q_bank=q_bank


    def nextques(self):
        i=self.q_number
        ques_text=self.q_bank[i].text
        correct_answer =self.q_bank[i].ans
        i+=1
        self.q_number+=1
        ques=input(f'Q.{i}:{ques_text} (True/False)?: ')
        self.answer_check(ques,correct_answer)




    def answer_check(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print('You got it right')
            self.score+=1
        else:
            print('Your answer is wrong')

        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is: {self.score}/{self.q_number}')




    def still_has_ques(self):
        limit=len(self.q_bank)
        return self.q_number<limit






