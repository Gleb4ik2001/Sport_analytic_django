from django.shortcuts import render
from django.views import View
from django.http import HttpResponse ,HttpRequest

class MainView(View):
    def get(self,request:HttpRequest)->HttpResponse:
        template_name = 'main/index.html'
        return render(
            template_name=template_name,
            request=request,
            context={}
        )