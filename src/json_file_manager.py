import os.path
import json
from src.abstract_json import AbstractJSON
from src.vacancy import Vacancy


class JSONFileManager(AbstractJSON):

    abs_path = os.path.abspath('.')
    file_path = os.path.join(abs_path, 'data', 'search_results.json')

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

    def del_vacancy_from_json_file(self, pos):
        vacancy_list = self.get_vacancies_from_json_file()
        vacancy_list.pop(pos)
        out_list = []
        for item in vacancy_list:
            vacancy = Vacancy(
                item['title'],
                item['url'],
                item['payment'],
                item['description'],
                item['requirements'],
                item['platform']
            )
            out_list.append(vacancy)
        self.save_vacancies_to_json_file(out_list)

    def file_exist(self) -> bool:
        return os.path.exists(JSONFileManager.file_path)

    def file_empty(self) -> bool:
        if os.path.getsize(JSONFileManager.file_path) == 0:
            return True
        else:
            return False
