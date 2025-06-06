from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
from django.http import HttpResponseRedirect
from django.http import Http404


def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})

def home(response):
    return HttpResponse("Hello, world. You're at the movies home.")

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    
    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')
    # Movie.objects.create(title=title, year=year)
    return render(request, 'movies/add.html')

def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404("Movie does not exist")
    movie.delete()
    return HttpResponseRedirect('/movies')