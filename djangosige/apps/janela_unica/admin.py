from django.contrib import admin
from django import forms

from djangosige.apps.janela_unica.forms.Form import DocumentoUnicoFinanceiroForm
from djangosige.apps.janela_unica.models.Models import StatusAnaliseFinaceira
from .models import TramitacaoModel, DocumentoUnicoFinanceiro
from fsm_admin.mixins import FSMTransitionMixin


@admin.register(TramitacaoModel)
class TramitacaoModelAdmin(admin.ModelAdmin,):
    list_display = ('user_enviado', 'user_recebido', 'data', 'doc',)
    fields = ()


@admin.register(DocumentoUnicoFinanceiro)
class DocumentoUnicoFinanceiroAdmin(FSMTransitionMixin, admin.ModelAdmin):
    fsm_field = ['situacao',]
    form = DocumentoUnicoFinanceiroForm
    # Desabilita as ações em massa
    actions = None
    # Atributos de filtragem
    list_filter = ('situacao', )
    search_fields = ('situacao',)
    # Atributos da tabela
    list_display = ('pk', 'descricao', 'situacao', 'data_inclusao', 'data_finalizacao', 'tipo_arquivo', 'numero', 'responsavel', 'fornecedor', 'valor_total',)

    def has_delete_permission(self, request, obj=None):
        return False

    # TODO: Ajustar aqui
    fieldsets = (
        ('Dados solicitação', {
            'fields': ('pk', 'data_inclusao', 'responsavel',
                       'tipo_arquivo', 'tipo_anexo','arquivo',)
        }),

        ('Dados bancários', {
            'fields': ('banco', 'agencia', 'conta', 'digito',
                       'plano_conta', 'projeto')
        }),

        ('Informações financeiras', {
            'fields': ('possui_parcelamento', 'extra_orcamentaria',
                       'possui_contrato', 'antecipacao_pagamento', 'pagamento_boleto')
        }),


        ('Aprovadores', {
            'fields': (
                'aprovado_gerencia', 'usuario_gerencia', 'observacao_gerencia', 'aprovado_superintendencia', 'usuario_superintencencia', 'observacao_superintendencia', 
                'aprovado_diretoria', 'usuario_diretoria','observacao_diretoria', 
                'aprovado_analise_financeira', 'usuario_analise_financeira','observacao_analise_financeira', 
                'aprovado_analise_fiscal', 'usuario_analise_fiscal','observacao_analise_fiscal')
        }),

        ('Lançamento no Questor', {
            'fields': ('usuario_lancamento', 'data_lancamento', 'numero_lancamento')
        }),
        
        ('Analise financeira', {
            'fields': ('pagamento_realizado', 'observacao_pagamento')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        ret = ['pk', 'responsavel', 'data_inclusao']
        # Se é um novo registro ou retorno para edicação do responsavel todos os campos estarão disponíveis para edição, exceto os de aprovação
        if not obj or not obj.situacao or obj.situacao in [StatusAnaliseFinaceira.EDICAO_RESPONSAVEL]:
            ret.extend(['aprovado_gerencia', 'observacao_gerencia', 'aprovado_superintendencia', 'observacao_superintendencia', 'aprovado_diretoria', 'observacao_diretoria',
                        'aprovado_analise_financeira', 'observacao_analise_financeira',
                        'aprovado_analise_fiscal', 'observacao_analise_fiscal',])
            return ret

        ret.extend(['fornecedor',
                    'tipo_arquivo', 'arquivo', 'numero', 'chave', 'mod', 'serie',
                    'plano_conta', 'rateio', 'observacoes', 'aprovado_gerencia',
                    'observacao_gerencia', 'aprovado_superintendencia',
                    'observacao_superintendencia', 'aprovado_diretoria', 'observacao_diretoria', 'aprovado_analise_financeira', 'observacao_analise_financeira',
                    'aprovado_analise_fiscal', 'observacao_analise_fiscal',
                    ])

        # Se o status for aprovado, todos os campos estarão disponíveis para edição
        if obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_GERENCIA:
            ret.remove('observacao_gerencia')
        elif obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_SUPERITENDENCIA:
            ret.remove('observacao_superintendencia')
        elif obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_DIRETORIA:
            ret.remove('observacao_diretoria')
        elif obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL:
            ret.remove('observacao_analise_fiscal')
        elif obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA:
            ret.remove('observacao_analise_financeira')
        return ret