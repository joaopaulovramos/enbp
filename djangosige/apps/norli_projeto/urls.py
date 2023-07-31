# -*- coding: utf-8 -*-



from django.conf.urls import url
from . import views

app_name = 'norli_projeto'
urlpatterns = [
############# projetos
    url(r'norli_projeto/lista/$', views.ListProjetosView.as_view(), name='listaprojetos'),
    url(r'norli_projeto/adicionar/$', views.AddProjetoView.as_view(), name='adicionaprojetos'),
    url(r'norli_projeto/editar/(?P<pk>[0-9]+)/$', views.EditProjetoView.as_view(), name='editarprojetos'),


############# Tipos de projetos
    url(r'norli_tipo/lista/$', views.ListTipoView.as_view(), name='listatipo'),
    url(r'norli_tipo/adicionar/$', views.AddTipoView.as_view(), name='adicionatipo'),
    url(r'norli_tipo/editar/(?P<pk>[0-9]+)/$', views.EditTipoView.as_view(), name='editartipo'),


############# Filiais
    url(r'norli_filial/lista/$', views.ListFilialView.as_view(), name='listafilial'),
    url(r'norli_filial/adicionar/$', views.AddFilialView.as_view(), name='adicionafilial'),
    url(r'norli_filial/editar/(?P<pk>[0-9]+)/$', views.EditFilialView.as_view(), name='editarfilial'),



]
