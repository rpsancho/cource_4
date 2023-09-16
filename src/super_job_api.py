import os
import requests
from src.abstract_api import AbstractAPI


class SuperJobAPI(AbstractAPI):

    __API_KEY = os.getenv('SUPER_JOB_API_KEY')

    def __init__(self):
        pass

    def get_vacancies(self, keyword: str, payment: int):

        params = {
            'count': 100,
            'keyword': keyword,
            'payment_from': payment
        }

        headers = {
            'X-Api-App-Id': SuperJobAPI.__API_KEY
        }

        response = requests.get('https://api.superjob.ru/2.0/vacancies/', params=params, headers=headers)
        return response.json()
