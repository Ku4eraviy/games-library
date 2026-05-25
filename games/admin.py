from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from image_uploader_widget.admin import ImageUploaderInline
from image_uploader_widget.widgets import ImageUploaderWidget

from .models import Game, Genre, Platform, Developer, FavoriteGame, GameScreenshot


class ImageAdminMixin:
    """Виджет предпросмотра изображений в админке (без изменения моделей)."""
    formfield_overrides = {
        models.ImageField: {'widget': ImageUploaderWidget},
    }


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('icon', 'name', 'slug')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')
    search_fields = ('name', 'short_name')
    ordering = ('name',)


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founded_year')
    search_fields = ('name', 'country')
    list_filter = ('country',)
    ordering = ('name',)


class GameScreenshotInline(ImageUploaderInline):
    model = GameScreenshot
    extra = 2
    fields = ('image', 'caption', 'order')


@admin.register(Game)
class GameAdmin(ImageAdminMixin, admin.ModelAdmin):
    list_display = (
        'cover_thumbnail', 'title', 'developer', 'release_year',
        'age_rating', 'metacritic_score', 'is_featured'
    )
    list_display_links = ('cover_thumbnail', 'title')
    search_fields = ('title', 'description', 'developer__name')
    list_filter = ('genres', 'platforms', 'release_year', 'age_rating', 'is_featured')
    ordering = ('-release_year', 'title')
    filter_horizontal = ('genres', 'platforms')
    list_editable = ('is_featured',)
    inlines = [GameScreenshotInline]

    fieldsets = (
        ('Основное', {
            'fields': ('title', 'slug', 'short_description', 'description')
        }),
        ('Медиа', {
            'fields': ('cover', 'cover_url', 'background_image')
        }),
        ('Классификация', {
            'fields': ('genres', 'platforms', 'developer', 'age_rating')
        }),
        ('Даты и рейтинг', {
            'fields': ('release_year', 'release_date', 'metacritic_score', 'is_featured')
        }),
    )

    def cover_thumbnail(self, obj):
        url = obj.get_cover()
        if url:
            return format_html(
                '<img src="{}" style="width:50px;height:70px;object-fit:cover;border-radius:4px;" />',
                url
            )
        return '—'
    cover_thumbnail.short_description = 'Обложка'


@admin.register(FavoriteGame)
class FavoriteGameAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'added_at')
    search_fields = ('user__username', 'game__title')
    list_filter = ('added_at',)
    ordering = ('-added_at',)
    readonly_fields = ('added_at',)


@admin.register(GameScreenshot)
class GameScreenshotAdmin(ImageAdminMixin, admin.ModelAdmin):
    list_display = ('game', 'caption', 'order')
    search_fields = ('game__title', 'caption')
    list_filter = ('game',)
    ordering = ('game', 'order')
