REST API социальной сети YaTube (Яндекс.Практикум)
=====

Описание проекта
----------
Проект создан в рамках учебного курса Яндекс.Практикум.

API сервис для [проекта социальной сети Yatube](https://github.com/StAndUP-ru/api_yatube).

Реализован REST API CRUD для основных моделей проекта, для аутентификации примненяются JWT-токены.
В проекте реализованы пермишены, фильтрации, сортировки и поиск по запросам клиентов, реализована пагинация ответов от API, установлено ограничение количества запросов к API.

Системные требования
----------
* Python 3.8+
* Works on Linux, macOS, Windows

Стек технологий
----------
* Python 3.8
* Django 2.2
* Django Rest Framework
* Pytest
* Simple-JWT
* SQLite3

Установка проекта из репозитория (Linux и macOS)
----------

1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/StAndUP-ru/api_yatube.git

cd api_final_yatube-1
```
2. Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv env

source env/bin/activate
```
3. Установить зависимости из файла ```requirements.txt```:
```bash
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```
4. Выполнить миграции:
```bash
cd yatube_api

python3 manage.py migrate
```
5. Создать суперпользователя:
```bash
python3 manage.py createsuperuser
```
6. Запустить проект (в режиме сервера Django):
```bash
python3 manage.py runserver
```

Установка проекта из репозитория (Windows)
----------

1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/StAndUP-ru/api_yatube.git

cd api_final_yatube-1
```
2. Cоздать и активировать виртуальное окружение:
```bash
python -m venv env

source venv/Scripts/activate
```
3. Установить зависимости из файла ```requirements.txt```:
```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```
4. Выполнить миграции:
```bash
cd yatube_api

python manage.py migrate
```
5. Создать суперпользователя:
```bash
python manage.py createsuperuser
```
6. Запустить проект (в режиме сервера Django):
```bash
python manage.py runserver
```

Создание токена аутентификации через браузер
----------
* http://127.0.0.1:8000/api/v1/jwt/create/


Тестовые запросы к API
----------
* Получить список постов - http://127.0.0.1:8000/api/v1/posts/
* Получить список сообществ - http://127.0.0.1:8000/api/v1/groups/

Документация к проекту
----------
Документация для API после установки доступна по адресу ```/redoc/```.
