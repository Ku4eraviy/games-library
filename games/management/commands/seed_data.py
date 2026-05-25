"""
Команда для наполнения БД тестовыми данными.
Запуск: python manage.py seed_data
       python manage.py seed_data --extra 20
"""
import random
from datetime import date

from django.core.management.base import BaseCommand
from faker import Faker

from games.cover_urls import get_cover_url
from games.models import Genre, Platform, Developer, Game

fake = Faker('ru_RU')

GENRES = [
    {'name': 'Экшен', 'slug': 'action', 'icon': '⚔️'},
    {'name': 'РПГ', 'slug': 'rpg', 'icon': '🧙'},
    {'name': 'Стратегия', 'slug': 'strategy', 'icon': '♟️'},
    {'name': 'Шутер', 'slug': 'shooter', 'icon': '🔫'},
    {'name': 'Приключения', 'slug': 'adventure', 'icon': '🗺️'},
    {'name': 'Спорт', 'slug': 'sports', 'icon': '⚽'},
    {'name': 'Гонки', 'slug': 'racing', 'icon': '🏎️'},
    {'name': 'Инди', 'slug': 'indie', 'icon': '🌱'},
    {'name': 'Хоррор', 'slug': 'horror', 'icon': '👻'},
    {'name': 'Файтинг', 'slug': 'fighting', 'icon': '🥊'},
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

# Названия из подготовленного списка (ключевые хиты)
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
    },
]

# Дополнительные названия для массового наполнения (описания — через Faker)
EXTRA_GAME_TITLES = [
    'Metro Exodus', 'Сталкер 2: Сердце Чернобыля', 'Baldur\'s Gate 3',
    'Cyberpunk 2077', 'Horizon Forbidden West', 'Ghost of Tsushima',
    'Sekiro: Shadows Die Twice', 'Dark Souls III', 'Bloodborne',
    'Resident Evil 4', 'Dead Space', 'Alan Wake 2',
    'Control', 'Disco Elysium', 'Persona 5 Royal',
    'Final Fantasy XVI', 'Monster Hunter Rise', 'Doom Eternal',
    'Forza Horizon 5', 'Gran Turismo 7', 'FIFA 24',
    'NBA 2K24', 'Street Fighter 6', 'Tekken 8',
    'Civilization VI', 'Total War: Warhammer III', 'Crusader Kings III',
    'Stardew Valley', 'Hollow Knight', 'Celeste',
    'Undertale', 'Portal 2', 'Half-Life 2',
    'BioShock Infinite', 'Mass Effect Legendary Edition',
    'Dragon Age: Inquisition', 'Fallout 4', 'Skyrim',
    'Assassin\'s Creed Valhalla', 'Far Cry 6', 'Watch Dogs: Legion',
]

AGE_RATINGS = ['0+', '6+', '12+', '16+', '18+']


