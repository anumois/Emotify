from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^getInfo$', views.debugOut, name='debugOut'),
]
