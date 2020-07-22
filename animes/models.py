from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    animes = models.CharField(max_length=255, verbose_name="Anime")


class Anime(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, verbose_name="Category",on_delete=models.CASCADE)
    anime = models.CharField(max_length=255, verbose_name="Anime")
    desc = models.TextField(max_length=1000, default='')
    seasons = models.CharField(max_length=100)
    status = models.TextField(max_length=100)
    thumb_nail = models.ImageField(upload_to='anime/images',default='')
    tags = models.TextField(max_length='500',default='')
    realese_date= models.DateField(auto_now_add=False)

