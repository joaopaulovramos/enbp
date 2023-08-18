from operator import is_
from typing import Any, List, Optional, Tuple, Type, Union
from django.contrib import admin
from django import forms
from django.contrib.admin.sites import AdminSite
from django.http.request import HttpRequest
from django.utils.safestring import mark_safe

# from djangosige.apps.janela_unica.forms.Form import DocumentoUnicoFinanceiroForm
from djangosige.apps.janela_unica.models.Models import AprovadorContrato, AvaliacaoDocumentoUnico, Contrato, StatusAnaliseFinaceira, TipoContrato, ArquivoSolicitacaoContrato
from .models import TramitacaoModel, DocumentoUnicoFinanceiro, ArquivoDocumentoUnico
from fsm_admin.mixins import FSMTransitionMixin
from simple_history.admin import SimpleHistoryAdmin
from django.utils.html import format_html

# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.InlineModelAdmin.form
# class ArquivoDocumentoUnicoInline(admin.StackedInline):


class AvaliacaoDocumentoUnicoInline(admin.TabularInline):
    model = AvaliacaoDocumentoUnico
    extra = 0
    max_num = 10

    class Meta:
        verbose_name = 'Arquivo do Documento'
        verbose_name_plural = 'Arquivos do Documento'
        fields = ['sequencia', 'usuario_avaliador', 'descricao', 'observacao', 'aprovado']
        can_delete = True
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def has_add_permission(self, request, obj=None):
    # if obj and obj.contrato and obj.situacao in [StatusAnaliseFinaceira.EDICAO_RESPONSAVEL]:
    #     return True
        return False

    def get_readonly_fields(self, request, obj=None):
        ret = ['sequencia', 'usuario_avaliador', 'descricao', 'observacao', 'aprovado']
        if obj and not obj.situacao in [StatusAnaliseFinaceira.EDICAO_RESPONSAVEL]:
            ret.extend(['observacao',])
        return ret

#https://stackoverflow.com/questions/20339520/django-admin-default-values-in-stackedinline-tabularinline

class ArquivoDocumentoUnicoInline(admin.TabularInline):
    model = ArquivoDocumentoUnico
    extra = 0
    max_num = 10

    class Meta:
        verbose_name = 'Arquivo do Documento'
        verbose_name_plural = 'Arquivos do Documento'
        fields = ['descricao', 'arquivo',]
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
        ret = ['descricao']
        # Se é um novo registro ou retorno para edicação do responsavel todos os campos estarão disponíveis para edição, exceto os de aprovação
        if obj and not obj.situacao in [StatusAnaliseFinaceira.EDICAO_RESPONSAVEL]:
            ret.extend(['descricao', 'arquivo',])
        return ret

    def __str__(self):
        return u'%s - %s' % (self.pk, self.descricao,)


class NorliAdminModelForm(forms.ModelForm):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            # print(visible)
            visible.field.widget.attrs['class'] = 'form-control'
            if isinstance(visible.field.widget, admin.widgets.RelatedFieldWidgetWrapper):
                visible.field.widget.widget.attrs['class'] = 'form-control'
                # visible.field.widget.can_add_related=False
                visible.field.widget.can_change_related = False
                visible.field.widget.can_delete_related = False


class TipoContratoForm(NorliAdminModelForm):
    class Meta:
        model = TipoContrato
        fields = '__all__'
        verbose_name = 'Tipo de Contrato'
        verbose_name_plural = 'Tipos de Contratos'


@admin.register(TipoContrato)
class TipoContratoModelAdmin(admin.ModelAdmin,):
    form = TipoContratoForm
    list_display = ('descricao',)
    fields = ('descricao',)


class AprovadorContratoInline(admin.TabularInline):
    model = AprovadorContrato
    extra = 2
    max_num = 10

    class Meta:
        fields = ('sequencia', 'descricao', 'usuario',),
        can_delete = True
        widgets = {
            'sequencia': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }

    def __str__(self):
        return u'%s - %s' % (self.pk, self.descricao,)

class ArquivoSolicitacaoContratoInline(admin.TabularInline):
    model = ArquivoSolicitacaoContrato
    extra = 0
    max_num = 10


class ContratoForm(NorliAdminModelForm):
    class Meta:
        model = Contrato
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        fields = '__all__'
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'data_inclusao': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control datepicker'}),
            'data_validade': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control datepicker'}),
        }


@admin.register(Contrato)
class ContratoModelAdmin(FSMTransitionMixin, SimpleHistoryAdmin):
    fsm_field = ['situacao',]
    form = ContratoForm
    list_display = ('descricao', 'data_inclusao', 'data_validade',)
    inlines = [AprovadorContratoInline, ArquivoSolicitacaoContratoInline,]
    fieldsets = (
        ('Dados contrato', {
            'fields': (
                'fornecedor',
                'descricao',
                ('data_validade', 'valor_total', 'arquivo',),
            ),
            # 'classes': ('formset-box',),
        }),
        # ('Avaliadores', {
        #     'fields': (),
        #     'classes': ('replacein', AprovadorContratoInline.__name__),
        # }),
        # ('Documentos para pagamento', {
        #     'fields': (),
        #     'classes': ('replacein', ArquivoSolicitacaoContrato.__name__),
        # }),
    )


class DocumentoUnicoFinanceiroForm(NorliAdminModelForm):

    def clean(self):
        contrato = self.cleaned_data.get('contrato')
        end_date = self.cleaned_data.get('end_date')
        if not contrato:
            raise forms.ValidationError("Contrato é obrigatorio")
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
            'observacao_analise_fiscal': forms.Textarea(attrs={'class': 'form-control'}),
        }


