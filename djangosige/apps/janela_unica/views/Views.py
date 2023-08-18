

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from geraldo.generators import PDFGenerator
from datetime import datetime
from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView, CustomView
from djangosige.apps.cadastro.models.empresa import MinhaEmpresa
from django.template.defaultfilters import date
from django.views.generic import TemplateView, ListView, View

from djangosige.apps.janela_unica.forms import *
from djangosige.apps.janela_unica.models import *
from django.utils.formats import localize
from django.shortcuts import render
import io

from djangosige.apps.janela_unica.report_janela_unica import DocumentoUnicoFinaceiroReport
from djangosige.apps.login.models import Usuario
from djangosige.configs.settings import MEDIA_ROOT

class ListDocumentosJanelaUnicaView(CustomListView):
    template_name = 'janela_unica/list_ja.html'
    form_class = TramitacaoForm
    model = DocumentoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('janela_unica:listadocumentos')
    permission_codename = 'cadastrar_item_janela_unica'

    def get_queryset(self):
        self.model.objects.filter()
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListDocumentosJanelaUnicaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'DOCUMENTOS'
        context['add_url'] = reverse_lazy('janela_unica:adicionardocumentos')
        return context


class CaixaEntradaJanelaUnicaView(ListView):
    template_name = 'janela_unica/caixa_entrada.html'
    model = DocumentoUnicoFinanceiro
    success_url = reverse_lazy('janela_unica:caixaentrada')
    context_object_name = 'documentos'

    # permission_codename = 'cadastrar_item_janela_unica'

    def get_queryset(self):
        # self.model.objects.filter()
        if self.request.user.is_superuser:
            return self.model.objects.all()
        elif self.request.user.has_perm('janela_unica.gerencia_documento_unico'):
            return self.model.objects.filter(situacao=StatusAnaliseFinaceira.AGUARDANDO_GERENCIA)
        elif self.request.user.has_perm('janela_unica.superintendencia_documento_unico'):
            return self.model.objects.filter(situacao=StatusAnaliseFinaceira.AGUARDANDO_SUPERINTENDENCIA)
        elif self.request.user.has_perm('janela_unica.diretoria_documento_unico'):
            return self.model.objects.filter(situacao=StatusAnaliseFinaceira.AGUARDANDO_DIRETORIA)
        elif self.request.user.has_perm('janela_unica.analise_fiscal_documento_unico'):
            return self.model.objects.filter(situacao=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FISCAL)
        elif self.request.user.has_perm('janela_unica.analise_financeira_documento_unico'):
            return self.model.objects.filter(situacao=StatusAnaliseFinaceira.AGUARDANDO_ANALISE_FINANCEIRA)
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CaixaEntradaJanelaUnicaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CAIXA DE ENTRADA DOCUMENTOS'
        # context['add_url'] = reverse_lazy('janela_unica:adicionardocumentos')
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

from pypdf import PdfWriter
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template


class GerarPDFDocumentoUnicoView(CustomView):
    def get(self, request, *args, **kwargs):
        documento_unico_id = kwargs.get('pk', None)

        if not documento_unico_id:
            return HttpResponse('Objeto não encontrado.')

        obj = DocumentoUnicoFinanceiro.objects.get(pk=documento_unico_id)
        template = get_template('janela_unica/pdf_list.html')
        context = {"obj": obj}
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
        if not pdf.err:
            merger = PdfWriter()
            merger.append(result)
            # TODO: Melhorar isso, se o arquivo não for pdf, necessário converter
            if obj.arquivo and obj.arquivo.name.endswith('.pdf'):
                merger.append(fileobj=obj.arquivo)
            merger.write(result)
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None
