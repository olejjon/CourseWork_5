import json


class JSONSaver:
    pass

    def add_vacancy(self, vacancy):
        text_json = {
            "title": vacancy.title,
            "url": vacancy.url,
            "salary": vacancy.salary,
            "conditions": vacancy.conditions
        }

        data = json.load(open("vacancy.json"))
        data.append(text_json)
        with open('vacancy.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


    def get_vacancies_by_salary(self, salary):
        with open('vacancy.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            list_salary = []
            for v in data:
                if v['salary'] == salary:
                    list_salary.append(v)

        return list_salary

    def delete_vacancy(self, vacancy):
        with open('vacancy.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for v in data:
                if v['url'] == vacancy.url:
                    data.remove(v)

        with open('vacancy.json', "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)