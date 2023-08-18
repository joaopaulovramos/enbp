# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'janela_unica'
urlpatterns = [
    url(r'pdf/documentounico/(?P<pk>[0-9]+)/$',
        views.GerarPDFDocumentoUnicoView.as_view(), name='gerarpdfdocumentounico'),        
    url(r'ju/list/$', views.ListDocumentosJanelaUnicaView.as_view(), name='listadocumentos'),
    url(r'ju/caixaentrada/$', views.CaixaEntradaJanelaUnicaView.as_view(), name='caixaentrada'),
    url(r'ju/add/$', views.AdicionarDocumentoUnicoFinanceiroView.as_view(), name='adicionar_documento_unico'),

]
