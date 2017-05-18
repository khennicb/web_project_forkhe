from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import get_list_or_404

from .models import Chatroom
from .models import Message


def index(request):
    print("On main page : User = " + str(request.user))
    if request.user.is_authenticated():
        # Do something for authenticated users.
        return render(request, 'main_page/main_user.html')
    else:
        # Do something for anonymous users.
        return render(request, 'main_page/main_guest.html')

# Create your views here.

def connection(request):
    return render(request, 'connection/index.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup/index.html')
    elif request.method == 'POST':
        print("New account created " + request.POST['login'] + " / " + request.POST['email'])
        user = User.objects.create_user(request.POST['login'], request.POST['email'], request.POST['pass'])
        user.save()
        u = authenticate(username=request.POST['login'], password=request.POST['pass'])
        login(request, u)
    return index(request)
    
def authent(request):
    if request.method == 'GET':
        print("unexpected GET method")
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print("logged")
            
        else:
            print("not logged")
        
    return render(request, 'connection/index.html')
    
#def chat_room(request, label):
#    # If the room with the given label doesn't exist, automatically create it
#    # upon first visit (a la etherpad).
#    
#    room, created = Chatroom.objects.get_or_create(label=label)
#    
#    # We want to show the last 50 messages, ordered most-recent-last
#    messages = reversed(room.messages.order_by('-timestamp')[:50])

#    return render(request, "chat/room.html", {
#        'room': room,
#        'messages': messages,
#    })
    
def chat_room(request):
    room = Chatroom.objects.get(label='main')
    
    messages = get_list_or_404(Message.objects.filter(chatroom=room))
    
    return render(request, "chat/room.html", {
        'room': room,
        'messages': messages,
    })
