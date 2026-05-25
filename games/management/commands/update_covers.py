"""Обновить cover_url у всех игр из каталога надёжных обложек."""
from django.core.management.base import BaseCommand

from games.cover_urls import get_cover_url
from games.models import Game


class Command(BaseCommand):
    help = 'Проставить реальные обложки (Steam/PS CDN) всем играм в БД'

    def handle(self, *args, **options):
        updated = 0
        skipped = 0

        for game in Game.objects.all():
            url = get_cover_url(slug=game.slug, title=game.title)
            if not url:
                skipped += 1
                self.stdout.write(f'  · нет обложки: {game.title} ({game.slug})')
                continue
            if game.cover_url != url:
                game.cover_url = url
                game.save(update_fields=['cover_url'])
                updated += 1
                self.stdout.write(f'  ✓ {game.title}')
            else:
                self.stdout.write(f'  · без изменений: {game.title}')

        self.stdout.write(self.style.SUCCESS(
            f'\nГотово: обновлено {updated}, пропущено {skipped}.'
        ))
