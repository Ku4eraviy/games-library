"""
Команда для наполнения БД тестовыми данными.
Запуск: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from games.models import Genre, Platform, Developer, Game


GENRES = [
    {'name': 'Экшен', 'slug': 'action', 'icon': '⚔️',
     'description': 'Игры с активным геймплеем, боевыми системами и динамикой'},
    {'name': 'РПГ', 'slug': 'rpg', 'icon': '🧙',
     'description': 'Ролевые игры с прокачкой персонажа и нелинейным сюжетом'},
    {'name': 'Стратегия', 'slug': 'strategy', 'icon': '♟️',
     'description': 'Тактические и стратегические игры'},
    {'name': 'Шутер', 'slug': 'shooter', 'icon': '🔫',
     'description': 'Игры от первого и третьего лица'},
    {'name': 'Приключения', 'slug': 'adventure', 'icon': '🗺️',
     'description': 'Исследование миров и решение головоломок'},
    {'name': 'Спорт', 'slug': 'sports', 'icon': '⚽',
     'description': 'Спортивные симуляторы'},
    {'name': 'Гонки', 'slug': 'racing', 'icon': '🏎️',
     'description': 'Гоночные симуляторы и аркады'},
    {'name': 'Инди', 'slug': 'indie', 'icon': '🌱',
     'description': 'Независимые авторские проекты'},
    {'name': 'Хоррор', 'slug': 'horror', 'icon': '👻',
     'description': 'Игры ужасов и выживания'},
    {'name': 'Файтинг', 'slug': 'fighting', 'icon': '🥊',
     'description': 'Боевые игры один на один'},
]

PLATFORMS = [
    {'name': 'PC (Windows)', 'short_name': 'PC'},
    {'name': 'PlayStation 5', 'short_name': 'PS5'},
    {'name': 'PlayStation 4', 'short_name': 'PS4'},
    {'name': 'Xbox Series X', 'short_name': 'XSX'},
    {'name': 'Xbox One', 'short_name': 'XBO'},
    {'name': 'Nintendo Switch', 'short_name': 'NSW'},
    {'name': 'macOS', 'short_name': 'Mac'},
    {'name': 'iOS', 'short_name': 'iOS'},
    {'name': 'Android', 'short_name': 'And'},
]

DEVELOPERS = [
    {'name': 'CD Projekt Red', 'country': 'Польша', 'founded_year': 1994},
    {'name': 'FromSoftware', 'country': 'Япония', 'founded_year': 1986},
    {'name': 'Rockstar Games', 'country': 'США', 'founded_year': 1998},
    {'name': 'Naughty Dog', 'country': 'США', 'founded_year': 1984},
    {'name': 'Nintendo EPD', 'country': 'Япония', 'founded_year': 2015},
    {'name': 'Valve Corporation', 'country': 'США', 'founded_year': 1996},
    {'name': 'Supergiant Games', 'country': 'США', 'founded_year': 2009},
    {'name': 'Insomniac Games', 'country': 'США', 'founded_year': 1994},
    {'name': 'Bethesda Game Studios', 'country': 'США', 'founded_year': 2001},
    {'name': 'Santa Monica Studio', 'country': 'США', 'founded_year': 1999},
]

GAMES = [
    {
        'title': 'The Witcher 3: Wild Hunt',
        'slug': 'witcher-3',
        'developer': 'CD Projekt Red',
        'genres': ['rpg', 'action', 'adventure'],
        'platforms': ['PC', 'PS5', 'PS4', 'XSX', 'XBO', 'NSW'],
        'release_year': 2015,
        'release_date': '2015-05-19',
        'age_rating': '18+',
        'metacritic_score': 93,
        'is_featured': True,
        'cover_url': 'https://image.api.playstation.com/vulcan/ap/rnd/202211/0711/kh4MQLEk8QME9GKcMRR5mRSF.png',
        'short_description': 'Эпическая ролевая игра в открытом мире с богатым нарративом и запоминающимися персонажами.',
        'description': 'The Witcher 3: Wild Hunt — это ролевая игра в открытом мире, действие которой происходит в визуально потрясающей фэнтезийной вселенной, наполненной значимыми выборами и последствиями.\n\nВы играете за Геральта из Ривии — профессионального охотника на монстров. Ищите свою пропавшую приёмную дочь Цири, скрывающуюся от могущественной группировки, известной как Дикая Охота.',
    },
    {
        'title': 'Elden Ring',
        'slug': 'elden-ring',
        'developer': 'FromSoftware',
        'genres': ['action', 'rpg'],
        'platforms': ['PC', 'PS5', 'PS4', 'XSX', 'XBO'],
        'release_year': 2022,
        'release_date': '2022-02-25',
        'age_rating': '16+',
        'metacritic_score': 96,
        'is_featured': True,
        'cover_url': 'https://image.api.playstation.com/vulcan/ap/rnd/202110/2000/phvVT0qZfcRms5qDAk0SI3CM.png',
        'short_description': 'Эпическое ролевое приключение в огромном тёмном фэнтезийном мире, созданном совместно с Джорджем Р. Р. Мартином.',
        'description': 'Elden Ring — это масштабная ролевая игра, разработанная FromSoftware совместно с Джорджем Р. Р. Мартином.\n\nОткройте для себя великолепный открытый мир — Земли Промеж, наполненный грозными врагами, скрытыми тайнами и запутанной историей. Создайте собственного персонажа и стройте уникальные билды.',
    },
    {
        'title': 'Red Dead Redemption 2',
        'slug': 'red-dead-redemption-2',
        'developer': 'Rockstar Games',
        'genres': ['action', 'adventure'],
        'platforms': ['PC', 'PS4', 'XBO'],
        'release_year': 2018,
        'release_date': '2018-10-26',
        'age_rating': '18+',
        'metacritic_score': 97,
        'is_featured': True,
        'cover_url': 'https://image.api.playstation.com/cdn/UP1004/CUSA03041_00/Hpl5MtwQgOVF9vJqlfui6SDB5Jl4oBSq.png',
        'short_description': 'Иммерсивный западный эпос об уходящей эпохе и цене лояльности.',
        'description': 'Америка, 1899 год. Эпоха дикого запада подходит к концу. Артур Морган и банда Ван дер Линде вынуждены скрываться после неудачного ограбления в городке Блэкуотер.\n\nОткрытый мир с невероятной детализацией, живыми экосистемами и глубокой системой чести.',
    },
    {
        'title': 'The Last of Us Part I',
        'slug': 'the-last-of-us-part-1',
        'developer': 'Naughty Dog',
        'genres': ['action', 'adventure', 'horror'],
        'platforms': ['PC', 'PS5'],
        'release_year': 2022,
        'release_date': '2022-09-02',
        'age_rating': '18+',
        'metacritic_score': 89,
        'is_featured': True,
        'cover_url': 'https://image.api.playstation.com/vulcan/ap/rnd/202206/0720/eEczyEMDd2BLa3dtkGJVE9Id.png',
        'short_description': 'Переосмысление культовой постапокалиптической истории о выживании и человечности.',
        'description': 'История о выживании в постапокалиптическом мире, захваченном грибковой инфекцией. Джоэл и Элли вынуждены пересечь разрушенную Америку.\n\nРемастер с полностью переработанной графикой, геймплеем и анимациями на движке The Last of Us Part II.',
    },
    {
        'title': 'The Legend of Zelda: Tears of the Kingdom',
        'slug': 'zelda-totk',
        'developer': 'Nintendo EPD',
        'genres': ['action', 'adventure', 'rpg'],
        'platforms': ['NSW'],
        'release_year': 2023,
        'release_date': '2023-05-12',
        'age_rating': '12+',
        'metacritic_score': 96,
        'is_featured': True,
        'cover_url': 'https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/en_US/games/switch/t/the-legend-of-zelda-tears-of-the-kingdom-switch/hero',
        'short_description': 'Сиквел Breath of the Wild с новыми островами в небесах и революционными механиками строительства.',
        'description': 'Линк исследует не только знакомую Хайрул, но и парящие острова в небе, и мрачные глубины под землёй.\n\nНовые силы — Ультрарука, Соединение, Возврат и Скольжение — открывают бесчисленные возможности для решения головоломок и создания механизмов.',
    },
    {
        'title': 'Half-Life: Alyx',
        'slug': 'half-life-alyx',
        'developer': 'Valve Corporation',
        'genres': ['shooter', 'adventure', 'horror'],
        'platforms': ['PC'],
        'release_year': 2020,
        'release_date': '2020-03-23',
        'age_rating': '16+',
        'metacritic_score': 93,
        'is_featured': False,
        'cover_url': 'https://cdn.akamai.steamstatic.com/steam/apps/546560/library_600x900.jpg',
        'short_description': 'Возвращение в Half-Life вселенную через VR — переломный момент в истории виртуальной реальности.',
        'description': 'Half-Life: Alyx — VR-приключение, действие которого происходит между событиями Half-Life и Half-Life 2.\n\nАликс Вэнс ведёт борьбу людей против Альянса. Игра переизобрела возможности VR, показав, каким может быть полноценный VR-проект AAA-класса.',
    },
    {
        'title': 'Hades',
        'slug': 'hades',
        'developer': 'Supergiant Games',
        'genres': ['action', 'rpg', 'indie'],
        'platforms': ['PC', 'NSW', 'PS5', 'PS4', 'XSX', 'XBO'],
        'release_year': 2020,
        'release_date': '2020-09-17',
        'age_rating': '12+',
        'metacritic_score': 93,
        'is_featured': False,
        'cover_url': 'https://image.api.playstation.com/vulcan/ap/rnd/202012/1618/TgtpOqBzLLBYjPXgZEnmGXyI.png',
        'short_description': 'Roguelike-экшен о сыне бога подземного царства, пытающемся сбежать из Аида.',
        'description': 'Hades — это roguelike от создателей Bastion, Transistor и Pyre. Вы играете за Загрея, сына Аида, вырывающегося из подземного царства.\n\nКаждый забег уникален. Благодаря нелинейному повествованию история развивается при каждом прохождении.',
    },
    {
        'title': 'Marvel\'s Spider-Man 2',
        'slug': 'spiderman-2',
        'developer': 'Insomniac Games',
        'genres': ['action', 'adventure'],
        'platforms': ['PS5'],
        'release_year': 2023,
        'release_date': '2023-10-20',
        'age_rating': '16+',
        'metacritic_score': 90,
        'is_featured': False,
        'cover_url': 'https://image.api.playstation.com/vulcan/ap/rnd/202306/1219/1c7b75d8ed9271516546560f219ad0f9d2a0e09b45e8fba3.png',
        'short_description': 'Питер Паркер и Майлз Моралес вместе против нового угрозы — Венома.',
        'description': 'Продолжение цикла Insomniac про Человека-Паука. Питер Паркер и Майлз Моралес объединяются против угрозы симбиота.\n\nНовые костюмы, способности, расширенный Нью-Йорк и захватывающий сюжет о цене силы.',
    },
    {
        'title': 'Starfield',
        'slug': 'starfield',
        'developer': 'Bethesda Game Studios',
        'genres': ['rpg', 'action', 'adventure'],
        'platforms': ['PC', 'XSX'],
        'release_year': 2023,
        'release_date': '2023-09-06',
        'age_rating': '16+',
        'metacritic_score': 83,
        'is_featured': False,
        'cover_url': 'https://upload.wikimedia.org/wikipedia/en/2/24/Starfield_game_cover.jpg',
        'short_description': 'Первая новая вселенная Bethesda за 25 лет — масштабная космическая RPG.',
        'description': 'В 2330 году человечество вышло за пределы Солнечной системы. Вы — исследователь организации Созвездие, которая ищет ответы на главный вопрос: одни ли мы во вселенной?\n\nОткройте сотни планет, стройте корабли и создавайте уникальных персонажей.',
    },
    {
        'title': 'God of War Ragnarök',
        'slug': 'gow-ragnarok',
        'developer': 'Santa Monica Studio',
        'genres': ['action', 'adventure', 'rpg'],
        'platforms': ['PS5', 'PS4'],
        'release_year': 2022,
        'release_date': '2022-11-09',
        'age_rating': '18+',
        'metacritic_score': 94,
        'is_featured': False,
        'cover_url': 'https://image.api.playstation.com/vulcan/ap/rnd/202207/1210/4xJ8XB3bi888QTLZYdl7Oi0s.png',
        'short_description': 'Кратос и Атрей встречают Рагнарёк — история о семье, судьбе и богах Скандинавии.',
        'description': 'Продолжение God of War 2018 года. Кратос и Атрей путешествуют по Девяти Мирам, сталкиваясь с норвежскими богами и надвигающимся Рагнарёком.\n\nГлубокая боевая система, эмоциональный нарратив и невероятные декорации делают игру одним из лучших эксклюзивов PlayStation.',
    },
]


class Command(BaseCommand):
    help = 'Заполнить базу данных тестовыми играми и жанрами'

    def handle(self, *args, **kwargs):
        self.stdout.write('🎮 Начинаем заполнение базы данных...\n')

        # Жанры
        genre_map = {}
        for g in GENRES:
            obj, created = Genre.objects.get_or_create(
                slug=g['slug'],
                defaults={
                    'name': g['name'],
                    'icon': g['icon'],
                    'description': g['description'],
                }
            )
            genre_map[g['slug']] = obj
            status = '✓ создан' if created else '· уже есть'
            self.stdout.write(f'  Жанр {g["icon"]} {g["name"]}: {status}')

        self.stdout.write('')

        # Платформы
        platform_map = {}
        for p in PLATFORMS:
            obj, created = Platform.objects.get_or_create(
                name=p['name'],
                defaults={'short_name': p['short_name']}
            )
            platform_map[p['short_name']] = obj
            status = '✓ создана' if created else '· уже есть'
            self.stdout.write(f'  Платформа {p["short_name"]}: {status}')

        self.stdout.write('')

        # Разработчики
        dev_map = {}
        for d in DEVELOPERS:
            obj, created = Developer.objects.get_or_create(
                name=d['name'],
                defaults={
                    'country': d['country'],
                    'founded_year': d['founded_year'],
                }
            )
            dev_map[d['name']] = obj
            status = '✓ создан' if created else '· уже есть'
            self.stdout.write(f'  Разработчик {d["name"]}: {status}')

        self.stdout.write('')

        # Игры
        for g in GAMES:
            game, created = Game.objects.get_or_create(
                slug=g['slug'],
                defaults={
                    'title': g['title'],
                    'developer': dev_map.get(g['developer']),
                    'release_year': g['release_year'],
                    'release_date': g['release_date'],
                    'age_rating': g['age_rating'],
                    'metacritic_score': g['metacritic_score'],
                    'is_featured': g['is_featured'],
                    'cover_url': g.get('cover_url', ''),
                    'short_description': g.get('short_description', ''),
                    'description': g.get('description', ''),
                }
            )
            if created:
                # Жанры
                for genre_slug in g['genres']:
                    if genre_slug in genre_map:
                        game.genres.add(genre_map[genre_slug])
                # Платформы
                for platform_short in g['platforms']:
                    if platform_short in platform_map:
                        game.platforms.add(platform_map[platform_short])
                self.stdout.write(f'  ✓ Игра: {g["title"]}')
            else:
                self.stdout.write(f'  · Уже есть: {g["title"]}')

        self.stdout.write('\n✅ Готово! База данных заполнена.\n')
        self.stdout.write('Теперь создайте суперпользователя:')
        self.stdout.write('  python manage.py createsuperuser\n')
