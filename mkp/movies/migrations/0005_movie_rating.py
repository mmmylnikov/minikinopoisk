# Generated by Django 5.0.3 on 2024-03-11 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.CharField(choices=[('1', '*'), ('2', '**'), ('3', '***'), ('4', '****'), ('5', '*****')], default='1', max_length=1, verbose_name='Рейтинг'),
            preserve_default=False,
        ),
    ]
