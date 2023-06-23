# -*- coding: utf-8 -*-
import re
from datetime import datetime

from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy

from djangosige.apps.cadastro.forms import EmpresaForm
from djangosige.apps.cadastro.models import Empresa

from .base import AdicionarPessoaView, PessoasListView, EditarPessoaView
from django_cpf_cnpj.validators import is_valid_cnpj

import requests
import json

from ..models.empresa import SITUACAO_CADASTRAL


class AdicionarEmpresaView(AdicionarPessoaView):
    template_name = "cadastro/pessoa_add.html"
    success_url = reverse_lazy('cadastro:listaempresasview')
    success_message = "Empresa <b>%(nome_razao_social)s </b>adicionada com sucesso."
    permission_codename = 'add_empresa'

    def get_context_data(self, **kwargs):
        context = super(AdicionarEmpresaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR EMPRESA'
        context['return_url'] = reverse_lazy('cadastro:listaempresasview')
        context['tipo_pessoa'] = 'empresa'
        return context

    def get(self, request, *args, **kwargs):
        form = EmpresaForm(prefix='empresa_form')
        return super(AdicionarEmpresaView, self).get(request, form, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'cnpj_sync_btn' in request.POST:
            cnpj = request.POST['pessoa_jur_form-cnpj']
            if is_valid_cnpj(cnpj):
                request.POST = loadCnpjFields(cnpj, request.POST.copy())

        form = EmpresaForm(request.POST, request.FILES,
                           prefix='empresa_form', request=request)
        return super(AdicionarEmpresaView, self).post(request, form, *args, **kwargs)

#teste
class EmpresasListView(PessoasListView):
    template_name = 'cadastro/pessoa_list.html'
    model = Empresa
    context_object_name = 'all_empresas'
    success_url = reverse_lazy('cadastro:listaempresasview')
    permission_codename = 'view_empresa'

    def get_context_data(self, **kwargs):
        context = super(EmpresasListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'EMPRESAS CADASTRADAS'
        context['add_url'] = reverse_lazy('cadastro:addempresaview')
        context['tipo_pessoa'] = 'empresa'
        return context

    def post(self, request, *args, **kwargs):
        if self.check_user_delete_permission(request, self.model):
            for key, value in request.POST.items():
                if value == "on":
                    instance = self.model.objects.get(id=key)
                    if (instance.codigo_legado != None or instance.inativo == '1'):
                        messages.add_message(
                            request,
                            messages.WARNING,
                            u'Empresa ' + instance.nome_razao_social + ' não pode ser excluída.',
                            'permission_warning')
                        break
                    try:
                        instance.delete()
                    except ProtectedError as exception:
                        messages.add_message(
                            request,
                            messages.WARNING,
                            u'Empresa ' + instance.nome_razao_social + ' não pode ser excluída pois existem movimentações.',
                            'permission_warning')

        return redirect(self.success_url)



class EditarEmpresaView(EditarPessoaView):
    form_class = EmpresaForm
    model = Empresa
    template_name = "cadastro/pessoa_edit.html"
    success_url = reverse_lazy('cadastro:listaempresasview')
    success_message = "Empresa <b>%(nome_razao_social)s </b>editada com sucesso."
    permission_codename = 'change_empresa'

    def get_context_data(self, **kwargs):
        context = super(EditarEmpresaView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('cadastro:listaempresasview')
        context['tipo_pessoa'] = 'empresa'
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form_class.prefix = "empresa_form"
        form = self.get_form(form_class)
        logo_file = Empresa.objects.get(pk=self.object.pk).logo_file
        return super(EditarEmpresaView, self).get(request, form, logo_file=logo_file, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = form_class(request.POST, request.FILES,
                          prefix='empresa_form', instance=self.object, request=request)
        logo_file = Empresa.objects.get(pk=self.object.pk).logo_file

        if 'cnpj_sync_btn' in request.POST:
            cnpj = request.POST['pessoa_jur_form-cnpj']
            if is_valid_cnpj(cnpj):
                request.POST = loadCnpjFields(cnpj, request.POST.copy())
                self.object = form_class(request.POST, request.FILES, prefix='empresa_form', instance=self.object, request=request).save()
                return redirect(reverse_lazy('cadastro:editarempresaview', kwargs=self.kwargs))

        return super(EditarEmpresaView, self).post(request, form, logo_file=logo_file, *args, **kwargs)

def loadCnpjFields(cnpj, post):
    url = "https://publica.cnpj.ws/cnpj/" + re.sub('[./-]', '', cnpj)
    resp = requests.get(url)
    json_object = json.loads(resp.text)
    if "razao_social" in json_object:
        post['empresa_form-nome_razao_social'] = json_object["razao_social"]
    if "estabelecimento" in json_object:
        estabelecimento_ = json_object["estabelecimento"]
        if "atividade_principal" in estabelecimento_:
            atividade_principal_ = estabelecimento_["atividade_principal"]
            if ("subclasse" in atividade_principal_):
                post['empresa_form-cnae'] = atividade_principal_["subclasse"]
        if 'data_inicio_atividade' in estabelecimento_:
            post['empresa_form-ini_atividades'] = convert_date_format(estabelecimento_['data_inicio_atividade'])
        if 'data_situacao_cadastral' in estabelecimento_:
            post['empresa_form-data_sit_cadastral'] = convert_date_format(estabelecimento_['data_situacao_cadastral'])
        if 'situacao_cadastral' in estabelecimento_:
            post['empresa_form-sit_cadastral'] = find_situacao_cadastral(estabelecimento_['situacao_cadastral'])
        if 'nome_fantasia' in estabelecimento_:
            post['pessoa_jur_form-nome_fantasia'] = estabelecimento_['nome_fantasia']
    return post

def find_situacao_cadastral(titulo):
    for sit in SITUACAO_CADASTRAL:
        if sit[1] == titulo:
            return sit[0]

def convert_date_format(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return date.strftime('%d/%m/%Y')

