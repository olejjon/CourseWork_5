import json
from abc import ABC, abstractmethod
import requests

from constants import superjob_token


class JobAPI(ABC):
    pass

class SuperJobAPI(JobAPI):
    pass

    def get_vacancies(self, name_profession, top_n):
        url = "https://api.superjob.ru/2.0/vacancies/"
        list_vacancy = []

        headers = {
            "X-Api-App-Id": superjob_token
        }

        params = {
            'profession': name_profession,
            'published': 1,
            'not_archive': True
        }

        res = requests.get(url, headers=headers, params=params)  # Посылаем запрос к API
        data = res.json()
        for vacancy in data['objects'][:top_n]:
            list_vacancy.append(vacancy)

        return list_vacancy



class HeadHunterAPI(JobAPI):
    pass

    def get_vacancies(self, name_profession, quantity_per_page):
        params = {
            'text': f'NAME:{name_profession}',
            'page': 1,
            'per_page': quantity_per_page  # Кол-во вакансий на 1 странице
        }

        list_vacancy = []
        res = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = res.json()
        for vacancy in data['items']:
            list_vacancy.append(vacancy)

        return list_vacancy


class Vacancy(JobAPI):  # пока не понимаю, где можно использовать???
    def __init__(self, name, url, salary, conditions):
        self.name = name
        self.url = url
        self.salary = salary
        self.conditions = conditions
