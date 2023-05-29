import codecs
import json


class JSONSaver:
    pass

    def clear_json(self):
        with open("vacancy.json", "w") as f:
            json.dump([], f, indent=2, ensure_ascii=False)

    def add_vacancy(self, vacancy):
        self.clear_json()

        for item in vacancy['items']:
            text_json = {
                "name": item['name'],
                "url": item['url'],
                "salary": item['salary'],
                "conditions": item['snippet']['requirement']
            }

            with codecs.open('vacancy.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                data.append(text_json)

            with codecs.open('vacancy.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)


    def data_filter(self, filter_words):
        with codecs.open('vacancy.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            list_salary = []
            for v in data:
                if filter_words[0] in v['conditions']:
                    list_salary.append(v)

        return list_salary