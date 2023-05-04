# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView

from djangosige.apps.fiscal.forms import NaturezaOperacaoForm
from djangosige.apps.fiscal.models import NaturezaOperacao


from djangosige.apps.zpfaturamento.forms.FormClasse import *
from djangosige.apps.zpfaturamento.models.classe import *

from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers

#########################################################################################################

class ListClassificacaoFaturamentoView(CustomListView):
    template_name = 'zpfaturamento/classificacaofaturamento_list.html'
    model = ClassificacaoFaturamentoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zpfaturamento:listclassificacaofaturamento')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListClassificacaoFaturamentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Classificação de Faturamento'
        context['add_url'] = reverse_lazy('zpfaturamento:adicionarclassificacaofaturamento')

        return context


class AdicionarClassificacaoFaturamentoView(CustomCreateView):

    form_class = ClassificacaoFaturamentoForm
    template_name = "zpfaturamento/add.html"
    success_url = reverse_lazy('zpfaturamento:listclassificacaofaturamento')
    success_message = "Classificação de Faturamento Adicionado Com Sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarClassificacaoFaturamentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Classificação de Faturamento'
        context['return_url'] = reverse_lazy('zpfaturamento:listclassificacaofaturamento')
        return context





class EditarClassificacaoFaturamentoView(CustomUpdateView):
    form_class = ClassificacaoFaturamentoForm
    model = ClassificacaoFaturamentoModel

    template_name = "zpfaturamento/edit.html"
    success_url = reverse_lazy('zpfaturamento:listclassificacaofaturamento')
    success_message = "Critério de Baixa Renda editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarClassificacaoFaturamentoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zpfaturamento:listclassificacaofaturamento')
        return context



#########################################################################################################

class ListItemFaturamentoView(CustomListView):
    template_name = 'zpfaturamento/itemfaturamento_list.html'
    model = ItemFaturamentoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zpfaturamento:listitemfaturamento')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListItemFaturamentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Itens de Faturamento'
        context['add_url'] = reverse_lazy('zpfaturamento:adicionaritemfaturamento')

        return context


class AdicionarItemfaturamentoView(CustomCreateView):

    form_class = ItemFaturamentoForm
    template_name = "zpfaturamento/add.html"
    success_url = reverse_lazy('zpfaturamento:listitemfaturamento')
    success_message = "Iten de Faturamento Adicionado Com Sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarItemfaturamentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Itens Classificação de Faturamento'
        context['return_url'] = reverse_lazy('zpfaturamento:listitemfaturamento')
        return context





class EditarItemfaturamentoView(CustomUpdateView):
    form_class = ItemFaturamentoForm
    model = ItemFaturamentoModel

    template_name = "zpfaturamento/edit.html"
    success_url = reverse_lazy('zpfaturamento:listitemfaturamento')
    success_message = "Item faturamento editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarItemfaturamentoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zpfaturamento:listitemfaturamento')
        return context

