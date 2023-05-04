# -*- coding: utf-8 -*-



from django.conf.urls import url
from . import views

app_name = 'zpfaturamento'
urlpatterns = [

    url(r'zplistclassificacaofaturamento/lista/$', views.ListClassificacaoFaturamentoView.as_view(), name='listclassificacaofaturamento'),
    url(r'zpadicionarclassificacaofaturamento/adicionar/$', views.AdicionarClassificacaoFaturamentoView.as_view(), name='adicionarclassificacaofaturamento'),
    url(r'zpeditclassificacaofaturamento/editar/(?P<pk>[0-9]+)/$', views.EditarClassificacaoFaturamentoView.as_view(), name='editclassificacaofaturamento'),

    url(r'zplistitemfaturamento/lista/$', views.ListItemFaturamentoView.as_view(), name='listitemfaturamento'),
    url(r'zpadicionaritemfaturamento/adicionar/$', views.AdicionarItemfaturamentoView.as_view(), name='adicionaritemfaturamento'),
    url(r'zpedititemfaturamento/editar/(?P<pk>[0-9]+)/$', views.EditarItemfaturamentoView.as_view(), name='edititemfaturamento'),

]
