from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import date
from django.core.validators import MinValueValidator
from decimal import Decimal
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

ESCALAS = [
    ('0', 'Direto'),
    ('1', '1 escala'),
    ('2', '2+ escalas'),
]

ITINERARIO = [
    ('0', 'Ida'),
    ('1', 'Ida e Volta'),
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


class MoedaModel(models.Model):
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao


class CategoriaPassagemModel(models.Model):
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao


class HorarioPreferencialModel(models.Model):
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao


class TiposNecessidadeEspecialModel(models.Model):
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao


class ViagemModel(models.Model):
    solicitante = models.ForeignKey(User, related_name="viagem_user", on_delete=models.CASCADE, null=True, blank=True)
    data_inclusao = models.DateTimeField(auto_now_add=True)
    valor_passagem = models.DecimalField(max_digits=16, decimal_places=2, validators=[
                                MinValueValidator(Decimal('0.01'))], default=Decimal('0.00'))

    itinerario = models.CharField(max_length=2, choices=ITINERARIO)
    escalas = models.CharField(max_length=1, choices=ESCALAS)

    dada_inicio = models.DateTimeField()
    dada_fim = models.DateField(blank=True, null=True)
    origem = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    objetivo = models.TextField(max_length=512)
    justificativa = models.TextField(max_length=512, blank=True)

    acompanhante = models.ForeignKey(User, related_name="viagem_acompanhante", on_delete=models.CASCADE, null=True,
                                     blank=True)
    necessidade_especial = models.ForeignKey(TiposNecessidadeEspecialModel, related_name="viagem_necessidade_especial", on_delete=models.CASCADE, null=True,
                                     blank=True)

    tipo_viagem = models.ForeignKey(TiposDeViagemModel, related_name="viagem_tipo", on_delete=models.CASCADE)
    tipo_solicitacao = models.ForeignKey(TiposDeSolicitacaoModel, related_name="viagem_solicitacao",
                                         on_delete=models.CASCADE)
    motivo = models.ForeignKey(MotivoDeViagemModel, related_name="viagem_motivo", on_delete=models.CASCADE)
    tipo_transporte = models.ForeignKey(TipoDeTransporteModel, related_name="viagem_transporte",
                                        on_delete=models.CASCADE)
    categoria_passagem = models.ForeignKey(CategoriaPassagemModel, related_name="viagem_passagem",
                                           on_delete=models.CASCADE)
    horario_preferencial = models.ForeignKey(HorarioPreferencialModel, related_name="viagem_horario",
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

    bagagem_tecnica = models.BooleanField(blank=True, default=False)
    bagagem_despachada = models.BooleanField(blank=True, default=False)
    crianca_colo = models.BooleanField(blank=True, default=False)

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
