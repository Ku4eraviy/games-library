"""
Наполнение БД играми из каталога seed_catalog.
Запуск: python manage.py seed_data
"""
from django.core.management.base import BaseCommand

from games.cover_urls import get_cover_url
from games.models import Genre, Platform, Developer, Game
from games.seed_catalog import (
    GENRES, PLATFORMS, DEVELOPERS, GAMES, get_game_text,
)


class Command(BaseCommand):
    help = 'Заполнить БД жанрами, платформами, разработчиками и играми с нормальными описаниями'

    def handle(self, *args, **kwargs):
        self.stdout.write('Начинаем заполнение базы данных...\n')

        genre_map = self._seed_genres()
        platform_map = self._seed_platforms()
        dev_map = self._seed_developers()
        created, updated = self._seed_games(genre_map, platform_map, dev_map)
        covers = self._apply_covers()

        self.stdout.write(self.style.SUCCESS(
            f'\nГотово! Игр в каталоге: {Game.objects.count()}. '
            f'Создано: {created}, обновлено: {updated}, обложек обновлено: {covers}.'
        ))
        self.stdout.write('\nДальше (если ещё не делали):')
        self.stdout.write('  python manage.py createsuperuser')
        self.stdout.write('  python manage.py runserver\n')

    def _seed_genres(self):
        genre_map = {}
        for g in GENRES:
            obj, created = Genre.objects.update_or_create(
                slug=g['slug'],
                defaults={
                    'name': g['name'],
                    'icon': g['icon'],
                    'description': g['description'],
                },
            )
            genre_map[g['slug']] = obj
            mark = '+' if created else '~'
            self.stdout.write(f'  [{mark}] Жанр {g["icon"]} {g["name"]}')
        return genre_map

    def _seed_platforms(self):
        platform_map = {}
        for p in PLATFORMS:
            obj, created = Platform.objects.get_or_create(
                name=p['name'],
                defaults={'short_name': p['short_name']},
            )
            platform_map[p['short_name']] = obj
            mark = '+' if created else '~'
            self.stdout.write(f'  [{mark}] Платформа {p["short_name"]}')
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
            mark = '+' if created else '~'
            self.stdout.write(f'  [{mark}] {d["name"]}')
        return dev_map

    def _seed_games(self, genre_map, platform_map, dev_map):
        created_count = 0
        updated_count = 0

        for g in GAMES:
            texts = get_game_text(g['slug'])
            cover = get_cover_url(slug=g['slug'], title=g['title']) or ''

            game, created = Game.objects.update_or_create(
                slug=g['slug'],
                defaults={
                    'title': g['title'],
                    'developer': dev_map.get(g['developer']),
                    'release_year': g['release_year'],
                    'release_date': g['release_date'],
                    'age_rating': g['age_rating'],
                    'metacritic_score': g['metacritic_score'],
                    'is_featured': g['is_featured'],
                    'cover_url': cover,
                    'short_description': texts['short_description'],
                    'description': texts['description'],
                },
            )

            game.genres.set(
                [genre_map[s] for s in g['genres'] if s in genre_map]
            )
            game.platforms.set(
                [platform_map[s] for s in g['platforms'] if s in platform_map]
            )

            if created:
                created_count += 1
                self.stdout.write(f'  [+] {g["title"]}')
            else:
                updated_count += 1
                self.stdout.write(f'  [~] {g["title"]}')

        return created_count, updated_count

    def _apply_covers(self):
        updated = 0
        for game in Game.objects.all():
            cover = get_cover_url(slug=game.slug, title=game.title)
            if cover and game.cover_url != cover:
                game.cover_url = cover
                game.save(update_fields=['cover_url'])
                updated += 1
        return updated
