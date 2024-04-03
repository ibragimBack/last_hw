from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='напишите тег для книги', default='#')

    def __str__(self):
        return self.name


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
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.name} - {self.tags}'

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Получение книг пользователей'


class ReviewBook(models.Model):
    name_correction = models.ForeignKey(Book_Forum, on_delete=models.CASCADE, related_name='comment')
    description = models.TextField()
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.description
