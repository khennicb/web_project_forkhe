from django.shortcuts import render
from django.http import HttpResponse
from .models import Square, Color
from django.template import loader

# Create your views here.

def index(request):
    last_squares = Square.objects.all()[:10]
    context = {
        'last_squares': last_squares
    }
    return render(request, 'mainPage/index.html', context)


def display(request, square_name):
    return HttpResponse("here is the square number %s" %square_name)
