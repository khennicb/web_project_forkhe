from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup/authent/$', views.signup, name='signup_succed'),
    url(r'^room/$', views.index, name='main_room'),
    #url(r'^room/(?P<label>[\w-]{,50})/$', views.chat_room, name='room'),
    #url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='room'),
    url(r'^room/ajax/send_message/$', views.send_message, name='send_message'),
    url(r'^ajax/send_message/$', views.send_message, name='send_message'),
    url(r'^ajax/receive_message/$', views.receive_message, name='receive_message'),
]