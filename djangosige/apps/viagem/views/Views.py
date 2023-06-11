# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView
from django.shortcuts import redirect

from djangosige.apps.viagem.forms import *
from djangosige.apps.viagem.models import *
import random
import string


#### Tipos de Viagens
class ListTipoViagensView(CustomListView):
    template_name = 'viagem/list_tipo_viagem.html'
    model = TiposDeViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listatiposviagens')
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(ListTipoViagensView, self).get_context_data(**kwargs)
        context['title_complete'] = 'TIPOS DE VIAGEM'
        context['add_url'] = reverse_lazy('viagem:adicionartiposviagens')
        return context


class AdicionarTipoViagemView(CustomCreateView):
    form_class = TipoViagemForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listatiposviagens')
    success_message = "Tipo de Viagem adicionado com sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarTipoViagemView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR TIPO DE VIAGEM'
        context['return_url'] = reverse_lazy('viagem:listatiposviagens')
        return context


class EditarTipoViagemView(CustomUpdateView):
    form_class = TipoViagemForm
    model = TiposDeViagemModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listatiposviagens')
    success_message = "Tipo de Viagem Editado com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarTipoViagemView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Edição do Tipo de Viagem'
        context['return_url'] = reverse_lazy('viagem:listatiposviagens')
        context['id'] = self.object.id
        return context


