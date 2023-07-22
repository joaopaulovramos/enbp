from datetime import datetime
from decimal import Decimal

from django.contrib import admin
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models
from django.template.defaultfilters import date
from django_fsm import FSMField, transition
from django_cpf_cnpj.fields import CPFField, CNPJField

from djangosige.apps.cadastro.models.bancos import BANCOS
from djangosige.apps.fiscal.models.nota_fiscal import (MOD_NFE_ESCOLHAS,
                                                       NotaFiscal)

TIPO_ARQUIVO_DOCUMENTO_UNICO_FINANCEIRO =  (
    (u'0', u'Nota Fiscal (NF-e)'),
    (u'1', u'Boleto'),
    (u'2', u'Comprovante de Pagamento'),
    (u'3', u'Outros'),
)

TIPO_ANEXO =  (
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
    CHOICES = (
        (EDICAO_RESPONSAVEL, EDICAO_RESPONSAVEL),
        (AGUARDANDO_GERENCIA, AGUARDANDO_GERENCIA),
        (AGUARDANDO_SUPERITENDENCIA, AGUARDANDO_SUPERITENDENCIA),
        (AGUARDANDO_DIRETORIA, AGUARDANDO_DIRETORIA),
        (AGUARDANDO_ANALISE_FISCAL, AGUARDANDO_ANALISE_FISCAL),
        (AGUARDANDO_ANALISE_FINANCEIRA, AGUARDANDO_ANALISE_FINANCEIRA),
        (REPROVADO, REPROVADO),
        (FINALIZADO, FINALIZADO),
    )

# Caso venha a surgir outros tipos de documentos
# subir para a classe abstrata os campos em comum
class DocumentoUnico(models.Model):
    arquivo = models.FileField(upload_to='janela_unica/documentos', null=True, blank=True)
    class Meta:
        abstract = True

class DocumentoUnicoFinanceiro(DocumentoUnico):
    situacao = FSMField(
        default=StatusAnaliseFinaceira.EDICAO_RESPONSAVEL,
        verbose_name='Situação',
        choices=StatusAnaliseFinaceira.CHOICES,
        protected=True, #Impede alteração de estado por usuários sem permissão
    )

    data_inclusao = models.DateTimeField(auto_now_add=True)
    tipo_arquivo = models.CharField(max_length=1, choices=TIPO_ARQUIVO_DOCUMENTO_UNICO_FINANCEIRO,null=True, blank=True)
    tipo_anexo = models.CharField(max_length=1, choices=TIPO_ANEXO,null=True, blank=True)

    numero = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{1,10}$')],null=True, blank=True)
    chave = models.CharField(max_length=44)
    mod = models.CharField(max_length=2, choices=MOD_NFE_ESCOLHAS,null=True, blank=True)
    serie = models.CharField(max_length=3,null=True, blank=True)

    cnpj = CNPJField(masked=True, null=True, blank=True)


    # TODO: Trocar para cadastro.Pessoa
    fornecedor = models.ForeignKey('cadastro.Fornecedor', related_name="fornecedor_documento_unico", on_delete=models.SET_NULL, null=True, blank=True)
    valor_total = models.DecimalField(max_digits=13, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], null=True, blank=True)
    
    # Plano de contas
    plano_conta = models.ForeignKey('financeiro.PlanoContasGrupo', related_name="nfe_entrada_analise_plano_conta", on_delete=models.PROTECT, null=True, blank=True)

    rateio = models.BooleanField(null=True, blank=True,)
    observacoes = models.CharField(max_length=1055, null=True, blank=True)

    # dados bancarios
    banco = models.CharField(max_length=3, choices=BANCOS, null=True, blank=True)
    agencia = models.CharField(max_length=8, null=True, blank=True)
    conta = models.CharField(max_length=32, null=True, blank=True)
    digito = models.CharField(max_length=8, null=True, blank=True)

    projeto = models.ForeignKey('norli_projeto.ExemploModel', related_name="projeto_ju", on_delete=models.CASCADE, null=False, blank=False)


    # Dados Aprovação

    aprovado_gerencia = models.BooleanField(null=True, blank=True)
    observacao_gerencia = models.CharField(max_length=1055, null=True, blank=True)
    aprovado_superintendencia = models.BooleanField(null=True, blank=True)
    observacao_superintendencia = models.CharField(max_length=1055, null=True, blank=True)
    aprovado_diretoria = models.BooleanField(null=True, blank=True)
    observacao_diretoria = models.CharField(max_length=1055, null=True, blank=True)
    aprovado_analise_financeira = models.BooleanField(null=True, blank=True)
    observacao_analise_financeira = models.CharField(max_length=1055, null=True, blank=True)
    aprovado_analise_fiscal = models.BooleanField(null=True, blank=True)
    observacao_analise_fiscal = models.CharField(max_length=1055, null=True, blank=True)

    # Novos
    responsavel = models.ForeignKey(User, related_name="responsavel_documento_unico", on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.CharField(max_length=1055, null=True, blank=True)


    class Meta:
        verbose_name = "Documento Janela Única"

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
    
    # Workflow 
    @transition(field=situacao, source=StatusAnaliseFinaceira.EDICAO_RESPONSAVEL, target=StatusAnaliseFinaceira.AGUARDANDO_GERENCIA,
                )
    def enviar_avaliacao(self):
        '''
        Envia para avaliação
        '''
    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_GERENCIA, 
                target=StatusAnaliseFinaceira.AGUARDANDO_SUPERITENDENCIA)
    def aprovacao_gerencia(self):
        self.aprovado_gerencia = True
        '''
        Aprovado pela gerência
        '''

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_GERENCIA, 
                target=StatusAnaliseFinaceira.EDICAO_RESPONSAVEL)
    def reprovacao_gerencia(self):
        self.aprovado_gerencia = False
        '''
        Reprovado pela gerência
        '''

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_SUPERITENDENCIA, target=StatusAnaliseFinaceira.AGUARDANDO_DIRETORIA)
    def aprovacao_superintendencia(self):
        self.aprovado_superintendencia = True
        '''
        Aprovado pela superintendência
        '''

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_SUPERITENDENCIA, target=StatusAnaliseFinaceira.AGUARDANDO_GERENCIA)
    def reprovado_superintendencia(self):
        self.aprovado_superintendencia = False
        '''
        Reprovado pela superintendência
        '''
    
    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_DIRETORIA, target=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL)
    def aprovar_diretoria(self):
        self.aprovado_diretoria = True
        '''
        Aprovado pela diretoria
        '''
    
    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_DIRETORIA, target=StatusAnaliseFinaceira.AGUARDANDO_SUPERITENDENCIA)
    def reprovar_diretoria(self):
        self.aprovado_diretoria = False
        '''
        Reprovado pela diretoria
        '''

    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL, target=StatusAnaliseFinaceira.APROVADO)
    def aprovar_analise_financeira(self):
        '''
        Aprovar análise financeira
        '''
        self.aprovado_analise_financeira = True
    
    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL, target=StatusAnaliseFinaceira.EDICAO_RESPONSAVEL)
    def reprovar_analise_financeira(self):
        '''
        Reprovar análise financeira
        '''
        self.aprovado_analise_financeira = False
    
    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL, target=StatusAnaliseFinaceira.REPROVADO)
    def reprovar_analise_fiscal(self):
        '''
        Reprovar análise fiscal
        '''
        self.aprovado_analise_fiscal = False
    
    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA, target=StatusAnaliseFinaceira.APROVADO)
    def aprovar_analise_fiscal(self):
        '''
        Aprovar análise fiscal
        '''
        self.aprovado_analise_fiscal = True
    
    @transition(field=situacao, source=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA, target=StatusAnaliseFinaceira.REPROVADO)
    def reprovar_analise_financeira(self):
        '''
        Reprovar análise financeira
        '''
        self.aprovado_analise_financeira = False

    @transition(field=situacao, source=[StatusAnaliseFinaceira.REPROVADO], 
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



