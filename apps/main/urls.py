from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

from .views import MainView , FavoritesView,change_status


urlpatterns = [
    path('',MainView.as_view(),name='main'),
    path('favorites/',FavoritesView.as_view(),name='favorites'),
    path('change_favorite_status/<int:game_id>/',change_status,name='change_status')
]
