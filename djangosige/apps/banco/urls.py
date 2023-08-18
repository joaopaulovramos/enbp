# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'banco'
urlpatterns = [

    # bancos
    url(r'banco/listabanco/$', views.ListBancoView.as_view(), name='listabanco'),
    url(r'banco/adicionarbanco/$', views.AdicionarBancoView.as_view(), name='adicionarbanco'),
    url(r'banco/editarbanco/(?P<pk>[0-9]+)/$', views.EditarBancoView.as_view(), name='editarbanco'),

    
]
