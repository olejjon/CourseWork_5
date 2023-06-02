import json
from abc import ABC, abstractmethod
import requests

from constants import superjob_token


class JobAPI(ABC):
    pass


class SuperJobAPI(JobAPI):
    pass

    def get_vacancies(self, name_profession, top_n):
        """Получается данные по запросу на superjob с параметрами"""

        url = "https://api.superjob.ru/2.0/vacancies/"
        list_vacancy = []

        headers = {"X-Api-App-Id": superjob_token}

        params = {
            'keyword': name_profession,
            # 'profession': f'NAME:{name_profession}',
            'count': top_n,
            'page': 1
        }

        res = requests.get(url, headers=headers, params=params)  # Посылаем запрос к API
        if res.status_code == 200:
            data = res.json()
            for item in data['objects']:
                vacancy = Vacancy(item['profession'], item['link'], item['payment_from'], item['candidat'])

                text_json = {
                    'name': vacancy.name,
                    'url': vacancy.url,
                    'salary': vacancy.salary,
                    'conditions': vacancy.conditions
                }

                with open('vacancy.json', 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    data.append(text_json)

            with open('vacancy.json', 'w') as outfile:
                json.dump(data, outfile, indent=2, ensure_ascii=False)

        else:
            return "Error:", res.status_code


class HeadHunterAPI(JobAPI):
    pass

    def get_vacancies(self, name_profession, quantity_per_page):
        """Получается данные по запросу на hh с параметрами"""

        params = {
            'text': f'NAME:{name_profession}',
            'page': 1,
            'per_page': quantity_per_page  # Кол-во вакансий на 1 странице
        }

        list_vacancy = []
        res = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        if res.status_code == 200:
            data = res.json()
            for item in data['items']:
                vacancy = Vacancy(item['name'], item['url'], item['salary'], item['snippet']['requirement'])

                text_json = {
                    'name': vacancy.name,
                    'url': vacancy.url,
                    'salary': vacancy.salary,
                    'conditions': vacancy.conditions
                }

                list_vacancy.append(text_json)

            # return list_vacancy
            with open('vacancy.json', 'w', encoding='utf-8') as outfile:
                json.dump(list_vacancy, outfile, indent=2, ensure_ascii=False)

        else:
            return "Error:", res.status_code


class Vacancy(JobAPI):  # пока не понимаю, где можно использовать???
    """Класс вакансии"""

    def __init__(self, name, url, salary, conditions):
        self.name = name
        self.url = url
        self.salary = salary
        self.conditions = conditions.lower()
