# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
import datetime
from djangosige.apps.orcamento.models import *


class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = OrcamentoModel
        fields = ('nome',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),

        }
        labels = {
            'nome': _('Descrição'),
        }