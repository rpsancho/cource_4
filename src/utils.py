from src.head_hunter_api import HeadHunterAPI
from src.super_job_api import SuperJobAPI
from src.json_file_manager import JSONFileManager

messages = {
    'search_msg': 'Список вакансий получен',
    'filter_msg': 'Вакансии отфильтрованы по ключевому слову',
    'sort_msg': 'Вакансии отсортированы по зарплате'
}


def search_vacancies(vacancy_list):
    user_input = input(f'Введите ключевые слова для поиска вакансий\n')
    keywords = user_input.strip()

    user_input = input(f'Введите минимальную зарплату в рублях\n')
    salary = int(user_input.strip())

    hh = HeadHunterAPI()
    sj = SuperJobAPI()

    vacancy_list.clear()
    vacancy_list.extend(hh.get_vacancies(keywords, salary))
    vacancy_list.extend(sj.get_vacancies(keywords, salary))

    # saver = JSONFileManager()
    # saver.save_vacancies_to_json_file(vacancy_list)

    user_query(messages['search_msg'], print_vacancies, vacancy_list)


def filter_vacancies(vacancy_list: list):
    if not vacancy_list:
        print('Результаты поиска отсутствуют. Сначала произведите поиск\n')
        return

    keywords = input(f'Введите ключевое слово для фильтрации вакансий\n').strip()

    filtered_vacancy_list = [item for item in vacancy_list if item.is_str_in_attr(keywords)]
    vacancy_list.clear()
    vacancy_list.extend(filtered_vacancy_list)
    user_query(messages['filter_msg'], print_vacancies, filtered_vacancy_list)


def sort_vacancies(vacancy_list: list):
    if not vacancy_list:
        print('Результаты поиска отсутствуют. Сначала произведите поиск\n')
        return

    sorted_vacancy_list = sorted(vacancy_list, key=lambda x: x.payment, reverse=True)
    vacancy_list.clear()
    vacancy_list.extend(sorted_vacancy_list)
    user_query(messages['sort_msg'], print_vacancies, sorted_vacancy_list)


def user_query(message, action, action_arg):
    while True:
        print(f'{message}. Вывести результат? (y/n)\n')
        user_cmd = input().lower().strip()
        if user_cmd == 'y':
            action(action_arg)
            return True
        elif user_cmd == 'n':
            return False
        else:
            print('Неизвестная команда')
            continue


def print_vacancies(vacancy_list: list):
    for count, vacancy in enumerate(vacancy_list):
        print(f"{count}  {vacancy.title}  {vacancy.payment}  {vacancy.url}\n")


def add_vacancy_to_file(vacancy_list: list):
    if not vacancy_list:
        print('Результаты поиска отсутствуют. Сначала произведите поиск\n')
        return
    pos = input(f'Введите номер сохраняемой вакансии\n').strip()
    pos = int(pos)
    saver = JSONFileManager()
    try:
        saver.save_vacancy_to_json_file(vacancy_list[pos])
        print('Вакансия сохранена')
    except IndexError:
        print('Некорректный номер')
