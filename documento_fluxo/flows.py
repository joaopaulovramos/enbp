from django.utils.translation import gettext_lazy as _

from viewflow import this
from viewflow.workflow import flow, lock, act
from viewflow.workflow.flow import views

from .models import DistribuirDocumentoProcess, DistribuirDocumento
from viewflow.workflow.flow.views import CreateArtifactView, UpdateProcessView, UpdateArtifactView


class DistribuirDocumentoFlow(flow.Flow):
    process_class = DistribuirDocumentoProcess
    process_title = _("Distribuir Documento")

        # office
    enviar_documento = (
        flow.Start(
            CreateArtifactView.as_view(
                model=DistribuirDocumento,
                fields=["usuario_destino", "despacho", "documento"]
            )
        )
        .Permission("department.can_register_bill")
        .Next(this.receber_documento)
    )

    # project manager
    receber_documento = (
        flow.View(UpdateProcessView.as_view(fields=["recebido"]))
        .Next(this.checar_recebimento)
    )

    checar_recebimento = (
        flow.If(act.process.recebido)
        .Then(this.aceito)
        .Else(this.rejeitado)
    )

    rejeitado = flow.End()

    aceito = flow.End()
