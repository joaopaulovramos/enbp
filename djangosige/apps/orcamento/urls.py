# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'orcamento'
urlpatterns = [

    # Orçamentos
    url(r'orcamento/listaorcamento/$', views.ListOrcamentoView.as_view(), name='listaorcamento'),
    url(r'orcamento/adicionarorcamento/$', views.AdicionarOrcamentoView.as_view(), name='adicionarorcamento'),
    url(r'orcamento/editarorcamento/(?P<pk>[0-9]+)/$', views.EditarOrcamentoView.as_view(), name='editarorcamento'),

    
]
