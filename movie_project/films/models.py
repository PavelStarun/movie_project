from django.db import models

# Create your models here.
class News_post(models.Model):
    films = models.CharField('Название фильма', max_length=50)
    short_description = models.CharField('описание фильма', max_length=200)
    text = models.TextField('Отзыв')