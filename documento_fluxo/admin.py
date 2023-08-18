from django.contrib import admin
from viewflow.workflow.admin import ProcessAdmin

from . import models


@admin.register(models.DistribuirDocumentoProcess)
class DistribuirDocumentoProcessAdmin(ProcessAdmin):
    list_display = ['pk', 'created', 'status', 'participants',
                    'despacho', 'documento']
    list_display_links = ['pk', 'created']
    sortable_by = ['pk', 'created', 'status', 'participants']
