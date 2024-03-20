from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from movies.views import (MovieCreateView, MovieDetailView, MovieListView,
                          MovieSearchView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('movies/search/', MovieSearchView.as_view(), name='movie_search'),
    path('movies/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('movies/create', MovieCreateView.as_view(), name='create_movie'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
