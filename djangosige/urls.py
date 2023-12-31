# -*- coding: utf-8 -*-
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from .configs.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

admin.autodiscover()


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^', include('djangosige.apps.base.urls')),
    url(r'^login/', include('djangosige.apps.login.urls')),
    url(r'^cadastro/', include('djangosige.apps.cadastro.urls')),
    url(r'^fiscal/', include('djangosige.apps.fiscal.urls')),
    url(r'^vendas/', include('djangosige.apps.vendas.urls')),
    url(r'^compras/', include('djangosige.apps.compras.urls')),
    url(r'^financeiro/', include('djangosige.apps.financeiro.urls')),
    url(r'^estoque/', include('djangosige.apps.estoque.urls')),

#zeppelin
    url(r'^exemplo/', include('djangosige.apps.exemplo.urls')),
    url(r'^zeppelin/', include('djangosige.apps.zeppelin.urls')),
    url(r'^zeppelin/', include('djangosige.apps.zpfaturamento.urls')),
    url(r'^zeppelin/', include('djangosige.apps.taticca_cv.urls')),
    url(r'^zeppelin/', include('djangosige.apps.norli_projeto.urls')),
    url(r'^zeppelin/', include('djangosige.apps.timesheet.urls')),
    url(r'^zeppelin/', include('djangosige.apps.viagem.urls')),
    url(r'^zeppelin/', include('djangosige.apps.janela_unica.urls')),
    url(r'^zeppelin/', include('djangosige.apps.opiniao.urls')),
    # url(r'^janela_unica/', include('djangosige.apps.janela_unica.urls')),
]

urlpatterns += [
    path('admin/', admin.site.urls),
]


if DEBUG is True:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
