from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Game, Genre, Platform, FavoriteGame


def game_list(request):
    """Главная страница — каталог игр."""
    games = Game.objects.select_related('developer').prefetch_related('genres', 'platforms')

    # Поиск
    search_query = request.GET.get('q', '').strip()
    if search_query:
        games = games.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(developer__name__icontains=search_query)
        )

    # Фильтр по жанру
    genre_slug = request.GET.get('genre', '')
    if genre_slug:
        games = games.filter(genres__slug=genre_slug)

    # Фильтр по платформе
    platform_id = request.GET.get('platform', '')
    if platform_id:
        games = games.filter(platforms__id=platform_id)

    # Фильтр по году
    year = request.GET.get('year', '')
    if year:
        games = games.filter(release_year=year)

    # Сортировка
    sort = request.GET.get('sort', '-release_year')
    sort_options = {
        '-release_year': '-release_year',
        'release_year': 'release_year',
        'title': 'title',
        '-title': '-title',
        '-metacritic_score': '-metacritic_score',
        '-created_at': '-created_at',
    }
    if sort in sort_options:
        games = games.order_by(sort_options[sort])
    else:
        games = games.order_by('-release_year')

    # Distinct чтобы не дублировались при фильтре many2many
    games = games.distinct()

    # Пагинация
    paginator = Paginator(games, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Данные для фильтров
    genres = Genre.objects.all()
    platforms = Platform.objects.all()

    # Доступные годы
    years = Game.objects.exclude(release_year=None).values_list(
        'release_year', flat=True
    ).distinct().order_by('-release_year')

    # Избранное текущего пользователя
    favorite_ids = set()
    if request.user.is_authenticated:
        favorite_ids = set(
            FavoriteGame.objects.filter(user=request.user).values_list('game_id', flat=True)
        )

    # Рекомендуемые игры (для hero-секции)
    featured_games = Game.objects.filter(is_featured=True).select_related('developer')[:5]

    context = {
        'page_obj': page_obj,
        'genres': genres,
        'platforms': platforms,
        'years': years,
        'search_query': search_query,
        'selected_genre': genre_slug,
        'selected_platform': platform_id,
        'selected_year': year,
        'selected_sort': sort,
        'favorite_ids': favorite_ids,
        'featured_games': featured_games,
        'total_count': paginator.count,
    }
    return render(request, 'pages/game_list.html', context)


def game_detail(request, slug):
    """Страница отдельной игры."""
    game = get_object_or_404(
        Game.objects.select_related('developer').prefetch_related(
            'genres', 'platforms', 'screenshots'
        ),
        slug=slug
    )

    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = FavoriteGame.objects.filter(
            user=request.user, game=game
        ).exists()

    # Похожие игры (по жанрам)
    similar_games = Game.objects.filter(
        genres__in=game.genres.all()
    ).exclude(id=game.id).distinct()[:6]

    context = {
        'game': game,
        'is_favorite': is_favorite,
        'similar_games': similar_games,
        'screenshots': game.screenshots.all(),
    }
    return render(request, 'pages/game_detail.html', context)


@login_required
def favorites(request):
    """Страница избранных игр пользователя."""
    favorite_games = Game.objects.filter(
        favorited_by__user=request.user
    ).select_related('developer').prefetch_related('genres').order_by(
        '-favorited_by__added_at'
    )

    favorite_ids = set(favorite_games.values_list('id', flat=True))

    context = {
        'games': favorite_games,
        'favorite_ids': favorite_ids,
        'total_count': favorite_games.count(),
    }
    return render(request, 'pages/favorites.html', context)


@login_required
def toggle_favorite(request, game_id):
    """AJAX: добавить/убрать из избранного."""
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    game = get_object_or_404(Game, id=game_id)
    fav, created = FavoriteGame.objects.get_or_create(
        user=request.user, game=game
    )

    if not created:
        fav.delete()
        is_favorite = False
    else:
        is_favorite = True

    return JsonResponse({
        'is_favorite': is_favorite,
        'game_id': game_id,
    })
