class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number >= len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(
            f"Q.{self.question_number}: {current_question.text}(True/False?)")
        self.check_answer(user=user_input, correct=current_question.answer)

    def check_answer(self, user, correct):
        status = bool()
        if user.lower() == correct.lower():
            print("you're right!")
            status = True
        else:
            print("you're wrong!")
            status = False
        print(f"the correct answer was {correct}")
        self.show_score(status=status)

    def show_score(self, status):
        if status == True:
            print('here')
            self.score += 1
        print(f"your current score is {self.score}/{self.question_number}")
