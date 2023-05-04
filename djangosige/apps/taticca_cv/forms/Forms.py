# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangosige.apps.taticca_cv.models import CVModel, CertificadoModel





class CertificadoForm(forms.ModelForm):

    class Meta:
        model = CertificadoModel

        fields = ('nome', 'file',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': _('Nome'),
            'file': _('Certificado'),
        }




class CVForm(forms.ModelForm):

    class Meta:
        model = CVModel
        fields = ('nome', 'telefone', 'email', 'cpf',
                  'inf_adicionais', 'cargo', 'nome_cv_executivo', 'cv_executivo',
                  'nome_cv_padrao', 'telefone_cv_padrao', 'endereco_cv_padrao',
                  'email_cv_padrao', 'perfil_cv_padrao', 'foto',  )
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'size': '50'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'size': '11'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control', 'size': '11'}),
            'inf_adicionais': forms.Textarea(attrs={'class': 'form-control'}),

            'cargo': forms.TextInput(attrs={'class': 'form-control', 'size': '10'}),
            'cv_executivo':  forms.Textarea(attrs={'class': 'form-control'}),
            'nome_cv_executivo': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),

            'nome_cv_padrao': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'telefone_cv_padrao': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'endereco_cv_padrao': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'email_cv_padrao': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'perfil_cv_padrao':  forms.Textarea(attrs={'class': 'form-control'}),

            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': _('Nome'),
            'inf_adicionais': _('Informações Adicionais'),
            'cpf': _('CPF'),
            'senha': _('Senha de Acesso'),

            'nome_cv_executivo':_('Nome (será exibido na proposta)'),
            'cargo': _('Cargo (será exibido na proposta'),
            'cv_executivo': _('Currículo Executivo'),

            'nome_cv_padrao': _('Nome (será exibido no CV Gerado)'),
            'telefone_cv_padrao': _('Telefone (será exibido no CV Gerado)'),
            'endereco_cv_padrao': _('Endereço (será exibido no CV Gerado)'),
            'email_cv_padrao': _('E-mail (será exibido no CV Gerado)'),
            'perfil_cv_padrao': _('Perfil Profissional'),

        }



