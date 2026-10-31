"""Задание 3. Хранение списка результатов."""
import json
from pathlib import Path


class ResultStorage:
    def __init__(self, path):
        self.path = Path(path)

    def load(self) -> list:
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            return []
        else:
            return data

    def save(self, result: dict):
        results = self.load()
        results.append(dict(result))

        self.path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(results, file, ensure_ascii=False, indent=2)
