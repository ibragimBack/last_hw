# Generated by Django 5.0.3 on 2024-04-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_forum', '0003_alter_reviewbook_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='#', max_length=100, verbose_name='напишите тег для книги')),
            ],
        ),
        migrations.AddField(
            model_name='book_forum',
            name='tags',
            field=models.ManyToManyField(to='book_forum.tag'),
        ),
    ]
