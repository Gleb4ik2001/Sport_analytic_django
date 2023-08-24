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