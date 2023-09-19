import os.path
import json
from src.abstract_json import AbstractJSON


class JSONFileManager(AbstractJSON):

    file_path = os.path.join('..', 'data', 'search_results.json')

    def __init__(self):
        pass

    def save_vacancies_to_json_file(self, items: list):

        if self.file_exist():
            mode = 'w'
        else:
            mode = 'x'
        with open(JSONFileManager.file_path, mode, encoding='UTF-8') as f:
            lst = []
            for item in items:
                lst.append(item.__dict__)
            json.dump(lst, f, ensure_ascii=False, indent=4)

    def save_vacancy_to_json_file(self, item: object):

        lst = self.get_vacancies_from_json_file()
        lst.append(item.__dict__)

        if self.file_exist():
            mode = 'w'
        else:
            mode = 'x'

        with open(JSONFileManager.file_path, mode, encoding='UTF-8') as f:
            json.dump(lst, f, ensure_ascii=False, indent=4)

    def get_vacancies_from_json_file(self) -> list:

        if self.file_exist():
            if self.file_empty():
                return []
            else:
                with open(JSONFileManager.file_path, 'r', encoding='UTF-8') as f:
                    vacancies = json.load(f)
                return vacancies
        else:
            return []

    def file_exist(self) -> bool:
        return os.path.exists(JSONFileManager.file_path)

    def file_empty(self) -> bool:
        if os.path.getsize(JSONFileManager.file_path) == 0:
            return True
        else:
            return False


j = JSONFileManager()
print(j.file_exist())
print(j.file_empty())
