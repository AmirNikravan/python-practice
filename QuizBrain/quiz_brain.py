class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.score = 0
        self.question_list = list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(
            f"Q.{self.question_number+1}: {current_question.text}.(True/False)?: "
        )
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current):
        if user_answer.lower() == current.lower():
            print("you got it right !")
            self.score += 1
        else:
            print("you're wrong")
        print(f"the correct answer was {current}")
        print(f"your score is {self.score} / {self.question_number}")

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    # def score(self, user_answer, current):
    #     if user_answer.lower() == current.lower():
