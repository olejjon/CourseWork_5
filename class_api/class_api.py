import json
from abc import ABC, abstractmethod
import requests


class JobAPI(ABC):
    pass


class SuperJobAPI(JobAPI):
    pass

    def get_vacancies(self, profession):
        params = {
            "text": f'NAME:{profession}'
        }
        # req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        # data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        # req.close()
        return params


class HeadHunterAPI(JobAPI):
    pass

    def get_vacancies(self, profession):
        params = {
            'text': f'NAME:{profession}',
            'per_page': 100
        }
        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()
        return data


class Vacancy(JobAPI):
    def __init__(self, title, url, salary, conditions):
        # "Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет..."
        self.title = title
        self.url = url
        self.salary = salary
        self.conditions = conditions


