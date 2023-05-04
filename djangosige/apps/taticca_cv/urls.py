# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'taticca_cv'
urlpatterns = [

    url(r'taticca_cv/lista/$', views.ListView.as_view(), name='listaexemplo'),
    url(r'taticca_cv/adicionar/$', views.AdicionarView.as_view(), name='adicionaexemplo'),
    url(r'taticca_cv/editar/$', views.EditarView.as_view(), name='editacv'),
    url(r'taticca_cv/editar/(?P<pk>[0-9]+)/$', views.EditarView.as_view(), name='editarexemplo'),

    url(r'taticca_cv/listacertificados/$', views.ListCertificadoView.as_view(), name='listacertificados'),
    url(r'taticca_cv/adicionarcertificados/$', views.AdicionarCertificadoView.as_view(), name='adicionacertificado'),



]
