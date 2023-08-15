from django.db import models
from datetime import datetime


class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now())


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    posted_at = models.DateTimeField(default=datetime.now())
    category = models.ForeignKey(Category, on_delete=models.CASCADE)