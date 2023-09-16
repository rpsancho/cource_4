from src.head_hunter_api import HeadHunterAPI
from src.super_job_api import SuperJobAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


def main():
    form = {}

    user_input = input(f'Введите ключевые слова для поиска вакансий\n')
    form['keywords'] = user_input.strip()

    user_input = input(f'Введите минимальную зарплату в рублях\n')
    form['payment_from'] = int(user_input.strip())

    hh = HeadHunterAPI()
    sj = SuperJobAPI()

    hh_vacancies = hh.get_vacancies(form['keywords'], form['payment_from'])
    sj_vacancies = sj.get_vacancies(form['keywords'], form['payment_from'])

    vacancy_list = []
    for item in hh_vacancies['items']:
        vacancy = Vacancy(
            item['name'],
            item['alternate_url'],
            item['salary']['from'],
            item['snippet']['responsibility'],
            item['snippet']['requirement']
        )
        vacancy_list.append(vacancy)

    for item in sj_vacancies['objects']:
        vacancy = Vacancy(
            item['profession'],
            item['link'],
            item['payment_from'],
            item['work'],
            item['candidat']
        )
        vacancy_list.append(vacancy)

        saver = JSONSaver()
        saver.save_vacancies_to_json_file(vacancy_list)


if __name__ == '__main__':
    main()
