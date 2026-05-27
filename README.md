# GameLib — библиотека игр

Сайт-каталог видеоигр: Django + PostgreSQL + Tailwind CSS.

---

## Что нужно на компьютере

1. **Python 3.10+** — [python.org/downloads](https://www.python.org/downloads/)  
   При установке отметьте «Add Python to PATH».

2. **PostgreSQL** — [postgresql.org/download](https://www.postgresql.org/download/)  
   Запомните пароль пользователя `postgres` (ниже в примере — `admin`).

3. **Git** (чтобы скачать проект) — [git-scm.com](https://git-scm.com/)

---

## Запуск с нуля (Windows)

Откройте **PowerShell** и выполняйте команды **по порядку**.

### 1. Скачать проект и зайти в папку

```powershell
cd C:\Users\Student\IS3\AFANASEV\ku4eryaviy\gamelib
```

*(Путь замените на свой, если проект лежит в другом месте.)*

### 2. Создать базу данных PostgreSQL

Откройте **pgAdmin** или **SQL Shell (psql)** и выполните:

```sql
CREATE DATABASE gamelib_db;
```

Пароль и логин по умолчанию в проекте:

| Параметр | Значение |
|----------|----------|
| База     | `gamelib_db` |
| Пользователь | `postgres` |
| Пароль   | `admin` |
| Хост     | `localhost` |
| Порт     | `5432` |

Если у вас другой пароль — измените его в файле `config/settings.py` (блок `DATABASES`).

### 3. Виртуальное окружение и пакеты

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

После `activate` в начале строки появится `(venv)`.

> Используйте **только** папку `venv`. Не создавайте вторую `.venv` — будет путаница.

**Или одной командой** (миграции + игры в БД):

```powershell
.\setup.ps1
venv\Scripts\activate
```

### 4. Таблицы в базе

```powershell
python manage.py migrate
```

### 5. Заполнить БД играми (обязательно)

```powershell
python manage.py seed_data
```

Команда создаёт:
- 10 жанров, платформы, разработчиков;
- **~50 игр** с нормальными описаниями на русском;
- обложки со Steam / PlayStation CDN.

Повторный запуск **обновит** описания и обложки, не сломает сайт.

Обновить только обложки:

```powershell
python manage.py update_covers
```

### 6. Админка (один раз)

```powershell
python manage.py createsuperuser
```

Введите логин, email (можно пустой) и пароль.

### 7. Запуск сервера

```powershell
python manage.py runserver
```

| Адрес | Что там |
|-------|---------|
| http://127.0.0.1:8000/ | Сайт с каталогом игр |
| http://127.0.0.1:8000/admin/ | Админ-панель |

Остановить сервер: **Ctrl+C**.

---

## Краткая шпаргалка (каждый день)

```powershell
cd C:\Users\Student\IS3\AFANASEV\ku4eryaviy\gamelib
venv\Scripts\activate
python manage.py runserver
```

---

## Linux / macOS

```bash
cd gamelib
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser
python manage.py runserver
```

---

## Частые проблемы

**`ModuleNotFoundError: image_uploader_widget`**  
Не активировано окружение или не установлены пакеты:
```powershell
venv\Scripts\activate
pip install -r requirements.txt
```

**Ошибка подключения к PostgreSQL**  
- PostgreSQL запущен? (служба в Windows)  
- База `gamelib_db` создана?  
- Пароль в `config/settings.py` совпадает с вашим?

**На сайте нет игр**  
```powershell
python manage.py seed_data
```

**Коты / странные обложки**  
```powershell
python manage.py update_covers
python manage.py seed_data
```

---

## Что умеет сайт

- Каталог игр с обложками, жанрами, годом
- Поиск и фильтры (жанр, платформа, год)
- Страница игры, похожие игры
- Избранное (нужна регистрация)
- Регистрация / вход
- Админ-панель с загрузкой картинок и autoslug

---

## Структура проекта

```
gamelib/
├── config/          # настройки Django
├── games/           # игры, жанры, сиды
├── users/           # пользователи
├── templates/       # HTML-шаблоны
├── manage.py
├── requirements.txt
├── setup.ps1        # быстрая установка (Windows)
└── venv/            # виртуальное окружение (не в git)
```

---

## Полезные команды

```powershell
python manage.py seed_data       # игры + описания в БД
python manage.py update_covers   # только обложки
python manage.py migrate         # применить миграции
python manage.py createsuperuser # создать админа
python manage.py runserver       # запустить сайт
```
