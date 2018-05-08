from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^NotFound', views.notFound, name='notFound'),
    url(r'^Display', views.display, name='display')
]
