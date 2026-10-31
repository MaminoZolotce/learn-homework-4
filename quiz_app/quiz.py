"""Задание 2. Загрузка вопросов и проверка ответов."""
import json
from pathlib import Path

from .question import Question


class Quiz:
    def __init__(self, questions_path, answer_key_path):
        self.questions_path = Path(questions_path)
        self.answer_key_path = Path(answer_key_path)

    def load_questions(self) -> list:
        with open(self.questions_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return [
            Question(item['id'], item['text'], item['options'])
            for item in data
        ]

    def check_answers(self, answers: dict) -> dict:
        with open(self.answer_key_path, 'r', encoding='utf-8') as file:
            correct_answers = json.load(file)

        total = len(correct_answers)
        if total == 0:
            return {'correct': 0, 'total': 0, 'percent': 0.0}

        correct = 0
        for question_id, rigth_answer in correct_answers.items():
            if answers.get(question_id) == rigth_answer:
                correct += 1

        percent = round(correct / total * 100,1)
        return {'correct': correct, 'total': total, 'percent': percent}
