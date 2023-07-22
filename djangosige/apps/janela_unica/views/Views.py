

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from geraldo.generators import PDFGenerator
from datetime import datetime
from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView, CustomView
from djangosige.apps.cadastro.models.empresa import MinhaEmpresa
from django.template.defaultfilters import date

from djangosige.apps.janela_unica.forms import *
from djangosige.apps.janela_unica.models import *
from django.utils.formats import localize
from django.shortcuts import render
import io

from djangosige.apps.janela_unica.report_janela_unica import DocumentoUnicoFinaceiroReport
from djangosige.apps.login.models import Usuario
from djangosige.configs.settings import MEDIA_ROOT

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

from pypdf import PdfWriter

class GerarPDFDocumentoUnicoView(CustomView):
    def get(self, request, *args, **kwargs):
        documento_unico_id = kwargs.get('pk', None)

        if not documento_unico_id:
            return HttpResponse('Objeto não encontrado.')

        obj = DocumentoUnicoFinanceiro.objects.get(pk=documento_unico_id)
        title = 'Solicitação Documento Único nº {}'.format(documento_unico_id)

        return self.gerar_pdf(title, obj, request.user.id)

    def gerar_pdf(self, title, documento, user_id):
        resp = HttpResponse(content_type='application/pdf')

        documento_pdf = io.BytesIO()
        documento_report = DocumentoUnicoFinaceiroReport(queryset=[documento, ])
        documento_report.title = title

        documento_report.band_page_footer = documento_report.banda_foot

        try:
            usuario = Usuario.objects.get(pk=user_id)
            m_empresa = MinhaEmpresa.objects.get(m_usuario=usuario)
            flogo = m_empresa.m_empresa.logo_file
            logo_path = '{0}{1}'.format(MEDIA_ROOT, flogo.name)
            if flogo != 'imagens/logo.png':
                documento_report.topo_pagina.inserir_logo(logo_path)

            documento_report.band_page_footer.inserir_nome_empresa(
                m_empresa.m_empresa.nome_razao_social)
            if m_empresa.m_empresa.endereco_padrao:
                documento_report.band_page_footer.inserir_endereco_empresa(
                    m_empresa.m_empresa.endereco_padrao.format_endereco_completo)
            if m_empresa.m_empresa.telefone_padrao:
                documento_report.band_page_footer.inserir_telefone_empresa(
                    m_empresa.m_empresa.telefone_padrao.telefone)
        except:
            pass

        documento_report.topo_pagina.inserir_data_emissao(documento.data_inclusao)
        documento_report.band_page_header = documento_report.topo_pagina

        if documento.fornecedor.tipo_pessoa == 'PJ':
            documento_report.dados_cliente.inserir_informacoes_pj()
        elif documento.fornecedor.tipo_pessoa == 'PF':
            documento_report.dados_cliente.inserir_informacoes_pf()
        
        documento_report.band_page_header.child_bands.append(
            documento_report.dados_cliente)

        documento_report.band_page_header.child_bands.append(
            documento_report.observacoes)

        documento_report.generate_by(PDFGenerator, filename=documento_pdf)
        pdf = documento_pdf.getvalue()

        #Fazer merge do relatorio geraldo + anexo
        merger = PdfWriter()
        merger.append(documento_pdf)
        #TODO: Melhorar isso, se o arquivo não for pdf, necessário converter
        if documento.arquivo and documento.arquivo.name.endswith('.pdf'):
            merger.append(fileobj=documento.arquivo)
        merger.write(resp)
        # resp.write(pdf)

        return resp

