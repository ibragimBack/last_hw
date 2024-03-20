from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Library(models.Model):

    GENRE_BOOKS = (
        ('Романтика', 'Романтика'),
        ('Детектив', 'Детектив'),
        ('Саморазвитие', 'Саморазвитие'),
        ('Психология', 'Психология'),
        ('Исторический', 'Исторический'),
        ('Приключения', 'Приключения')
    )

    title = models.CharField(max_length=100, verbose_name='Заголовок', null=True)
    description = models.TextField(max_length=250, verbose_name='Описание', null=True)
    location = models.CharField(max_length=50, verbose_name='Место нахождение', null=True)
    price = models.IntegerField(max_length=20, default=799, verbose_name='Цена',null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', verbose_name='Фото',blank=True, null=True)
    music = models.FileField(upload_to='music/', verbose_name='Музыка',blank=True, null=True)
    types_books = models.CharField(max_length=100, choices=GENRE_BOOKS, verbose_name='Выберите жанр', null=True)
    email = models.EmailField(max_length=30, unique=True, verbose_name='Укажите вашу электронную почти', blank=True, null=True)
    phone_number = PhoneNumberField(region='KG', unique=True, verbose_name='Введите номер телефона', blank=True, null=True)
    youtube_url = models.URLField(verbose_name='Вставтьте URL видео с YouTube', null=True)

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'

