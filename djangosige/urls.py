# -*- coding: utf-8 -*-
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from .configs.settings import DEBUG, MEDIA_ROOT, MEDIA_URL


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

]

# Papermerge

from django.conf import settings
from django.views.generic.base import RedirectView
from django.views.i18n import JavaScriptCatalog
from papermerge.contrib.admin.views import browse as index_view

js_info_dict = {
    'domain': 'django',
    'packages': None,
}

favicon_view = RedirectView.as_view(
    url='/static/admin/img/favicon.ico',
    permanent=True
)

urlpatterns += [
    re_path(r'favicon\.ico$', favicon_view),
    path('accounts/', include('allauth.urls')),
    path(
        'jsi18n/',
        JavaScriptCatalog.as_view(),
        js_info_dict,
        name='javascript-catalog'
    ),
    path('admin/', include('papermerge.contrib.admin.urls')),
    path('', include('papermerge.core.urls')),
    path('', index_view, name='index')
]

if DEBUG is True:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
