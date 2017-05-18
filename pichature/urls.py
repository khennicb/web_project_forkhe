from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^room/$', views.chat_room, name='room'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup/authent/$', views.signup, name='signup_succed'),
]