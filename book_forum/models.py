from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Book_Forum(models.Model):

    GENRE_BOOKS = (
        ('Романтика', 'Романтика'),
        ('Детектив', 'Детектив'),
        ('Саморазвитие', 'Саморазвитие'),
        ('Психология', 'Психология'),
        ('Исторический', 'Исторический'),
        ('Приключения', 'Приключения')
    )
    name = models.CharField(max_length=100, verbose_name='Введите ваше имя')
    book = models.TextField(max_length=30, verbose_name='Введите название книги')
    genre = models.CharField(max_length=100, choices=GENRE_BOOKS, verbose_name='Выберите жанр книги')
    phone_number = PhoneNumberField(region='KG', blank=True, verbose_name='Введите ваш номер телефона')
    description = models.TextField(max_length=250, verbose_name='Введите краткий сюжет')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Получение книг пользователей'