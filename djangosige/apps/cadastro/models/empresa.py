# -*- coding: utf-8 -*-

import os

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.template.defaultfilters import date

from .base import Pessoa
from djangosige.apps.login.models import Usuario
from djangosige.configs.settings import MEDIA_ROOT

BOOLEAN = [
    ('1', 'SIM'),
    ('0', 'NÃO')
]

TRIBUTACAO = [
    ('1', 'Lucro Real'),
    ('2', 'Lucro Real/Arbitrado'),
    ('3', 'Lucro Presumido/Real'),
    ('4', 'Lucro Presumido/Real/Arbitrado'),
    ('5', 'Lucro Presumido'),
    ('6', 'Lucro Arbitrado'),
    ('7', 'Lucro Presumido/Arbitrado'),
    ('8', 'Imune do IRPJ'),
    ('9', 'Isenta do IRPJ')
]

SITUACAO_CADASTRAL = [
    ('1', 'Ativa'),
    ('2', 'Suspensa'),
    ('3', 'Inapta'),
    ('4', 'Baixada'),
    ('5', 'Nula'),
    ('6', 'Inativa')
]

INDICADOR_INICIO_PERIODO = [
    ('0', '0 - Regular (Início no primeiro dia do ano)'),
    ('1', '1 - Abertura (Início de atividades no ano-calendário)'),
    ('2', '2 - Resultante de cisão/fusão ou remanescente de cisão, ou realizou incorporação'),
    ('3', '3 - Resultante de Mudança de Qualificação da Pessoa Jurídica'),
    ('4', '4 - Início de obrigatoriedade da entrega no curso do ano calendário')
]

INDICADOR_SITUACAO_ESPECIAL = [
    ('0', '0 - Normal (Sem ocorrência de situação especial ou evento)'),
    ('1', '1 - Extinção'),
    ('2', '2 - Fusão'),
    ('3', '3 - Incorporação \ Incorporada'),
    ('4', '4 - Incorporação \ Incorporadora'),
    ('5', '5 - Cisão Total'),
    ('6', '6 - Cisão Parcial'),
    ('7', '7 - Mudança de Qualificação da Pessoa Jurídica'),
    ('8', '8 - Desenquadramento de Imune/Isenta'),
    ('9', '9 - Inclusão no Simples Nacional')
]

QUALIFICACAO = [
    ('001', '001 - Pessoa Jurídica (e-CNPJ ou e-PJ)'),
    ('203', '203 - Diretor'),
    ('204', '204 - Conselheiro de Administração'),
    ('205', '205 - Administrador'),
    ('206', '206 - Administrador do Grupo'),
    ('207', '207 - Administrador de Sociedade Filiada'),
    ('220', '220 - Administrador Judicial – Pessoa Física'),
    ('222', '222 - Administrador Judicial – Pessoa Jurídica - Profissional Responsável'),
    ('223', '223 - Administrador Judicial/Gestor'),
    ('226', '226 - Gestor Judicial'),
    ('309', '309 - Procurador'),
    ('312', '312 - Inventariante'),
    ('313', '313 - Liquidante'),
    ('315', '315 - Interventor'),
    ('401', '401 - Titular – Pessoa Física - EIRELI'),
    ('801', '801 - Empresário'),
    ('900', '900 - Contador/Contabilista'),
    ('940', '940 - Auditor Independente'),
    ('999', '999 - Outros')
]

def logo_directory_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    return 'imagens/empresas/logo_{0}_{1}{2}'.format(instance.nome_razao_social, instance.id, extension)


class Empresa(Pessoa):
    logo_file = models.ImageField(
        upload_to=logo_directory_path, default='imagens/logo.png', blank=True, null=True)
    cnae = models.CharField(max_length=10, blank=True, null=True)
    iest = models.CharField(max_length=32, null=True, blank=True)
    inativo = models.CharField(max_length=1, null=False, blank=True, choices=BOOLEAN, default=1)
    codigo_legado = models.CharField(max_length=10, null=True, blank=True)
    forma_tributacao = models.CharField(
        max_length=2, null=True, blank=True, choices=TRIBUTACAO)
    sit_cadastral = models.CharField(
        max_length=2, null=True, blank=True, choices=SITUACAO_CADASTRAL)
    ini_atividades = models.DateField(blank=True, null=True)
    data_sit_cadastral = models.DateField(null=True, blank=True)
    indi_ini_periodo = models.CharField(
        max_length=2, null=True, blank=True, choices=INDICADOR_INICIO_PERIODO)
    indi_sit_especial = models.CharField(
        max_length=2, null=True, blank=True, choices=INDICADOR_SITUACAO_ESPECIAL)
    qualificacao = models.CharField(
        max_length=3, null=True, blank=True, choices=QUALIFICACAO)


    class Meta:
        verbose_name = "Empresa"

    @property
    def caminho_completo_logo(self):
        if self.logo_file.name != 'imagens/logo.png':
            return os.path.join(MEDIA_ROOT, self.logo_file.name)
        else:
            return ''

    def save(self, *args, **kwargs):
        # Deletar logo se ja existir um
        try:
            obj = Empresa.objects.get(id=self.id)
            if obj.logo_file != self.logo_file and obj.logo_file != 'imagens/logo.png':
                obj.logo_file.delete(save=False)
        except:
            pass
        super(Empresa, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.nome_razao_social

    def __str__(self):
        return u'%s' % self.nome_razao_social

# Deletar logo quando empresa for deletada


@receiver(post_delete, sender=Empresa)
def logo_post_delete_handler(sender, instance, **kwargs):
    # Nao deletar a imagem default 'logo.png'
    if instance.logo_file != 'imagens/logo.png':
        instance.logo_file.delete(False)


class MinhaEmpresa(models.Model):
    m_empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, related_name='minha_empresa', blank=True, null=True)
    m_usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='empresa_usuario')
