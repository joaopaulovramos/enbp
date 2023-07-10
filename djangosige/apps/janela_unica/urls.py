# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'janela_unica'
urlpatterns = [

    url(r'ju/list/$', views.ListDocumentosViagensView.as_view(), name='listadocumentos'),
    url(r'ju/add/$', views.AdicionarDocumentoView.as_view(), name='adicionardocumentos'),
    url(r'ju/edit/(?P<pk>[0-9]+)/$', views.EditarDocumentoView.as_view(), name='editardocumentos'),

    url(r'ju/board/$', views.home, name='board'),
    url(r'ju/tasks/$', views.ListTask, name='tasks'),



]
