from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User
from django.template.defaultfilters import date
from django.core.validators import MinValueValidator
from decimal import Decimal
from django import forms

from djangosige.apps.login.models import Usuario

GRUPO_FUNCIONAL_DIRETOR = '0'

PAGAMENTO = [
    ('RECURSOS DA EMPRESA', 'Recursos da Empresa'),
    ('RECURSOS PRÓPRIOS', 'Recursos Próprios'),
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
    ('2', 'Em trânsito'),
]

GRUPO_FUNCIONAL = [
    ('0', 'A - DIRETORES e CONSELHEIROS'),
    ('1', 'B – PROFISSIONAIS'),
]

DURACAO_VIAGEM = [
    ('0', 'Inferior a 6hs'),
    ('1', 'Igual/Superior a 6hs'),
]


class TiposDeViagemModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return u'%s - %s' % (self.id, self.nome)


class TiposDeSolicitacaoModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return u'%s - %s' % (self.id, self.nome)


class MotivoDeViagemModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return u'%s - %s' % (self.id, self.nome)


class TipoDeTransporteModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return u'%s - %s' % (self.id, self.nome)


class TipoDeDespesaModel(models.Model):
    sigla = models.CharField(max_length=10)
    descricao = models.CharField(max_length=300)
    nome = models.CharField(max_length=10)

    def __str__(self):
        return u'%s - %s' % (self.id, self.sigla)


class MoedaModel(models.Model):
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return u'%s - %s' % (self.id, self.descricao)


class CategoriaPassagemModel(models.Model):
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return u'%s - %s' % (self.id, self.descricao)


class HorarioPreferencialModel(models.Model):
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return u'%s - %s' % (self.id, self.descricao)


class TiposNecessidadeEspecialModel(models.Model):
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return u'%s - %s' % (self.id, self.descricao)


class LocalidadeModel(models.Model):
    descricao = models.CharField(max_length=400)

    def __str__(self):
        return u'%s - %s' % (self.id, self.descricao)

class TipoDePagamentoModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return u'%s - %s' % (self.id, self.nome)

