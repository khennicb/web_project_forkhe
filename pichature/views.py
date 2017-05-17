from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User



def index(request):
    return HttpResponse("main page");

# Create your views here.

def connection(request):
    return render(request, 'connection/index.html')

def authent(request):
    if request.method == 'GET':
        print("unexpected GET method")
    elif request.method == 'POST':
        print("New account created " + request.POST['login'] + " / " + request.POST['email'])
        user = User.objects.create_user(request.POST['login'], request.POST['email'], request.POST['pass'])
        user.save()
        
    return render(request, 'connection/index.html')
    
#def chat_room(request, label):
    # If the room with the given label doesn't exist, render main room
    
