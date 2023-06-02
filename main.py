from class_api.class_api import HeadHunterAPI, SuperJobAPI, Vacancy
from class_api.json_saver import JSONSaver
import pandas as pd

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()
json_saver = JSONSaver()


def user_interaction():
    """Функция приема параметров и получения вакансий"""
    #Очистка json файла
    json_saver.clear_json()

    # Взаимодействие с пользователем
    platforms = ["HeadHunter", "SuperJob"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().split()

    # Проход по всем платформам запросами
    for platform in platforms:
        if platform == "HeadHunter":
            hh_api.get_vacancies(search_query, top_n)
        else:
            superjob_api.get_vacancies(search_query, top_n)

    # Отбор и сохранение данных
    list_sort_vacancy = json_saver.data_filter(filter_words)
    save_excel(list_sort_vacancy)


def save_excel(list_sort_vacancy):
    try:
        df = pd.DataFrame(list_sort_vacancy)
        writer = pd.ExcelWriter('list_vacancies.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='vacancies', index=True)
        writer._save()
        print('Файл успешно сохранен')
    except Exception:
        print('Что-то пошло не так с сохранением Excel файла...')


if __name__ == "__main__":
    user_interaction()
