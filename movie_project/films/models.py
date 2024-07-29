from django.db import models

# Create your models here.
class Movie(models.Model):
    films = models.CharField('Название фильма', max_length=50)
    description = models.TextField('описание фильма', max_length=200)
    text = models.TextField('Отзыв')


    def __str__(self):
        return self.title
