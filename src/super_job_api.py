import os
import requests
from src.abstract_api import AbstractAPI
from src.vacancy import Vacancy


class SuperJobAPI(AbstractAPI):

    __API_KEY = os.getenv('SUPER_JOB_API_KEY')

    def get_vacancies(self, keyword: str, payment: int) -> list:

        params = {
            'count': 100,
            'keyword': keyword,
            'payment_from': payment
        }

        headers = {
            'X-Api-App-Id': SuperJobAPI.__API_KEY
        }

        response = requests.get('https://api.superjob.ru/2.0/vacancies/', params=params, headers=headers).json()

        vacancy_list = []
        for item in response['objects']:
            vacancy = Vacancy(
                item['profession'],
                item['link'],
                item['payment_from'],
                item['work'],
                item['candidat'],
                'SJ'
            )
            vacancy_list.append(vacancy)

        return vacancy_list
