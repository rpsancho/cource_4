from abc import ABC, abstractmethod


class AbstractJSON(ABC):

    @abstractmethod
    def save_vacancies_to_json_file(self, items: list):
        pass
