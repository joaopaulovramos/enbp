

from django.urls import reverse_lazy

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView

from djangosige.apps.janela_unica.forms import *
from djangosige.apps.janela_unica.models import *
from django.utils.formats import localize
from django.shortcuts import render


class ListDocumentosViagensView(CustomListView):
    template_name = 'janela_unica/list_ja.html'
    model = DocumentoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('janela_unica:listadocumentos')
    permission_codename = 'cadastrar_item_viagens'

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

    def get_context_data(self, **kwargs):
        context = super(AdicionarDocumentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR DOCUMENTO'
        context['return_url'] = reverse_lazy('viagem:listatiposviagens')
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


def home(request):
    all_tasks = []
    t_list = request.user.tasks.all()
    for t in t_list:
        t_dict = {
            'uuid': str(t.uuid),
            'name': t.name if t.name is not None else 'Без названия',
            'boardName': t.boardName,
            'date': str(localize(t.date))
        }
        all_tasks.append(t_dict)
    return render(request, 'janela_unica/board/index.html', {'tasks': all_tasks})
