from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

import urllib2
import json
import re

from .models import Chatroom
from .models import Message


def index(request):
    print("On main page : User = " + str(request.user))
    if request.user.is_authenticated():
        # Do something for authenticated users.
        
        room = Chatroom.objects.get(label='main')
    
        messages = Message.objects.filter(chatroom=room)
        
        return render(request, "chat/room.html", {
            'room': room,
            'messages': messages,
        })
        #return render(request, 'main_page/main_user.html')
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
        existing_user = User.objects.filter(username=request.POST['login']).first()
        
        if existing_user == None:
            print("New account created " + request.POST['login'] + " / " + request.POST['email'])
            user = User.objects.create_user(request.POST['login'], request.POST['email'], request.POST['pass'])
            user.save()
            u = authenticate(username=request.POST['login'], password=request.POST['pass'])
            login(request, u)
            return redirect('/')
        else:
            print("User \"" + existing_user.username + "\" is already signed in.")
            
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
    
    
def chat_room(request):
    print("chat_room ")
    print(request.user)
    
    #room, created = Chatroom.objects.get_or_create(label=label, defaults={'name':label})
    #room.chatroomUsers.add(request.user);
    #room.chatroomAdmin.add(request.user);
    
    room = Chatroom.objects.get(label='main')
    
    room.save()
    
    messages = Message.objects.filter(chatroom=room)
    
    return render(request, "chat/room.html", {
        'room': room,
        'messages': messages,
    })

def send_message(request):
    print("send_message")
    userName = request.user
    messageReceved = request.POST.get('message', None)
    
    wordList = re.findall(r"[\w']+", messageReceved.replace('\'',' ').replace('"', ' '))
    
    message_picture_string = ""
    
    # get translated message
    for word in wordList:
        request = urllib2.Request("http://api.giphy.com/v1/stickers/translate?s="+word+"&api_key=dc6zaTOxFJmzC")
        response = urllib2.urlopen(request)
        jsonObj = json.loads(response.read())
        if not jsonObj['data']:
            message_picture_string += word + " "
        else:
            message_picture_string += "<img class=\"pictureText\" src=\""
            message_picture_string += str(jsonObj['data']['images']['original']['url'])
            message_picture_string += "\" alt=\"" + word +"\" title=\"" + word + "\" > "
    
    print(message_picture_string)
    
    # insert into bd
    chatroomObj = Chatroom.objects.get(label='main')
    userObj = User.objects.get(username=userName)
    
    message = Message(chatroom=chatroomObj, user=userObj, message_text=messageReceved, message_picture=message_picture_string)
    message.save()
    
    return HttpResponse(204)


def receive_message(request):
    msgID = request.GET.get('messageid', None)
    print("receive_message after msgID "+ msgID)

    arrayOfMsg = Message.objects.filter(id__gt=3)
    
    arrayToSend = []
    for msg in arrayOfMsg:
        print("msg.id ? msgID  (" + str(msg.id) + "; " + str(msgID) +")" )
        if(int(msg.id) > int(msgID)):
            JsonMsg = {}
            JsonMsg["id"] =msg.id
            JsonMsg["user"] =msg.user
            JsonMsg["timestamp"] =msg.timestamp
            JsonMsg["message_picture"] =msg.message_picture
            
            arrayToSend.append(JsonMsg)
            print("yes")
            
    print("Without serealization " + str(arrayToSend))

    data = {
        'new_msg':list(Message.objects.filter(id__gt=3))
    }
    #print("data =" + str(data))
    return JsonResponse(data)
    
    
    
    
    