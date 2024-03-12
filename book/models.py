from django.db import models

class Library(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=50)
    price = models.IntegerField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)