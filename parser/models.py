from django.db import models

class HousesParser(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class NewsParser(models.Model):
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.title