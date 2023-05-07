# -*- coding: utf-8 -*-

from django import forms
from djangosige.apps.norli_projeto.models import *





class FilialForm(forms.ModelForm):

    class Meta:
        model = FilialModel
        fields = ('nome', 'empresa','cnpj', 'endereco', )
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': ('Nome'),
            'cnpj': ('CNPJ'),
        }






class TipoForm(forms.ModelForm):

    class Meta:
        model = TipoModel
        fields = ('nome', )
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }





class ExemploForm(forms.ModelForm):

    class Meta:
        model = ExemploModel
        fields = ('nome', 'cliente', 'tipo', 'filial', 'parcelas', 'valor_proposta', 'desconto', 'valor_final' )
        widgets = {
            'nome'    : forms.TextInput(attrs={'class': 'form-control'}),
            'cliente' : forms.Select(attrs={'class': 'form-control'}),
            'tipo'    : forms.Select(attrs={'class': 'form-control'}),
            'filial': forms.Select(attrs={'class': 'form-control'}),

            'valor_proposta': forms.TextInput(attrs={'class': 'form-control decimal-mask', 'placeholder': 'R$ 0,00'} ),
            'parcelas': forms.NumberInput(attrs={'class': 'form-control'}),

            'desconto': forms.TextInput( attrs={'class': 'form-control decimal-mask', 'placeholder': 'R$ 0,00'}),

            'valor_final' : forms.TextInput( attrs={'class': 'form-control decimal-mask', 'placeholder': 'R$ 0,00'}),

        }










