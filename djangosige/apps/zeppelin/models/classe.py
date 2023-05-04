from django.db import models

FICHA_DE_LEITURA = [
    ('SIM', 'SIM'),
    ('NÃO', 'NÃO')
]

TIPO_SERVICO_ESSENCIAL = [
    ('SERVIÇO PÚBLICO', 'SERVIÇO PÚBLICO'),
    ('EQUIPAMENTO VITAL', 'EQUIPAMENTO VITAL')
]
MOTIVO = [
    ('DEFICIÊNCIA DO MEDIDOR', 'DEFICIÊNCIA DO MEDIDOR'),
    ('OUTROS', 'OUTROS')
]

ALERTAR = [
    ('SIM', 'SIM'),
    ('NÃO', 'NÃO')
]

ATIVO = [
    ('SIM', 'SIM'),
    ('NÃO', 'NÃO')
]
PERMITE_RURAL = [
    ('SIM', 'SIM'),
    ('NÃO', 'NÃO')
]
EXPORTAR_CARGA_MENSAL = [
    ('SIM', 'SIM'),
    ('NÃO', 'NÃO')
]

GERAR_SOLICITACAO_DESLIGAMENTO = [
    ('SIM', 'SIM'),
    ('NÃO', 'NÃO')
]

CRM = [
    ('SIM', 'SIM'),
    ('NÃO', 'NÃO')
]

TIPO_DESLIGAMENTO = [
    ('DEFINITIVO', 'DEFINITIVO'),
    ('PROGRAMADO', 'PROGRAMADO')
]

GRUPO = [
    ('A', 'GRUPO A'),
    ('B', 'GRUPO B')
]
TIPO_CONTABILIDADE = [
    ('NORMAL', 'NORMAL'),
    ('INDIVIDUAL', 'INDIVIDUAL')
]

TIPO_FORNECIMENTO = [
    ('MONOFÁSICO', 'MONOFÁSICO'),
    ('BIFÁSICO', 'BIFÁSICO'),
    ('TRIFÁSICO', 'TRIFÁSICO')
]

MODALIDADES = [
    ('1', 'HORÁRIO VERDE'),
    ('2', 'HORÁRIO AZUL'),
    ('3', 'FORA DE PONTA'),
    ('4', 'CONVENCIONAL'),
    ('5', 'HORÁRIO BRANCO'),
]
#modalidades tarifárias
#monofásico, bifásico ou trifásico
class SubGrupoModel(models.Model):
    nome = models.CharField(max_length=50, default='Sub-Grupo')
    tensao_maxima = models.DecimalField(max_digits=5, decimal_places=2)
    tensao_minima = models.DecimalField(max_digits=5, decimal_places=2)
    carga = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        s = u'%s' % (self.nome)
        return s



# class SubClasseModel(models.Model):
#     #classe = models.ForeignKey('zeppelin.ClasseModel', related_name="classe", on_delete=models.CASCADE)
#     nome = models.CharField(max_length=50, default=' ')
#     minimo_monofasico = models.DecimalField(max_digits=5, decimal_places=2)
#     minimo_bifasico = models.DecimalField(max_digits=5, decimal_places=2)
#     minimo_trifasico = models.DecimalField(max_digits=5, decimal_places=2)
#     tributado_na_UC = models.BooleanField()




class ClasseModel(models.Model):
    nome = models.CharField(max_length=50, default=' ')

    def __str__(self):
        s = u'%s' % (self.nome)
        return s



class SubClasseModel(models.Model):
    nome = models.CharField(max_length=50, default=' ')
    classe = models.ForeignKey(ClasseModel, related_name="classe_sub_classe", on_delete=models.CASCADE)

    def __str__(self):
        s = u'%s' % (self.nome)
        return s





class RegionalModel(models.Model):
    nome_regional = models.CharField(max_length=50)
    funcionarios_proprios = models.IntegerField()
    funcionarios_terceirizados = models.IntegerField()




