from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /main-page/5/
    url(r'^(?P<square_name>[0-9]+)/$', views.display, name='display'),
]