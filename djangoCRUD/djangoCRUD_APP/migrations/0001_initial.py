# Generated by Django 4.1.4 on 2022-12-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('url', models.CharField(max_length=100, verbose_name='Ссылка')),
                ('content', models.TextField(max_length=1000, verbose_name='Контент')),
                ('published', models.CharField(max_length=20, verbose_name='Публикация')),
                ('category', models.CharField(max_length=50, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
