"""Задание 1. Реализуй Question по README."""
class Question:
    def __init__(self, question_id:int, text:str, options:dict):
            self.question_id =question_id
            self.text = text
            self.options = dict(options)

    def as_dict(self):
        return{
                   'id' : self.question_id,
                   'text' : self.text,
                   'options' : dict(self.options),
               }
