# -*- coding: utf-8 -*-

from django.db import models

TIPO_GRUPO_ESCOLHAS = (
    (u'0', u'Entrada'),
    (u'1', u'Saída'),
)


class PlanoContasGrupo(models.Model):
    codigo_legado = models.CharField(max_length=20, blank=True, null=True)
    codigo = models.CharField(max_length=20)
    tipo_grupo = models.CharField(max_length=1, choices=TIPO_GRUPO_ESCOLHAS)
    descricao = models.CharField(max_length=255)
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Grupo do Plano de Contas"

    def __unicode__(self):
        s = u'%s' % (self.descricao)
        return s

    def __str__(self):
        s = u'%s' % (self.descricao)
        return s


class PlanoContasSubgrupo(PlanoContasGrupo):
    grupo = models.ForeignKey('financeiro.PlanoContasGrupo',
                              related_name="subgrupos", on_delete=models.CASCADE)
