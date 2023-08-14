import random
import string

import requests
from django.urls import reverse_lazy

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView, CustomListViewFilter, \
    CustomCreateViewAddUser

from djangosige.apps.opiniao.forms.opiniao_forms import *
from djangosige.apps.opiniao.models.opiniao_model import *

from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect


class ListOpiniaoView(CustomListViewFilter):
    template_name = 'opiniao/opiniaomodel_list.html'
    model = OpiniaoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('opiniao:listaropinioes')
    permission_codename = 'view_opiniaomodel'

    def get_queryset(self):
        return OpiniaoModel.objects.filter(usuario=self.request.user)

    def get_object(self):
        return OpiniaoModel.objects.all(usuario=self.request.user)

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if value == "on" and key != 'selecionar_todos':
                acao = request.POST['acao']
                if acao == 'excluir':
                    instance = self.model.objects.get(id=key)
                    instance.delete()

        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(ListOpiniaoView, self).get_context_data(**kwargs, object_list=None)
        context['title_complete'] = 'Opiniões'
        context['add_url'] = reverse_lazy('opiniao:adicionaopiniao')
        return context


class AdicionarOpiniaoView(CustomCreateView):
    form_class = OpiniaoForm
    template_name = "timesheet/add_feedback.html"
    success_url = reverse_lazy('opiniao:listaropinioes')
    success_message = "Feedback Adicionado com Sucesso."
    permission_codename = 'add_opiniaomodel'
    context_object_name = 'all_natops'

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()

        form = OpiniaoForm(request.POST, request.FILES, instance=self.object)
        form.request_user = self.request.user
        if(request.FILES.get('anexo')):
            letters = string.ascii_lowercase
            name = ''.join(random.choice(letters) for i in range(20))
            nome_antigo = request.FILES['anexo'].name
            nome_antigo = nome_antigo.split('.')
            ext = nome_antigo[-1]



        if form.is_valid():
            if(request.FILES.get('anexo')):
                request.FILES['anexo'].name = name + '.' + ext

            self.object = form.save(commit=False)
            # self.object.rating = 5
            self.object.save()
            return redirect(self.success_url)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        self.form_class.Meta.model.user = self.request.user
        context = super(AdicionarOpiniaoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR FEEDBACK'
        context['return_url'] = reverse_lazy('opiniao:adicionaopiniao')
        return context


class EditarOpiniaoView(CustomUpdateView):
    form_class = OpiniaoForm
    model = OpiniaoModel
    template_name = 'timesheet/edit.html'
    success_url = reverse_lazy('opiniao:listaropinioes')
    success_message = "Opinião editada com sucesso."
    permission_codename = 'change_opiniaomodel'
    context_object_name = 'all_natops'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.request_user = self.request.user

        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.save()
            return redirect(self.success_url)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(EditarOpiniaoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'EDITAR OPINIÃO'
        context['return_url'] = reverse_lazy('opiniao:listaropinioes')
        return context
