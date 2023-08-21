from operator import is_
from typing import Any, List, Optional, Tuple, Type, Union
from django.contrib import admin
from django import forms
from django.contrib.admin.sites import AdminSite
from django.http import HttpResponseRedirect
from django.http.request import HttpRequest
from django.utils.safestring import mark_safe
from django.contrib.admin.options import csrf_protect_m
from djangosige.apps.janela_unica.admin import NorliAdminModelForm

# from djangosige.apps.janela_unica.forms.Form import DocumentoUnicoFinanceiroForm
from djangosige.apps.janela_unica.models.Models import AprovadorContrato, AvaliacaoDocumentoUnico, Contrato, StatusAnaliseFinaceira, TipoContrato, ArquivoSolicitacaoContrato
from .models import TramitacaoModel, DocumentoUnicoFinanceiro, ArquivoDocumentoUnico
from fsm_admin.mixins import FSMTransitionMixin
from simple_history.admin import SimpleHistoryAdmin
from django.utils.html import format_html



# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.InlineModelAdmin.form
# class ArquivoDocumentoUnicoInline(admin.StackedInline):

class AvaliacaoDocumentoUnicoForm(NorliAdminModelForm):
    model = AvaliacaoDocumentoUnico
    class Meta:
        model = AvaliacaoDocumentoUnico
        fields = ['sequencia', 'descricao', 'usuario_avaliador', 'observacao', 'aprovado']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            if self.instance and self.instance.documento_unico:
                if self.instance.documento_unico.situacao in [StatusAnaliseFinaceira.AGUARDANDO_AVALIACAO]:
                    ap = self.instance.documento_unico.aprovacao_atual()
                    if ap != self.instance:
                        self.fields['observacao'].widget.attrs['readonly'] = 'readonly'
        except:
            pass

class AvaliacaoDocumentoUnicoInline(admin.TabularInline):
    model = AvaliacaoDocumentoUnico
    form = AvaliacaoDocumentoUnicoForm
    extra = 0
    max_num = 10
    fields = ['sequencia', 'descricao', 'usuario_avaliador', 'observacao', 'aprovado']
    class Meta:
        verbose_name = 'Arquivo do Documento'
        verbose_name_plural = 'Arquivos do Documento'
        fields = ['sequencia', 'descricao', 'usuario_avaliador', 'observacao', 'aprovado']
        can_delete = False
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        ret = ['sequencia', 'descricao', 'usuario_avaliador', 'observacao', 'aprovado']
        #  Tentar isso: https://stackoverflow.com/questions/70340853/how-to-make-some-django-inlines-read-only
        
        if obj and obj.situacao in [StatusAnaliseFinaceira.AGUARDANDO_AVALIACAO] and obj.pode_aprovar(request.user):    #and request.user == obj.usuario_avaliador :
            ret.remove('observacao')
        return ret

#https://stackoverflow.com/questions/20339520/django-admin-default-values-in-stackedinline-tabularinline

class ArquivoDocumentoUnicoInline(admin.TabularInline):
    model = ArquivoDocumentoUnico
    extra = 0
    max_num = 10
    fields = ['descricao', 'arquivo',]

    class Meta:
        verbose_name = 'Arquivo do Documento'
        verbose_name_plural = 'Arquivos do Documento'
        can_delete = True
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'arquivo': forms.FileInput(attrs={'class': 'form-control'}),
        }

    # def __init__(self, parent_model: type | Any, admin_site: AdminSite) -> None:
    #     super().__init__(parent_model, admin_site)

    def has_add_permission(self, request, obj=None):
        # if obj and obj.contrato and obj.situacao in [StatusAnaliseFinaceira.EDICAO_RESPONSAVEL]:
        #     return True
        return False

    def get_readonly_fields(self, request, obj=None):
        ret = ['descricao',]
        # Se é um novo registro ou retorno para edicação do responsavel todos os campos estarão disponíveis para edição, exceto os de aprovação
        if obj and not obj.situacao in [StatusAnaliseFinaceira.EDICAO_RESPONSAVEL, StatusAnaliseFinaceira.DEVOLVIDO_RESPONSAVEL]:
            ret.extend(['arquivo',])
        return ret

    def __str__(self):
        return u'%s - %s' % (self.pk, self.descricao,)

