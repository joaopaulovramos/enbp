from django.db import models

FORMA_DO_VALOR = [
    ('Informado', 'Informado'),
    ('Fixo', 'Fixo'),
    ('Fixo por fase e grupo', 'Fixo por fase e grupo'),
    ('% sobre energia não paga', '% sobre energia não paga'),
    ('% sobre energia', '% sobre energia'),
    ('% sobre energia s/ ICMS', '% sobre energia s/ ICMS'),
    ('% sobre itens positivos', '% sobre itens positivos'),
    ('Valor x KVA instalado', 'Qtde . KWh x Valor KWh'),
    ('Qtde . KWh x Valor item', 'Qtde . KWh x Valor item'),
    ('% sobre itens positivos menos convênios', '% sobre itens positivos menos convênios'),
    ('% sobre consumo Kwh', '% sobre consumo Kwh'),
    ('% sobre consumo  Kw', '% sobre consumo  Kw'),
    ('% sobre consumo Kwh s/ ICMS/PIS/COFINS', '% sobre consumo Kwh s/ ICMS/PIS/COFINS'),
    ('% sobre consumo Kwh + UFER + Tributação', '% sobre consumo Kwh + UFER + Tributação'),
]


CONTABILIZAR = [
    ('Manualmente no faturamento', 'Manualmente no faturamento'),
    ('No lançamento de outras faturas', 'No lançamento de outras faturas:'),
    ('Contabiliza pela classe', 'Contabiliza pela classe'),
    ('Não apropria', 'Não apropria'),
    ('Apropria quando insere pela data', 'Apropria quando insere pela data'),
]


BOOLEAN= [
    ('SIM', 'SIM'),
    ('NÃO', 'NÃO')
]
ACAO_VALOR = [
    ('SOMA', 'SOMA'),
    ('DIMINUI', 'DIMINUI')
]


class ClassificacaoFaturamentoModel(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=2)
    nome = models.CharField(max_length=50)

    def __str__(self):
        s = u'%s' % (self.nome)
        return s


class ItemFaturamentoModel(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=2)
    nome = models.CharField(max_length=50)
    acao_no_valor = models.CharField(max_length=50, null=True, blank=True, choices=ACAO_VALOR)
    base_icms = models.CharField(max_length=50, null=True, blank=True, choices=BOOLEAN)
    faturar_desligados = models.CharField(max_length=50, null=True, blank=True, choices=BOOLEAN)
    exclusivo_outras_faturas = models.CharField(max_length=50, null=True, blank=True, choices=BOOLEAN)
    forma_do_valor = models.CharField(max_length=50, null=True, blank=True, choices=FORMA_DO_VALOR)
    mais_de_uma_cobranca_no_mes = models.CharField(max_length=50, null=True, blank=True, choices=BOOLEAN)
    transferir_no_pedido_de_ligacao = models.CharField(max_length=50, null=True, blank=True, choices=BOOLEAN)
    gera_provisao = models.CharField(max_length=50, null=True, blank=True, choices=BOOLEAN)
    contabilizar = models.CharField(max_length=50, null=True, blank=True, choices=CONTABILIZAR)
    gera_quotas = models.CharField(max_length=50, null=True, blank=True, choices=BOOLEAN)


    def __str__(self):
        s = u'%s' % (self.nome)
        return s



class FaturamentoTUSTModel(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=2)
    nome = models.CharField(max_length=50)
    def __str__(self):
        s = u'%s' % (self.nome)
        return s


'''
Ação
Base ICMS:
Classificação:
Forma do Valor:
Valor da Ocorrência:
Contabilizar:
Data inicio
Data fim
'''
class CaracteristicaFTModel(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=2)
    acao  = models.CharField(max_length=50, null=True, blank=True, choices=ACAO_VALOR)
    base_icms = models.CharField(max_length=50, null=True, blank=True, choices=BOOLEAN)
    def __str__(self):
        s = u'%s' % (self.nome)
        return s
