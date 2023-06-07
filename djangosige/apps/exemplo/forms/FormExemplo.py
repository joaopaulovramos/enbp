# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangosige.apps.exemplo.models import CarroModel, ExemploModel




class ExemploForm(forms.ModelForm):

    class Meta:
        model = ExemploModel
        fields = ('nome', 'apelido')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '50'}),
            'apelido': forms.TextInput(attrs={'class': 'form-control', 'size': '50'}),



        }
        labels = {
            'nome': _('Nome'),
            'apelido': _('Apelido'),
        }



class CarroForm(forms.ModelForm):

    class Meta:
        model = CarroModel
        fields = ('nome', 'placa', 'chaci',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '50'}),
            'placa': forms.TextInput(attrs={'class': 'form-control', 'size': '50'}),
            'chaci': forms.TextInput(attrs={'class': 'form-control', 'size': '50'}),


        }
        labels = {
            'nome': _('Nome'),
            'placa': _('Placa'),
            'chaci': _('Chaci'),
        }