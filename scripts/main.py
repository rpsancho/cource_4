from src.utils import search_vacancies, filter_vacancies, sort_vacancies, add_vacancy_to_file


def main():

    vacancy_list = []

    while True:
        print("1 - поиск вакансий\n"
              "2 - фильтрация по ключевому слову\n"
              "3 - сортировка по зарплате\n"
              "4 - сохранение в файл\n"
              "5 - выход")

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
            return
        else:
            print('Неизвестная команда\n')


if __name__ == '__main__':
    main()
