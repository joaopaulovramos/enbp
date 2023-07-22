# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'janela_unica'
urlpatterns = [
    url(r'pdf/documentounico/(?P<pk>[0-9]+)/$',
        views.GerarPDFDocumentoUnicoView.as_view(), name='gerarpdfdocumentounico'),
    url(r'ju/list/$', views.ListDocumentosViagensView.as_view(), name='listadocumentos'),
    url(r'ju/add/$', views.AdicionarDocumentoView.as_view(), name='adicionardocumentos'),
    url(r'ju/edit/(?P<pk>[0-9]+)/$', views.EditarDocumentoView.as_view(), name='editardocumentos'),

    url(r'ju/tramitar/$', views.TramitarView.as_view(), name='tramitar'),
    url(r'ju/listtramitacao/$', views.ListTramitacaoView.as_view(), name='listtramitacao'),



]
