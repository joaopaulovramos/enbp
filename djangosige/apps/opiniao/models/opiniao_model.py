from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
import calendar
import datetime
from decimal import Decimal

from django.template.defaultfilters import date


class OpiniaoModel(models.Model):
    nome = models.CharField(blank=True, null=True, max_length=200)
    email = models.CharField(blank=True, null=True, max_length=100)
    tipo = models.CharField(max_length=1,
                            default='2',
                            choices=[('1', 'Dúvida'),
                                     ('2', 'Sugestão/Opinião'),
                                     ('3', 'Elogio'),
                                     ('4', 'Crítica'),
                                     ('5', 'Reportar um problema'),
                                     ])
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, related_name="opiniao_opiniao_user", on_delete=models.CASCADE, null=True,
                                blank=True)
    opiniao = models.CharField(max_length=500, blank=False, null=False)
    rating = models.IntegerField(default=0, null=True, blank=True)
    anexo = models.FileField(upload_to='files/', null=True, blank=True)

    class Meta:
        verbose_name = "Opiniões"
        permissions = (
            ("analisar_opinioes", "Vizualiza todas as opiniões"),
        )

    def data_formated(self):
        return '%s' % date(self.data, "d/m/Y")

    def opiniao_truncated(self):
        return '%s' % self.opiniao[:200]