# https://stackoverflow.com/questions/46892851/django-simple-history-displaying-changed-fields-in-admin


@admin.register(DocumentoUnicoFinanceiro)
class DocumentoUnicoFinanceiroAdmin(FSMTransitionMixin, SimpleHistoryAdmin):
    def save_model(self, request, obj, form, change):
        obj.responsavel = request.user
        super().save_model(request, obj, form, change)
        if obj.contrato:
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
    actions = None
    # Atributos de filtragem
    list_filter = ('situacao', 'data_inclusao', 'projeto', 'plano_conta', 'tipo_arquivo')
    search_fields = ('situacao',)
    # Atributos da tabela
    list_display = ('pk', 'descricao', 'situacao', 'data_inclusao', 'data_finalizacao', 'tipo_arquivo', 'responsavel', 'fornecedor', 'projeto', 'plano_conta', 'valor_total',)

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
                ('pk', 'data_inclusao', 'responsavel'),
                ('contrato', 'observacoes'),
                ('tipo_arquivo', 'arquivo', ),
                ('data_emissao', 'valor_total'),

                # ('chave', 'numero', 'serie', 'cfop'),
                # ('cnpj', 'data_emissao', 'valor_total'),
                'descricao',
            ),
            # 'classes': ('formset-box',),
        }),
        # ('Arquivos adicionais', {

        ('Dados pagamento', {
            'fields': (
                ('fornecedor',),
                ('plano_conta', 'projeto'),
                ('forma_pagamento',),
            )
        }),

        (None, {
            'fields': (),
            'classes': ('replacein',),
        }),


        ('Informações financeiras', {
            'fields': (
                ('possui_parcelamento', 'extra_orcamentaria',
                 'possui_contrato', 'antecipacao_pagamento', 'pagamento_boleto'),
            )
        }),


        # ('Aprovadores', {
        #     'fields': (
        #         ('aprovado_gerencia', 'usuario_gerencia', 'observacao_gerencia'),

        #         ('aprovado_superintendencia', 'usuario_superintencencia', 'observacao_superintendencia'),

        #         ('aprovado_diretoria', 'usuario_diretoria', 'observacao_diretoria')
        #     )
        # }),

        # ('Analise fiscal e lançamento questor', {
        #     'fields': (
        #         ('aprovado_analise_fiscal', 'usuario_analise_fiscal', 'observacao_analise_fiscal'),
        #         ('valor_retencao', 'valor_liquido',),
        #         ('usuario_lancamento', 'data_lancamento', 'numero_lancamento', 'comprovante_lancamento')
        #     )
        # }),

        # ('Analise financeira e pagamento', {
        #     'fields': (
        #         ('aprovado_analise_financeira', 'usuario_analise_financeira', 'observacao_analise_financeira'),
        #         ('pagamento_realizado', 'observacao_pagamento', 'comprovante_pagamento')
        #     )
        # }),
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
        ret = ['pk', 'responsavel', 'data_inclusao', 'arquivo_documento_unico_inline']
        # Se é um novo registro ou retorno para edicação do responsavel todos os campos estarão disponíveis para edição, exceto os de aprovação
        if not obj or not obj.situacao or obj.situacao in [StatusAnaliseFinaceira.EDICAO_RESPONSAVEL]:
            ret.extend(['aprovado_gerencia', 'usuario_gerencia', 'observacao_gerencia', 'aprovado_superintendencia', 'usuario_superintencencia', 'observacao_superintendencia',
                        'aprovado_diretoria', 'usuario_diretoria', 'observacao_diretoria',
                        'aprovado_analise_financeira', 'usuario_analise_financeira', 'observacao_analise_financeira',
                        'aprovado_analise_fiscal', 'usuario_analise_fiscal', 'observacao_analise_fiscal', 'usuario_lancamento', 'data_lancamento', 'numero_lancamento', 'pagamento_realizado', 'observacao_pagamento',
                        'valor_retencao', 'valor_liquido',
                        'comprovante_pagamento', 'comprovante_lancamento'])
            return ret

        ret.extend(['fornecedor', 'observacoes', 'descricao',
                    'tipo_arquivo', 'tipo_anexo', 'valor_total', 'arquivo', 'numero', 'chave', 'mod', 'serie',
                    'plano_conta', 'rateio', 'observacoes', 'aprovado_gerencia',
                    'observacao_gerencia', 'aprovado_superintendencia',
                    'observacao_superintendencia', 'aprovado_diretoria', 'observacao_diretoria', 'aprovado_analise_financeira', 'observacao_analise_financeira',
                    'aprovado_analise_fiscal', 'observacao_analise_fiscal',
                    'usuario_lancamento', 'data_lancamento', 'numero_lancamento', 'pagamento_realizado', 'observacao_pagamento', 'usuario_gerencia', 'usuario_diretoria', 'usuario_superintencencia', 'usuario_analise_financeira', 'usuario_analise_fiscal', 'possui_parcelamento', 'possui_contrato', 'extra_orcamentaria', 'antecipacao_pagamento', 'pagamento_boleto', 'banco', 'agencia', 'conta', 'digito', 'projeto', 'chave', 'numero', 'mod', 'serie', 'cnpj', 'data_emissao', 'cfop', 'comprovante_pagamento', 'comprovante_lancamento', 'forma_pagamento', 'linha_digitavel', 'chave_pix', 'valor_retencao', 'valor_liquido',
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
            ret.remove('valor_retencao')
            ret.remove('valor_liquido')
        elif obj.situacao == StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA:
            ret.remove('observacao_analise_financeira')
            ret.remove('pagamento_realizado')
            ret.remove('observacao_pagamento')
            ret.remove('comprovante_pagamento')
        return ret
