from django.shortcuts import render, redirect
from django.contrib import messages
from animes.models import Category, Anime


def index(request):

    return render(request, 'index.html')


def search(request,):
    query = request.GET['query']
    anime = Anime.objects.filter(category=query)
    print(anime)

    return render(request,'results.html',{'query':query,'animes':anime})

