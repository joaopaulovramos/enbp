from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import date
from django.core.validators import MinValueValidator
from decimal import Decimal
from django import forms

from djangosige.apps.login.models import Usuario




class BancoModel(models.Model):
    nome = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return u'%s - %s' % (self.id, self.nome)

class Meta:
        verbose_name = "Banco"
        permissions = (
            ("cadastrar_item_bancos", "Pode cadastrar banco"),            
        )


