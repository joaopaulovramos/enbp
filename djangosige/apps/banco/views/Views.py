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
from djangosige.apps.banco.forms import *
from djangosige.apps.banco.models import *
import random
import string

from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template

from djangosige.configs import settings


#### Banco
class ListBancoView(CustomListView):
    template_name = 'banco/list_banco.html'
    model = BancoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('banco:listabanco')
    permission_codename = 'cadastrar_item_bancos'

    def get_context_data(self, **kwargs):
        context = super(ListBancoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Banco'
        context['add_url'] = reverse_lazy('banco:adicionarbanco')
        return context


class AdicionarBancoView(CustomCreateView):
    form_class = BancoForm
    template_name = 'banco/add.html'
    success_url = reverse_lazy('banco:listabanco')
    success_message = "Banco Adicionado com Sucesso."
    permission_codename = 'cadastrar_item_bancos'

    def get_context_data(self, **kwargs):
        context = super(AdicionarBancoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Banco'
        context['return_url'] = reverse_lazy('banco:listabanco')
        return context

class EditarBancoView(CustomUpdateView):
    form_class = BancoForm
    model = BancoModel
    template_name = 'banco/edit.html'
    success_url = reverse_lazy('banco:listabanco')
    success_message = "Banco Editado com Sucesso."
    permission_codename = 'cadastrar_item_bancos'

    def get_context_data(self, **kwargs):
        context = super(EditarBancoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Editar Banco'
        context['return_url'] = reverse_lazy('banco:listabanco')
        context['id'] = self.object.id
        return context

