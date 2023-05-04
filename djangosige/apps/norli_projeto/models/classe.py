from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator


class FilialModel(models.Model):
    nome = models.CharField(max_length=50, default='')
    cnpj = models.CharField(max_length=50, default='')
    endereco = models.CharField(max_length=200, default='')
    empresa = models.ForeignKey('cadastro.Empresa', related_name="filial_empresa",
                                on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Controle de Projeto"
        permissions = (
            ("controle_projeto", "Pode controlar projetos"),
        )


    def __str__(self):
        s = u'%s' % (self.nome)
        return s







class TipoModel(models.Model):
    nome = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = "Controle de Projeto"
        permissions = (
            ("controle_projeto", "Pode controlar projetos"),
        )


    def __str__(self):
        s = u'%s' % (self.nome)
        return s






class ExemploModel(models.Model):
    nome = models.CharField(max_length=50, default='projeto')
    cliente = models.ForeignKey('cadastro.Cliente', related_name="cliente_projeto",  on_delete=models.CASCADE, null=True, blank=True)
    filial = models.ForeignKey(FilialModel, related_name="filial_projeto",  on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.ForeignKey(TipoModel, related_name="tipo_projeto", on_delete=models.CASCADE, null=True, blank=True)
    parcelas = models.IntegerField( null=True, blank=True)

    valor_proposta = models.IntegerField( null=True, blank=True)
    desconto = models.IntegerField( null=True, blank=True)
    valor_final = models.IntegerField( null=True, blank=True)


    class Meta:
        verbose_name = "Controle de Projeto"
        permissions = (
            ("controle_projeto", "Pode controlar projetos"),
        )


    def __str__(self):
        s = u'%s' % (self.nome)
        return s


