

from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView

from djangosige.apps.janela_unica.forms import *
from djangosige.apps.janela_unica.models import *
from django.utils.formats import localize
from django.shortcuts import render


class ListDocumentosViagensView(CustomListView):
    template_name = 'janela_unica/list_ja.html'
    form_class = TramitacaoForm
    model = DocumentoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('janela_unica:listadocumentos')
    permission_codename = 'cadastrar_item_viagens'

    def get_queryset(self):
        self.model.objects.filter()
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListDocumentosViagensView, self).get_context_data(**kwargs)
        context['title_complete'] = 'DOCUMENTOS'
        context['add_url'] = reverse_lazy('janela_unica:adicionardocumentos')
        return context


class AdicionarDocumentoView(CustomCreateView):
    form_class = DocumentoForm
    template_name = 'janela_unica/add.html'
    success_url = reverse_lazy('janela_unica:listadocumentos')
    success_message = "Documento adicionado com sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.instance.dono = self.request.user
        if form.is_valid():
            self.object = form.save()
            messages.success(self.request, self.get_success_message(form.cleaned_data))
            return redirect(self.success_url)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AdicionarDocumentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR DOCUMENTO'
        context['return_url'] = reverse_lazy('janela_unica:listadocumentos')
        return context


class EditarDocumentoView(CustomUpdateView):
    form_class = DocumentoForm
    model = DocumentoModel
    template_name = 'janela_unica/edit.html'
    success_url = reverse_lazy('janela_unica:listadocumentos')
    success_message = "Documento Editado com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(EditarDocumentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Edição de Documento'
        context['return_url'] = reverse_lazy('janela_unica:listadocumentos')
        context['id'] = self.object.id
        return context


class TramitarView(CustomCreateView):
    form_class = TramitacaoForm
    template_name = 'janela_unica/add.html'
    success_url = reverse_lazy('janela_unica:tramitar')
    success_message = "Documento tramitado com sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.instance.user_enviado = self.request.user
        if form.is_valid():
            self.object = form.save()
            messages.success(self.request, self.get_success_message(form.cleaned_data))
            return redirect(self.success_url)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(TramitarView, self).get_context_data(**kwargs)
        context['title_complete'] = 'TRAMITAR DOCUMENTO'
        context['return_url'] = reverse_lazy('janela_unica:tramitar')
        return context




class ListTramitacaoView(CustomListView):
    template_name = 'janela_unica/list_tramitacao.html'
    model = TramitacaoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('janela_unica:listtramitacao')
    permission_codename = 'cadastrar_item_viagens'

    def get_queryset(self):
        user  = self.request.user
        retorno = self.model.objects.filter(user_recebido = user)
        return retorno #self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListTramitacaoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'DOCUMENTOS'
        context['add_url'] = reverse_lazy('janela_unica:tramitar')
        return context

