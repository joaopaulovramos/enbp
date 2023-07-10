
from django import forms
from djangosige.apps.janela_unica.models import *
from django.utils.translation import ugettext_lazy as _

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = DocumentoModel
        fields = ('nome',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),

        }
        labels = {
            'nome': _('Descrição'),
        }
