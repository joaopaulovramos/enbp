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

    # Atributos de filtragem
    list_filter = ('situacao', 'tipo_arquivo')
    search_fields = ('pk', 'serie',)
    # Atributos da tabela
    list_display = ('pk', 'situacao', 'serie',)

    def get_readonly_fields(self, request, obj=None):
        # Se é um novo registro ou retorno para edicação do responsavel todos os campos estarão disponíveis para edição, exceto os de aprovação
        if not obj or not obj.situacao or obj.situacao in [StatusAnaliseFinaceira.EDICAO_RESPONSAVEL]:
            return ['aprovado_gerencia', 'observacao_gerencia', 'aprovado_superintendencia', 'observacao_superintendencia', 'aprovado_diretoria', 'observacao_diretoria',
            'aprovado_analise_financeira', 'observacao_analise_financeira',
            'aprovado_analise_fiscal', 'observacao_analise_fiscal',]

        ret = ['fornecedor',
               'tipo_arquivo', 'arquivo', 'numero', 'chave', 'mod', 'serie',
               'plano_conta', 'rateio', 'observacoes', 'aprovado_gerencia', 
               'observacao_gerencia', 'aprovado_superintendencia', 
               'observacao_superintendencia', 'aprovado_diretoria','observacao_diretoria', 'aprovado_analise_financeira', 'observacao_analise_financeira',
               'aprovado_analise_fiscal', 'observacao_analise_fiscal'
        ]

        # Se o status for aprovado, todos os campos estarão disponíveis para edição
        if obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_GERENCIA:
            ret.remove('observacao_gerencia')
        elif obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_SUPERITENDENCIA:
            ret.remove('observacao_superintendencia')
        elif obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_DIRETORIA:
            ret.remove('observacao_diretoria')
        elif obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL:
            ret.remove('observacao_analise_financeira')
        elif obj.siutacao == StatusAnaliseFinaceira.APROVADO_ANALISE_FINANCEIRA:
            ret.remove('observacao_analise_fiscal')
        return ret
