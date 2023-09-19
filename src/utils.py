from src.head_hunter_api import HeadHunterAPI
from src.super_job_api import SuperJobAPI
from src.json_file_manager import JSONFileManager

messages = {
    'search_msg': 'Список вакансий получен',
    'filter_msg': 'Вакансии отфильтрованы по ключевому слову',
    'sort_msg': 'Вакансии отсортированы по зарплате',
    'del_msg': 'Вакансия удалена'
}

main_menu = {
    '1': '1 - новый поиск вакансий',
    '2': '2 - фильтрация по ключевому слову',
    '3': '3 - сортировка по зарплате',
    '4': '4 - сохранение вакансии в файл',
    '5': '5 - показать все вакансии из файла',
    '6': '6 - удалить вакансию из файла',
    '7': '7 - выход'
}

# search_menu = {
#     '1': '1 - фильтрация по ключевому слову',
#     '2': '2 - сортировка по зарплате',
#     '3': '3 - сохранение в файл',
#     '4': '4 - наверх'
# }
#
# file_menu = {
#     '1': '1 - показать все вакансии из файла',
#     '2': '2 - удалить вакансию из файла',
#     '3': '3 - наверх'
# }


def show_menu(menu: dict):
    for item in menu.values():
        print(item)


def search_vacancies(vacancy_list: list):
    """
    Search vacancies by keywords and salary in HH and SJ platforms and put result in vacancy_list
    :param vacancy_list: list of Vacancy objects
    :return: None (modify vacancy_list param)
    """
    keywords = input(f'Введите ключевые слова для поиска вакансий\n').strip()
    salary = int(input(f'Введите минимальную зарплату в рублях\n').strip())

    hh = HeadHunterAPI()
    sj = SuperJobAPI()

    vacancy_list.clear()
    vacancy_list.extend(hh.get_vacancies(keywords, salary))
    vacancy_list.extend(sj.get_vacancies(keywords, salary))

    user_confirmation(messages['search_msg'], show_vacancies_from_list, vacancy_list)


def filter_vacancies(vacancy_list: list):
    """
    Filter vacancies in vacancy_list by keyword
    :param vacancy_list: list of Vacancy objects
    :return: None (modify vacancy_list param)
    """
    if not vacancy_list:
        print('Результаты поиска отсутствуют. Сначала произведите поиск\n')
        return

    keywords = input(f'Введите ключевое слово для фильтрации вакансий\n').strip()

    filtered_vacancy_list = [item for item in vacancy_list if item.is_str_in_attr(keywords)]
    vacancy_list.clear()
    vacancy_list.extend(filtered_vacancy_list)
    user_confirmation(messages['filter_msg'], show_vacancies_from_list, filtered_vacancy_list)


def sort_vacancies(vacancy_list: list):
    """
    Sort vacancies in vacancy_list by salary
    :param vacancy_list: list of Vacancy objects
    :return: None (modify vacancy_list param)
    """
    if not vacancy_list:
        print('Результаты поиска отсутствуют. Сначала произведите поиск\n')
        return

    sorted_vacancy_list = sorted(vacancy_list, key=lambda x: x.payment, reverse=True)
    vacancy_list.clear()
    vacancy_list.extend(sorted_vacancy_list)
    user_confirmation(messages['sort_msg'], show_vacancies_from_list, sorted_vacancy_list)


def user_confirmation(message, action, args):
    while True:
        print(f'{message}. Вывести результат? (y/n)\n')
        user_cmd = input().lower().strip()
        if user_cmd == 'y':
            action(args)
            return True
        elif user_cmd == 'n':
            return False
        else:
            print('Неизвестная команда')
            continue


def show_vacancies_from_list(vacancy_list: list):
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


def show_vacancies_from_file(*args):
    manager = JSONFileManager()
    vacancy_list = manager.get_vacancies_from_json_file()
    if not vacancy_list:
        print('Файл пустой\n')
    else:
        for count, vacancy in enumerate(vacancy_list):
            print(f"{count}  {vacancy['title']}  {vacancy['payment']}  {vacancy['url']}\n")


def del_vacancy_from_file(*args):
    manager = JSONFileManager()
    vacancy_list = manager.get_vacancies_from_json_file()
    if not vacancy_list:
        print('Файл пустой\n')
        return
    else:
        pos = int(input(f'Введите номер удаляемой вакансии\n').strip())
        try:
            manager.del_vacancy_from_json_file(pos)
            user_confirmation(messages['del_msg'], show_vacancies_from_file, None)
        except IndexError:
            print('Некорректный номер')

