from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    PLACES_OF_KG = (
        ('Бишкек', 'Бишкек'),
        ('Нарын', 'Нарын'),
        ('Баткен', 'Баткен'),
        ('Исык-Куль', 'Исык-Куль'),
        ('Джалал-Абад', 'Джалал-Абад'),
        ('Чуй', 'Чуй'),
        ('Талас', 'Талас'),
        ('Ош', 'Ош'),
    )
    COLORS = (
        ('Синий', 'Синий'),
        ('Красный', 'Красный'),
        ('Желтый', 'Желтый'),
        ('Зеленый', 'Зеленый'),
        ('Фиолетовый', 'Фиолетовый'),
    )
    date_of_births = models.DateField()
    place_of_births = models.CharField(max_length=50, choices=PLACES_OF_KG)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=30, default='+996')
    favourite_color = models.CharField(max_length=30, choices=COLORS)
    hobby = models.TextField(max_length=50)
    profession = models.TextField(max_length=50)
