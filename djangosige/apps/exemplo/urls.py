# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'exemplo'
urlpatterns = [

    url(r'exemplo/lista/$', views.ListView.as_view(), name='listaexemplo'),
    url(r'exemplo/adicionar/$', views.AdicionarView.as_view(), name='adicionaexemplo'),
    # url(r'exemplo/editar/(?P<pk>[0-9]+)/$', views.EditarView.as_view(), name='editaexemplo'),

    url(r'exemplo/listacarro/$', views.ListCarroView.as_view(), name='listacarro'),
    url(r'exemplo/adicionarcarro/$', views.AdicionarCarroView.as_view(), name='adicionacarro'),
    url(r'exemplo/editarcarro/(?P<pk>[0-9]+)/$', views.EditarCarroView.as_view(), name='editacarro'),

]
