from django.db import models
from django.contrib.auth.models import User






class CVModel(models.Model):

    user = models.ForeignKey(User, related_name="cv_user", on_delete=models.CASCADE,  null=True, blank=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    cpf = models.CharField(max_length=200, null=True, blank=True)
    inf_adicionais = models.CharField(max_length=1055, null=True, blank=True)

    cargo = models.CharField(max_length=200, null=True, blank=True)
    nome_cv_executivo = models.CharField(max_length=200, null=True, blank=True)
    cv_executivo = models.CharField(max_length=1055, null=True, blank=True)

    nome_cv_padrao = models.CharField(max_length=200, null=True, blank=True)
    telefone_cv_padrao = models.CharField(max_length=200, null=True, blank=True)
    endereco_cv_padrao = models.CharField(max_length=200, null=True, blank=True)
    email_cv_padrao = models.CharField(max_length=200, null=True, blank=True)
    perfil_cv_padrao = models.CharField(max_length=1055, null=True, blank=True)

    foto = models.ImageField(upload_to='imagens/users', null=True, blank=True)


class CertificadoModel(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to='files/users', null=True, blank=True)
    user = models.ForeignKey(User, related_name="certificados_user", on_delete=models.CASCADE,  null=True, blank=True)

