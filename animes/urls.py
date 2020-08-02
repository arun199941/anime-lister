from django.contrib import admin
from django.urls import path,include
from . import views 



urlpatterns = [
        path('<str:anime>',views.anime,name='anime'),
]
