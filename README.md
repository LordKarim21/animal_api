# 🐈 Animal api

## Стек
Python, Django, DjangoRestFramework
## Функциональные возможности
API содержит четыре модели.

Животное (Animal). Поля: name, created_at, age, weight, height, omens


## Запуск проекта
На локальном компьютере должен быть установлен Python 3 или выше.

1. Склонировать данный репозиторий на свой локальный компьютер.
2. Установить виртуальное окружение используя команду `python3 -m venv venv`.
3. Установить необходимые библиотеки используя команду `pip install -r requirements.txt`.
4. Выполнить миграции командой `python manage.py migrate`.
5. Запустить локальный сервер командой `python manage.py runserver`.

## Доступные методы API
| Endpoint               | Методы                  | Описание                                                                             |
|------------------------|-------------------------|--------------------------------------------------------------------------------------|
| api/animal/            | GET, POST               | Администратор и приют, имеет права: получение списка/создание животных               |
| api/animal/            | GET                     | Гость, имеет право только на чтение                                                  |
| api/animal/{int:id}/   | GET, PUT, PATCH, DELETE | Администратор, имеет права: получение конкретного животного, его изменение, удаление |
| api/animal/{int:id}/   | GET, PUT, PATCH         | Приют, имеет права: создание, редактирование, чтение                                 |
| api/animal/{int:id}/   | GET                     | Гость, имеет право только на чтение                                                  |
                                    |
