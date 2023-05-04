# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView

from djangosige.apps.fiscal.forms import NaturezaOperacaoForm
from djangosige.apps.fiscal.models import NaturezaOperacao


from djangosige.apps.exemplo.forms.FormExemplo import ExemploForm
from djangosige.apps.exemplo.models.exemplo import ExemploModel



class ListView(CustomListView):
    template_name = 'exemplo/exemplo_operacao/exemplo_operacao_list.html'
    model = ExemploModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('exemplo:listaexemplo')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Exemplo'
        context['add_url'] = reverse_lazy('exemplo:adicionaexemplo')
        return context

class AdicionarView(CustomCreateView):
    #form_class = NaturezaOperacaoForm
    form_class = ExemploForm
    template_name = "exemplo/exemplo_operacao/exemplo_operacao_add.html"
    success_url = reverse_lazy('exemplo:adicionaexemplo')
    success_message = "Adicionar Exemplo <b>%(cfop)s </b>adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR EXEMPLO'
        context['return_url'] = reverse_lazy('exemplo:adicionaexemplo')
        return context





class EditarView(CustomUpdateView):
    form_class = NaturezaOperacaoForm
    model = NaturezaOperacao
   # template_name = "fiscal/natureza_operacao/natureza_operacao_edit.html"
    template_name = "exemplo/exemplo_operacao/exemplo_operacao_edit.html"
    success_url = reverse_lazy('fiscal:listanaturezaoperacaoview')
    success_message = "Natureza da operação <b>%(cfop)s </b>editada com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarView,
                        self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy(
            'fiscal:listanaturezaoperacaoview')
        return context
