from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangosige.apps.opiniao.models.opiniao_model import OpiniaoModel
from decimal import Decimal


class OpiniaoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(OpiniaoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = OpiniaoModel

        fields = ('nome',
                  'email',
                  'tipo',
                  'opiniao',
                  'rating',
                  'anexo',
                  )

        widgets = {

            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'size': '100'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'opiniao': forms.Textarea(attrs={'class': 'form-control', 'size': '512'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'size': '512'}),
            'anexo': forms.FileInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'nome': _('Nome'),
            'email': _('E-mail'),
            'tipo': _('O que você tem a nos dizer é uma:'),
            'opiniao': _('Sua colaboração é muito importante para nós, sinta-se em casa e nos diga:'),
            'anexo': _('Gostaria de enviar um anexo?'),
        }

    def save(self, commit=True):
        instance = super(OpiniaoForm, self).save(commit=False)
        instance.usuario = self.request_user
        if commit:
            instance.save()
        return instance