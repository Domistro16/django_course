from django.http import HttpResponse
from django.shortcuts import render


data = {
    'movies': [
        {
            "id": 5,
            "title": "Jaws",
            "Year": 1995
        },
        {
             "id": 6,
            "title": "Sharknado",
            "Year": 1997
        },
        {
             "id": 7,
            "title": "The Meg",
            "Year": 2000
        }
        ]
}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse('Home Page')