class DocumentoUnicoFinanceiroForm(NorliAdminModelForm):
    def clean(self):
        contrato = self.cleaned_data.get('contrato')
        # if not contrato:
        #     raise forms.ValidationError("Contrato é obrigatorio")
        return self.cleaned_data

    class Meta:
        model = DocumentoUnicoFinanceiro
        fields = '__all__'

        labels = {
            'pk': 'Solicitação',
            'data_inclusao': 'Data de Inclusão',
            'data_emissao': 'Data de Emissão',
            'plano_conta': 'Centro de custos',
            'fornecedor': 'Fornecedor/funcionário',
        }

        widgets = {
            'data_emissao': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control datepicker'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'observacao_gerencia': forms.Textarea(attrs={'class': 'form-control'}),
            'observacao_superintendencia': forms.Textarea(attrs={'class': 'form-control'}),
            'observacao_diretoria': forms.Textarea(attrs={'class': 'form-control'}),
            'observacao_analise_financeira': forms.Textarea(attrs={'class': 'form-control'}),
            'observacao_analise_orcamentaria': forms.Textarea(attrs={'class': 'form-control'}),
            'observacao_analise_fiscal': forms.Textarea(attrs={'class': 'form-control'}),
        }


# https://stackoverflow.com/questions/46892851/django-simple-history-displaying-changed-fields-in-admin


