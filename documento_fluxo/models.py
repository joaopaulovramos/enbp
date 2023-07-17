from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from papermerge.core.models import Document
from viewflow import jsonstore
from django.db import models
from viewflow.workflow.models import Process


class DistribuirDocumento(models.Model):
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE)
    documento = models.ForeignKey(Document, on_delete=models.CASCADE)
    despacho = models.TextField(blank=True, null=True)
    data_despacho = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
            if self.pk:
                return f"#{self.pk}"
            return super().__str__()

class DistribuirDocumentoProcess(Process):
    text = jsonstore.TextField(_("Despacho"))
    recebido = jsonstore.BooleanField(_("Recebido"), blank=True)

    class Meta:
        proxy = True
        verbose_name = _("Distribuir documento")
        verbose_name_plural = _("Distribuição de documentos")
