import requests
from src.abstract_api import AbstractAPI


class HeadHunterAPI(AbstractAPI):

    def __init__(self):
        pass

    def get_vacancies(self, keyword: str, payment: int):

        params = {
            'page': 1,
            'per_page': 100,
            'text': keyword,
            'salary': payment,
            'currency': 'RUR',
            'only_with_salary': True
        }

        response = requests.get('https://api.hh.ru/vacancies', params)
        return response.json()
