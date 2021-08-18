from django.db import models

# Create your models here.

class Gif(models.Model):
    title = models.CharField(max_length=80)
    url = models.URLField()
    uploader_name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Category: {self.title}'

class Category(models.Model):
    name = models.CharField(max_length=80)
    gifs = models.ManyToManyField(Gif, blank=True)
    def __str__(self):
        return f'Category: {self.name}'

# class Like(models.Model):
#     gif = models.ForeignKey(Gif, on_delete=models.PROTECT)