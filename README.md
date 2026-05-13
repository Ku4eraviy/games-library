# 🎮 GameLib — Библиотека игр

Персональная библиотека видеоигр на Django + PostgreSQL + Tailwind CSS.

## Структура БД

| Таблица | Описание |
|---------|----------|
| `users_customuser` | Пользователи (расширение AbstractUser) |
| `games_genre` | Жанры игр |
| `games_platform` | Игровые платформы |
| `games_developer` | Разработчики |
| `games_game` | Основная таблица игр |
| `games_game_genres` | M2M: игры ↔ жанры |
| `games_game_platforms` | M2M: игры ↔ платформы |
| `games_favoritegame` | Избранные игры пользователя |
| `games_gamescreenshot` | Скриншоты игр |

## Связи

```
Genre ←M2M→ Game ←FK→ Developer
Platform ←M2M→ Game
Game ←FK→ GameScreenshot
CustomUser ←FK→ FavoriteGame ←FK→ Game
```

## Быстрый старт

### 1. Создать виртуальное окружение
```bash
cd gamelib
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2. Установить зависимости
```bash
pip install -r requirements.txt
```

### 3. Настроить PostgreSQL
```sql
CREATE DATABASE gamelib_db;
CREATE USER gamelib_user WITH PASSWORD 'gamelib_password';
GRANT ALL PRIVILEGES ON DATABASE gamelib_db TO gamelib_user;
```

Или через переменные окружения:
```bash
export DB_NAME=gamelib_db
export DB_USER=gamelib_user
export DB_PASSWORD=gamelib_password
export DB_HOST=localhost
export DB_PORT=5432
```

### 4. Применить миграции
```bash
python manage.py migrate
```

### 5. Создать суперпользователя
```bash
python manage.py createsuperuser
```

### 6. Заполнить тестовыми данными
```bash
python manage.py seed_data
```

### 7. Запустить сервер
```bash
python manage.py runserver
```

Открыть в браузере: http://127.0.0.1:8000

Админ-панель: http://127.0.0.1:8000/admin/

## Функциональность

- 📋 **Каталог игр** — карточки с обложками, жанрами, годом
- 🔍 **Поиск** — по названию, описанию, разработчику
- 🎛️ **Фильтры** — жанр, платформа, год выпуска
- 📊 **Сортировка** — по дате, названию, рейтингу
- 📄 **Страница игры** — подробная карточка, похожие игры
- ❤️ **Избранное** — добавление/удаление через AJAX
- 👤 **Авторизация** — регистрация, вход, выход
- 🔧 **Админ-панель** — полное управление всеми данными

## Структура шаблонов

```
templates/
├── base.html                    # Базовый шаблон
├── partials/
│   ├── header.html              # Навигация
│   └── footer.html              # Подвал
├── components/
│   ├── game_card.html           # Карточка игры
│   ├── filters.html             # Панель фильтров
│   └── pagination.html          # Пагинация
├── pages/
│   ├── game_list.html           # Список игр
│   ├── game_detail.html         # Карточка игры
│   └── favorites.html           # Избранное
└── registration/
    ├── login.html               # Вход
    └── register.html            # Регистрация
```
