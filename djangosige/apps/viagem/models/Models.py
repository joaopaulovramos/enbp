from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import date
from django import forms

PAGAMENTO = [
    ('RECURSOS DA EMPRESA', 'RECURSOS DA EMPRESA'),
    ('RECURSOS PRÓPRIOS', 'RECURSOS PRÓPRIOS'),
]

BOOLEANO = [
    ('1', 'SIM'),
    ('0', 'NAO'),
]

PC = [
    ('2', 'REPROVADO'),
    ('1', 'APROVADO'),
    ('0', 'EM ANÁLISE'),
]


class TiposDeViagemModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class TiposDeSolicitacaoModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class MotivoDeViagemModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class TipoDeTransporteModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class TipoDeDespesaModel(models.Model):
    sigla = models.CharField(max_length=10)
    descricao = models.CharField(max_length=300)
    nome = models.CharField(max_length=10)

    def __str__(self):
        return self.sigla


class ViagemModel(models.Model):
    solicitante = models.ForeignKey(User, related_name="viagem_user", on_delete=models.CASCADE, null=True, blank=True)
    valor_passagem = models.CharField(max_length=200)
    dada_inicio = models.DateTimeField()
    dada_fim = models.DateField()
    origem = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    objetivo = models.CharField(max_length=200)
    tipo_viagem = models.ForeignKey(TiposDeViagemModel, related_name="viagem_tipo", on_delete=models.CASCADE)
    tipo_solicitacao = models.ForeignKey(TiposDeSolicitacaoModel, related_name="viagem_solicitacao",
                                         on_delete=models.CASCADE)
    motivo = models.ForeignKey(MotivoDeViagemModel, related_name="viagem_motivo", on_delete=models.CASCADE)
    tipo_transporte = models.ForeignKey(TipoDeTransporteModel, related_name="viagem_transporte",
                                        on_delete=models.CASCADE)
    autorizada = models.BooleanField(default=False)
    homologada = models.BooleanField(default=False)
    pagamento = models.CharField(max_length=50, null=True, blank=True, choices=PAGAMENTO)
    descricao = models.TextField(blank=True, null=True)

    dada_inicio_realizada = models.DateTimeField(null=True, blank=True)
    dada_fim_realizada = models.DateField(null=True, blank=True)
    remarcacao_interesse_particular = models.CharField(max_length=50, null=False, blank=False, choices=BOOLEANO,
                                                       default=0)
    finalizar_pc = models.CharField(max_length=50, null=True, blank=True, choices=BOOLEANO, default='0')
    aprovar_pc = models.CharField(max_length=50, null=True, blank=True, choices=PC, default='0')

    def __str__(self):
        return self.origem + ' - ' + self.destino + ' ( ' + str(self.dada_inicio) + ' - ' + str(self.dada_fim) + ' )'

    class Meta:
        verbose_name = "Viagens"
        permissions = (
            ("solicitar_viagens", "Pode solicitar viagens"),
            ("autorizar_viagens", "Pode autorizar viagens"),
            ("homologar_viagens", "Pode homologar viagens"),
            ("cadastrar_item_viagens", "Cadastrar Items de Viagem")
        )

    @property
    def format_data_pagamento(self):
        return '%s' % date(self.dada_inicio, "d/m/Y")


class Arquivos(models.Model):
    descricao = models.TextField(blank=False, null=False)
    file = models.FileField(upload_to='files/', null=False, blank=False)
    viagem = models.ForeignKey(ViagemModel, related_name="arquivos_viagem", null=True, on_delete=models.CASCADE)
