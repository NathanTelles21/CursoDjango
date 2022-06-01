from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html')


def contato(request):
    return HttpResponse(request, 'recipes/contato')


def sobre(request):
    return HttpResponse(request, 'recipes/sobre')
