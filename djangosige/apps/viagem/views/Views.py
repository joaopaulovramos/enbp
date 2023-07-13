# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView
from django.shortcuts import redirect
from django.utils import timezone
from datetime import datetime, date, timedelta
from django.contrib import messages
from djangosige.apps.login.models import Usuario
from djangosige.apps.viagem.forms import *
from djangosige.apps.viagem.models import *
import random
import string

from djangosige.apps.viagem.utils import *

ID_TIPO_VIAGEM_REGULAR = '1'
ID_TIPO_VIAGEM_NACIONAL = '1'


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

    def get_context_data(self, **kwargs):
        context = super(AdicionarMotivoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'MOTIVO DE VIAGEM'
        context['return_url'] = reverse_lazy('viagem:listamotivos')
        return context


class EditarMotivoView(CustomUpdateView):
    form_class = TipoMotivoForm
    model = MotivoDeViagemModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listamotivos')
    success_message = "Motivo de Viagem Editada com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

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
        context['title_complete'] = 'Horários Preferenciais'
        context['add_url'] = reverse_lazy('viagem:adicionarhorariopreferencial')
        return context


class AdicionarHorarioPreferencialView(CustomCreateView):
    form_class = HorarioPreferencialForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listahorariopreferencial')
    success_message = "Horário Preferencial adicionado com sucesso."
    permission_codename = 'cadastrar_item_viagens'

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
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(AdicionarTipoNecessidadeEspecialView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR NECESSIDADE ESPECIAL'
        context['return_url'] = reverse_lazy('viagem:listatiposnecessidadeespecial')
        return context

    def get(self, request, *args, **kwargs):
        return super(AdicionarTipoNecessidadeEspecialView, self).get(request, *args, **kwargs)

class EditarTipoNecessidadeEspecialView(CustomUpdateView):
    form_class = TiposNecessidadeEspecialForm
    model = TiposNecessidadeEspecialModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listatiposnecessidadeespecial')
    success_message = "Tipo de Necessidade EspeciaL Editado com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(EditarTipoNecessidadeEspecialView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Edição de Tipo de Necessidade Especial'
        context['return_url'] = reverse_lazy('viagem:listatiposnecessidadeespecial')
        context['id'] = self.object.id
        return context

#### Localidades
class ListLocalidadeView(CustomListView):
    template_name = 'viagem/list_localidades.html'
    model = LocalidadeModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listalocalidades')
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(ListLocalidadeView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Localidades'
        context['add_url'] = reverse_lazy('viagem:adicionarlocalidade')
        return context


class AdicionarLocalidadeView(CustomCreateView):
    form_class = LocalidadeForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listalocalidades')
    success_message = "Localidade adicionada com sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(AdicionarLocalidadeView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR LOCALIDADE'
        context['return_url'] = reverse_lazy('viagem:listalocalidades')
        return context

    def get(self, request, *args, **kwargs):
        return super(AdicionarLocalidadeView, self).get(request, *args, **kwargs)


class EditarLocalidadeView(CustomUpdateView):
    form_class = LocalidadeForm
    model = LocalidadeModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listalocalidades')
    success_message = "Localidade Editada com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(EditarLocalidadeView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Edição de Localidades'
        context['return_url'] = reverse_lazy('viagem:listalocalidades')
        context['id'] = self.object.id
        return context


#### Tabela de Diárias
class ListTabelaDiariaView(CustomListView):
    template_name = 'viagem/list_tabela_diarias.html'
    model = TabelaDiariaModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listatabeladiarias')
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(ListTabelaDiariaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Tabela de Diárias'
        context['add_url'] = reverse_lazy('viagem:adicionartabeladiaria')
        return context


class AdicionarTabelaDiariaView(CustomCreateView):
    form_class = TabelaDiariaForm
    template_name = 'viagem/add.html'
    success_url = reverse_lazy('viagem:listatabeladiarias')
    success_message = "Localidade adicionada com sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(AdicionarTabelaDiariaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR TABELA DIÁRIA'
        context['return_url'] = reverse_lazy('viagem:listatabeladiarias')
        return context

    def get(self, request, *args, **kwargs):
        return super(AdicionarTabelaDiariaView, self).get(request, *args, **kwargs)


class EditarTabelaDiariaView(CustomUpdateView):
    form_class = TabelaDiariaForm
    model = TabelaDiariaModel
    template_name = 'viagem/edit.html'
    success_url = reverse_lazy('viagem:listatabeladiarias')
    success_message = "Tabela de Diária Editada com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(EditarTabelaDiariaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Edição de Tabela de Diárias'
        context['return_url'] = reverse_lazy('viagem:listatabeladiarias')
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
                    if not instance.autorizada_dus and not instance.homologada:
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

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()

        form = self.get_form(form_class)
        form.request_user = self.request.user

        data_hoje = datetime.datetime.now()
        data_inicio = datetime.datetime.strptime(request.POST['dada_inicio'], "%d/%m/%Y %H:%M:%S")
        data_fim = False

        _qtd_diarias = 0
        _valor_diaria = 0
        _valor_total_diarias = 0

        if request.POST['dada_fim']:
            data_fim = datetime.datetime.strptime(request.POST['dada_fim'], "%d/%m/%Y %H:%M:%S")

        if 'itinerario' in request.POST.keys():
            if request.POST['itinerario'] == '1' and not request.POST['dada_fim']:
                form.add_error('dada_fim', 'Informe a data da volta')

        if data_fim and data_fim < data_inicio:
            form.add_error('dada_fim', 'A data fim não pode ser anterior à data início')

        if data_inicio < data_hoje:
            form.add_error('dada_inicio', 'A viagem não pode ser anterior a hoje.')

        # checando se a solicitação é "regular" (id=1) para aplicar a regra de dias de antecedência
        if request.POST['tipo_solicitacao'] == ID_TIPO_VIAGEM_REGULAR:
            diff_dias = data_inicio - data_hoje
            if diff_dias.days < 15:
                form.add_error('dada_inicio',
                               'Para viagens regulares, solicitar com pelo menos 15 dias de antecedência')

        # checando se a solicitação é do tipo nacional (id=1) para aplicar a regra de bagagem despachada
        if request.POST['tipo_viagem'] == ID_TIPO_VIAGEM_NACIONAL and data_fim:
            diff_dias = data_fim - data_inicio

            if 'bagagem_despachada' in request.POST.keys():
                if diff_dias.days < 3 and request.POST['bagagem_despachada']:
                    form.add_error('bagagem_despachada',
                                   'Você não pode despachar bagagem para esta viagem.')

        if data_fim:
            _qtd_diarias = get_diarias(data_inicio, data_fim, 'reservar_hotel' in request.POST.keys())
            usuario = Usuario.objects.get(id=self.request.user.id)
            tabela_diaria = TabelaDiariaModel.objects.filter(localidade_destino=request.POST['localidade_destino'])
            try:
                tabela_diaria = tabela_diaria.get(grupo_funcional=usuario.grupo_funcional)
                _valor_diaria = tabela_diaria.valor_diaria
                _valor_total_diarias = _valor_diaria * Decimal(_qtd_diarias)
            except TabelaDiariaModel.DoesNotExist:
                form.add_error('localidade_destino',  'Seu grupo funcional não tem valores de diárias cadastrado para este destino')

        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.qtd_diarias = _qtd_diarias
            self.object.valor_diaria = _valor_diaria
            self.object.valor_total_diarias = _valor_total_diarias
            self.object.save()
            return self.form_valid(form)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AdicionarViagemView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR VIAGEM'
        context['return_url'] = reverse_lazy('viagem:listaviagem')

        usuario = Usuario.objects.get(id=self.request.user.id)
        context['pcd'] = usuario.pcd

        return context


class EditarViagemView(CustomUpdateView):
    form_class = ViagemForm
    model = ViagemModel
    template_name = 'viagem/edit_viagem.html'
    success_url = reverse_lazy('viagem:listaviagem')
    success_message = "Viagem Editada com Sucesso."
    permission_codename = 'solicitar_viagens'

    def get_context_data(self, **kwargs):
        context = super(EditarViagemView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('viagem:listaviagem')
        context['title_complete'] = 'Edição de viagem'
        context['id'] = self.object.id
        context['user'] = self.request.user
        context['data_inclusao'] = self.object.data_inclusao

        usuario = Usuario.objects.get(id=self.object.solicitante_id)
        context['pcd'] = usuario.pcd

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = form_class(request.POST, instance=self.object)
        form.request_user = self.request.user

        data_hoje = datetime.datetime.now()
        data_inicio = datetime.datetime.strptime(request.POST['dada_inicio'], "%d/%m/%Y %H:%M:%S")
        data_fim = False

        _qtd_diarias = 0
        _valor_diaria = 0
        _valor_total_diarias = 0

        if request.POST['dada_fim']:
            data_fim = datetime.datetime.strptime(request.POST['dada_fim'], "%d/%m/%Y %H:%M:%S")

        if 'itinerario' in request.POST.keys():
            if request.POST['itinerario'] == '1' and not request.POST['dada_fim']:
                form.add_error('dada_fim', 'Informe a data da volta')

        if data_fim and data_fim < data_inicio:
            form.add_error('dada_fim', 'A data fim não pode ser anterior à data início')

        if data_inicio < data_hoje:
            form.add_error('dada_inicio', 'A viagem não pode ser anterior a hoje.')

        # checando se a solicitação é "regular" (id=1) para aplicar a regra de dias de antecedência
        if request.POST['tipo_solicitacao'] == ID_TIPO_VIAGEM_REGULAR:
            diff_dias = data_inicio - data_hoje
            if diff_dias.days < 15:
                form.add_error('dada_inicio',
                               'Para viagens regulares, solicitar com pelo menos 15 dias de antecedência')

        # checando se a solicitação é do tipo nacional (id=1) para aplicar a regra de bagagem despachada
        if request.POST['tipo_viagem'] == ID_TIPO_VIAGEM_NACIONAL and data_fim:
            diff_dias = data_fim - data_inicio

            if 'bagagem_despachada' in request.POST.keys():
                if diff_dias.days < 3 and request.POST['bagagem_despachada']:
                    form.add_error('bagagem_despachada',
                                   'Você não pode despachar bagagem para esta viagem.')
        if data_fim:
            _qtd_diarias = get_diarias(data_inicio, data_fim, 'reservar_hotel' in request.POST.keys())
            usuario = Usuario.objects.get(id=self.object.solicitante_id)
            tabela_diaria = TabelaDiariaModel.objects.filter(localidade_destino=request.POST['localidade_destino'])
            tabela_diaria = tabela_diaria.get(grupo_funcional=usuario.grupo_funcional)
            _valor_diaria = tabela_diaria.valor_diaria
            _valor_total_diarias = _valor_diaria * Decimal(_qtd_diarias)

            print(f'{_valor_total_diarias} * {_qtd_diarias} = {_valor_total_diarias}')

            print(form.errors)


        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.qtd_diarias = _qtd_diarias
            self.object.valor_diaria = _valor_diaria
            self.object.valor_total_diarias = _valor_total_diarias
            self.object.save()
            return redirect(self.success_url)
        return self.form_invalid(form)


class VerSolicitacaoViagem(CustomUpdateView):
    form_class = VerViagemForm
    model = ViagemModel
    template_name = 'viagem/ver_solicitacao.html'
    success_url = reverse_lazy('viagem:listaviagem')
    success_message = "Visualização."
    permission_codename = 'solicitar_viagens'

    def get_context_data(self, **kwargs):
        context = super(VerSolicitacaoViagem, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('viagem:listaviagem')
        context['title_complete'] = 'Visualizando solicitação de viagem'
        context['id'] = self.object.id
        context['user'] = self.request.user
        context['data_inclusao'] = self.object.data_inclusao

        usuario = Usuario.objects.get(id=self.object.solicitante_id)
        context['pcd'] = usuario.pcd

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = form_class(request.POST, instance=self.object)
        form.request_user = self.request.user

        if form.is_valid():
            self.object = form.save()
            return redirect(self.success_url)
        return self.form_invalid(form)


class ListSupAutorizarViagensView(CustomListView):
    template_name = 'viagem/list_all_sup_viagens.html'
    model = ViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listasupautorizarviagem')
    permission_codename = 'autorizar_viagens_sup'

    def get_queryset(self):
        # return self.model.objects.all()
        user_viagens = ViagemModel.objects.filter(autorizada_sup=False)
        user_viagens = user_viagens.filter(recusado_sup =False)

        return user_viagens

    # Remover items selecionados da database
    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if value == "on":

                instance = self.model.objects.get(id=key)
                try:
                    acao = request.POST['acao']
                    if acao == 'sup_recusa_viagem':
                        instance.recusado_sup = True
                        instance.save()
                except Exception:
                    instance.autorizada_sup = True
                    instance.save()
        return redirect(self.success_url)

    def get_object(self):
        current_user = self.request.user
        return ViagemModel.objects.get(user=current_user)

    def get_context_data(self, **kwargs):
        context = super(ListSupAutorizarViagensView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Viagens para autorização - Superintendente'
        return context


class ListAutorizarViagensView(CustomListView):
    template_name = 'viagem/list_all_viagens.html'
    model = ViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listaautorizarviagem')
    permission_codename = 'autorizar_viagens_dus'

    def get_queryset(self):
        # return self.model.objects.all()
        current_user = self.request.user
        user_viagens = ViagemModel.objects.filter(autorizada_dus=False)
        user_viagens = user_viagens.filter(autorizada_sup=True)
        user_viagens = user_viagens.filter(recusado_dus=False)


        return user_viagens

    # Remover items selecionados da database
    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if value == "on":
                instance = self.model.objects.get(id=key)
                try:
                    acao = request.POST['acao']
                    if acao == 'dus_recusa_viagem':
                        instance.recusado_dus = True
                        instance.save()
                except Exception:
                    instance.autorizada_dus = True
                    instance.save()

        return redirect(self.success_url)

    def get_object(self):
        current_user = self.request.user
        return ViagemModel.objects.get(user=current_user)

    def get_context_data(self, **kwargs):
        context = super(ListAutorizarViagensView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Viagens para autorização - DUS'
        return context


class ListHomologarViagensView(CustomListView):
    template_name = 'viagem/list_homologar_viagens.html'
    model = ViagemModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('viagem:listahomologacaoviagem')
    permission_codename = 'homologar_viagens'

    def get_queryset(self):
        user_viagens = ViagemModel.objects.filter(autorizada_dus=True)
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

    def get_context_data(self, **kwargs):
        context = super(PrestarContasView, self).get_context_data(**kwargs)
        context['form_2'] = self.form_2
        context['return_url'] = reverse_lazy('viagem:listaviagem')
        context['title_complete'] = "Realizando prestação de contas"

        context['id'] = self.object.id
        context['origem'] = self.object.origem
        context['destino'] = self.object.destino
        context['data_inicio'] = self.object.dada_inicio
        context['data_fim'] = self.object.dada_fim
        context['data_inclusao'] = self.object.data_inclusao

        usuario_solicitante_id = self.object.solicitante_id
        usuario_solicitante = User.objects.get(id=usuario_solicitante_id)

        context[
            'solicitante'] = f'{usuario_solicitante.get_username()} - {usuario_solicitante.get_full_name()} [{usuario_solicitante_id}]'

        # User.objects.get(id='1').get_username()

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

        viagem = ViagemModel.objects.get(pk=kwargs['pk'])

        # Verifica a submimissão do botão finalizar (que é o salvar prestação de contas)
        if 'finalizar' in request.POST.keys():
            url = reverse_lazy('viagem:prestar_contas_arquivos', kwargs={'pk': kwargs['pk']}, )

            if 'check_remarcacao' in request.POST.keys():
                viagem.remarcacao_interesse_particular = '1'
            else:
                viagem.remarcacao_interesse_particular = '0'

            if 'check_cancelada' in request.POST.keys():
                viagem.justificativa_cancelamento = request.POST['justificativa_cancelamento']
            else:
                viagem.justificativa_cancelamento = ""

            if 'finalizar_pc' in request.POST.keys():
                viagem.finalizar_pc = '1'
                viagem.aprovar_pc = '0'
                url = reverse_lazy('viagem:listaviagem')

            viagem.save()
            return redirect(url)

        self.object = None
        form = ArquivosForm(request.POST, request.FILES, instance=self.object)
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(20))
        nome_antigo = request.FILES['file'].name
        nome_antigo = nome_antigo.split('.')
        ext = nome_antigo[-1]

        data_evento = datetime.datetime.strptime(request.POST['data_evento'], "%d/%m/%Y")
        data_evento = timezone.make_aware(data_evento, timezone.utc)
        if viagem.dada_fim:
            data_fim_viagem = viagem.dada_fim+timedelta(days=1)
            data_inicio_viagem = viagem.dada_inicio + timedelta(days=-1)
            if data_evento < data_inicio_viagem or data_evento > data_fim_viagem:
                form.add_error('data_evento', 'O Evento tem que estar entre o inicio e o fim da viagem com intervalo máximo de 1 dia')
        else:
            data_inicio_viagem = viagem.dada_inicio + timedelta(days=-1)
            if data_evento < data_inicio_viagem:
                form.add_error('data_evento',
                               'O Evento tem que estar entre o inicio e o fim da viagem com intervalo máximo de 1 dia')

        if form.is_valid():
            request.FILES['file'].name = name + '.' + ext
            self.object = self.get_object()
            form.instance.viagem = viagem
            self.object = form.save()
            url = reverse_lazy('viagem:prestar_contas_arquivos', kwargs={'pk': kwargs['pk']}, )
            return redirect(url)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(PrestarContasArquivosView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Prestação de contras'
        context['form_2'] = self.form_2
        context['return_url'] = reverse_lazy('viagem:listaviagem')
        context['viagem_pk'] = pk
        context['arquivos'] = Arquivos.objects.filter(viagem=context['viagem_pk'])

        #Captura o último número de item inserido. Idealmente, os números deveriam ser reorganizados depois de um exclusão
        if context['arquivos'].count() >= 1:
            _qtd_arquivos_enviados = context['arquivos'].latest('numero_item').numero_item
            if _qtd_arquivos_enviados is None:
                _qtd_arquivos_enviados = 1
            context['num_item'] = _qtd_arquivos_enviados + 1
        else:
            context['num_item'] = 1



        total_recursos_proprios = 0
        total_recursos_empresa = 0
        for arquivo in context['arquivos']:
            if arquivo.pagamento == 'RECURSOS PRÓPRIOS':
                total_recursos_proprios += arquivo.valor_pago_reais
            if arquivo.pagamento == 'RECURSOS DA EMPRESA':
                total_recursos_empresa += arquivo.valor_pago_reais

        context['totais_pagos'] = {'recursos_proprios': total_recursos_proprios,
                                   'recursos_empresa': total_recursos_empresa}

        viagem_solicitada = ViagemModel.objects.get(pk=pk)

        context['id'] = viagem_solicitada.id
        context['origem'] = viagem_solicitada.origem
        context['destino'] = viagem_solicitada.destino
        context['data_inicio'] = viagem_solicitada.dada_inicio
        context['data_fim'] = viagem_solicitada.dada_fim
        context['data_inclusao'] = viagem_solicitada.data_inclusao
        context['aprovar_pc'] = viagem_solicitada.aprovar_pc
        context['motivo_pc_reprovacao'] = viagem_solicitada.motivo_reprovacao_pc
        context['remarcacao_interesse_particular'] = viagem_solicitada.remarcacao_interesse_particular
        context['finalizar_pc'] = viagem_solicitada.finalizar_pc
        context['justificativa_cancelamento'] = viagem_solicitada.justificativa_cancelamento

        usuario_solicitante_id = viagem_solicitada.solicitante_id
        usuario_solicitante = User.objects.get(id=usuario_solicitante_id)

        context['solicitante'] = f'{usuario_solicitante.get_username()} - ' \
                                 f'{usuario_solicitante.get_full_name()} [{usuario_solicitante_id}]'

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
    permission_codename = 'aprovar_pc_viagens'

    def get_queryset(self):
        # return self.model.objects.all()
        current_user = self.request.user
        user_viagens = ViagemModel.objects.filter(autorizada_dus=True)
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
    permission_codename = 'aprovar_pc_viagens'
    success_url = reverse_lazy('viagem:listaaprovarpcviagem')

    def post(self, request, *args, **kwargs):

        # self.object.qtd_diarias.di


        if 'acao' in request.POST.keys():
            acao = request.POST['acao']
            instance = self.model.objects.get(pk=kwargs['pk'])
            if acao == 'aprovar_pc':
                instance.aprovar_pc = 1
                instance.save()
                print("aprovando PC")
            if acao == 'reprovar_pc':
                instance.aprovar_pc = 2
                instance.finalizar_pc = 0
                instance.motivo_reprovacao_pc = request.POST['motivo']
                instance.save()

        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(AvaliarArquivosView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Visualizando Prestação de Contas'
        context['form_2'] = self.form_2
        context['return_url'] = reverse_lazy('viagem:listaaprovarpcviagem')
        context['viagem_pk'] = pk
        context['arquivos'] = Arquivos.objects.filter(viagem=context['object'])

        viagem_solicitada = ViagemModel.objects.get(pk=pk)

        total_recursos_proprios = 0
        total_recursos_empresa = 0
        for arquivo in context['arquivos']:
            if arquivo.pagamento == 'RECURSOS PRÓPRIOS':
                total_recursos_proprios += arquivo.valor_pago_reais
            if arquivo.pagamento == 'RECURSOS DA EMPRESA':
                total_recursos_empresa += arquivo.valor_pago_reais

        context['totais_pagos'] = {'recursos_proprios': total_recursos_proprios,
                                   'recursos_empresa': total_recursos_empresa}

        context['id'] = viagem_solicitada.id
        context['origem'] = viagem_solicitada.origem
        context['destino'] = viagem_solicitada.destino
        context['data_inicio'] = viagem_solicitada.dada_inicio
        context['data_fim'] = viagem_solicitada.dada_fim
        context['data_inclusao'] = viagem_solicitada.data_inclusao
        context['remarcacao_interesse_particular'] = viagem_solicitada.remarcacao_interesse_particular
        context['justificativa_cancelamento'] = viagem_solicitada.justificativa_cancelamento

        usuario_solicitante_id = viagem_solicitada.solicitante_id
        usuario_solicitante = User.objects.get(id=usuario_solicitante_id)

        context['solicitante'] = f'{usuario_solicitante.get_username()} - ' \
                                 f'{usuario_solicitante.get_full_name()} [{usuario_solicitante_id}]'
        return context
