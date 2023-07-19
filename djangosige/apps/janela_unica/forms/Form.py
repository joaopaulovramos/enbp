

from djangosige.apps.janela_unica.models import *
from django.utils.translation import ugettext_lazy as _
from django import forms

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = DocumentoModel
        fields = ('nome', 'file',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'nome': _('Descrição'),
            'file': _('Documento'),
        }




class   TramitacaoForm(forms.ModelForm):
    class Meta:
        model = TramitacaoModel
        fields = ('user_recebido', 'doc',)
        widgets = {
            'user_recebido':  forms.Select(attrs={'class': 'form-control'}),
            'doc':  forms.Select(attrs={'class': 'form-control'}),

        }
        labels = {
            'user_recebido': _('Enviar Para'),
            'doc': _('Documento'),
        }



