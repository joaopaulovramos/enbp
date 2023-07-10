from django.db import models



class DocumentoModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return u'%s - %s' % (self.id, self.nome)
