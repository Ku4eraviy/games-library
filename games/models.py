from django.db import models
from django.conf import settings
from autoslug import AutoSlugField


class Genre(models.Model):
    """Жанр игры."""
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = AutoSlugField(
        populate_from='name',
        max_length=100,
        unique=True,
        verbose_name='Slug',
    )
    description = models.TextField(blank=True, verbose_name='Описание')
    icon = models.CharField(max_length=50, blank=True, default='🎮', verbose_name='Иконка (эмодзи)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']


class Platform(models.Model):
    """Платформа (PC, PS5, Xbox и т.д.)."""
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    short_name = models.CharField(max_length=20, verbose_name='Сокращение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'
        ordering = ['name']


class Developer(models.Model):
    """Разработчик игры."""
    name = models.CharField(max_length=200, verbose_name='Название студии')
    country = models.CharField(max_length=100, blank=True, verbose_name='Страна')
    founded_year = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Год основания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'
        ordering = ['name']


class Game(models.Model):
    """Основная модель игры."""

    RATING_CHOICES = [
        ('0+',  '0+'),
        ('6+',  '6+'),
        ('12+', '12+'),
        ('16+', '16+'),
        ('18+', '18+'),
    ]

    title = models.CharField(max_length=200, verbose_name='Название')
    slug = AutoSlugField(
        populate_from='title',
        max_length=200,
        unique=True,
        verbose_name='Slug',
    )

    # Связи
    genres = models.ManyToManyField(
        Genre,
        related_name='games',
        blank=True,
        verbose_name='Жанры'
    )
    developer = models.ForeignKey(
        Developer,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='games',
        verbose_name='Разработчик'
    )
    platforms = models.ManyToManyField(
        Platform,
        related_name='games',
        blank=True,
        verbose_name='Платформы'
    )

    # Медиа
    cover = models.ImageField(
        upload_to='covers/',
        null=True, blank=True,
        verbose_name='Обложка'
    )
    cover_url = models.URLField(
        blank=True,
        verbose_name='URL обложки (если нет файла)'
    )
    background_image = models.ImageField(
        upload_to='backgrounds/',
        null=True, blank=True,
        verbose_name='Фоновое изображение'
    )

    # Информация
    description = models.TextField(blank=True, verbose_name='Описание')
    short_description = models.CharField(
        max_length=300,
        blank=True,
        verbose_name='Краткое описание'
    )
    release_year = models.PositiveSmallIntegerField(
        null=True, blank=True,
        verbose_name='Год выпуска'
    )
    release_date = models.DateField(null=True, blank=True, verbose_name='Дата выпуска')
    age_rating = models.CharField(
        max_length=5,
        choices=RATING_CHOICES,
        default='0+',
        verbose_name='Возрастной рейтинг'
    )

    # Мета
    metacritic_score = models.PositiveSmallIntegerField(
        null=True, blank=True,
        verbose_name='Оценка Metacritic'
    )
    is_featured = models.BooleanField(default=False, verbose_name='Рекомендуемая')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.title

    def get_cover(self):
        """Возвращает URL обложки (файл → cover_url → каталог Steam/PS)."""
        if self.cover:
            return self.cover.url
        if self.cover_url:
            return self.cover_url
        from .cover_urls import get_cover_url
        return get_cover_url(slug=self.slug, title=self.title)

    def get_banner(self):
        """Широкий баннер для карусели (EA-style)."""
        from .cover_urls import get_banner_url
        return get_banner_url(slug=self.slug, title=self.title) or self.get_cover()

    def get_score_color(self):
        """Цвет оценки Metacritic."""
        if self.metacritic_score is None:
            return 'text-neutral-400'
        if self.metacritic_score >= 75:
            return 'text-green-400'
        if self.metacritic_score >= 50:
            return 'text-yellow-400'
        return 'text-red-400'

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['-release_year', 'title']


class FavoriteGame(models.Model):
    """Избранные игры пользователя."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь'
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='favorited_by',
        verbose_name='Игра'
    )
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено в избранное')

    def __str__(self):
        return f'{self.user.username} → {self.game.title}'

    class Meta:
        verbose_name = 'Избранная игра'
        verbose_name_plural = 'Избранные игры'
        unique_together = ('user', 'game')
        ordering = ['-added_at']


class GameScreenshot(models.Model):
    """Скриншоты игры."""
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='screenshots',
        verbose_name='Игра'
    )
    image = models.ImageField(upload_to='screenshots/', verbose_name='Скриншот')
    caption = models.CharField(max_length=200, blank=True, verbose_name='Подпись')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')

    def __str__(self):
        return f'Скриншот {self.game.title} #{self.order}'

    class Meta:
        verbose_name = 'Скриншот'
        verbose_name_plural = 'Скриншоты'
        ordering = ['order']
