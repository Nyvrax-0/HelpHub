# HelpHub: платформа для поиска волонтёров и помощи НКО

Сейчас готово (этапы 1–2 плана): проект, подключение к PostgreSQL, регистрация с выбором роли (волонтёр / НКО), вход, выход, админ-панель.

## Что нужно установить заранее
1. Python 3.12 или новее
2. PostgreSQL (на Windows: установщик с postgresql.org, запомни пароль для пользователя `postgres`)
3. Git

## Запуск по шагам

### 1. Создай базу данных
Открой терминал и зайди в PostgreSQL:

    psql -U postgres

Внутри выполни (пароль придумай свой и потом впиши его в `.env`):

    CREATE USER helphub WITH PASSWORD 'твой_пароль';
    CREATE DATABASE helphub OWNER helphub;
    \q

### 2. Подготовь проект

    cd helphub
    python -m venv venv

Включи виртуальное окружение:
- Windows: `venv\Scripts\activate`
- Mac / Linux: `source venv/bin/activate`

Дальше:

    pip install -r requirements.txt

### 3. Настрой .env
Скопируй `.env.example` в `.env` (Windows: `copy .env.example .env`, Mac/Linux: ) и открой его:`cp .env.example .env`
- `DB_PASSWORD` впиши тот же пароль, что создал в шаге 1
- `SECRET_KEY` сгенерируй командой:

      python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

- `TIME_ZONE` поставь свой, например `Europe/Moscow` (нужно для напоминаний)

### 4. Создай таблицы в базе
Важно: сначала `makemigrations accounts`, потому что у нас своя модель пользователя.

    python manage.py makemigrations accounts
    python manage.py migrate

### 5. Создай админа и запусти сайт

    python manage.py createsuperuser
    python manage.py runserver

Открой http://127.0.0.1:8000 — должна быть главная страница.

## Как проверить, что всё работает
1. Нажми «Регистрация», создай аккаунт волонтёра. Тебя должно сразу залогинить.
2. Нажми «Выйти», потом «Войти» с теми же данными.
3. Зайди на http://127.0.0.1:8000/admin (логин суперпользователя) → «Пользователи»: там твой аккаунт с ролью.
4. Проверь в базе: `psql -U helphub -d helphub` → `\dt` покажет таблицы, `SELECT username, role FROM accounts_user;` покажет пользователей.

## Что за файл что делает
| Файл / папка | Зачем |
|---|---|
| `manage.py` | команды проекта (запуск сервера, миграции) |
| `config/settings.py` | настройки: база PostgreSQL, язык, наша модель пользователя |
| `config/urls.py` | какие адреса есть на сайте |
| `accounts/models.py` | модель пользователя (роль, город, телефон) |
| `accounts/forms.py` | форма регистрации и входа |
| `accounts/views.py` | логика регистрации |
| `accounts/admin.py` | как пользователи выглядят в админ-панели |
| `templates/` | HTML-страницы (base.html это общий каркас) |
| `.env` | секреты (пароль БД). В GitHub НЕ попадает |

## Сохрани в GitHub

    git init
    git add .
    git commit -m "Начало проекта: Django + PostgreSQL, регистрация"

(Создай пустой репозиторий на github.com и выполни команды, которые он покажет.)

## Дальше
Этап 3 (23–29 ноября): задачи. Модель Task, форма создания для НКО, список задач.
