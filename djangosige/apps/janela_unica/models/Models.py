from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from datetime import datetime
from django.core.validators import RegexValidator, MinValueValidator
from django.template.defaultfilters import date
from django_fsm import FSMField, transition
from djangosige.apps.fiscal.models.nota_fiscal import MOD_NFE_ESCOLHAS, NotaFiscal


TIPO_ARQUIVO_DOCUMENTO_UNICO_FINANCEIRO =  (
    (u'0', u'Nota Fiscal (NF-e)'),
    (u'1', u'Boleto'),
    (u'2', u'Comprovante de Pagamento'),
    (u'3', u'Outros'),
)


class StatusAnaliseFinaceira(object):
    EDICAO_RESPONSAVEL = 'Edição Responsável'
    AGUARDANDO_AVALIACAO = 'Aguardando avaliação'
    APROVADO_GERENCIA = 'Aprovado Gerência'
    APROVADO_SUPERITENDENCIA = 'Aprovado Superintendencia'
    APROVADO_DIRETORIA = 'Aprovado Diretoria'
    APROVADO_ANALISE_FISCAL = 'Aprovado Análise Fiscal'
    APROVADO_ANALISE_FINANCEIRA = 'Aprovado Análise Financeira'
    REPROVADO = 'Reprovado'
    FINALIZADO = 'Finalizado'
    CHOICES = (
        (EDICAO_RESPONSAVEL, EDICAO_RESPONSAVEL),
        (AGUARDANDO_AVALIACAO, AGUARDANDO_AVALIACAO),
        (APROVADO_GERENCIA, APROVADO_GERENCIA),
        (APROVADO_SUPERITENDENCIA, APROVADO_SUPERITENDENCIA),
        (APROVADO_DIRETORIA, APROVADO_DIRETORIA),
        (APROVADO_ANALISE_FISCAL, APROVADO_ANALISE_FISCAL),
        (APROVADO_ANALISE_FINANCEIRA, APROVADO_ANALISE_FINANCEIRA),
        (REPROVADO, REPROVADO),
        (FINALIZADO, FINALIZADO),
    )

class DocumentoUnico(models.Model):
    arquivo = models.FileField(upload_to='janela_unica/documentos', null=True, blank=True)
    class Meta:
        abstract = True

class DocumentoUnicoFinanceiro(DocumentoUnico):
    situacao = FSMField(
        default=StatusAnaliseFinaceira.EDICAO_RESPONSAVEL,
        verbose_name='Avaliação',
        choices=StatusAnaliseFinaceira.CHOICES,
        protected=True, #Impede alteração de estado por usuários sem permissão
    )
    data_inclusao = models.DateTimeField(auto_now_add=True)
    tipo_arquivo = models.CharField(max_length=1, choices=TIPO_ARQUIVO_DOCUMENTO_UNICO_FINANCEIRO,null=True, blank=True)
    numero = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{1,10}$')],null=True, blank=True)
    chave = models.CharField(max_length=44)
    mod = models.CharField(
        max_length=2, choices=MOD_NFE_ESCOLHAS,null=True, blank=True)
    serie = models.CharField(max_length=3,null=True, blank=True)
    fornecedor = models.ForeignKey(
        'cadastro.Fornecedor', related_name="fornecedor_documento_unico", on_delete=models.SET_NULL, null=True, blank=True)
    
    valor_total = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                 MinValueValidator(Decimal('0.00'))], null=True, blank=True)
    
    # Plano de contas
    plano_conta = models.ForeignKey(
        'financeiro.PlanoContasGrupo', related_name="nfe_entrada_analise_plano_conta", on_delete=models.PROTECT, null=True, blank=True)

    rateio = models.BooleanField(null=True, blank=True,)
    observacoes = models.CharField(max_length=1055, null=True, blank=True)

    # Dados Aprovação

    aprovado_gerencia = models.BooleanField(null=True, blank=True)
    observacao_gerencia = models.CharField(max_length=1055, null=True, blank=True)
    aprovado_superintendencia = models.BooleanField(null=True, blank=True)
    observacao_superintendencia = models.CharField(max_length=1055, null=True, blank=True)
    aprovado_diretoria = models.BooleanField(null=True, blank=True)
    observacao_diretoria = models.CharField(max_length=1055, null=True, blank=True)

    class Meta:
        verbose_name = "Documento Único Financeiro Entrada"

    def can_edit(self, user):
        return self.situacao == StatusAnaliseFinaceira.EDICAO_RESPONSAVEL and user == self.responsavel

    @property
    def estado(self):
        if self.emit_entrada:
            if self.emit_entrada.endereco_padrao:
                return self.emit_entrada.endereco_padrao.uf
        return ''
    
    # Workflow 
    @transition(field=situacao, source=StatusAnaliseFinaceira.EDICAO_RESPONSAVEL, 
                target=StatusAnaliseFinaceira.AGUARDANDO_AVALIACAO)
    def enviar_avaliacao(self):
        '''
        Envia para avaliação
        '''
    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_AVALIACAO, 
                target=StatusAnaliseFinaceira.APROVADO_GERENCIA)
    def aprovacao_gerencia(self):
        self.aprovado_gerencia = True
        '''
        Aprovado pela gerência
        '''

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_AVALIACAO, 
                target=StatusAnaliseFinaceira.REPROVADO)
    def reprovacao_gerencia(self):
        self.aprovado_gerencia = False
        '''
        Reprovado pela gerência
        '''

    @transition(field=situacao, source=StatusAnaliseFinaceira.APROVADO_GERENCIA, target=StatusAnaliseFinaceira.APROVADO_SUPERITENDENCIA)
    def aprovacao_superintendencia(self):
        self.aprovado_superintendencia = True
        '''
        Aprovado pela superintendência
        '''

    @transition(field=situacao, source=StatusAnaliseFinaceira.APROVADO_GERENCIA, target=StatusAnaliseFinaceira.REPROVADO)
    def reprovado_superintendencia(self):
        self.aprovado_superintendencia = False
        '''
        Reprovado pela superintendência
        '''

    @transition(field=situacao, source=StatusAnaliseFinaceira.APROVADO_SUPERITENDENCIA  , 
                target=StatusAnaliseFinaceira.FINALIZADO)
    def finalizar(self):
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



