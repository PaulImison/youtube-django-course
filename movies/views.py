from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
               {
                   'id':5,
                   'title': 'Jaws',
                   'year': 1975
               },
               {
                   'id':6,
                   'title': 'Sharknado',
                   'year': 2010
               },
               {
                   'id':5,
                   'title': 'The Meg',
                   'year': 2000
                   
               }
               ]
    }

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(response):
    return HttpResponse("Hello, world. You're at the movies home.")