@admin.register(DocumentoUnicoFinanceiro)
class DocumentoUnicoFinanceiroAdmin(FSMTransitionMixin, SimpleHistoryAdmin):
    actions = ['aprovar']

    def aprovar(self, request, object_id):
        msg = "Aprovado Objeto {}".format(object_id)
        self.message_user(request, msg)

    aprovar.short_description = "Aprovar solicitação"

    @csrf_protect_m
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        # print('change form view')
        if request.method == 'POST' and '_aprovar' in request.POST:
            # obj = self.get_object(request, unquote(object_id))
            self.make_published(request, object_id)
            return HttpResponseRedirect(request.get_full_path())

        return admin.ModelAdmin.changeform_view(
            self, request,
            object_id=object_id,
            form_url=form_url,
            extra_context=extra_context,
        )


    def save_model(self, request, obj, form, change):
        if not obj.responsavel:
            obj.responsavel = request.user.usuario
        if obj.contrato:
            obj.fornecedor = obj.contrato.fornecedor
            obj.empresa = obj.contrato.empresa
        super().save_model(request, obj, form, change)
        if obj.contrato and not ArquivoDocumentoUnico.objects.filter(documento_unico=obj).exists():
            documentos_contrato = ArquivoSolicitacaoContrato.objects.filter(contrato=obj.contrato)
            # documentos_contrato = obj.contrato.arquivosolicitacaocontrato_set.all()
            for ar in documentos_contrato:
                ArquivoDocumentoUnico.objects.create(documento_unico=obj,
                                                     descricao=ar.descricao,
                                                     #arquivo=ar.arquivo
                                                     )
            avalidadores_contrato = AprovadorContrato.objects.filter(contrato=obj.contrato)
            for av in avalidadores_contrato:
                AvaliacaoDocumentoUnico.objects.create(sequencia=av.sequencia,
                                                       usuario_avaliador=av.usuario,
                                                       descricao=av.descricao,
                                                       documento_unico=obj)


    fsm_field = ['situacao',]
    form = DocumentoUnicoFinanceiroForm
    # Desabilita as ações em massa
    # actions = None
    # Atributos de filtragem
    list_filter = ('situacao', 'data_inclusao', 'projeto', 'plano_conta', 'tipo_arquivo', 'contrato')
    search_fields = ('situacao',)
    # Atributos da tabela
    list_display = ('pk', 'descricao', 'situacao', 'data_inclusao', 'data_finalizacao', 'tipo_arquivo', 'responsavel', 'contrato', 'fornecedor', 'projeto', 'valor_total',) #'plano_conta', 

    history_list_display = ["changed_fields", "list_changes"]

    # def has_change_permission(self, request, obj=None):
    #     retorno = super().has_change_permission(request, obj)
    #     return True

    class Media:
        css = {
            'all': ('css/janela-unica.css',)
        }
        js = ['admin/js/jquery.init.js', 'js/janela-unica.js']

    # TODO: Ajustar aqui
    fieldsets = (
        ('Dados solicitação', {
            'fields': (
                ('pk', 'situacao', 'data_inclusao', 'responsavel'),
                ('contrato', 'fornecedor', 'observacoes'),
                ('empresa', 'plano_conta', 'projeto'),
                ('tipo_arquivo', 'arquivo', ),
                ('data_emissao', 'valor_total'),

                # ('chave', 'numero', 'serie', 'cfop'),
                # ('cnpj', 'data_emissao', 'valor_total'),
                'descricao',
            ),
            # 'classes': ('formset-box',),
        }),
        # ('Arquivos adicionais', {

        ('Informações financeiras', {
            'fields': (
                ('possui_parcelamento', 'extra_orcamentaria',
                 'possui_contrato', 'antecipacao_pagamento', 'pagamento_boleto'),
            )
        }),


        (None, {
            'fields': (),
            'classes': ('documento_unico_arquivo-group',),
        }),


        (None, {
            'fields': (),
            'classes': ('documento_unico_avaliacao-group',),
        }),


        # ('Aprovadores', {
        #     'fields': (
        #         ('aprovado_gerencia', 'usuario_gerencia', 'observacao_gerencia'),

        #         ('aprovado_superintendencia', 'usuario_superintencencia', 'observacao_superintendencia'),

        #         ('aprovado_diretoria', 'usuario_diretoria', 'observacao_diretoria')
        #     )
        # }),
        ('Analise orçamentária', {
            'fields': (
                ('aprovado_analise_orcamentaria', 'usuario_analise_orcamentaria', 'observacao_analise_orcamentaria'),
            )
        }),


        ('Analise fiscal e lançamento questor', {
            'fields': (
                ('aprovado_analise_fiscal', 'usuario_analise_fiscal', 'observacao_analise_fiscal'),
                # ('data_analise_fiscal', 'valor_retencao', 'valor_liquido',),
                ('usuario_lancamento', 'data_lancamento', 'numero_lancamento', 'comprovante_lancamento')
            )
        }),


        ('Financeiro - Dados pagamento', {
            'fields': (
                ('conta_pagadora', 'conta_recebedora'),
                ('descricacao_pagamento', 'data_vencimento', 'data_pagamento'),
                ('documento_remessa_pagamento', 'forma_pagamento',),
                ('moeda_pagamento', 'data_cotacao', 'cotacao'),
                ('valor_bruto', 'valor_desconto', 'valor_juros', 'valor_juros_mora'),
                ('valor_multa', 'valor_retencao', 'valor_outros','valor_liquido',)
            )
        }),

        ('Analise financeira e pagamento', {
            'fields': (
                ('aprovado_analise_financeira', 'usuario_analise_financeira', 'observacao_analise_financeira'),
                ('pagamento_realizado', 'observacao_pagamento', 'comprovante_pagamento')
            )
        }),


        ('Processamento Financeiro', {
            'fields': (
                ('aprovado_processamento_financeiro', 'usuario_processamento_financeiro', 'observacao_processamento_financeiro'),
                # ('pagamento_realizado', 'observacao_pagamento', 'comprovante_pagamento')
            )
        }),

        ('Retorno Financeiro', {
            'fields': (
                ('observacao_retorno_financeiro', 'comprovante_retorno')
            )
        }),
    )

    inlines = [ArquivoDocumentoUnicoInline, AvaliacaoDocumentoUnicoInline,]

    def formfield_for_dbfield(self, *args, **kwargs):
        formfield = super().formfield_for_dbfield(*args, **kwargs)

        formfield.widget.can_delete_related = False
        formfield.widget.can_change_related = False
        formfield.widget.can_add_related = False  # can change this, too
        # formfield.widget.can_view_related = False  # can change this, too
        return formfield

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

    def get_readonly_fields(self, request, obj=None):
        ret = ['pk', 'situacao', 'responsavel', 'data_inclusao', 'fornecedor', 'empresa']
        # Se é um novo registro ou retorno para edicação do responsavel todos os campos estarão disponíveis para edição, exceto os de aprovação
        #FIXME: Bloqueando a alteração do contrato para decidir 
        # o que fazer com a cadeia de aprovação e de arquivos
        if obj and obj.contrato:
            ret.extend(['contrato'])
        if not obj or not obj.situacao or obj.situacao in [StatusAnaliseFinaceira.EDICAO_RESPONSAVEL, StatusAnaliseFinaceira.DEVOLVIDO_RESPONSAVEL]:
            ret.extend(['aprovado_gerencia', 'usuario_gerencia', 'observacao_gerencia', 'aprovado_superintendencia', 'usuario_superintencencia', 'observacao_superintendencia',
                        'aprovado_diretoria', 'usuario_diretoria', 'observacao_diretoria',
                        'aprovado_analise_financeira', 'usuario_analise_financeira', 'observacao_analise_financeira',
                        'aprovado_analise_fiscal', 'usuario_analise_fiscal', 'observacao_analise_fiscal', 'usuario_lancamento', 'data_lancamento', 'numero_lancamento', 'pagamento_realizado', 'observacao_pagamento',
                        'valor_retencao', 'valor_liquido',
                        'comprovante_pagamento', 'comprovante_lancamento',
                        'conta_pagadora', 'conta_recebedora', 'descricacao_pagamento', 'data_vencimento', 'data_pagamento', 'documento_remessa_pagamento', 'forma_pagamento', 'moeda_pagamento', 'data_cotacao', 'cotacao','valor_bruto', 'valor_desconto', 'valor_juros', 'valor_juros_mora', 'valor_multa', 'valor_outros', 'valor_liquido',
                        'aprovado_processamento_financeiro', 'usuario_processamento_financeiro', 'observacao_processamento_financeiro',
                        'observacao_retorno_financeiro', 'comprovante_retorno','aprovado_analise_orcamentaria', 'usuario_analise_orcamentaria', 'observacao_analise_orcamentaria'])
            return ret

        ret.extend(['fornecedor', 'observacoes', 'descricao',
                    'tipo_arquivo', 'tipo_anexo', 'valor_total', 'arquivo', 'numero', 'chave', 'mod', 'serie',
                    'plano_conta', 'rateio', 'observacoes', 'aprovado_gerencia', 'usuario_gerencia', 'observacao_gerencia',
                    'aprovado_superintendencia', 'usuario_superintencencia', 'observacao_superintendencia',
                    'usuario_gerencia', 'usuario_diretoria', 'usuario_superintencencia',
                    'usuario_analise_financeira', 'usuario_analise_fiscal',
                    'possui_parcelamento', 'possui_contrato', 'extra_orcamentaria',
                    'antecipacao_pagamento', 'pagamento_boleto', 'banco', 'agencia',
                    'conta', 'digito', 'projeto', 'chave', 'numero', 'mod',
                    'serie', 'cnpj', 'data_emissao', 'cfop'
                    'aprovado_diretoria', 'usuario_diretoria', 'observacao_diretoria',
                    'aprovado_analise_financeira', 'usuario_analise_financeira', 'observacao_analise_financeira',
                    'aprovado_analise_fiscal', 'usuario_analise_fiscal', 'observacao_analise_fiscal', 'usuario_lancamento', 'data_lancamento', 'numero_lancamento', 'pagamento_realizado', 'observacao_pagamento',
                    'valor_retencao', 'valor_liquido',
                    'comprovante_pagamento', 'comprovante_lancamento',
                    'conta_pagadora', 'conta_recebedora', 'descricacao_pagamento', 'data_vencimento', 'data_pagamento', 'documento_remessa_pagamento', 'forma_pagamento', 'moeda_pagamento', 'data_cotacao', 'cotacao','valor_bruto', 'valor_desconto', 'valor_juros', 'valor_juros_mora', 'valor_multa', 'valor_outros', 'valor_liquido',
                    'aprovado_processamento_financeiro', 'usuario_processamento_financeiro', 'observacao_processamento_financeiro',
                    'observacao_retorno_financeiro', 'comprovante_retorno','aprovado_analise_orcamentaria', 'usuario_analise_orcamentaria', 'observacao_analise_orcamentaria'
                    ])

        # Se o status for aprovado, todos os campos estarão disponíveis para edição
        if obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL:
            ret.remove('observacao_analise_fiscal')
            ret.remove('usuario_lancamento')
            ret.remove('data_lancamento')
            ret.remove('numero_lancamento')
            ret.remove('comprovante_lancamento')
            ret.remove('valor_retencao')
            ret.remove('valor_liquido')
            ret.remove('conta_pagadora')
            ret.remove('conta_recebedora')
            ret.remove('descricacao_pagamento')
            ret.remove('data_vencimento')
            ret.remove('data_pagamento')
            ret.remove('documento_remessa_pagamento')
            ret.remove('forma_pagamento')
            ret.remove('moeda_pagamento')
            ret.remove('data_cotacao')
            ret.remove('cotacao')
            ret.remove('valor_bruto')
            ret.remove('valor_desconto')
            ret.remove('valor_juros')
            ret.remove('valor_juros_mora')
            ret.remove('valor_multa')
            ret.remove('valor_outros')
            ret.remove('valor_liquido')
        elif obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA:
            ret.remove('observacao_analise_financeira')
            ret.remove('pagamento_realizado')
            ret.remove('observacao_pagamento')
            ret.remove('comprovante_pagamento')
        elif obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_ANALISE_ORCAMENTARIA:
            # ret.remove('aprovado_analise_orcamentaria')
            # ret.remove('usuario_analise_orcamentaria')
            ret.remove('observacao_analise_orcamentaria')
        elif obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_PROCESSAMENTO_FINANCEIRO:
            # ret.remove('aprovado_processamento_financeiro')
            # ret.remove('usuario_processamento_financeiro')
            ret.remove('observacao_processamento_financeiro')
        elif obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_RETORNO_FINANCEIRO:
            ret.remove('observacao_retorno_financeiro')
            ret.remove('comprovante_retorno')
        return ret