class TabelaDiariaModel(models.Model):
    grupo_funcional = models.CharField(max_length=1, choices=GRUPO_FUNCIONAL, default=GRUPO_FUNCIONAL[1][0])
    localidade_destino = models.ForeignKey(LocalidadeModel, related_name="diaria_localidade", on_delete=models.RESTRICT)
    moeda = models.ForeignKey(MoedaModel, related_name="diaria_moeda", on_delete=models.RESTRICT)
    valor_diaria = models.DecimalField(max_digits=16, decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0.01'))], default=Decimal('0.00'))

    def __str__(self):
        return f'{self.localidade_destino} - {self.valor_diaria}'


class ViagemModel(models.Model):
    solicitante = models.ForeignKey(User, related_name="viagem_user", on_delete=models.RESTRICT, null=True, blank=True)
    data_inclusao = models.DateTimeField(auto_now_add=True)
    valor_passagem = models.DecimalField(max_digits=16, decimal_places=2, validators=[
        MinValueValidator(Decimal('0.01'))], default=Decimal('0.00'))

    itinerario = models.CharField(max_length=2, choices=ITINERARIO)
    escalas = models.CharField(max_length=1, choices=ESCALAS)
    duracao = models.CharField(max_length=1, choices=DURACAO_VIAGEM)

    dada_inicio = models.DateTimeField()
    dada_fim = models.DateTimeField(blank=True, null=True)
    # origem = models.CharField(max_length=200)
    # destino = models.CharField(max_length=200)
    objetivo = models.TextField(max_length=512)
    justificativa = models.TextField(max_length=512, blank=True)

    acompanhante = models.ForeignKey(Usuario, related_name="viagem_acompanhante", on_delete=models.RESTRICT, null=True,
                                     blank=True, limit_choices_to={'grupo_funcional': GRUPO_FUNCIONAL_DIRETOR})
    necessidade_especial = models.ForeignKey(TiposNecessidadeEspecialModel, related_name="viagem_necessidade_especial",
                                             on_delete=models.RESTRICT, null=True,
                                             blank=True)

    localidade_destino = models.ForeignKey(LocalidadeModel, related_name="viagem_localidade_destino",
                                           on_delete=models.RESTRICT)

    tipo_viagem = models.ForeignKey(TiposDeViagemModel, related_name="viagem_tipo", on_delete=models.RESTRICT)
    tipo_solicitacao = models.ForeignKey(TiposDeSolicitacaoModel, related_name="viagem_solicitacao",
                                         on_delete=models.RESTRICT)
    # motivo = models.ForeignKey(MotivoDeViagemModel, related_name="viagem_motivo", on_delete=models.RESTRICT)
    # tipo_transporte = models.ForeignKey(TipoDeTransporteModel, related_name="viagem_transporte",
    #                                     on_delete=models.RESTRICT)
    # categoria_passagem = models.ForeignKey(CategoriaPassagemModel, related_name="viagem_passagem",
    #                                        on_delete=models.RESTRICT)
    horario_preferencial = models.ForeignKey(HorarioPreferencialModel, related_name="viagem_horario",
                                             on_delete=models.RESTRICT)

    autorizada_sup = models.BooleanField(default=False)
    recusado_sup = models.BooleanField(default=False)

    autorizada_dus = models.BooleanField(default=False)
    recusado_dus = models.BooleanField(default=False)

    homologada = models.BooleanField(default=False)
    homologada_reembolso = models.BooleanField(default=False)
    tem_reembolso = models.BooleanField(default=False)

    pagamento = models.CharField(max_length=50, null=True, blank=True, choices=PAGAMENTO)
    descricao = models.TextField(blank=True, null=True)

    dada_inicio_realizada = models.DateTimeField(null=True, blank=True)
    dada_fim_realizada = models.DateField(null=True, blank=True)
    remarcacao_interesse_particular = models.CharField(max_length=50, null=False, blank=False, choices=BOOLEANO,
                                                       default=0)
    finalizar_pc = models.CharField(max_length=50, null=True, blank=True, choices=BOOLEANO, default='0')
    aprovar_pc = models.CharField(max_length=50, null=True, blank=True, choices=PC, default='0')
    motivo_reprovacao_pc = models.TextField(max_length=512, null=True, blank=True)

    bagagem_tecnica = models.BooleanField(blank=True, default=False)
    bagagem_despachada = models.BooleanField(blank=True, default=False)
    local_risco = models.BooleanField(blank=True, default=False)
    exige_vacina = models.BooleanField(blank=True, default=False)
    reservar_hotel = models.BooleanField(blank=True, default=False)
    alimentacao_terceiros = models.BooleanField(blank=True, default=False)

    qtd_diarias = models.FloatField(blank=True)
    valor_diaria = models.DecimalField(max_digits=16, decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0.00'))],
                                       default=Decimal('0.00'), blank=True, null=True)
    valor_total_diarias = models.DecimalField(max_digits=16, decimal_places=2,
                                              validators=[MinValueValidator(Decimal('0.00'))],
                                              default=Decimal('0.00'), blank=True, null=True)
    justificativa_cancelamento = models.TextField(blank=True, null=True)
    history = HistoricalRecords()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pagamento_diarias_autorizado = AprovarPagamentoDiariasModel.objects.filter(viagem=self).exists()
        self.pagamento_reembolso_autorizado = AprovarPagamentoReembolsoModel.objects.filter(viagem=self).exists()
        
    def data_inicio_formated(self):
        return '%s' % date(self.dada_inicio, "d/m/Y")

    def __str__(self):
        return ' ( ' + str(self.dada_inicio) + ' - ' + str(self.dada_fim) + ' )'

    class Meta:
        verbose_name = "Viagens"
        permissions = (
            ("solicitar_viagens", "Pode solicitar viagens"),
            ("autorizar_viagens_sup", "Pode autorizar viagens - Superintendente"),
            ("autorizar_viagens_dus", "Pode autorizar viagens - Diretor de Unidade de Serviço"),
            ("homologar_viagens", "Pode homologar viagens"),
            ("cadastrar_item_viagens", "Cadastrar Items de Viagem"),
            ("aprovar_pc_viagens", "Aprovar prestação de contras de Viagem"),
            ("autorizar_pagamento_diarias", "Pode autorizar pagamento de diárias"),
            ("autorizar_pagamento_reembolso", "Pode autorizar pagamento de reembolso")
        )

    @property
    def format_data_pagamento(self):
        return '%s' % date(self.dada_inicio, "d/m/Y")

class AprovarPagamentoDiariasModel(models.Model):
    viagem = models.ForeignKey(ViagemModel, on_delete=models.RESTRICT, null=True, blank=True)
    banco = models.CharField(max_length=3, null=True, blank=True)
    agencia = models.CharField(max_length=8, null=True, blank=True)
    conta = models.CharField(max_length=32, null=True, blank=True)
    digito = models.CharField(max_length=8, null=True, blank=True)
    tipo_pagamento = models.ForeignKey(TipoDePagamentoModel, on_delete=models.RESTRICT, null=True, blank=True)
    qtd_diarias = models.FloatField(blank=True, null=True)
    valor_diaria = models.DecimalField(max_digits=16, decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0.00'))],
                                       default=Decimal('0.00'), blank=True, null=True)
    valor_total_diarias = models.DecimalField(max_digits=16, decimal_places=2,
                                              validators=[MinValueValidator(Decimal('0.00'))],
                                              default=Decimal('0.00'), blank=True, null=True)
    data_autorizacao = models.DateTimeField(null=True, blank=True)
    autorizado_por = models.ForeignKey(Usuario, on_delete=models.RESTRICT, null=True, blank=True)

class AprovarPagamentoReembolsoModel(models.Model):
    viagem = models.ForeignKey(ViagemModel, on_delete=models.RESTRICT, null=True, blank=True)
    banco = models.CharField(max_length=3, null=True, blank=True)
    agencia = models.CharField(max_length=8, null=True, blank=True)
    conta = models.CharField(max_length=32, null=True, blank=True)
    digito = models.CharField(max_length=8, null=True, blank=True)
    total_recursos_proprios = models.DecimalField(max_digits=16, decimal_places=2,
                                              validators=[MinValueValidator(Decimal('0.00'))],
                                              default=Decimal('0.00'), blank=True, null=True)
    total_recursos_empresa = models.DecimalField(max_digits=16, decimal_places=2,
                                              validators=[MinValueValidator(Decimal('0.00'))],
                                              default=Decimal('0.00'), blank=True, null=True)
    valor_total_reembolso = models.DecimalField(max_digits=16, decimal_places=2,
                                              validators=[MinValueValidator(Decimal('0.00'))],
                                              default=Decimal('0.00'), blank=True, null=True)
    tipo_pagamento = models.ForeignKey(TipoDePagamentoModel, on_delete=models.RESTRICT, null=True, blank=True)
    data_autorizacao = models.DateTimeField(null=True, blank=True)
    autorizado_por = models.ForeignKey(Usuario, on_delete=models.RESTRICT, null=True, blank=True)

class Arquivos(models.Model):
    descricao = models.TextField(blank=False, null=False)
    file = models.FileField(upload_to='files/', null=False, blank=False)
    viagem = models.ForeignKey(ViagemModel, related_name="arquivos_viagem", null=True, on_delete=models.RESTRICT)

    numero_item = models.IntegerField(null=False)
    tipo_despesa = models.ForeignKey(TipoDeDespesaModel, related_name="arquivos_despesa", on_delete=models.RESTRICT)
    moeda = models.ForeignKey(MoedaModel, related_name="arquivos_moeda", on_delete=models.RESTRICT)

    data_evento = models.DateField(null=True, blank=True)
    pagamento = models.CharField(max_length=50, blank=True, choices=PAGAMENTO)
    valor_pago = models.DecimalField(max_digits=16, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    cotacao = models.DecimalField(max_digits=16, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    valor_pago_reais = models.DecimalField(max_digits=16, decimal_places=2,
                                           validators=[MinValueValidator(Decimal('0.01'))])


class TrechoModel(models.Model):
    viagem = models.ForeignKey(ViagemModel, on_delete=models.RESTRICT, related_name='viagem_trechos')
    data_inicio_trecho = models.DateTimeField()
    data_fim_trecho = models.DateTimeField()
    origem_trecho = models.CharField(max_length=200)
    destino_trecho = models.CharField(max_length=200)
    tipo_transporte_trecho = models.ForeignKey(TipoDeTransporteModel, related_name="viagem_trecho_transporte",
                                               on_delete=models.RESTRICT)
    categoria_passagem_trecho = models.ForeignKey(CategoriaPassagemModel, related_name="viagem_trecho_passagem",
                                                  on_delete=models.RESTRICT)

    # localidade_trecho = models.ForeignKey(LocalidadeModel, related_name="viagem_trecho_localidade_destino",
    #                                       on_delete=models.RESTRICT)

    motivo_trecho = models.ForeignKey(MotivoDeViagemModel, related_name="viagem_trecho_motivo",
                                      on_delete=models.RESTRICT)

    @property
    def format_data_inicio(self):
        return '%s' % date(self.data_inicio_trecho, "d/m/Y")

    @property
    def format_data_fim(self):
        return '%s' % date(self.data_fim_trecho, "d/m/Y")
