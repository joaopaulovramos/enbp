from datetime import datetime
from decimal import Decimal
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models
from django.forms import ValidationError
from django.template.defaultfilters import date
from django_fsm import FSMField, transition
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.contrib.contenttypes.models import ContentType
from simple_history.models import HistoricalRecords
from djangosige.apps.cadastro.models.bancos import BANCOS
from djangosige.apps.fiscal.models.nota_fiscal import (MOD_NFE_ESCOLHAS,
                                                       NotaFiscal)

TIPO_ARQUIVO_DOCUMENTO_UNICO_FINANCEIRO = (
    (u'0', u'Nota Fiscal (NF-e)'),
    (u'1', u'DANFE'),
    (u'2', u'Boleto'),
    (u'3', u'Comprovante de Pagamento'),
    (u'9', u'Outros'),
)

TIPO_FORMA_PAGAMENTO = (
    (u'0', u'Boleto'),
    (u'1', u'TED'),
    (u'2', u'PIX'),
    (u'9', u'Outros'),
)


TIPO_ANEXO = (
    (u'0', u'.xml'),
    (u'1', u'.pdf'),
    (u'2', u'.doc'),
    (u'3', u'Outros'),
)


class StatusAnaliseFinaceira(object):
    EDICAO_RESPONSAVEL = 'Edição Responsável'
    AGUARDANDO_GERENCIA = 'Aguardando avaliação Gerência'
    AGUARDANDO_SUPERITENDENCIA = 'Aguardando avaliação Superintendencia'
    AGUARDANDO_DIRETORIA = 'Aguardando avaliação Diretoria'
    AGUARDANDO_ANALISE_FISCAL = 'Aguardando Análise Fiscal'
    AGUARDANDO_ANALISE_FINANCEIRA = 'Aguardando Análise Financeira'
    APROVADO = 'Aprovado'
    REPROVADO = 'Reprovado'
    FINALIZADO = 'Finalizado'
    CANCELADO = 'Cancelado'
    CHOICES = (
        (EDICAO_RESPONSAVEL, EDICAO_RESPONSAVEL),
        (AGUARDANDO_GERENCIA, AGUARDANDO_GERENCIA),
        (AGUARDANDO_SUPERITENDENCIA, AGUARDANDO_SUPERITENDENCIA),
        (AGUARDANDO_DIRETORIA, AGUARDANDO_DIRETORIA),
        (AGUARDANDO_ANALISE_FISCAL, AGUARDANDO_ANALISE_FISCAL),
        (AGUARDANDO_ANALISE_FINANCEIRA, AGUARDANDO_ANALISE_FINANCEIRA),
        (REPROVADO, REPROVADO),
        (FINALIZADO, FINALIZADO),
        (CANCELADO, CANCELADO),
        (APROVADO, APROVADO),
    )

# Caso venha a surgir outros tipos de documentos
# subir para a classe abstrata os campos em comum

class ArquivoDocumentoUnico(models.Model):
    descricao = models.CharField(max_length=255, null=True, blank=True)
    arquivo = models.FileField(upload_to='janela_unica/documentos', null=True, blank=True)
    data_inclusao = models.DateTimeField(auto_now_add=True)
    documento_unico = models.ForeignKey('DocumentoUnicoFinanceiro', related_name="documento_unico_arquivo", on_delete=models.PROTECT, null=True, blank=True)
    class Meta:
        verbose_name = 'Arquivo do Documento Unico'
        verbose_name_plural = 'Arquivos do Documento Unico'
        
    def __str__(self):
        return u'%s - %s' % (self.pk, self.descricao)


class DocumentoUnico(models.Model):
    class Meta:
        abstract = True



