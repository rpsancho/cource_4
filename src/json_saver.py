import os.path
import json
from src.abstract_json import AbstractJSON


class JSONSaver(AbstractJSON):

    file_path = os.path.join('..', 'data', 'search_results.json')

    def __init__(self):
        pass

    def save_vacancies_to_json_file(self, items: list):

        if not os.path.exists(JSONSaver.file_path):
            mode = 'x'
        else:
            mode = 'w'

        with open(JSONSaver.file_path, mode, encoding='UTF-8') as f:
            lst = []
            for item in items:
                lst.append(item.__dict__)
            json.dump(lst, f, ensure_ascii=False, indent=4)

    def sort_vacancies(self, parameter, order):
        pass