#### Tipos de Solicitação
class ListTipoSolicitacaoView(CustomListView):
    template_name = 'viagem/list_tipo_solicitacao.html'
    model = TiposDeSolicitacaoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listatiposolicitacao')
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(ListTipoSolicitacaoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'TIPOS DE SOLICITAÇÃO'
        context['add_url'] = reverse_lazy('viagem:adicionartiposolicitacao')
        return context


class AdicionarTipoSolicitacaoView(CustomCreateView):
    form_class = TipoDeSolicitacaoForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listatiposolicitacao')
    success_message = "Tipo de Solicitação adicionado com sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarTipoSolicitacaoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR TIPO DE SOLICITAÇÃO'
        context['return_url'] = reverse_lazy('viagem:listatiposolicitacao')
        return context


class EditarTipoSolicitacaoView(CustomUpdateView):
    form_class = TipoDeSolicitacaoForm
    model = TiposDeSolicitacaoModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listatiposolicitacao')
    success_message = "Tipo de Solicitacao Editado com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarTipoSolicitacaoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Edição do Tipo de Solicitação'
        context['return_url'] = reverse_lazy('viagem:listatiposolicitacao')
        context['id'] = self.object.id
        return context


#### Tipos de Transporte
class ListTipoTransporteView(CustomListView):
    template_name = 'viagem/list_tipo_transporte.html'
    model = TipoDeTransporteModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listatipotransporte')
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(ListTipoTransporteView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Tipos de Transporte'
        context['add_url'] = reverse_lazy('viagem:adicionartipotransporte')
        return context


class AdicionarTipoTransporteView(CustomCreateView):
    form_class = TipoDeTransporteForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listatipotransporte')
    success_message = "Tipo de Transporte adicionado com sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarTipoTransporteView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR TIPO DE TRANSPORTE'
        context['return_url'] = reverse_lazy('viagem:listatipotransporte')
        return context


class EditarTipoTransporteView(CustomUpdateView):
    form_class = TipoDeTransporteForm
    model = TipoDeTransporteModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listatipotransporte')
    success_message = "Tipo de Transporte Editado com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarTipoTransporteView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Edição do Tipo de Transporte'
        context['return_url'] = reverse_lazy('viagem:listatipotransporte')
        context['id'] = self.object.id
        return context


#### MotivosViagem
class ListMotivosView(CustomListView):
    template_name = 'viagem/list_motivo.html'
    model = MotivoDeViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listamotivos')
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(ListMotivosView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Motivos de Viagens'
        context['add_url'] = reverse_lazy('viagem:adicionarmotivo')
        return context


class AdicionarMotivoView(CustomCreateView):
    form_class = TipoMotivoForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listamotivos')
    success_message = "Motivo de Viagem adicionado com sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarMotivoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR VIAGEM'
        context['return_url'] = reverse_lazy('viagem:listamotivos')
        return context


class EditarMotivoView(CustomUpdateView):
    form_class = TipoMotivoForm
    model = MotivoDeViagemModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listamotivos')
    success_message = "Motivo de Viagem Editada com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarMotivoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Edição do Motivo da Viagem'
        context['return_url'] = reverse_lazy('viagem:listamotivos')
        context['id'] = self.object.id
        return context


#### TipoDespesa
class ListTipoDespesaView(CustomListView):
    template_name = 'viagem/list_tipo_despesa.html'
    model = TipoDeDespesaModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listatipodespesa')
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(ListTipoDespesaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Tipos de Despesa'
        context['add_url'] = reverse_lazy('viagem:adicionartipodespesa')
        return context


class AdicionarTipoDespesaView(CustomCreateView):
    form_class = TipoDespesaForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listatipodespesa')
    success_message = "Tipo de despesa adicionado com sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarTipoDespesaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR TIPO DE DESPESA'
        context['return_url'] = reverse_lazy('viagem:listatipodespesa')
        return context


class EditarTipoDespesaView(CustomUpdateView):
    form_class = TipoDespesaForm
    model = TipoDeDespesaModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listatipodespesa')
    success_message = "Tipo de Despesa Editado com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarTipoDespesaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Edição de tipo de Despesa'
        context['return_url'] = reverse_lazy('viagem:listatipodespesa')
        context['id'] = self.object.id
        return context


#### Moeda
class ListMoedaView(CustomListView):
    template_name = 'viagem/list_moeda.html'
    model = MoedaModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listamoeda')
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(ListMoedaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Tipos de Moeda'
        context['add_url'] = reverse_lazy('viagem:adicionarmoeda')
        return context


class AdicionarMoedaView(CustomCreateView):
    form_class = MoedaForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listamoeda')
    success_message = "Tipo de moeda adicionado com sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarMoedaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR TIPO DE MOEDA'
        context['return_url'] = reverse_lazy('viagem:listamoeda')
        return context


class EditarMoedaView(CustomUpdateView):
    form_class = MoedaForm
    model = MoedaModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listamoeda')
    success_message = "Tipo de Moeda Editado com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarMoedaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Edição de tipo de Moeda'
        context['return_url'] = reverse_lazy('viagem:listamoeda')
        context['id'] = self.object.id
        return context


#### Categoria Passagem
class ListCategoriaPassagemView(CustomListView):
    template_name = 'viagem/list_categoria_passagem.html'
    model = CategoriaPassagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listacategoriapassagem')
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(ListCategoriaPassagemView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Categorias de Passagem'
        context['add_url'] = reverse_lazy('viagem:adicionarcategoriapassagem')
        return context


class AdicionarCategoriaPassagemView(CustomCreateView):
    form_class = CategoriaPassagemForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listacategoriapassagem')
    success_message = "Categoria de passagem adicionada com sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarCategoriaPassagemView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR CATEGORIA DE PASSAGEM'
        context['return_url'] = reverse_lazy('viagem:listacategoriapassagem')
        return context


class EditarCategoriaPassagemView(CustomUpdateView):
    form_class = CategoriaPassagemForm
    model = CategoriaPassagemModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listacategoriapassagem')
    success_message = "Categoria de Passagem Editada com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarCategoriaPassagemView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Edição de Categoria de Passagem'
        context['return_url'] = reverse_lazy('viagem:listacategoriapassagem')
        context['id'] = self.object.id
        return context


#### Horário Prefencial
class ListHorarioPreferencialView(CustomListView):
    template_name = 'viagem/list_horario_preferencial.html'
    model = HorarioPreferencialModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listahorarioprefencial')
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(ListHorarioPreferencialView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Horários Prefenciais'
        context['add_url'] = reverse_lazy('viagem:adicionarhorariopreferencial')
        return context


class AdicionarHorarioPreferencialView(CustomCreateView):
    form_class = HorarioPreferencialForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listahorariopreferencial')
    success_message = "Horário Preferencial adicionado com sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarHorarioPreferencialView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR HORÁRIO PREFERENCIAL'
        context['return_url'] = reverse_lazy('viagem:listahorariopreferencial')
        return context


class EditarHorarioPreferencialView(CustomUpdateView):
    form_class = HorarioPreferencialForm
    model = HorarioPreferencialModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listahorariopreferencial')
    success_message = "Horário Prefencial Editado com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarHorarioPreferencialView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Edição de Horário Preferencial'
        context['return_url'] = reverse_lazy('viagem:listahorariopreferencial')
        context['id'] = self.object.id
        return context


#### Tipos Necessidade Especial
class ListTiposNecessidadeEspecialView(CustomListView):
    template_name = 'viagem/list_tipo_necessidade_especial.html'
    model = TiposNecessidadeEspecialModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listatiposnecessidadeespecial')
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(ListTiposNecessidadeEspecialView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Tipos de Necessidades Especiais'
        context['add_url'] = reverse_lazy('viagem:adicionartiponecessidadeespecial')
        return context


class AdicionarTipoNecessidadeEspecialView(CustomCreateView):
    form_class = TiposNecessidadeEspecialForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listatiposnecessidadeespecial')
    success_message = "Tipo de Necessidade Especial adicionado com sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarTipoNecessidadeEspecialView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR NECESSIDADE ESPECIAL'
        context['return_url'] = reverse_lazy('viagem:listatiposnecessidadeespecial')
        return context


class EditarTipoNecessidadeEspecialView(CustomUpdateView):
    form_class = TiposNecessidadeEspecialForm
    model = TiposNecessidadeEspecialModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listatiposnecessidadeespecial')
    success_message = "Tipo de Necessidade EspeciaL Editado com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarTipoNecessidadeEspecialView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Edição de Tipo de Necessidade Especial'
        context['return_url'] = reverse_lazy('viagem:listatiposnecessidadeespecial')
        context['id'] = self.object.id
        return context


#### Viagem
class ListViagensView(CustomListView):
    template_name = 'viagem/list_viagens.html'
    model = ViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listaviagem')
    permission_codename = 'solicitar_viagens'

    def get_queryset(self):
        # return self.model.objects.all()
        current_user = self.request.user
        user_viagens = ViagemModel.objects.filter(solicitante=current_user)

        return user_viagens

    def post(self, request, *args, **kwargs):
        if self.check_user_delete_permission(request, self.model):
            for key, value in request.POST.items():
                if value == "on":
                    instance = self.model.objects.get(id=key)
                    if not instance.autorizada and not instance.homologada:
                        instance.delete()

        return redirect(self.success_url)

    def get_object(self):
        current_user = self.request.user
        return ViagemModel.objects.get(user=current_user)

    def get_context_data(self, **kwargs):
        context = super(ListViagensView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Viagens'
        context['add_url'] = reverse_lazy('viagem:adicionarviagem')
        context['login'] = self.request.user
        return context


class AdicionarViagemView(CustomCreateView):
    form_class = ViagemForm
    template_name = 'viagem/add_viagem.html'
    success_url = reverse_lazy('viagem:listaviagem')
    success_message = "Tipo de Viagem adicionado com sucesso."
    permission_codename = 'solicitar_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()

        form = self.get_form(form_class)
        form.request_user = self.request.user

        if form.is_valid():
            self.object = form.save()
            return redirect(self.success_url)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AdicionarViagemView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR VIAGEM'
        context['return_url'] = reverse_lazy('viagem:listaviagem')
        return context


class EditarViagemView(CustomUpdateView):
    form_class = ViagemForm
    model = ViagemModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listaviagem')
    success_message = "Viagem Editada com Sucesso."
    permission_codename = 'solicitar_viagens'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarViagemView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('viagem:listaviagem')
        return context


class ListAutorizarViagensView(CustomListView):
    template_name = 'viagem/list_all_viagens.html'
    model = ViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listaautorizarviagem')
    permission_codename = 'autorizar_viagens'

    def get_queryset(self):
        # return self.model.objects.all()
        current_user = self.request.user
        user_viagens = ViagemModel.objects.filter(autorizada=False)

        return user_viagens

    # Remover items selecionados da database
    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if value == "on":
                instance = self.model.objects.get(id=key)
                instance.autorizada = True
                instance.save()
        return redirect(self.success_url)

    def get_object(self):
        current_user = self.request.user
        return ViagemModel.objects.get(user=current_user)

    def get_context_data(self, **kwargs):
        context = super(ListAutorizarViagensView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Viagens'
        return context


class ListHomologarViagensView(CustomListView):
    template_name = 'viagem/list_homologar_viagens.html'
    model = ViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listahomologacaoviagem')
    permission_codename = 'homologar_viagens'

    def get_queryset(self):
        # return self.model.objects.all()
        current_user = self.request.user
        user_viagens = ViagemModel.objects.filter(autorizada=True)
        user_viagens = user_viagens.filter(homologada=False)

        return user_viagens

    # Remover items selecionados da database
    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if value == "on":
                instance = self.model.objects.get(id=key)
                instance.homologada = True
                instance.save()
        return redirect(self.success_url)

    def get_object(self):
        current_user = self.request.user
        return ViagemModel.objects.get(user=current_user)

    def get_context_data(self, **kwargs):
        context = super(ListHomologarViagensView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Viagens'
        return context


class PrestarContasView(CustomUpdateView):
    form_class = PrestacaoContaForm
    model = ViagemModel
    form_2 = ArquivosForm
    template_name = 'viagem/prestacao_de_contas.html'
    success_url = reverse_lazy('viagem:listaviagem')
    success_message = "Viagem Editada com Sucesso."
    permission_codename = 'solicitar_viagens'

    def post(self, request, *args, **kwargs):
        # arquivo = request.FILES['file']
        if request.FILES:
            self.object = None
            form = ArquivosForm(request.POST, request.FILES, instance=self.object)

            letters = string.ascii_lowercase
            name = ''.join(random.choice(letters) for i in range(20))
            nome_antigo = request.FILES['file'].name
            nome_antigo = nome_antigo.split('.')
            ext = nome_antigo[-1]

            if form.is_valid():
                request.FILES['file'].name = name + '.' + ext

                self.object = self.get_object()
                form.instance.viagem = ViagemModel.objects.get(pk=kwargs['pk'])
                self.object = form.save()
                return redirect(self.success_url)
            # return self.form_invalid(form)
        else:
            self.object = self.get_object()
            form_class = self.get_form_class()
            form = form_class(request.POST, instance=self.object)
            if form.is_valid():
                self.object = form.save()
                return redirect(self.success_url)
            return self.form_invalid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(PrestarContasView, self).get_context_data(**kwargs)
        context['form_2'] = self.form_2
        context['return_url'] = reverse_lazy('viagem:listaviagem')
        # Arquivos.objects.get(pk=kwargs['pk'])
        # viagem = ViagemModel.objects.get(pk=kwargs['pk'])

        context['arquivos'] = Arquivos.objects.filter(viagem=context['object'])

        return context


#######################################################################################


class RemoverArquivoView(CustomUpdateView):
    form_class = ArquivosForm
    model = Arquivos
    template_name = 'viagem/remove_file_control.html'
    success_url = reverse_lazy('viagem:listaviagem')
    success_message = "Viagem Editada com Sucesso."
    permission_codename = 'solicitar_viagens'

    def get_success_message(self, cleaned_data):
        objetos = self.success_message % dict(cleaned_data, cfop=self.object.cfop)
        return objetos

    def get_context_data(self, **kwargs):
        context = super(RemoverArquivoView, self).get_context_data(**kwargs)
        context['object'].delete()
        context['viagem'] = self.kwargs['viagem']
        url = reverse_lazy('viagem:prestar_contas_arquivos', kwargs={'pk': self.kwargs['viagem']}, )
        return context


class PrestarContasArquivosView(CustomUpdateView):
    form_class = PrestacaoContaForm
    model = ViagemModel
    form_2 = ArquivosForm
    template_name = 'viagem/prestacao_de_contas_arquivos.html'
    success_message = "Viagem Editada com Sucesso."
    permission_codename = 'solicitar_viagens'

    def post(self, request, *args, **kwargs):
        self.object = None
        form = ArquivosForm(request.POST, request.FILES, instance=self.object)
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(20))
        nome_antigo = request.FILES['file'].name
        nome_antigo = nome_antigo.split('.')
        ext = nome_antigo[-1]

        if form.is_valid():
            request.FILES['file'].name = name + '.' + ext
            self.object = self.get_object()
            form.instance.viagem = ViagemModel.objects.get(pk=kwargs['pk'])
            self.object = form.save()
            url = reverse_lazy('viagem:prestar_contas_arquivos', kwargs={'pk': kwargs['pk']}, )
            return redirect(url)
            # return self.form_invalid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(PrestarContasArquivosView, self).get_context_data(**kwargs)
        context['form_2'] = self.form_2
        context['return_url'] = reverse_lazy('viagem:listaviagem')
        context['viagem_pk'] = pk
        context['arquivos'] = Arquivos.objects.filter(viagem=context['object'])

        return context


#######################################################################################


class EnviarArquivosView(CustomUpdateView):
    form_class = ArquivosForm
    model = ViagemModel
    form_2 = ArquivosForm
    template_name = 'viagem/enviar_arquivos.html'
    success_url = reverse_lazy('viagem:listaviagem')
    success_message = "Viagem Editada com Sucesso."
    permission_codename = 'solicitar_viagens'

    def post(self, request, *args, **kwargs):
        self.object = None
        form = ArquivosForm(request.POST, request.FILES, instance=self.object)

        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(20))
        nome_antigo = request.FILES['file'].name
        nome_antigo = nome_antigo.split('.')
        ext = nome_antigo[-1]

        if form.is_valid():
            request.FILES['file'].name = name + '.' + ext

            self.object = self.get_object()
            form.instance.viagem = ViagemModel.objects.get(pk=kwargs['pk'])
            self.object = form.save()
            return redirect(self.success_url)
        # return self.form_invalid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EnviarArquivosView, self).get_context_data(**kwargs)
        context['form_2'] = self.form_2
        context['return_url'] = reverse_lazy('viagem:listaviagem')
        # Arquivos.objects.get(pk=kwargs['pk'])
        # viagem = ViagemModel.objects.get(pk=kwargs['pk'])

        context['arquivos'] = Arquivos.objects.filter(viagem=context['object'])

        return context


class ArquivosViagemView(CustomCreateView):
    form_class = ArquivosForm
    template_name = 'viagem/add_files.html'
    success_url = reverse_lazy('viagem:arquivosviagem')
    success_message = "Arquivos da Viagem"
    permission_codename = 'cadastrar_item_viagens'

    def get(self, request, *args, **kwargs):
        self.object = None
        obj = super().get(request, *args, **kwargs)
        # viagem = ViagemModel.objects.get(id=45)
        # # form_class = ArquivosForm(initial={'viagem': viagem})
        # obj.context_data['form'](initial={'viagem': viagem})

        # current_user = self.request.user
        # lviagems = ViagemModel.objects.get(id=45)
        # #lviagems = ViagemModel.objects.filter(solicitante=current_user)
        # valor = obj.context_data['form'].fields['viagem'] = lviagems
        return obj

    # def get_queryset(self):
    #     # # return self.model.objects.all()
    #     # current_user = self.request.user
    #     # user_viagens = ArquivosForm.objects.filter(autorizada=True)
    #     # user_viagens = user_viagens.filter(homologada=False)
    #     return self.model.objects.all()

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def post(self, request, *args, **kwargs):
        self.object = None

        form = ArquivosForm(request.POST, request.FILES, instance=self.object)
        form.instance.viagem = ViagemModel.objects.get(pk=45)
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(20))
        nome_antigo = request.FILES['file'].name
        nome_antigo = nome_antigo.split('.')
        ext = nome_antigo[-1]

        if form.is_valid():
            request.FILES['file'].name = name + '.' + ext
            self.object = form.save()
            return redirect(self.success_url)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(ArquivosViagemView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR ARQUIVOS'
        context['return_url'] = reverse_lazy('viagem:arquivosviagem')
        return context


class ListAprovarPCViagensView(CustomListView):
    template_name = 'viagem/list_aprovar_pc_viagens.html'
    model = ViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listaaprovarpcviagem')
    permission_codename = 'homologar_viagens'

    def get_queryset(self):
        # return self.model.objects.all()
        current_user = self.request.user
        user_viagens = ViagemModel.objects.filter(autorizada=True)
        user_viagens = user_viagens.filter(homologada=True)
        user_viagens = user_viagens.filter(finalizar_pc=1).exclude(aprovar_pc=1)

        return user_viagens

    # Remover items selecionados da database
    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if value == "on":
                acao = request.POST['acao']
                if acao == 'aprovar_pc':
                    instance = self.model.objects.get(id=key)
                    instance.aprovar_pc = 1
                    instance.save()
                if acao == 'reprovar_pc':
                    instance = self.model.objects.get(id=key)
                    instance.aprovar_pc = 2
                    instance.finalizar_pc = 0
                    instance.save()
        return redirect(self.success_url)

    def get_object(self):
        current_user = self.request.user
        return ViagemModel.objects.get(user=current_user)

    def get_context_data(self, **kwargs):
        context = super(ListAprovarPCViagensView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Viagens'
        return context


class AvaliarPrestacaoDeContas(CustomUpdateView):
    form_class = AvaliarPrestacaoContaForm
    model = ViagemModel
    form_2 = ArquivosForm
    template_name = 'viagem/ver_prestacao_de_contas.html'
    success_url = reverse_lazy('viagem:listaaprovarpcviagem')
    success_message = "Viagem Editada com Sucesso."
    permission_codename = 'solicitar_viagens'

    def post(self, request, *args, **kwargs):
        # arquivo = request.FILES['file']
        if request.FILES:
            self.object = None
            form = ArquivosForm(request.POST, request.FILES, instance=self.object)

            letters = string.ascii_lowercase
            name = ''.join(random.choice(letters) for i in range(20))
            nome_antigo = request.FILES['file'].name
            nome_antigo = nome_antigo.split('.')
            ext = nome_antigo[-1]

            if form.is_valid():
                request.FILES['file'].name = name + '.' + ext

                self.object = self.get_object()
                form.instance.viagem = ViagemModel.objects.get(pk=kwargs['pk'])
                self.object = form.save()
                return redirect(self.success_url)
            # return self.form_invalid(form)
        else:
            self.object = self.get_object()
            form_class = self.get_form_class()
            form = form_class(request.POST, instance=self.object)
            if form.is_valid():
                self.object = form.save()
                return redirect(self.success_url)
            return self.form_invalid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AvaliarPrestacaoDeContas, self).get_context_data(**kwargs)
        context['form_2'] = self.form_2
        context['return_url'] = reverse_lazy('viagem:listaaprovarpcviagem')
        # Arquivos.objects.get(pk=kwargs['pk'])
        # viagem = ViagemModel.objects.get(pk=kwargs['pk'])

        context['arquivos'] = Arquivos.objects.filter(viagem=context['object'])

        return context


class AvaliarSolicitacaoViagem(CustomUpdateView):
    form_class = AvaliarSolicitacaoViagemForm
    model = ViagemModel
    form_2 = ArquivosForm
    template_name = 'viagem/ver_prestacao_de_contas.html'
    success_url = reverse_lazy('viagem:listaaprovarpcviagem')
    success_message = "Viagem Editada com Sucesso."
    permission_codename = 'solicitar_viagens'

    def post(self, request, *args, **kwargs):
        # arquivo = request.FILES['file']
        if request.FILES:
            self.object = None
            form = ArquivosForm(request.POST, request.FILES, instance=self.object)

            letters = string.ascii_lowercase
            name = ''.join(random.choice(letters) for i in range(20))
            nome_antigo = request.FILES['file'].name
            nome_antigo = nome_antigo.split('.')
            ext = nome_antigo[-1]

            if form.is_valid():
                request.FILES['file'].name = name + '.' + ext

                self.object = self.get_object()
                form.instance.viagem = ViagemModel.objects.get(pk=kwargs['pk'])
                self.object = form.save()
                return redirect(self.success_url)
            # return self.form_invalid(form)
        else:
            self.object = self.get_object()
            form_class = self.get_form_class()
            form = form_class(request.POST, instance=self.object)
            if form.is_valid():
                self.object = form.save()
                return redirect(self.success_url)
            return self.form_invalid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AvaliarSolicitacaoViagem, self).get_context_data(**kwargs)
        context['form_2'] = self.form_2
        context['return_url'] = reverse_lazy('viagem:listaaprovarpcviagem')
        # Arquivos.objects.get(pk=kwargs['pk'])
        # viagem = ViagemModel.objects.get(pk=kwargs['pk'])

        context['arquivos'] = Arquivos.objects.filter(viagem=context['object'])

        return context


class AvaliarArquivosView(CustomUpdateView):
    form_class = PrestacaoContaForm
    model = ViagemModel
    form_2 = ArquivosForm
    template_name = 'viagem/avaliar_arquivos.html'
    success_message = "Viagem Editada com Sucesso."
    permission_codename = 'solicitar_viagens'

    def post(self, request, *args, **kwargs):
        self.object = None
        form = ArquivosForm(request.POST, request.FILES, instance=self.object)
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(20))
        nome_antigo = request.FILES['file'].name
        nome_antigo = nome_antigo.split('.')
        ext = nome_antigo[-1]

        if form.is_valid():
            request.FILES['file'].name = name + '.' + ext
            self.object = self.get_object()
            form.instance.viagem = ViagemModel.objects.get(pk=kwargs['pk'])
            self.object = form.save()
            url = reverse_lazy('viagem:prestar_contas_arquivos', kwargs={'pk': kwargs['pk']}, )
            return redirect(url)
            # return self.form_invalid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(AvaliarArquivosView, self).get_context_data(**kwargs)
        context['form_2'] = self.form_2
        context['return_url'] = reverse_lazy('viagem:listaaprovarpcviagem')
        context['viagem_pk'] = pk
        context['arquivos'] = Arquivos.objects.filter(viagem=context['object'])

        return context
