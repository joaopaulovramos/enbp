# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'opiniao'
urlpatterns = [

    url(r'opiniao/listaropinioes/$', views.ListOpiniaoView.as_view(), name='listaropinioes'),
    url(r'opiniao/adicionaopiniao/$', views.AdicionarOpiniaoView.as_view(), name='adicionaopiniao'),
    url(r'opiniao/editaropiniao/(?P<pk>[0-9]+)$', views.EditarOpiniaoView.as_view(), name='editaropiniao'),


]
