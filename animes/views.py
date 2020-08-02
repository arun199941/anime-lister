from django.shortcuts import render,redirect
from .models import Anime
from django.contrib import messages
# Create your views here.

def anime(request,anime):
    if Anime.objects.filter(anime=anime).exists():
        params = Anime.objects.filter(anime=anime)
        return render(request,'anime.html',{'params':params})
    else:
        messages.error(request,'No Anime found')
    return render(request,'anime.html')
