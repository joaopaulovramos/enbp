

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


class TramitacaoForm(forms.ModelForm):
    class Meta:
        model = TramitacaoModel
        fields = ('user_recebido', 'doc',)

        widgets = {

            'user_recebido': forms.Select(attrs={'class': 'form-control'}),
            'doc': forms.Select(attrs={'class': 'form-control'}),

        }


        labels = {
            'user_recebido': _('Enviar Para'),
            'doc': _('Documento'),
        }

# https://stackoverflow.com/questions/47113794/add-css-class-to-all-admin-form-field


class DocumentoUnicoFinanceiroForm(forms.ModelForm):
    class Meta:
        model = DocumentoUnicoFinanceiro
        fields = (
            'responsavel', 'descricao', 'fornecedor',
            # Dados arquivo
            'tipo_arquivo', 'arquivo',
            # Dados Notas
            'numero', 'chave', 'mod', 'serie',
            # Dados financeiros
            'plano_conta', 'rateio', 'observacoes',
            # Dados bancarios
            'banco', 'agencia', 'conta', 'digito',
            #projeto
            'projeto', 'cnpj',
            # Aprovações
            'aprovado_gerencia', 'observacao_gerencia', 'aprovado_superintendencia', 'observacao_superintendencia', 'aprovado_diretoria', 'observacao_diretoria',
            'aprovado_analise_financeira', 'observacao_analise_financeira',
            'aprovado_analise_fiscal', 'observacao_analise_fiscal',
        )

        widgets = {

            'projeto': forms.Select(attrs={'class': 'form-control'}),
            'plano_conta': forms.Select(attrs={'class': 'form-control'}),
            'fornecedor': forms.Select(attrs={'class': 'form-control'}),
            'responsavel' : forms.Select(attrs={'class': 'form-control'}),

        }


    # TODO: Melhorar isso, gambiarra para funcionar o form-control
    # https://stackoverflow.com/questions/48067882/django-admin-making-a-required-field-read-only
    def __init__(self, *args, **kwargs):
        super(DocumentoUnicoFinanceiroForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            # print(visible.field)
            visible.field.widget.attrs['class'] = 'form-control'
