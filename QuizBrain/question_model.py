class Question:
    def __init__(self,question,answer):
        self.text = question
        self.answer = answer
    def GetAnswer(self):
        return self.answer