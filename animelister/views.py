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
      
   
    print(anime)

    return render(request,'results.html',{'query':id,'animes':anime})

