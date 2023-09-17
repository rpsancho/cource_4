from src.head_hunter_api import HeadHunterAPI
from src.super_job_api import SuperJobAPI
from src.json_file_manager import JSONFileManager
from src.vacancy import Vacancy
from src.utils import is_string_in_dict


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

    # спрятать в функцию
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

        saver = JSONFileManager()
        saver.save_vacancies_to_json_file(vacancy_list)
        saver.get_vacancies_from_json_file()

        print(f'Список вакансий, удовлетворяющих запросу, получен и сохранен.')
        user_input = input(f'Выберите дальнейшее действие:\n'
                           f'1  -  cортировать вакансии по зарплате\n'
                           f'2  -  фильтровать вакансии по дополнительному ключевому слову\n')
        user_input = user_input.strip()
        if user_input == '1':
            vac_list = saver.get_vacancies_from_json_file()
            sorted_vacancies = sorted(vac_list, key=lambda x: x['payment'], reverse=True)
            for vac in sorted_vacancies:
                print(f"{vac['title']}  {vac['payment']}  {vac['url']}")
        elif user_input == '2':
            vac_list = saver.get_vacancies_from_json_file()
            user_input = input(f'введите ключевое слово:\n')
            user_input = user_input.strip()
            filtered_vacancies = [item for item in vac_list if is_string_in_dict(user_input, item)]
            for vac in filtered_vacancies:
                print(f"{vac['title']}  {vac['payment']}  {vac['url']}")
        else:
            print(f'непонятно')
        return


if __name__ == '__main__':
    main()