class DocumentoUnicoFinanceiro(DocumentoUnico):
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True))
    situacao = FSMField(
        default=StatusAnaliseFinaceira.EDICAO_RESPONSAVEL,
        verbose_name='Situação',
        choices=StatusAnaliseFinaceira.CHOICES,
        protected=True,  # Impede alteração de estado por usuários sem permissão
    )
    arquivo = models.FileField(upload_to='janela_unica/documentos', null=True, blank=True)
    data_inclusao = models.DateTimeField(auto_now_add=True)
    data_finalizacao = models.DateTimeField(null=True, blank=True)
    tipo_arquivo = models.CharField(max_length=1, choices=TIPO_ARQUIVO_DOCUMENTO_UNICO_FINANCEIRO, null=True, blank=True)
    tipo_anexo = models.CharField(max_length=1, choices=TIPO_ANEXO, null=True, blank=True)

    numero = models.CharField(max_length=9, null=True, blank=True)
    chave = models.CharField(max_length=44, null=True, blank=True)
    mod = models.CharField(max_length=2, choices=MOD_NFE_ESCOLHAS, null=True, blank=True)
    serie = models.CharField(max_length=3, null=True, blank=True)
    cnpj = CNPJField(masked=True, null=True, blank=True)
    data_emissao = models.DateField(null=True, blank=True)
    cfop = models.CharField(max_length=5, null=True, blank=True)

    # Plano de contas
    plano_conta = models.ForeignKey('financeiro.PlanoContasGrupo', related_name="nfe_entrada_analise_plano_conta", on_delete=models.PROTECT, null=True, blank=True)

    # projeto = models.ForeignKey('norli_projeto.ExemploModel', related_name="projeto_ju", on_delete=models.CASCADE, null=False, blank=False)
    projeto = models.ForeignKey('norli_projeto.ExemploModel', related_name="projeto_ju", on_delete=models.CASCADE, null=True, blank=True)

    # Dados para o pagamento
    forma_pagamento = models.CharField(max_length=1, choices=TIPO_FORMA_PAGAMENTO, default='9')
    fornecedor = models.ForeignKey('cadastro.Pessoa', related_name="pessoa_documento_unico", on_delete=models.SET_NULL, null=True, blank=True)

    # dados boleto
    linha_digitavel = models.CharField(max_length=48, null=True, blank=True)

    # dados chave pix
    chave_pix = models.CharField(max_length=255, null=True, blank=True)

    # dados bancarios para Ted
    banco = models.CharField(max_length=3, choices=BANCOS, null=True, blank=True)
    agencia = models.CharField(max_length=8, null=True, blank=True)
    conta = models.CharField(max_length=32, null=True, blank=True)
    digito = models.CharField(max_length=8, null=True, blank=True)

    valor_total = models.DecimalField(max_digits=13, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    valor_liquido = models.DecimalField(max_digits=13, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], null=True, blank=True)
    valor_retencao = models.DecimalField(max_digits=13, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], null=True, blank=True)

    rateio = models.BooleanField(null=True, blank=True,)
    observacoes = models.CharField(max_length=1055, null=True, blank=True)


    # Dados informações financeiras
    possui_parcelamento = models.BooleanField(null=True, blank=True)
    possui_contrato = models.BooleanField(null=True, blank=True)
    extra_orcamentaria = models.BooleanField(null=True, blank=True)
    antecipacao_pagamento = models.BooleanField(null=True, blank=True)
    pagamento_boleto = models.BooleanField(null=True, blank=True)

    # Dados Aprovação

    usuario_gerencia = models.ForeignKey(User, related_name="documento_unico_usuario_gerencia", on_delete=models.SET_NULL, null=True, blank=True)
    aprovado_gerencia = models.BooleanField(null=True, blank=True)
    observacao_gerencia = models.CharField(max_length=1055, null=True, 
                                           blank=True)
    
    usuario_superintencencia = models.ForeignKey(User, related_name="documento_unico_usuario_superintendencia", on_delete=models.SET_NULL, null=True, blank=True)
    aprovado_superintendencia = models.BooleanField(null=True, blank=True)
    observacao_superintendencia = models.CharField(max_length=1055, null=True, blank=True)

    usuario_diretoria = models.ForeignKey(User, related_name="documento_unico_usuario_diretoria", on_delete=models.SET_NULL, null=True, blank=True)
    aprovado_diretoria = models.BooleanField(null=True, blank=True)
    observacao_diretoria = models.CharField(max_length=1055, null=True, blank=True)

    # Analise financeira
    usuario_analise_financeira = models.ForeignKey(User, related_name="documento_unico_usuario_analise_financeira", on_delete=models.SET_NULL, null=True, blank=True)
    aprovado_analise_financeira = models.BooleanField(null=True, blank=True)
    observacao_analise_financeira = models.CharField(max_length=1055, null=True, blank=True)
    comprovante_lancamento = models.FileField(upload_to='janela_unica/documentos', null=True, blank=True)


    # Analise fiscal
    usuario_analise_fiscal = models.ForeignKey(User, related_name="documento_unico_usuario_analise_fiscal", on_delete=models.SET_NULL, null=True, blank=True)
    aprovado_analise_fiscal = models.BooleanField(null=True, blank=True)
    observacao_analise_fiscal = models.CharField(max_length=1055, null=True, blank=True)
    comprovante_pagamento = models.FileField(upload_to='janela_unica/documentos', null=True, blank=True)

    # Novos
    responsavel = models.ForeignKey(User, related_name="responsavel_documento_unico", on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.CharField(max_length=1055, null=True, blank=True)

    # Lançamentos Questor
    usuario_lancamento =  models.CharField(max_length=255, null=True, blank=True)
    data_lancamento = models.DateField(null=True, blank=True)
    numero_lancamento = models.CharField(max_length=255, null=True, blank=True)

    # Analise financeira
    pagamento_realizado = models.BooleanField(null=True, blank=True)
    observacao_pagamento = models.CharField(max_length=1055, null=True, blank=True)

    class Meta:
        verbose_name = "Documento Janela Única"
        permissions = (
            ("gerencia_documento_unico", "Aprovar documentos janela única - Gerência"),
            ("superintendencia_documento_unico", "Aprovar documentos janela única - Superintendencia"),
            ("diretoria_documento_unico", "Aprovar documentos janela única - Diretoria"),
            ("analise_fiscal_documento_unico", "Aprovar documentos analise fiscal - Fiscal"),
            ("analise_financeira_documento_unico", "Aprovar documentos analise financeira - Financeiro")
        )

    def __str__(self):
        return 'Documento Único N° ' + str(self.pk)

    @admin.display(description="Solicitação")
    def numero_solicitacao(obj):
        return obj.pk

    @property
    def format_data_emissao(self):
        return '%s' % date(self.data_inclusao, "d/m/Y")

    @property
    def estado(self):
        if self.emit_entrada:
            if self.emit_entrada.endereco_padrao:
                return self.emit_entrada.endereco_padrao.uf
        return ''
    
    # def can_reprovar_gerencia(self):
    #     return self.observacao_gerencia

    # Workflow
    def logar_detalhes(self, request, mensagem):
        LogEntry.objects.log_action(
            # user_id=by.id,
            user_id=request.user.id,
            content_type_id=ContentType.objects.get_for_model(self).pk,
            object_id=self.id,
            object_repr=str(self),
            change_message=mensagem,
            action_flag=CHANGE)

    @transition(field=situacao, source=StatusAnaliseFinaceira.EDICAO_RESPONSAVEL, target=StatusAnaliseFinaceira.AGUARDANDO_GERENCIA,
                custom=dict(button_name='Enviar para Avaliação'))
    def enviar_avaliacao(self, by=None, request=None):
        self.responsavel = request.user
        self.logar_detalhes(request, mensagem='Enviado para avaliação')

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_GERENCIA,
                target=StatusAnaliseFinaceira.AGUARDANDO_SUPERITENDENCIA,
                permission='janela_unica.gerencia_documento_unico',
                custom=dict(button_name='Aprovar (Gerência)'))
    def aprovar_gerencia(self, by=None, request=None):
        self.aprovado_gerencia = True
        self.usuario_gerencia = request.user
        #https://django-simple-history.readthedocs.io/en/2.7.0/historical_model.html#textfield-as-history-change-reason
        # self.changeReason = 'Aprovado pela gerência'
        self.logar_detalhes(request, mensagem='Aprovado pela gerência')


    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_GERENCIA, target=StatusAnaliseFinaceira.EDICAO_RESPONSAVEL, permission='janela_unica.gerencia_documento_unico',
                custom=dict(button_name='Reprovar Solictação')
                # , conditions=[can_reprovar_gerencia]
    )
    def reprovar_gerencia(self, by=None, request=None):
        self.aprovado_gerencia = False
        self.usuario_gerencia = request.user
        self.logar_detalhes(request, mensagem='Reprovado pela gerência')


    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_SUPERITENDENCIA, target=StatusAnaliseFinaceira.AGUARDANDO_DIRETORIA, permission='janela_unica.superintendencia_documento_unico', custom=dict(button_name='Aprovar Solictação (Superintendência)'))
    def aprovar_superintendencia(self, by=None, request=None):
        self.aprovado_superintendencia = True
        self.usuario_superintencencia = request.user
        self.logar_detalhes(request, mensagem='Aprovado pela superintendência')


    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_SUPERITENDENCIA, target=StatusAnaliseFinaceira.AGUARDANDO_GERENCIA, permission='janela_unica.superintendencia_documento_unico', custom=dict(button_name='Reprovar Solicitação'))
    def reprovar_superintendencia(self, by=None, request=None):
        self.usuario_superintencencia = request.user
        self.aprovado_superintendencia = False
        self.logar_detalhes(request, mensagem='Reprovado pela superintendência')

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_DIRETORIA, target=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL, permission='janela_unica.diretoria_documento_unico', custom=dict(button_name='Aprovar Solictação (Diretoria)'))
    def aprovar_diretoria(self, by=None, request=None):
        self.aprovado_diretoria = True
        self.usuario_diretoria = request.user
        self.logar_detalhes(request, mensagem='Aprovado pela diretoria')
        '''
        Aprovado pela diretoria
        '''

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_DIRETORIA, target=StatusAnaliseFinaceira.AGUARDANDO_SUPERITENDENCIA, permission='janela_unica.diretoria_documento_unico', custom=dict(button_name='Reprovar Solictação'))
    def reprovar_diretoria(self, by=None, request=None):
        self.aprovado_diretoria = False
        self.logar_detalhes(request, mensagem='Reprovado pela diretoria')


    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL, target=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA, permission='janela_unica.analise_fiscal_documento_unico',
    custom=dict(button_name='Aprovar Solictação (Fiscal)'))
    def aprovar_analise_fiscal(self, by=None, request=None):
        self.aprovado_analise_fiscal = True
        self.logar_detalhes(request, mensagem='Aprovado pela Analise Fiscal')


    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL, target=StatusAnaliseFinaceira.EDICAO_RESPONSAVEL, permission='janela_unica.analise_fiscal_documento_unico', custom=dict(button_name='Aprovar Solictação (Fiscal)'))
    def reprovar_analise_fiscal(self, by=None, request=None):
        self.aprovado_analise_fiscal = False
        self.logar_detalhes(request, mensagem='Reprovado pela Analise Fiscal')


    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA, target=StatusAnaliseFinaceira.FINALIZADO, permission='janela_unica.analise_financeira_documento_unico',
        custom=dict(button_name='Aprovar Solictação (Financeiro)'))
    def aprovar_analise_financeira(self, by=None, request=None):
        self.data_finalizacao = datetime.now()
        self.aprovado_analise_financeira = True
        self.logar_detalhes(request, mensagem='Aprovado pelo Financeiro')

    
    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA, target=StatusAnaliseFinaceira.EDICAO_RESPONSAVEL, permission='janela_unica.analise_financeira_documento_unico', custom=dict(button_name='Reprovar Solictação'))
    def reprovar_analise_financeira(self, by=None, request=None):
        self.aprovado_analise_financeira = False
        self.logar_detalhes(request, mensagem='Reprovado pelo Financeiro')

    @transition(field=situacao, source=[StatusAnaliseFinaceira.EDICAO_RESPONSAVEL, StatusAnaliseFinaceira.REPROVADO],
                target=StatusAnaliseFinaceira.CANCELADO)
    def cancelar(self, by=None, request=None):
        self.data_finalizacao = datetime.now()
        self.logar_detalhes(request, mensagem='Cancelado pelo responsável')
        '''
        Finalizar
        '''


class DocumentoModel(models.Model):
    nome = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/users', null=True, blank=True)
    dono = models.ForeignKey(User, related_name="dono_doc", on_delete=models.CASCADE, null=True, blank=True)
    data_inclusao = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return u'%s - %s' % (self.id, self.nome)


class TramitacaoModel(models.Model):
    user_enviado = models.ForeignKey(User, related_name="user_enviado", on_delete=models.CASCADE, null=True, blank=True)
    user_recebido = models.ForeignKey(User, related_name="user_recebido", on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True, blank=True)
    doc = models.ForeignKey(DocumentoModel, related_name="documento_tramitacao", on_delete=models.CASCADE)
