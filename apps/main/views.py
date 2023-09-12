from django.shortcuts import render
from django.views import View
from django.http import HttpResponse ,HttpRequest
from .models import Game

class MainView(View):
    def get(self,request:HttpRequest)->HttpResponse:
        template_name = 'main/index.html'
        games = Game.objects.all()
        context = {
            'games':games
        }
        return render(
            template_name=template_name,
            request=request,
            context=context
        )
    def post(self,request:HttpRequest,game_id)->HttpResponse:
        data = request.POST
        if data.get('add'):
            pass


class FavoritesView(View):
    template_name = 'main/favorites.html'
    def get(self,request:HttpRequest)->HttpResponse:
        favorites = Game.objects.filter(is_favorite=True)
        return render(
            request=request,
            template_name=self.template_name,
            context={'favorites':favorites}
        )

def change_status(request:HttpRequest,game_id)->HttpResponse:
    data = request.POST
    game = Game.objects.get(id = game_id)
    if data.get('add'):
        game.is_favorite = True
        game.save()
        games = Game.objects.all()
        return render(
            request=request,
            template_name='main/index.html',
            context={'games':games}
        )
    else:
        game.is_favorite = False
        game.save()
        games = Game.objects.all()
        return render(
            request=request,
            template_name='main/index.html',
            context={'games':games}
        )