class MunicipioModel(models.Model):
    nome_municipio = models.CharField(max_length=50)
    codigo_ibge = models.IntegerField()
    conta_cosip = models.IntegerField()
    conta_ativo = models.IntegerField()
    provisao    = models.IntegerField()
    uf_nome     = models.CharField(max_length=2)
    uf_cod      = models.IntegerField()



class GrupoModel(models.Model):
    nome = models.CharField(max_length=50, default=' ')
    numero = models.IntegerField()
    conjunto_aneel = models.CharField(max_length=50, default=' ')

    def __str__(self):
        s = u'%s' % (self.nome)
        return s



class TipoEspecialModel(models.Model):
    nome = models.CharField(max_length=50, default=' ')
    codigo = models.IntegerField()

    def __str__(self):
        s = u'%s' % (self.nome)
        return s



class MedidorModel(models.Model):
    codigo = models.IntegerField()

    def __str__(self):
        s = u'%s' % (self.codigo)
        return s

class UnidadeConsumidoraModel(models.Model):

    numero = models.IntegerField()
    cliente = models.ForeignKey('cadastro.Cliente', related_name="uc_cliente", on_delete=models.CASCADE)
    grupo = models.CharField(max_length=10, null=True, blank=True, choices=GRUPO)
    modalidade_tarifaria = models.CharField(max_length=10, null=True, blank=True, choices=MODALIDADES)
    subgrupo =   models.ForeignKey(SubGrupoModel, related_name="uc_sg", on_delete=models.CASCADE)
    sub_classe = models.ForeignKey(SubClasseModel, related_name="uc_classe", on_delete=models.CASCADE)
    tipo_fornecimento = models.CharField(max_length=10, null=True, blank=True, choices=TIPO_FORNECIMENTO)
    tipo_especial = models.ForeignKey(TipoEspecialModel, related_name="uc_sg", on_delete=models.CASCADE, null=True, blank=True)
    tipo_contabilidade = models.CharField(max_length=10, null=True, blank=True, choices=TIPO_CONTABILIDADE)
    medidor = models.ForeignKey(MedidorModel, related_name="uc_sg", on_delete=models.CASCADE)


    def __str__(self):
        s = u'%s' % (self.numero)
        return s


class ServicoModel(models.Model):
    nome = models.CharField(max_length=50, default=' ')
    codigo = models.IntegerField()

    def __str__(self):
        s = u'%s' % (self.nome)
        return s


class MotivoDesligamento(models.Model):
    nome = models.CharField(max_length=100)
    sai_ficha_de_leitura = models.CharField(max_length=10, null=True, blank=True, choices=FICHA_DE_LEITURA)
    exporta_carga_mensal = models.CharField(max_length=10, null=True, blank=True, choices=EXPORTAR_CARGA_MENSAL)
    gera_solicitacao_desligamento = models.CharField(max_length=10, null=True, blank=True, choices=GERAR_SOLICITACAO_DESLIGAMENTO)
    servico = models.ForeignKey(ServicoModel, related_name="servico_motivo", on_delete=models.CASCADE)
    situacao = models.CharField(max_length=100)
    crm = models.CharField(max_length=10, null=True, blank=True, choices=CRM)
    tipo = models.CharField(max_length=10, null=True, blank=True, choices=TIPO_DESLIGAMENTO)

    def __str__(self):
        s = u'%s' % (self.nome)
        return s



class GrupoEquipamentoModel(models.Model):

    codigo = models.IntegerField()
    descricao = models.CharField(max_length=50, default=' ')
    ativo = models.CharField(max_length=10, null=True, blank=True, choices=ATIVO)

    def __str__(self):
        s = u'%s' % (self.codigo)
        return s



class EquipamentoModel(models.Model):

    codigo = models.IntegerField()
    nome = models.CharField(max_length=100, default=' ')
    grupo = models.ForeignKey(GrupoEquipamentoModel, related_name="grupo_equipamento", on_delete=models.CASCADE)
    potencia = models.FloatField()
    hora_dia = models.IntegerField()
    dia_mes = models.IntegerField()
    classe = models.ManyToManyField(ClasseModel)

    def __str__(self):
        s = u'%s' % (self.nome)
        return s



