# Курсовой проект по курсу "Работа с базами данных" 
### Задача

В рамках проекта вам необходимо получить данные о компаниях и вакансиях с сайта hh.ru, 
спроектировать таблицы в БД PostgreSQL и загрузить полученные данные в созданные таблицы. с условиями: 
- [+]  Проект выложен на GitHub.
- [+]  Оформлен файл README.md с информацией о чем проект, как его запустить и как с ним работать.
- [+]  Есть Python-модуль для создания и заполнения данными таблиц БД.
- [+]  SQL-запросы для портала хранятся в файле queries.sql.


### Установка
##### Загрузить репозиторий

##### Установить зависимости (pip install -r requirements.txt)

##### Прописать данные для подключения к БД (файл database.ini)

### Как это работает
Программа выполняет GET запросы к HEAD HUNTER 

По умолчанию, список компаний: ["МТС", "Мегафон", "Билайн", "Теле2", "Yandex", "Google", "Газпром", "Роснефть"]

Пользователь имеет возможность указать компанию для получения данных
