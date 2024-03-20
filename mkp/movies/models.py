from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=32, verbose_name='Жанр')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        get_latest_by = "name"

    def __str__(self) -> str:
        return f'{self.name.lower()}'


class Movie(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    year = models.PositiveSmallIntegerField(verbose_name='Год')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    cover = models.ImageField(
        upload_to="media/movie_covers", null=True, blank=True,
        verbose_name='Обложка')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    rating = models.CharField(max_length=1, choices=(
        ('1', '*'), ('2', '**'), ('3', '***'), ('4', '****'), ('5', '*****')
    ), verbose_name='Рейтинг')

    class Meta:
        ordering = ['-year']
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        get_latest_by = "year"

    def __str__(self) -> str:
        return f'{self.title.upper()} ({self.year})'

    def get_absolute_url(self) -> str:
        return reverse("movie_detail", kwargs={"pk": self.pk})
