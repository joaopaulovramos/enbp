# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangosige.apps.zpfaturamento.models import *



class ClassificacaoFaturamentoForm(forms.ModelForm):

    class Meta:
        model = ClassificacaoFaturamentoModel
        fields = ('codigo', 'nome', )
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }



class ItemFaturamentoForm(forms.ModelForm):
    class Meta:
        model = ItemFaturamentoModel
        fields = ('codigo', 'nome', 'acao_no_valor', 'base_icms', 'faturar_desligados', 'exclusivo_outras_faturas', 'forma_do_valor', 'mais_de_uma_cobranca_no_mes',
                 'transferir_no_pedido_de_ligacao', 'gera_provisao', 'contabilizar', 'gera_quotas' )
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'acao_no_valor': forms.Select(attrs={'class': 'form-control'}),
            'base_icms': forms.Select(attrs={'class': 'form-control'}),
            'faturar_desligados': forms.Select(attrs={'class': 'form-control'}),
            'exclusivo_outras_faturas': forms.Select(attrs={'class': 'form-control'}),
            'forma_do_valor': forms.Select(attrs={'class': 'form-control'}),
            'mais_de_uma_cobranca_no_mes': forms.Select(attrs={'class': 'form-control'}),
            'transferir_no_pedido_de_ligacao': forms.Select(attrs={'class': 'form-control'}),
            'gera_provisao': forms.Select(attrs={'class': 'form-control'}),
            'contabilizar': forms.Select(attrs={'class': 'form-control'}),
            'gera_quotas': forms.Select(attrs={'class': 'form-control'}),
        }

