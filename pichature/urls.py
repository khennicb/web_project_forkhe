from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^connection/$', views.connection, name='connection'),
    url(r'^connection/authent/$', views.authent, name='authent'),
]