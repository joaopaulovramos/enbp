from django.contrib import admin
from django import forms
from .models import TramitacaoModel, DocumentoUnicoFinanceiro
from fsm_admin.mixins import FSMTransitionMixin


@admin.register(TramitacaoModel)
class TramitacaoModelAdmin(admin.ModelAdmin,):
    list_display = ('user_enviado', 'user_recebido', 'data', 'doc',)
    fields = ()


@admin.register(DocumentoUnicoFinanceiro)
class DocumentoUnicoFinanceiroAdmin(FSMTransitionMixin, admin.ModelAdmin):
    fsm_field = ['situacao',]
    fields = ('fornecedor', 'tipo_arquivo', 'arquivo',
              'numero', 'chave', 'mod', 'serie', 'plano_conta', 'rateio', 'observacoes', 'aprovado_gerencia', 'observacao_gerencia', 'aprovado_superintendencia', 'observacao_superintendencia', 'aprovado_diretoria', 'observacao_diretoria',)
    # Atributos de filtragem
    list_filter = ('situacao', 'tipo_arquivo')
    
    # Atributos da tabela
    list_display = ('pk', 'situacao', 'serie',)

    widgets = {
        'versao': forms.Select(attrs={'class': 'form-control'}),
        'status_nfe': forms.Select(attrs={'class': 'form-control', 'disabled': True}),
        'natop': forms.TextInput(attrs={'class': 'form-control'}),
        'indpag': forms.Select(attrs={'class': 'form-control'}),
        'mod': forms.Select(attrs={'class': 'form-control'}),
        'serie': forms.TextInput(attrs={'class': 'form-control'}),
        'dhemi': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker'}, format='%d/%m/%Y %H:%M'),
        'dhsaient': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker'}, format='%d/%m/%Y %H:%M'),
        'iddest': forms.Select(attrs={'class': 'form-control'}),
        'tp_imp': forms.Select(attrs={'class': 'form-control'}),
        'tp_emis': forms.Select(attrs={'class': 'form-control'}),
        'tp_amb': forms.Select(attrs={'class': 'form-control'}),
        'fin_nfe': forms.Select(attrs={'class': 'form-control'}),
        'ind_final': forms.Select(attrs={'class': 'form-control'}),
        'ind_pres': forms.Select(attrs={'class': 'form-control'}),
        'inf_ad_fisco': forms.Textarea(attrs={'class': 'form-control'}),
        'inf_cpl': forms.Textarea(attrs={'class': 'form-control'}),
    }
    labels = {
        'versao': ('Versão'),
        'status_nfe': ('Status'),
        'natop': ('Natureza da Operação'),
        'indpag': ('Forma de pagamento'),
        'mod': ('Modelo'),
        'serie': ('Série'),
        'dhemi': ('Data e hora de emissão'),
        'dhsaient': ('Data e hora de Saída/Entrada'),
        'iddest': ('Destino da operação'),
        'tp_imp': ('Tipo impressão da DANFE'),
        'tp_emis': ('Forma de emissão'),
        'tp_amb': ('Ambiente'),
        'fin_nfe': ('Finalidade da emissão'),
        'ind_final': ('Consumidor final'),
        'ind_pres': ('Tipo de atendimento'),
        'inf_ad_fisco': ('Informações Adicionais de Interesse do Fisco'),
        'inf_cpl': ('Informações Complementares de interesse do Contribuinte'),
    }
