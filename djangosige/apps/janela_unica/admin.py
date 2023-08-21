from operator import is_
from typing import Any, List, Optional, Tuple, Type, Union
from django.contrib import admin
from django import forms
from django.contrib.admin.sites import AdminSite
from django.http import HttpResponseRedirect
from django.http.request import HttpRequest
from django.utils.safestring import mark_safe
from django.contrib.admin.options import csrf_protect_m

# from djangosige.apps.janela_unica.forms.Form import DocumentoUnicoFinanceiroForm
from djangosige.apps.janela_unica.models.Models import AprovadorContrato, AvaliacaoDocumentoUnico, Contrato, StatusAnaliseFinaceira, TipoContrato, ArquivoSolicitacaoContrato
from djangosige.apps.login.models import Usuario
from .models import TramitacaoModel, DocumentoUnicoFinanceiro, ArquivoDocumentoUnico
from fsm_admin.mixins import FSMTransitionMixin
from simple_history.admin import SimpleHistoryAdmin
from django.utils.html import format_html




class NorliAdminModelForm(forms.ModelForm):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            # print(visible)
            visible.field.widget.attrs['class'] = 'form-control'
            if isinstance(visible.field.widget, admin.widgets.RelatedFieldWidgetWrapper):
                visible.field.widget.widget.attrs['class'] = 'form-control'
                # visible.field.widget.can_add_related=False
                visible.field.widget.can_change_related = False
                visible.field.widget.can_delete_related = False


class TipoContratoForm(NorliAdminModelForm):
    class Meta:
        model = TipoContrato
        fields = '__all__'
        verbose_name = 'Tipo de Contrato'
        verbose_name_plural = 'Tipos de Contratos'


@admin.register(TipoContrato)
class TipoContratoModelAdmin(admin.ModelAdmin,):
    form = TipoContratoForm
    list_display = ('descricao',)
    fields = ('descricao',)


class AprovadorContratoInline(admin.TabularInline):
    model = AprovadorContrato
    extra = 0
    max_num = 10
    fields = ('sequencia', 'descricao', 'usuario',),
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        can_delete = True
        classes = ['replace-input-css',]
        widgets = {
            'sequencia': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }

    def __str__(self):
        return u'%s - %s' % (self.pk, self.descricao,)

class ArquivoSolicitacaoContratoInline(admin.TabularInline):
    model = ArquivoSolicitacaoContrato
    extra = 0
    max_num = 10


class ContratoForm(NorliAdminModelForm):
    class Meta:
        model = Contrato
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'detalhe_pagamento': forms.Textarea(attrs={'class': 'form-control'}),
            'data_inclusao': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control datepicker'}),
            'data_validade': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control datepicker'}),
        }
        labels = {
            'pk': 'Nº Contrato',
        }


@admin.register(Contrato)
class ContratoModelAdmin(FSMTransitionMixin, SimpleHistoryAdmin):
    fsm_field = ['situacao',]
    form = ContratoForm
    actions = None
    list_display = ('pk', 'fornecedor', 'descricao', 'data_inclusao', 'data_validade', 'valor_total')
    list_filter = ('fornecedor','data_validade')
    inlines = [AprovadorContratoInline, ArquivoSolicitacaoContratoInline,]
    
    class Media:
        js = ['admin/js/jquery.init.js', 'js/replace-input-css.js']
        # css = {
        #     'all': ('css/janela-unica.css',)
        # }


    def formfield_for_dbfield(self, *args, **kwargs):
        formfield = super().formfield_for_dbfield(*args, **kwargs)
        formfield.widget.can_delete_related = False
        formfield.widget.can_change_related = False
        formfield.widget.can_add_related = False
        return formfield
    
    fieldsets = (
        ('Dados contrato', {
            'fields': (
                ('empresa', 'fornecedor'),
                'descricao',
                ('data_validade', 'valor_total', 'arquivo',),
                ('forma_pagamento', 'detalhe_pagamento', ),
            ),
            # 'classes': ('formset-box',),
        }),
        # ('Avaliadores', {
        #     'fields': (),
        #     'classes': ('replacein', AprovadorContratoInline.__name__),
        # }),
        # ('Documentos para pagamento', {
        #     'fields': (),
        #     'classes': ('replacein', ArquivoSolicitacaoContrato.__name__),
        # }),
    )

from .admin_documento_unico import *
