from typing import Any

from django.db.models import Q, QuerySet
from django.http import request
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from movies.apps import MoviesConfig
from movies.models import Movie


class ExtraContextMixin:
    title: str | None = None

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict:
        context = super().get_context_data(**kwargs)  # type: ignore
        context['app_name'] = MoviesConfig.verbose_name
        if self.title:
            context['title'] = self.title
        return context


class MovieCreateView(ExtraContextMixin, CreateView):
    model = Movie
    fields = '__all__'
    title = 'Добавить фильм'

    def get_success_url(self) -> str:
        return reverse('create_movie')


class MovieDetailView(ExtraContextMixin, DetailView):
    model = Movie


def movie_year_filter(request: request, object_list: QuerySet) -> QuerySet:
    year_raw = request.GET.get('year')
    if not year_raw:
        return object_list
    try:
        year = int(year_raw)
    except ValueError:
        year = None
    if not year:
        return object_list
    return object_list.filter(year=year)


def movie_rating_filter(request: request, object_list: QuerySet) -> QuerySet:
    rating = request.GET.get('rating')
    if not rating:
        return object_list
    return object_list.filter(rating=rating)


def movie_genre_filter(request: request, object_list: QuerySet) -> QuerySet:
    genre_raw = request.GET.get('genre')
    if not genre_raw:
        return object_list
    genres = genre_raw.split(',')
    return object_list.filter(genre__name__in=genres)


class MovieListView(ExtraContextMixin, ListView):
    template_name = 'movies/movie_list.html'
    model = Movie
    title = 'Кинотека'

    def get_queryset(self) -> QuerySet:
        object_list = self.model.objects.all()
        object_list = movie_year_filter(self.request, object_list)
        object_list = movie_rating_filter(self.request, object_list)
        object_list = movie_genre_filter(self.request, object_list)

        return object_list


class MovieSearchView(ExtraContextMixin, ListView):
    template_name = MovieListView.template_name
    model = MovieListView.model
    title = MovieListView.title + ' - поиск'

    def get_queryset(self) -> QuerySet:
        query = self.request.GET.get('q')
        object_list = self.model.objects.all()
        if query:
            object_list = object_list.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        return object_list
