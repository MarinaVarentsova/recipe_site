from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    steps = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='recipes')

    def __str__(self):
        return self.title