class cnaeModel(models.Model):

    codigo = models.IntegerField()
    descricao = models.CharField(max_length=50, default=' ')
    prioridade = models.IntegerField()
    permite_rural = models.CharField(max_length=10, null=True, blank=True, choices=PERMITE_RURAL)

    def __str__(self):
        s = u'%s' % (self.codigo)
        return s


class HistoricoPadraoModel(models.Model):

    codigo = models.IntegerField()
    nome = models.CharField(max_length=100, default=' ')
    alertar  = models.CharField(max_length=10, null=True, blank=True, choices=ALERTAR)

    def __str__(self):
        s = u'%s' % (self.codigo)
        return s


class TipoBoletimAfericaoModel(models.Model):

    codigo = models.IntegerField()
    nome = models.CharField(max_length=100, default=' ')
    motivo  = models.CharField(max_length=25, null=True, blank=True, choices=MOTIVO)

    def __str__(self):
        s = u'%s' % (self.nome)
        return s



class TipoDocumentoModel(models.Model):

    codigo = models.IntegerField()
    nome = models.CharField(max_length=100, default=' ')
    ativo  = models.CharField(max_length=25, null=True, blank=True, choices=ATIVO)

    def __str__(self):
        s = u'%s' % (self.nome)
        return s



class TipoServicoEssencialModel(models.Model):

    codigo = models.IntegerField()
    definicao = models.CharField(max_length=100, default=' ')
    ativo  = models.CharField(max_length=25, null=True, blank=True, choices=ATIVO)
    descricao_completa = models.CharField(max_length=100, default=' ')
    tipo = models.CharField(max_length=25, null=True, blank=True, choices=TIPO_SERVICO_ESSENCIAL)


    def __str__(self):
        s = u'%s' % (self.nome)
        return s


class CadastroDeFinalidadeModel(models.Model):

    codigo = models.IntegerField()
    nome = models.CharField(max_length=100, default=' ')
    descricao = models.CharField(max_length=100, default=' ')

    def __str__(self):
        s = u'%s' % (self.codigo)
        return s




class MotivoReprovacaoVistoriaModel(models.Model):

    codigo = models.IntegerField()
    ativo = models.CharField(max_length=25, null=True, blank=True, choices=ATIVO)
    descricao = models.CharField(max_length=100, default=' ')
    motivo = models.CharField(max_length=100, default=' ')
    finalidade_obra = models.ForeignKey(CadastroDeFinalidadeModel, related_name="grupo_equipamento", on_delete=models.CASCADE)


    def __str__(self):
        s = u'%s' % (self.codigo)
        return s


class MotivoCancelamentoModel(models.Model):

    codigo = models.IntegerField()
    descricao = models.CharField(max_length=100, default=' ')

    def __str__(self):
        s = u'%s' % (self.codigo)
        return s

class MotivoReprovacaoAnaliseModel(models.Model):

    codigo = models.IntegerField()
    descricao = models.CharField(max_length=100, default=' ')
    motivo_cancelamento = models.ForeignKey(MotivoCancelamentoModel, related_name="reprovacao_cancelamento", on_delete=models.CASCADE)
    motivo_reprovacao = models.ForeignKey(MotivoReprovacaoVistoriaModel, related_name="reprovacao_reprovacao", on_delete=models.CASCADE)

    def __str__(self):
        s = u'%s' % (self.codigo)
        return s




class MotivoDeferimentoBaixaRendaModel(models.Model):

    codigo = models.IntegerField()
    descricao = models.CharField(max_length=100, default=' ')
    origem_solicitacao = models.CharField(max_length=100, default=' ')

    def __str__(self):
        s = u'%s' % (self.codigo)
        return s


class CriterioBaixaRendaModel(models.Model):

    codigo = models.IntegerField()
    descricao = models.CharField(max_length=100, default=' ')
    tipo = models.CharField(max_length=100, default=' ')
    ativo = models.CharField(max_length=10, null=True, blank=True, choices=ATIVO)


    def __str__(self):
        s = u'%s' % (self.codigo)
        return s
