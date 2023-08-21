# -*- coding: utf-8 -*-
import os.path
from django.db import IntegrityError
from django.db.models import Q
import pytz
from django.forms import inlineformset_factory
from django.http import HttpResponse

from django.urls import reverse_lazy

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView, CustomView
from django.shortcuts import redirect
from django.utils import timezone
from datetime import datetime, date, timedelta
from django.contrib import messages

from djangosige.apps.login.models import Usuario
from djangosige.apps.orcamento.forms import *
from djangosige.apps.orcamento.models import *
import random
import string

from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template

from djangosige.configs import settings


#### Orçamento
class ListOrcamentoView(CustomListView):
    template_name = 'orcamento/list_orcamento.html'
    model = OrcamentoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('orcamento:listaorcamento')
    permission_codename = 'cadastrar_item_orcamento'

    def get_context_data(self, **kwargs):
        context = super(ListOrcamentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Orçamento'
        context['add_url'] = reverse_lazy('orcamento:adicionarorcamento')
        return context


class AdicionarOrcamentoView(CustomCreateView):
    form_class = OrcamentoForm
    template_name = 'orcamento/add.html'
    success_url = reverse_lazy('orcamento:listaorcamento')
    success_message = "Orçamento Adicionado com Sucesso."
    permission_codename = 'cadastrar_item_orcamento'

    def get_context_data(self, **kwargs):
        context = super(AdicionarOrcamentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Orçamento'
        context['return_url'] = reverse_lazy('orcamento:listaorcamento')
        return context

class EditarOrcamentoView(CustomUpdateView):
    form_class = OrcamentoForm
    model = OrcamentoModel
    template_name = 'orcamento/edit.html'
    success_url = reverse_lazy('orcamento:listaorcamento')
    success_message = "Orçamento Editado com Sucesso."
    permission_codename = 'cadastrar_item_orcamento'

    def get_context_data(self, **kwargs):
        context = super(EditarOrcamentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Editar Orçamento'
        context['return_url'] = reverse_lazy('orcamento:listaorcamento')
        context['id'] = self.object.id
        return context