class Command(BaseCommand):
    help = 'Заполнить базу данных тестовыми играми и жанрами (Faker + подготовленные списки)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--extra',
            type=int,
            default=15,
            help='Сколько дополнительных игр сгенерировать из списка названий (по умолчанию 15)',
        )

    def handle(self, *args, **kwargs):
        extra_count = kwargs['extra']
        self.stdout.write('🎮 Начинаем заполнение базы данных...\n')

        genre_map = self._seed_genres()
        self.stdout.write('')
        platform_map = self._seed_platforms()
        self.stdout.write('')
        dev_map = self._seed_developers()
        self.stdout.write('')
        self._seed_featured_games(genre_map, platform_map, dev_map)
        self.stdout.write('')
        created_extra = self._seed_extra_games(
            extra_count, genre_map, platform_map, dev_map
        )
        self.stdout.write(f'\n  Дополнительно сгенерировано игр: {created_extra}')
        self._apply_covers()
        self.stdout.write('\n✅ Готово! База данных заполнена.\n')
        self.stdout.write('Теперь создайте суперпользователя:')
        self.stdout.write('  python manage.py createsuperuser\n')

    def _seed_genres(self):
        genre_map = {}
        for g in GENRES:
            obj, created = Genre.objects.get_or_create(
                slug=g['slug'],
                defaults={
                    'name': g['name'],
                    'icon': g['icon'],
                    'description': fake.text(max_nb_chars=200),
                },
            )
            genre_map[g['slug']] = obj
            status = '✓ создан' if created else '· уже есть'
            self.stdout.write(f'  Жанр {g["icon"]} {g["name"]}: {status}')
        return genre_map

    def _seed_platforms(self):
        platform_map = {}
        for p in PLATFORMS:
            obj, created = Platform.objects.get_or_create(
                name=p['name'],
                defaults={'short_name': p['short_name']},
            )
            platform_map[p['short_name']] = obj
            status = '✓ создана' if created else '· уже есть'
            self.stdout.write(f'  Платформа {p["short_name"]}: {status}')
        return platform_map

    def _seed_developers(self):
        dev_map = {}
        for d in DEVELOPERS:
            obj, created = Developer.objects.get_or_create(
                name=d['name'],
                defaults={
                    'country': d['country'],
                    'founded_year': d['founded_year'],
                },
            )
            dev_map[d['name']] = obj
            status = '✓ создан' if created else '· уже есть'
            self.stdout.write(f'  Разработчик {d["name"]}: {status}')
        return dev_map

    def _faker_game_text(self):
        """Описания и прочие текстовые поля — через Faker."""
        short = fake.paragraph(nb_sentences=2)
        if len(short) > 300:
            short = short[:297] + '...'
        return short, fake.text(max_nb_chars=1200)

    def _seed_featured_games(self, genre_map, platform_map, dev_map):
        for g in GAMES:
            short_desc, description = self._faker_game_text()
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
                    'cover_url': get_cover_url(slug=g['slug'], title=g['title']) or '',
                    'short_description': short_desc,
                    'description': description,
                },
            )
            if created:
                for genre_slug in g['genres']:
                    if genre_slug in genre_map:
                        game.genres.add(genre_map[genre_slug])
                for platform_short in g['platforms']:
                    if platform_short in platform_map:
                        game.platforms.add(platform_map[platform_short])
                self.stdout.write(f'  ✓ Игра: {g["title"]}')
            else:
                self.stdout.write(f'  · Уже есть: {g["title"]}')

    def _seed_extra_games(self, count, genre_map, platform_map, dev_map):
        titles = random.sample(
            EXTRA_GAME_TITLES,
            min(count, len(EXTRA_GAME_TITLES)),
        )
        genre_slugs = list(genre_map.keys())
        platform_keys = list(platform_map.keys())
        dev_list = list(dev_map.values())
        created = 0

        for title in titles:
            if Game.objects.filter(title=title).exists():
                continue

            release_year = fake.random_int(min=2010, max=2024)
            short_desc, description = self._faker_game_text()
            game = Game(
                title=title,
                developer=random.choice(dev_list) if dev_list else None,
                release_year=release_year,
                release_date=date(release_year, fake.random_int(1, 12), fake.random_int(1, 28)),
                age_rating=random.choice(AGE_RATINGS),
                metacritic_score=fake.random_int(min=55, max=99),
                is_featured=fake.boolean(chance_of_getting_true=20),
                cover_url='',
                short_description=short_desc,
                description=description,
            )
            game.save()
            cover = get_cover_url(slug=game.slug, title=game.title)
            if cover:
                game.cover_url = cover
                game.save(update_fields=['cover_url'])

            for slug in random.sample(genre_slugs, k=random.randint(1, 3)):
                game.genres.add(genre_map[slug])
            for key in random.sample(platform_keys, k=random.randint(1, 4)):
                game.platforms.add(platform_map[key])

            created += 1
            self.stdout.write(f'  ✓ Faker: {title} (slug: {game.slug})')

        return created

    def _apply_covers(self):
        """Проставить обложки всем играм (без случайных картинок Faker)."""
        self.stdout.write('\n  Обновление обложек...')
        for game in Game.objects.all():
            cover = get_cover_url(slug=game.slug, title=game.title)
            if cover and game.cover_url != cover:
                game.cover_url = cover
                game.save(update_fields=['cover_url'])
