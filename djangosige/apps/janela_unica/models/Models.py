from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class DocumentoModel(models.Model):
    nome = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/users', null=True, blank=True)
    dono = models.ForeignKey(User, related_name="dono_doc", on_delete=models.CASCADE, null=True, blank=True)
    data_inclusao = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return u'%s - %s' % (self.id, self.nome)



class TramitacaoModel(models.Model):
    user_enviado = models.ForeignKey(User, related_name="user_enviado", on_delete=models.CASCADE, null=True, blank=True)
    user_recebido = models.ForeignKey(User, related_name="user_recebido", on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True, blank=True)
    doc = models.ForeignKey(DocumentoModel, related_name="documento_tramitacao", on_delete=models.CASCADE)