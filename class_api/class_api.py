import json
from abc import ABC, abstractmethod
import requests

from constants import superjob_token


class JobAPI(ABC):
    pass


class SuperJobAPI(JobAPI):
    pass



    def get_vacancies(self, profession):
        url = "https://api.superjob.ru/2.0/vacancies/"

        headers = {
            "X-Api-App-Id": superjob_token
        }

        payload = {
            'keyword': f'{profession}',
            'published': 1
        }
        res = requests.get(url, headers=headers, params=payload)  # Посылаем запрос к API
        data = res.json()
        return data


class HeadHunterAPI(JobAPI):
    pass

    def get_vacancies(self, profession):
        params = {
            'text': f'NAME:{profession}',
            'per_page': 3
        }
        res = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = res.json()
        return data


class Vacancy(JobAPI):
    def __init__(self, name, url, salary, conditions):
        self.name = name
        self.url = url
        self.salary = salary
        self.conditions = conditions


