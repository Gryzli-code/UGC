# UGC - сервис опросов
## Описание
UGC - это сервис для создания опросов для других пользователей с целью сбора статистики, а так же возможностью проходить опросы других пользователей.
### Возможности:
- создавать опрос
- изменять последовательность вопросов и ответов
- проходить опросы

# Setup

### Требования
- Python 3.11+
- poetry
- Docker

### Установка и запуск приложения без использования Docker

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/ugc.git
cd UGC
```

2. Установка зависимостей:
```bash
poetry install
```

3. В корне проекта где лежит manage.py создайте файл .env и внесите туда настройки подключения к БД
4. Примените миграции:
```bash
poetry run python manage.py migrate
```
5. Создайте суперпользователя
```bash
poetry run python manage.py createsuperuser
```

6. Запустите скрипт для генерации тестовых данных
```bash
poetry run python manage.py generate_data
```

7. Запустите сервер:
```bash
poetry run python manage.py runserver
```

Откройте http://localhost:8000 в браузере.


### Установка и запуск приложения c использования Docker

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/ugc.git
cd UGC
```

2. Соберите образ командой:
```bash
docker-compose build --no-cache
```

3. Запустите контейнер
```bash
docker-compose up -d
```

4. Создайте суперпользователя командой:
```bash
docker-compose exec web python manage.py createsuperuser
```

5. Сгенерируйте тестовые данные с помощью команды:
```bash
docker-compose exec web python manage.py generate_data
```

Откройте http://localhost:8000 в браузере.

# Использование
Для проверки работы эндпоинта необходимо перейти по адресу http://localhost:8000/admin и авторизироваться.

Для получения вопроса с ответами достаточно перейти по адресу http://localhost:8000/survey/{id_опроса}/{номер_вопроса}.

При попытки пройти по адресу для получения вопроса без авторизации получим ошибку 404 и перенаправление на старницу авторизации.

# Структура проекта

```
UGC/
    ├── UGC/ # Основное приложение проекта/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py # Файл настроки проекта Django
    │   ├── urls.py # Главные файл urls
    │   └── wsagi.py
    ├── main/ # Приложение для работы с опросами/
    │   ├── management/
    │   │   ├── commands/
    │   │   │   ├── __init__.py
    │   │   │   └── generate_data.py # файл для генерации тестовых данных
    │   │   └── __init__.py
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py # Регистрация моделей в админке
    │   ├── apps.py
    │   ├── models.py # Описание моделей связанных с опросами
    │   ├── tests.py
    │   ├── urls.py # urls для приложения main
    │   └── views.py # функции обработки приложения main
    ├── templates/ # шаблоны проекта
    │   ├── survey # шаблоны для приложения main
    │   │   └── question.html
    │   └── base.html
    ├── user/ # Приложения работы с пользователями
    ├── manage.py # файл для запуска проекта
    ├── poetry.lock
    └── poetry.toml # Зависимости
```
