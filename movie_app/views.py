from django.shortcuts import render
from .models import Movie
from django.http import Http404

def show_all(request):
    movies = Movie.objects.all()
    return render(request, 'movie_app/all_movies.html', {'movies': movies})

def show_one(request, film):
    print(film)
    try:
        film = Movie.objects.get(name__iexact=film)
    except:
        raise Http404('Фильм не найден')
    return render(request, 'movie_app/show_one.html', {'film': film})


#Movie.objects.filter(rate__gt=85) фильтр больше
#Movie.objects.filter(rate__lt=85) фильтр меньше
#Movie.objects.filter(rate__gte=85) фильтр больше или равно
#Movie.objects.exclude(rate__gt=90) фильтр не равно
#Movie.objects.get(rate=80) возвращает один(!) объект или ошибку
#Movie.objects.filter(year__isnull=True, rate__gt=80) равнозначно союзу AND
#Movie.objects.filter(Q(year__isnull=True & Q(rate__gt=80)) равнозначно союзу AND
#Movie.objects.filter(Q(year__isnull=True | Q(rate__gt=80)) равнозначно союзу OR
#Movie.objects.filter( ~Q(rate__gt=80)) ~ равнозначно not
#Movie.objects.filter(Q(name__contains='a')) проверка на содержание символов в названии
