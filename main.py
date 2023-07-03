from class_api.RequestManager import RequestManager
from class_api.DBManager import DBManager
from class_api.utils import config

# Создание экземпляра класса для работы с API сайтов с вакансиями
request_data = RequestManager()


def main():
    """Функция приема параметров и получения вакансий"""
    connection_params = config()

    connector_to_db = DBManager(connection_params, "vacancies")

    while True:
        user_answer_hh = input("1. Стандартный запрос по компаниям. \n"
                               "2. Произвольный запрос.\n"
                               "3. Без запроса в БД.\n")

        # Request to HEAD HUNTER
        if user_answer_hh == "1":
            all_companies = ["МТС", "Мегафон", "Билайн", "Теле2", "Yandex", "Google", "Газпром", "Роснефть"]
            for company in all_companies:
                print(f"Обрабатываем {company}.")
                request_data.get_request(company)
            companies_data, vacancies_data = request_data.companies_data, request_data.vacancies_data
            connector_to_db.insert_data("companies", companies_data)
            connector_to_db.insert_data("vacancies", vacancies_data)
            break
        elif user_answer_hh == "2":
            user_query = input("Введите название компании.\n")
            request_data.get_request(user_query)
            companies_data, vacancies_data = request_data.companies_data, request_data.vacancies_data
            connector_to_db.insert_data("companies", companies_data)
            connector_to_db.insert_data("vacancies", vacancies_data)
            break
        elif user_answer_hh == "3":
            break
        else:
            print("Некорректный запрос.\n")


    while True:
        print()
        user_answer = input("1.Получить список всех компаний и количество вакансий у каждой компании.\n"
                            "2.Получить список всех вакансий с информацией о них.\n"
                            "3.Получить среднюю зарплату по вакансиям в разрезе компаний.\n"
                            "4.Получить список всех вакансий, у которых зарплата выше средней.\n"
                            "5.Получить список всех вакансий, в названии которых содержатся переданные слова.\n"
                            "6.Завершить обработку.\n")

        # End processing
        if user_answer == "6":
            break

        # Get_companies_and_vacancies
        elif user_answer == "1":
            connector_to_db.get_companies_and_vacancies_count()
            input("Для продолжения нажмите Enter...")

        # Get_all_vacancies
        elif user_answer == "2":
            connector_to_db.get_all_vacancies()
            input("Для продолжения нажмите Enter...\n")

        # Get_avg_salary_by_company
        elif user_answer == "3":
            input("Расчет идет по 'Зарплата от'. Если данных нет, то результат не включен в выборку.\n"
                  "Для продолжения нажмите Enter...\n")
            connector_to_db.get_avg_salary()
            input("Для продолжения нажмите Enter...\n")

        # Get_vacancies_with_higher_salary
        elif user_answer == "4":
            connector_to_db.get_vacancies_with_higher_salary()
            input("Для продолжения нажмите Enter...\n")

        # Get_vacancies_with_keyword
        elif user_answer == "5":
            user_keyword = input("Введите слово для поиска.\n")
            connector_to_db.get_vacancies_with_keyword(user_keyword)
            input("Для продолжения нажмите Enter...\n")

        else:
            print("Некорректный запрос.\n")


if __name__ == "__main__":
    main()
