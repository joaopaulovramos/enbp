from django.contrib import admin
from django import forms

from djangosige.apps.janela_unica.forms.Form import DocumentoUnicoFinanceiroForm
from djangosige.apps.janela_unica.models.Models import StatusAnaliseFinaceira
from .models import TramitacaoModel, DocumentoUnicoFinanceiro
from fsm_admin.mixins import FSMTransitionMixin
from simple_history.admin import SimpleHistoryAdmin
from django.utils.html import format_html


@admin.register(TramitacaoModel)
class TramitacaoModelAdmin(admin.ModelAdmin,):
    list_display = ('user_enviado', 'user_recebido', 'data', 'doc',)
    fields = ()

# https://stackoverflow.com/questions/46892851/django-simple-history-displaying-changed-fields-in-admin


@admin.register(DocumentoUnicoFinanceiro)
class DocumentoUnicoFinanceiroAdmin(FSMTransitionMixin, SimpleHistoryAdmin):
    fsm_field = ['situacao',]
    form = DocumentoUnicoFinanceiroForm
    # Desabilita as ações em massa
    actions = None
    # Atributos de filtragem
    list_filter = ('situacao', 'data_inclusao')
    search_fields = ('situacao',)
    # Atributos da tabela
    list_display = ('pk', 'descricao', 'situacao', 'data_inclusao', 'data_finalizacao', 'tipo_arquivo', 'numero', 'responsavel', 'fornecedor', 'valor_total',)

    history_list_display = ["changed_fields", "list_changes"]

    def changed_fields(self, obj):
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)
            return delta.changed_fields
        return None

    def list_changes(self, obj):
        fields = ""
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)

            for change in delta.changes:
                fields += str("<strong>{}</strong> de <span style='background-color:#ffb5ad'>{}</span> para <span style='background-color:#b3f7ab'>{}</span> . <br/>".format(change.field, change.old, change.new))
            return format_html(fields)
        return None

    def has_delete_permission(self, request, obj=None):
        return False

    # TODO: Ajustar aqui
    fieldsets = (
        ('Dados solicitação', {
            'fields': (
                ('pk', 'data_inclusao', 'responsavel'),
                ('tipo_arquivo', 'tipo_anexo', 'arquivo', 'observacoes'),
                ('chave', 'numero', 'serie', 'cfop'),
                ('cnpj', 'data_emissao', 'valor_total'),
                'descricao'
            ),
            'classes': ({
                'pk': 'sm-3',
            })
        }),

        ('Dados pagamento', {
            'fields': (
                ('fornecedor', 'plano_conta', 'projeto'),
                ('banco', 'agencia', 'conta', 'digito')
            )
        }),

        ('Informações financeiras', {
            'fields': (
                ('possui_parcelamento', 'extra_orcamentaria',
                       'possui_contrato', 'antecipacao_pagamento', 'pagamento_boleto'),
                )
        }),


        ('Aprovadores', {
            'fields': (
                ('aprovado_gerencia', 'usuario_gerencia', 'observacao_gerencia'),

                ('aprovado_superintendencia', 'usuario_superintencencia', 'observacao_superintendencia'),

                ('aprovado_diretoria', 'usuario_diretoria', 'observacao_diretoria')
            )
        }),

        ('Analise fiscal e lançamento questor', {
            'fields': (
                ('aprovado_analise_fiscal', 'usuario_analise_fiscal', 'observacao_analise_fiscal'),
                ('usuario_lancamento', 'data_lancamento', 'numero_lancamento', 'comprovante_lancamento')
            )
        }),

        ('Analise financeira e pagamento', {
            'fields': (
                ('aprovado_analise_financeira', 'usuario_analise_financeira', 'observacao_analise_financeira'),
                ('pagamento_realizado', 'observacao_pagamento', 'comprovante_pagamento')
            )
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        ret = ['pk', 'responsavel', 'data_inclusao']
        # Se é um novo registro ou retorno para edicação do responsavel todos os campos estarão disponíveis para edição, exceto os de aprovação
        if not obj or not obj.situacao or obj.situacao in [StatusAnaliseFinaceira.EDICAO_RESPONSAVEL]:
            ret.extend(['aprovado_gerencia', 'usuario_gerencia', 'observacao_gerencia', 'aprovado_superintendencia', 'usuario_superintencencia', 'observacao_superintendencia',
                        'aprovado_diretoria', 'usuario_diretoria', 'observacao_diretoria',
                        'aprovado_analise_financeira', 'usuario_analise_financeira', 'observacao_analise_financeira',
                        'aprovado_analise_fiscal', 'usuario_analise_fiscal', 'observacao_analise_fiscal', 'usuario_lancamento', 'data_lancamento', 'numero_lancamento', 'pagamento_realizado', 'observacao_pagamento', 'comprovante_pagamento', 'comprovante_lancamento'])
            return ret

        ret.extend(['fornecedor', 'observacoes', 'descricao',
                    'tipo_arquivo', 'tipo_anexo', 'valor_total', 'arquivo', 'numero', 'chave', 'mod', 'serie',
                    'plano_conta', 'rateio', 'observacoes', 'aprovado_gerencia',
                    'observacao_gerencia', 'aprovado_superintendencia',
                    'observacao_superintendencia', 'aprovado_diretoria', 'observacao_diretoria', 'aprovado_analise_financeira', 'observacao_analise_financeira',
                    'aprovado_analise_fiscal', 'observacao_analise_fiscal',
                    'usuario_lancamento', 'data_lancamento', 'numero_lancamento', 'pagamento_realizado', 'observacao_pagamento', 'usuario_gerencia', 'usuario_diretoria', 'usuario_superintencencia', 'usuario_analise_financeira', 'usuario_analise_fiscal', 'possui_parcelamento', 'possui_contrato', 'extra_orcamentaria', 'antecipacao_pagamento', 'pagamento_boleto', 'banco', 'agencia', 'conta', 'digito', 'projeto', 'chave', 'numero', 'mod', 'serie', 'cnpj', 'data_emissao', 'cfop', 'comprovante_pagamento', 'comprovante_lancamento',
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
            ret.remove('usuario_lancamento')
            ret.remove('data_lancamento')
            ret.remove('numero_lancamento')
            ret.remove('comprovante_lancamento')
        elif obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA:
            ret.remove('observacao_analise_financeira')
            ret.remove('pagamento_realizado')
            ret.remove('observacao_pagamento')
            ret.remove('compromante_pagamento')
        return ret
