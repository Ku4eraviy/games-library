from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('game/<slug:slug>/', views.game_detail, name='game_detail'),
    path('favorites/', views.favorites, name='favorites'),
    path('api/favorite/<int:game_id>/', views.toggle_favorite, name='toggle_favorite'),
]
