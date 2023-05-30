from class_api.class_api import HeadHunterAPI, SuperJobAPI, Vacancy
from class_api.json_saver import JSONSaver
import pandas as pd

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()
json_saver = JSONSaver()

# Функция для взаимодействия с пользователем
def filter_vacancies(hh_vacancies, superjob_vacancies, filter_words):
    json_saver = JSONSaver()
    json_saver.add_vacancy_hh(hh_vacancies)
    json_saver.add_vacancy_superjob(superjob_vacancies)
    list_sort_vacancy = json_saver.data_filter(filter_words)

    try:
        df = pd.DataFrame(list_sort_vacancy)
        writer = pd.ExcelWriter('list_vacancies.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='vacancies', index=True)
        writer._save()
        print('Файл успешно сохранен')
    except Exception:
        print('Что-то пошло не так...')


def user_interaction():
    platforms = ["HeadHunter", "SuperJob"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    hh_vacancies = hh_api.get_vacancies(search_query, top_n)
    superjob_vacancies = superjob_api.get_vacancies(search_query, top_n)

    filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)


if __name__ == "__main__":
    user_interaction()
