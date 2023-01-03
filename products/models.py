from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=70)

class Product(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateField(auto_now=True)
    update_date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    commentable = models.BooleanField(default=True)

class Review(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    created_date = models.DateField(auto_now=True)