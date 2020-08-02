from django.shortcuts import render, redirect
from django.contrib import messages
from animes.models import Category, Anime


def index(request):

    return render(request, 'index.html')


def search(request):
    var1 = request.GET['query']
    if var1 == 'Slice of Life':
        id = 1
        anime = Anime.objects.filter(category=id)
    elif var1 == 'Action':
        id = 5
        anime = Anime.objects.filter(category=id)
    else:
        messages.error(request,'No such category found')
 

    return render(request,'results.html',{'query':var1,'animes':anime})

