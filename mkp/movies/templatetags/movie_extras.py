from typing import Any

from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def get_movie_rating_percent(context: dict[str, Any]) -> int:
    movie = context["object"]
    return int(int(movie.rating)/5*100)
