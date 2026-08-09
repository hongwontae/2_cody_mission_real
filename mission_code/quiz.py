class Quiz :
    def __init__(self, question : str, choices : list, answer : int, hint : str):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def print_quiz(self):
        print(self.question)

        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer

    def get_answer (self) :
        return self.answer

    
    def to_dict (self) :
        return {
            "question" : self.question,
            "choices" : self.choices,
            "answer" : self.answer,
        }

    def print_hint(self) :
        print() 
        print(f"힌트 : {self.hint}")

