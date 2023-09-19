from src.utils import *


def main():

    vacancy_list = []

    while True:
        show_menu(main_menu)

        user_cmd = input().strip()

        if user_cmd == '1':
            search_vacancies(vacancy_list)
        elif user_cmd == '2':
            filter_vacancies(vacancy_list)
        elif user_cmd == '3':
            sort_vacancies(vacancy_list)
        elif user_cmd == '4':
            add_vacancy_to_file(vacancy_list)
        elif user_cmd == '5':
            show_vacancies_from_file()
        elif user_cmd == '6':
            del_vacancy_from_file()
        elif user_cmd == '7':
            return
        else:
            print('Неизвестная команда\n')


if __name__ == '__main__':
    main()
