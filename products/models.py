from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=70)

class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateField(auto_now=True)
    update_date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="review")
    comments = models.CharField(max_length=255)
    created_date = models.DateField(auto_now=True)