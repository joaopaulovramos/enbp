from django.contrib import admin
from django import forms
from djangosige.apps.compras.models.compras import PedidoCompra


@admin.register(PedidoCompra)
class PedidoCompraAdmin(admin.ModelAdmin):
    list_display = ('data_entrega', 'status', 'orcamento', 'data_emissao', 'fornecedor', 'mod_frete', 'desconto', 'tipo_desconto', 'frete', 'despesas', 'local_dest', 'plano_conta',
                    'movimentar_estoque', 'seguro', 'total_ipi', 'total_icms', 'valor_total', 'cond_pagamento', 'observacoes')
    fields = ()
