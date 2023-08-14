from django.contrib import admin
from django import forms
from django.http.request import HttpRequest
from django.utils.safestring import mark_safe

from djangosige.apps.financeiro.models.plano import PlanoContasGrupo, PlanoContasSubgrupo


@admin.register(PlanoContasGrupo)
class PlanoContasGrupoAdmin(admin.ModelAdmin,):
    list_display = ('codigo_legado', 'codigo', 'tipo_grupo', 'descricao', 'observacao')
    fields = ('codigo_legado', 'codigo', 'tipo_grupo', 'descricao', 'observacao')
    list_filter = ('tipo_grupo',)
    readonly_fields = ('codigo_legado', 'codigo')
    widget = {
        'codigo': forms.TextInput(attrs={'class': 'form-control'}),
    }


@admin.register(PlanoContasSubgrupo)
class PlanoContasSubgrupoAdmin(admin.ModelAdmin,):
    list_display = ('codigo_legado', 'codigo', 'grupo', 'tipo_grupo', 'descricao', 'observacao')
    fields = ('codigo', 'grupo', 'tipo_grupo', 'descricao',)
    readonly_fields = ('codigo_legado', 'codigo')
    list_filter = ('tipo_grupo',)
