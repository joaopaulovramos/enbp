from datetime import datetime
from decimal import Decimal
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models
from django.forms import ValidationError
from django.template.defaultfilters import date
from django_fsm import FSMField, transition
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.contrib.contenttypes.models import ContentType
from simple_history.models import HistoricalRecords
from djangosige.apps.cadastro.models.bancos import BANCOS
from djangosige.apps.cadastro.models.base import Banco
from djangosige.apps.cadastro.models.empresa import Empresa
from djangosige.apps.fiscal.models.nota_fiscal import (MOD_NFE_ESCOLHAS,
                                                       NotaFiscal)
from djangosige.apps.viagem.forms.Form import MoedaForm
from djangosige.apps.viagem.models.Models import MoedaModel

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
    AGUARDANDO_AVALIACAO = 'Aguardando avaliação'

    AGUARDANDO_GERENCIA = 'Aguardando avaliação Gerência'
    AGUARDANDO_SUPERITENDENCIA = 'Aguardando avaliação Superintendencia'
    AGUARDANDO_DIRETORIA = 'Aguardando avaliação Diretoria'

    AGUARDANDO_ANALISE_ORCAMENTARIA = 'Aguardando Análise Orçamentária'
    AGUARDANDO_ANALISE_FISCAL = 'Aguardando Análise Fiscal'
    AGUARDANDO_ANALISE_FINANCEIRA = 'Aguardando Análise Financeira'
    AGUARDANDO_PROCESSAMENTO_FINANCEIRO = 'Aguardando Processamento (Taticca)'
    AGUARDANDO_RETORNO_FINANCEIRO = 'Aguardando Retorno Financeiro'
    APROVADO = 'Aprovado'
    # REPROVADO = 'Reprovado'
    FINALIZADO = 'Finalizado'
    CANCELADO = 'Cancelado'
    DEVOLVIDO_RESPONSAVEL = 'Devolvido (Responsável)'
    CHOICES = (
        (EDICAO_RESPONSAVEL, EDICAO_RESPONSAVEL),
        (AGUARDANDO_AVALIACAO, AGUARDANDO_AVALIACAO),
        # (AGUARDANDO_GERENCIA, AGUARDANDO_GERENCIA),
        # (AGUARDANDO_SUPERITENDENCIA, AGUARDANDO_SUPERITENDENCIA),
        # (AGUARDANDO_DIRETORIA, AGUARDANDO_DIRETORIA),
        (AGUARDANDO_ANALISE_ORCAMENTARIA, AGUARDANDO_ANALISE_ORCAMENTARIA),
        (AGUARDANDO_ANALISE_FISCAL, AGUARDANDO_ANALISE_FISCAL),
        (AGUARDANDO_ANALISE_FINANCEIRA, AGUARDANDO_ANALISE_FINANCEIRA),
        (AGUARDANDO_PROCESSAMENTO_FINANCEIRO, AGUARDANDO_PROCESSAMENTO_FINANCEIRO),
        (AGUARDANDO_RETORNO_FINANCEIRO, AGUARDANDO_RETORNO_FINANCEIRO),
        # (REPROVADO, REPROVADO),
        (FINALIZADO, FINALIZADO),
        (CANCELADO, CANCELADO),
        (APROVADO, APROVADO),
        (DEVOLVIDO_RESPONSAVEL, DEVOLVIDO_RESPONSAVEL),
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


class AvaliacaoDocumentoUnico(models.Model):
    sequencia = models.IntegerField(null=True, blank=True)
    usuario_avaliador = models.ForeignKey(User, related_name="documento_unico_usuario_avaliador", on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    observacao = models.CharField(max_length=1055, null=True, blank=True)
    aprovado = models.BooleanField(null=True, blank=True)
    documento_unico = models.ForeignKey('DocumentoUnicoFinanceiro', related_name="documento_unico_avaliacao", on_delete=models.PROTECT, null=True, blank=True)
    data_avaliacao = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Avaliação para Pagamento'
        verbose_name_plural = 'Avaliações para Pagamento'

    def __str__(self):
        return u'%s - %s' % (self.pk, self.descricao)


class SituacaoContrato(object):
    RASCUNHO = 'Rascunho'
    EXECUCAO = 'Em Execução'
    FINALIZADO = 'Finalizado'
    CANCELADO = 'Cancelado'
    CHOICES = (
        (RASCUNHO, RASCUNHO),
        (EXECUCAO, EXECUCAO),
        (FINALIZADO, FINALIZADO),
        (CANCELADO, CANCELADO),
    )


class TipoContrato(models.Model):
    descricao = models.CharField('Descrição', max_length=100)

    class Meta:
        verbose_name = 'Tipo de Contrato'
        verbose_name_plural = 'Tipos de Contratos'

    def __str__(self):
        return self.descricao


class Contrato(models.Model):
    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
    descricao = models.CharField(max_length=255, null=True, blank=True)
    arquivo = models.FileField(upload_to='janela_unica/contratos', null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True, related_name="empresa_contrato")
    fornecedor = models.ForeignKey('cadastro.Pessoa', on_delete=models.SET_NULL,
                                   related_name="fornecedor_contrato", null=True, blank=True)
    data_inclusao = models.DateTimeField(auto_now_add=True)
    data_validade = models.DateTimeField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    tipo_contrato = models.ForeignKey(TipoContrato, related_name="tipo_contrato", on_delete=models.PROTECT, null=True, blank=True)
    forma_pagamento = models.CharField(max_length=1, choices=TIPO_FORMA_PAGAMENTO, default='9')
    detalhe_pagamento = models.CharField(max_length=1055, null=True, blank=True)
    situacao = FSMField(
        default=SituacaoContrato.RASCUNHO,
        verbose_name='Situação',
        choices=SituacaoContrato.CHOICES,
        protected=True,  # Impede alteração de estado por usuários sem permissão
    )
    # TODO: Adicionar demais campos

    def __str__(self) -> str:
        return f'Nº {self.pk} - {self.descricao}'


class ArquivoSolicitacaoContrato(models.Model):
    descricao = models.CharField(max_length=255, null=True, blank=True)
    obrigatorio = models.BooleanField(default=False)
    contrato = models.ForeignKey(Contrato, related_name="contrato_arquivo_solicitacao", on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = 'Documento para fim de Pagamento'
        verbose_name_plural = 'Documentos para fins de Pagamento'

    def __str__(self):
        return u'%s - %s' % (self.pk, self.descricao)


class AprovadorContrato(models.Model):
    sequencia = models.IntegerField(null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.ForeignKey(User, related_name="aprovador_usuario_contrato", on_delete=models.PROTECT, null=True, blank=True)
    grupo = models.ForeignKey(Group, related_name="aprovador_grupo_contrato", on_delete=models.PROTECT, null=True, blank=True)
    obrigatorio = models.BooleanField(default=False)
    contrato = models.ForeignKey('Contrato', related_name="contrato_aprovador_solicitacao", on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = 'Aprovador Solicitação'
        verbose_name_plural = 'Avaliadores para fins de Pagamento'

    def __str__(self):
        return u'%s - %s' % (self.pk, self.descricao)


class FormaPagamentoContrato(models.Model):
    descricao = models.CharField(max_length=255, null=True, blank=True)
    # contrato = models.ForeignKey('Contrato', related_name="contrato_forma_pagamento", on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = 'Forma de Pagamento'

    def __str__(self):
        return u'%s - %s' % (self.pk, self.descricao)


class DocumentoUnico(models.Model):
    class Meta:
        abstract = True


# Campos removidos:
# dados boleto
# linha_digitavel = models.CharField(max_length=48, null=True, blank=True)

# dados chave pix
# chave_pix = models.CharField(max_length=255, null=True, blank=True)

# dados bancarios para Ted

# tipo_anexo = models.CharField(max_length=1, choices=TIPO_ANEXO, null=True, blank=True)

# numero = models.CharField(max_length=9, null=True, blank=True)
# chave = models.CharField(max_length=44, null=True, blank=True)
# mod = models.CharField(max_length=2, choices=MOD_NFE_ESCOLHAS, null=True, blank=True)
# serie = models.CharField(max_length=3, null=True, blank=True)
# cnpj = CNPJField(masked=True, null=True, blank=True)
# cfop = models.CharField(max_length=5, null=True, blank=True)

# projeto = models.ForeignKey('norli_projeto.ExemploModel', related_name="projeto_ju", on_delete=models.CASCADE, null=False, blank=False)

# banco = models.CharField(max_length=3, choices=BANCOS, null=True, blank=True)
# agencia = models.CharField(max_length=8, null=True, blank=True)
# conta = models.CharField(max_length=32, null=True, blank=True)
# digito = models.CharField(max_length=8, null=True, blank=True)

class DocumentoUnicoFinanceiro(DocumentoUnico):
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True))
    situacao = FSMField(
        default=StatusAnaliseFinaceira.EDICAO_RESPONSAVEL,
        verbose_name='Situação',
        choices=StatusAnaliseFinaceira.CHOICES,
        # protected=True,  # Impede alteração de estado por usuários sem permissão
    )
    data_inclusao = models.DateTimeField(auto_now_add=True)
    data_finalizacao = models.DateTimeField(null=True, blank=True)

    contrato = models.ForeignKey('Contrato', related_name="documento_unico_contrato", on_delete=models.PROTECT, null=True, blank=True)
    arquivo = models.FileField(upload_to='janela_unica/documentos', null=True, blank=True)
    data_emissao = models.DateField(null=True, blank=True)

    # Plano de contas
    plano_conta = models.ForeignKey('financeiro.PlanoContasGrupo', related_name="nfe_entrada_analise_plano_conta", on_delete=models.PROTECT, null=True, blank=True)

    tipo_arquivo = models.CharField(max_length=1, null=True, blank=True,
                                    choices=TIPO_ARQUIVO_DOCUMENTO_UNICO_FINANCEIRO)

    projeto = models.ForeignKey('norli_projeto.ExemploModel', related_name="projeto_ju", on_delete=models.CASCADE, null=True, blank=True)

    # Dados para o pagamento
    forma_pagamento = models.CharField(max_length=1, choices=TIPO_FORMA_PAGAMENTO, default='9')
    fornecedor = models.ForeignKey('cadastro.Pessoa', related_name="pessoa_documento_unico", on_delete=models.SET_NULL, null=True, blank=True)

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

    # Analise orcamentaria
    usuario_analise_orcamentaria = models.ForeignKey(User,
                                                     null=True, blank=True, on_delete=models.SET_NULL,
                                                     related_name="documento_unico_usuario_analise_orcamentaria")
    aprovado_analise_orcamentaria = models.BooleanField(null=True, blank=True)
    observacao_analise_orcamentaria = models.CharField(max_length=1055, null=True, blank=True)

    # Analise financeira
    usuario_analise_financeira = models.ForeignKey(User, related_name="documento_unico_usuario_analise_financeira", on_delete=models.SET_NULL, null=True, blank=True)
    aprovado_analise_financeira = models.BooleanField(null=True, blank=True)
    observacao_analise_financeira = models.CharField(max_length=1055, null=True, blank=True)
    comprovante_lancamento = models.FileField(upload_to='janela_unica/documentos', null=True, blank=True)

    # Analise fiscal
    data_analise_fiscal = models.DateTimeField(null=True, blank=True)
    usuario_analise_fiscal = models.ForeignKey(User, related_name="documento_unico_usuario_analise_fiscal", on_delete=models.SET_NULL, null=True, blank=True)
    aprovado_analise_fiscal = models.BooleanField(null=True, blank=True)
    observacao_analise_fiscal = models.CharField(max_length=1055, null=True, blank=True)
    comprovante_pagamento = models.FileField(upload_to='janela_unica/documentos', null=True, blank=True)

    # Novos
    responsavel = models.ForeignKey(User, related_name="responsavel_documento_unico", on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.CharField(max_length=1055, null=True, blank=True)

    # Lançamentos Questor
    usuario_lancamento = models.CharField(max_length=255, null=True, blank=True)
    data_lancamento = models.DateField(null=True, blank=True)
    numero_lancamento = models.CharField(max_length=255, null=True, blank=True)

    # Analise financeira
    pagamento_realizado = models.BooleanField(null=True, blank=True)
    observacao_pagamento = models.CharField(max_length=1055, null=True, blank=True)

    usuario_retorno_financeiro = models.ForeignKey(User, related_name="documento_unico_usuario_retorno_financiero", on_delete=models.SET_NULL, null=True, blank=True)
    aprovado_retorno_financeiro = models.BooleanField(null=True, blank=True)
    observacao_retorno_financeiro = models.CharField(max_length=1055, null=True, blank=True)

    aprovado_processamento_financeiro = models.BooleanField(null=True, blank=True)
    usuario_processamento_financeiro = models.ForeignKey(User, related_name="documento_unico_usuario_processamento_financeiro", on_delete=models.SET_NULL, null=True, blank=True)
    observacao_processamento_financeiro = models.CharField(max_length=1055, null=True, blank=True)

    # Novos
    conta_pagadora = models.ForeignKey(Banco, related_name="conta_pagadora_documento_unico", on_delete=models.SET_NULL, null=True, blank=True)
    conta_recebedora = models.ForeignKey(Banco, related_name="conta_recebedora_documento_unico", on_delete=models.SET_NULL, null=True, blank=True)
    moeda_pagamento = models.ForeignKey(MoedaModel, related_name="moeda_pagamento_documento_unico", on_delete=models.SET_NULL, null=True, blank=True)

    empresa = models.ForeignKey(Empresa, related_name="empresa_documento_unico", on_delete=models.SET_NULL, null=True, blank=True)
    valor_outros = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    valor_liquido = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    observacao_retorno_financeiro = models.CharField(max_length=1055, null=True, blank=True)
    valor_juros = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    data_vencimento = models.DateField(null=True, blank=True)
    valor_multa = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    data_cotacao = models.DateField(null=True, blank=True)
    valor_juros_mora = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    valor_bruto = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    descricao_pagamento = models.CharField(max_length=1055, null=True, blank=True)
    valor_desconto = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    documento_remessa_pagamento = models.FileField(upload_to='janela_unica/documentos/remessa', null=True, blank=True)
    descricacao_pagamento = models.CharField(max_length=1055, null=True, blank=True)
    comprovante_retorno = models.FileField(upload_to='janela_unica/documentos/retorno', null=True, blank=True)
    data_pagamento = models.DateField(null=True, blank=True)
    cotacao = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    @property
    def tipo_documento_formatado(self):
        tipo_formatdo = ''
        if self.tipo_arquivo:
            tipo_formatdo = self.get_tipo_arquivo_display()
        # if self.tipo_anexo:
        #     tipo_formatdo = tipo_formatdo + '/' + self.get_tipo_anexo_display()

        return tipo_formatdo

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

    def aprovacao_atual(self):
        aprovacoe_pendentes = AvaliacaoDocumentoUnico.objects.filter(documento_unico=self, aprovado__isnull=True).order_by('sequencia')
        ap = None
        if aprovacoe_pendentes.exists():
            ap = aprovacoe_pendentes.first()
            ap.restantes = aprovacoe_pendentes.count()
        return ap

    def pode_aprovar(self, user):
        ap = self.aprovacao_atual()
        if not ap:
            return False
        if user.is_superuser or ap.usuario_avaliador == user:
            return True
        return False

    @transition(field=situacao, source=StatusAnaliseFinaceira.EDICAO_RESPONSAVEL,
                # target=StatusAnaliseFinaceira.AGUARDANDO_GERENCIA,
                target=StatusAnaliseFinaceira.AGUARDANDO_AVALIACAO,
                custom=dict(button_name='Enviar para Avaliação'))
    def enviar_avaliacao(self, by=None, request=None):
        self.logar_detalhes(request, mensagem='Enviado para avaliação')

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_AVALIACAO,
                custom=dict(button_name='Aprovar'),
                permission=lambda instance, user: instance.pode_aprovar(user))
    def aprovar_documento(self, by=None, request=None):
        ap = self.aprovacao_atual()
        ap.aprovado = True
        ap.usuario_avaliador = request.user
        ap.data_avaliacao = datetime.now()
        # Se for o ultimo na cadeia de aprovação, muda o status do documento
        if ap.restantes == 1:
            self.situacao = StatusAnaliseFinaceira.AGUARDANDO_ANALISE_ORCAMENTARIA
        ap.save()
        self.aprovado_gerencia = True
        self.usuario_gerencia = request.user
        # https://django-simple-history.readthedocs.io/en/2.7.0/historical_mod
        # self.changeReason = 'Aprovado pela gerência'
        self.logar_detalhes(request, mensagem='Aprovado pela gerência')

    @transition(field=situacao, source=[StatusAnaliseFinaceira.AGUARDANDO_AVALIACAO,
                                        StatusAnaliseFinaceira.AGUARDANDO_ANALISE_ORCAMENTARIA,
                                        StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL,
                                        StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA],
                target=StatusAnaliseFinaceira.DEVOLVIDO_RESPONSAVEL,
                permission='janela_unica.gerencia_documento_unico',
                custom=dict(button_name='Devolver p/ Correção')
                # , conditions=[can_reprovar_gerencia]
                )
    def devolver_documento(self, by=None, request=None):
        motivo = ''
        if (self.aprovado_analise_financeira):
            self.aprovado_analise_financeira = None
        if (self.aprovado_analise_fiscal):
            self.aprovado_analise_fiscal = None
        if (self.aprovado_analise_orcamentaria):
            self.aprovado_analise_orcamentaria = None

        self.logar_detalhes(request, mensagem='Reprovado pela gerência')
        self.notificar('Documento devolvido para correção', request.user)

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_GERENCIA,
                target=StatusAnaliseFinaceira.AGUARDANDO_SUPERITENDENCIA,
                permission='janela_unica.gerencia_documento_unico',
                custom=dict(button_name='Aprovar (Gerência)'))
    def aprovar_gerencia(self, by=None, request=None):
        self.aprovado_gerencia = True
        self.usuario_gerencia = request.user
        # https://django-simple-history.readthedocs.io/en/2.7.0/historical_model.html#textfield-as-history-change-reason
        # self.changeReason = 'Aprovado pela gerência'
        self.logar_detalhes(request, mensagem='Aprovado pela gerência')

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_GERENCIA, target=StatusAnaliseFinaceira.DEVOLVIDO_RESPONSAVEL, permission='janela_unica.gerencia_documento_unico',
                custom=dict(button_name='Devolver Solictação')
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

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_SUPERITENDENCIA, target=StatusAnaliseFinaceira.DEVOLVIDO_RESPONSAVEL,  # target=StatusAnaliseFinaceira.AGUARDANDO_GERENCIA,
                permission='janela_unica.superintendencia_documento_unico', custom=dict(button_name='Devolver Solicitação'))
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

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_DIRETORIA, target=StatusAnaliseFinaceira.DEVOLVIDO_RESPONSAVEL,  # target=StatusAnaliseFinaceira.AGUARDANDO_SUPERITENDENCIA,
                permission='janela_unica.diretoria_documento_unico', custom=dict(button_name='Devolver Solictação'))
    def reprovar_diretoria(self, by=None, request=None):
        self.aprovado_diretoria = False
        self.logar_detalhes(request, mensagem='Reprovado pela diretoria')

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL, target=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA, permission='janela_unica.analise_fiscal_documento_unico',
                custom=dict(button_name='Aprovar Solictação (Fiscal)'))
    def aprovar_analise_fiscal(self, by=None, request=None):
        self.aprovado_analise_fiscal = True
        if not self.data_analise_fiscal:
            self.data_analise_fiscal = datetime.now()
        self.logar_detalhes(request, mensagem='Aprovado pela Analise Fiscal')

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL, target=StatusAnaliseFinaceira.DEVOLVIDO_RESPONSAVEL, permission='janela_unica.analise_fiscal_documento_unico', custom=dict(button_name='Devolver Solictação (Responsável)'))
    def reprovar_analise_fiscal(self, by=None, request=None):
        self.aprovado_analise_fiscal = False
        self.logar_detalhes(request, mensagem='Reprovado pela Analise Fiscal')

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA, target=StatusAnaliseFinaceira.AGUARDANDO_PROCESSAMENTO_FINANCEIRO, permission='janela_unica.analise_financeira_documento_unico',
                custom=dict(button_name='Aprovar Solictação (Financeiro)'))
    def aprovar_analise_financeira(self, by=None, request=None):
        self.aprovado_analise_financeira = True
        self.logar_detalhes(request, mensagem='Aprovado pelo Financeiro')

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA, target=StatusAnaliseFinaceira.DEVOLVIDO_RESPONSAVEL, permission='janela_unica.analise_financeira_documento_unico', custom=dict(button_name='Devolver Solictação'))
    def reprovar_analise_financeira(self, by=None, request=None):
        self.aprovado_analise_financeira = False
        self.logar_detalhes(request, mensagem='Reprovado pelo Financeiro')

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_PROCESSAMENTO_FINANCEIRO, target=StatusAnaliseFinaceira.AGUARDANDO_RETORNO_FINANCEIRO, permission='janela_unica.processamento_financeiro_documento_unico',
                custom=dict(button_name='Aprovar Solictação (Taticca)'))
    def aprovar_processamento_financeiro(self, by=None, request=None):
        self.aprovado_processamento_financeiro = True
        self.logar_detalhes(request, mensagem='Aprovado pelo Financeiro')

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_PROCESSAMENTO_FINANCEIRO, target=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA, permission='janela_unica.processamento_financeiro_documento_unico', custom=dict(button_name='Devolver Solictação (Financeiro)'))
    def reprovar_processamento_financeiro(self, by=None, request=None):
        self.aprovado_processamento_financeiro = False
        self.logar_detalhes(request, mensagem='Reprovado pelo Financeiro')

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_RETORNO_FINANCEIRO, target=StatusAnaliseFinaceira.FINALIZADO, permission='janela_unica.retorno_financeiro_documento_unico',
                custom=dict(button_name='Finalizar Solictação'))
    def aprovar_retorno_financeiro(self, by=None, request=None):
        self.data_finalizacao = datetime.now()
        self.aprovado_retorno_financeiro = True
        self.logar_detalhes(request, mensagem='Aprovado pelo Financeiro')

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_ORCAMENTARIA, target=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL, permission='janela_unica.analise_orcamentaria_documento_unico',
                custom=dict(button_name='Aprovar Solictação (Orçamento)'))
    def aprovar_analise_orcamentaria(self, by=None, request=None):
        self.aprovado_analise_orcamentaria = True
        self.logar_detalhes(request, mensagem='Aprovado pela Analise Orçamentaria')

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_ORCAMENTARIA, target=StatusAnaliseFinaceira.DEVOLVIDO_RESPONSAVEL, permission='janela_unica.analise_orcamentaria_documento_unico', custom=dict(button_name='Devolver  Solictação (Responsável)'))
    def reprovar_analise_orcamentaria(self, by=None, request=None):
        self.aprovado_analise_orcamentaria = False
        self.logar_detalhes(request, mensagem='Reprovado pela Analise Fiscal')

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_PROCESSAMENTO_FINANCEIRO, target=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA, permission='janela_unica.retorno_financeiro_documento_unico', custom=dict(button_name='Devolver Solictação (Financeiro)'))
    def reprovar_retorno_financeiro(self, by=None, request=None):
        self.aprovado_retorno_financeiro = False
        self.logar_detalhes(request, mensagem='Reprovado pelo Financeiro')

    @transition(field=situacao, source=[StatusAnaliseFinaceira.EDICAO_RESPONSAVEL, StatusAnaliseFinaceira.DEVOLVIDO_RESPONSAVEL],
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
