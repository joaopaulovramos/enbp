# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView



from djangosige.apps.norli_projeto.forms.FormClasse import *
from djangosige.apps.norli_projeto.models.classe import *

class ListProjetosView(CustomListView):
    template_name = 'norli_projeto/projeto_list.html'
    model = ExemploModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('norli_projeto:listaprojetos')
    permission_codename = 'controle_projeto'

    def get_context_data(self, **kwargs):
        context = super(ListProjetosView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Projetos'
        context['add_url'] = reverse_lazy('norli_projeto:adicionaprojetos')
        return context

class AddProjetoView(CustomCreateView):

    form_class = ExemploForm
    template_name = "norli_projeto/add.html"
    success_url = reverse_lazy('norli_projeto:listaprojetos')
    success_message = "Projeto adicionado com sucesso."
    permission_codename = 'controle_projeto'


    def get_context_data(self, **kwargs):
        context = super(AddProjetoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Projeto'
        context['return_url'] = reverse_lazy('norli_projeto:listaprojetos')
        return context


class EditProjetoView(CustomUpdateView):
    form_class = ExemploForm
    model = ExemploModel

    template_name = "norli_projeto/edit.html"
    success_url = reverse_lazy('norli_projeto:listaprojetos')
    success_message = "Projeto Editado com sucesso."
    permission_codename = 'controle_projeto'



    def get_context_data(self, **kwargs):
        context = super(EditProjetoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('norli_projeto:listaprojetos')
        return context


######## Tipo Projeto



class ListTipoView(CustomListView):
    template_name = 'norli_projeto/tipo_list.html'
    model = TipoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('norli_projeto:listatipo')
    permission_codename = 'controle_projeto'

    def get_context_data(self, **kwargs):
        context = super(ListTipoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Tipos de Projetos'
        context['add_url'] = reverse_lazy('norli_projeto:adicionatipo')
        return context

class AddTipoView(CustomCreateView):

    form_class = TipoForm
    template_name = "norli_projeto/add_simples.html"
    success_url = reverse_lazy('norli_projeto:listatipo')
    success_message = "Tipo de projeto adicionado com sucesso."
    permission_codename = 'controle_projeto'



    def get_context_data(self, **kwargs):
        context = super(AddTipoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Tipo de Projeto'
        context['return_url'] = reverse_lazy('norli_projeto:listatipo')
        return context


class EditTipoView(CustomUpdateView):
    form_class = TipoForm
    model = TipoModel

    template_name = "norli_projeto/edit.html"
    success_url = reverse_lazy('norli_projeto:listatipo')
    success_message = "Tipo de Projeto Editado com sucesso."
    permission_codename = 'controle_projeto'



    def get_context_data(self, **kwargs):
        context = super(EditTipoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('norli_projeto:listatipo')
        return context


######## Filial
class ListFilialView(CustomListView):
    template_name = 'norli_projeto/filial_list.html'
    model = FilialModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('norli_projeto:listafilial')
    permission_codename = 'controle_projeto'

    def get_context_data(self, **kwargs):
        context = super(ListFilialView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Filiais'
        context['add_url'] = reverse_lazy('norli_projeto:adicionafilial')
        return context

class AddFilialView(CustomCreateView):

    form_class = FilialForm
    template_name = "norli_projeto/add_simples.html"
    success_url = reverse_lazy('norli_projeto:listafilial')
    success_message = "Filial adicionado com sucesso."
    permission_codename = 'controle_projeto'


    def get_context_data(self, **kwargs):
        context = super(AddFilialView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Filial'
        context['return_url'] = reverse_lazy('norli_projeto:listafilial')
        return context


class EditFilialView(CustomUpdateView):
    form_class = FilialForm
    model = FilialModel

    template_name = "norli_projeto/edit.html"
    success_url = reverse_lazy('norli_projeto:listafilial')
    success_message = "Filial Editado com sucesso."
    permission_codename = 'controle_projeto'


    def get_context_data(self, **kwargs):
        context = super(EditFilialView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('norli_projeto:listafilial')
        return context


