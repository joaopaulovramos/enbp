from django.urls import reverse_lazy

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView, CustomListViewFilter, \
    CustomCreateViewAddUser

from djangosige.apps.timesheet.forms.timesheet_forms import *
from djangosige.apps.timesheet.models.timesheet_model import *

from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect

LIMITE_HORAS_DIA = 8


class AprovarTimesheetView(CustomListViewFilter):
    template_name = 'timesheet/timesheet_aprovar.html'
    model = HorasSemanais
    context_object_name = 'all_natops'
    success_url = reverse_lazy('timesheet:aprovartimesheet')
    permission_codename = 'view_naturezaoperacao'

    def get_queryset(self):
        querry = HorasSemanais.objects.filter(submetida=True)

        return querry

    # def get_queryset(self):
    #     return self.model.objects.all()

    def get_object(self):
        current_user = self.request.user
        return HorasSemanais.objects.all(user='1')

    def get_context_data(self, **kwargs):
        context = super(AprovarTimesheetView, self).get_context_data(**kwargs, object_list=None)
        # context = self.get_object()
        context['title_complete'] = 'Aprovar Horas'
        return context


class ListTimesheetView(CustomListViewFilter):
    template_name = 'timesheet/timesheet_list.html'
    model = HorasSemanais
    context_object_name = 'all_natops'
    success_url = reverse_lazy('timesheet:listatimesheet')
    permission_codename = 'view_naturezaoperacao'

    def get_queryset(self):
        current_user = self.request.user
        querry = HorasSemanais.objects.filter(solicitante=current_user)
        # querry = querry.filter(submetida=False)
        return querry

    def get_object(self):
        current_user = self.request.user
        return HorasSemanais.objects.all(user='1')

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if value == "on":
                acao = request.POST['acao']
                if acao == 'submeter_horas':
                    instance = self.model.objects.get(id=key)
                    instance.situacao = 1
                    instance.save()
                elif acao == 'excluir':
                    instance = self.model.objects.get(id=key)
                    if instance.situacao == 0:
                        instance.delete()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(ListTimesheetView, self).get_context_data(**kwargs, object_list=None)
        # context = self.get_object()
        context['title_complete'] = 'Timesheet'
        context['add_url'] = reverse_lazy('timesheet:adicionatimesheet')
        return context


class AdicionarTimesheetView(CustomCreateViewAddUser):
    form_class = HorasSemanaisForm
    template_name = "timesheet/add_percentual.html"
    success_url = reverse_lazy('timesheet:listatimesheet')
    success_message = "Horas adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'
    context_object_name = 'all_natops'

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()

        form = self.get_form(form_class)
        form.request_user = self.request.user

        # É permitido horas fracionada?
        # validar quantidade de horas e horas futuras

        # date_selected = request.POST['semanas'].split(" - ")
        # inicio_semana = datetime.datetime.strptime(date_selected[0], "%d/%m/%Y").date()
        # fim_semana = datetime.datetime.strptime(date_selected[1], "%d/%m/%Y").date()
        # hoje = datetime.datetime.now().date()
        #
        # inputs_dias_semana = ['hr_seg', 'hr_ter', 'hr_qua', 'hr_qui', 'hr_sex', 'hr_sab', 'hr_dom', ]
        #
        # if hoje > fim_semana:
        #     return self.form_invalid(form)
        # else:
        #     if hoje >= inicio_semana:
        #         for i, v in enumerate(inputs_dias_semana):
        #             if i > hoje.isoweekday():
        #                 print(hoje.isoweekday(), " ", i, "d eu ruim")
        #
        # print(hoje <= fim_semana)
        #
        # print(inicio_semana, " ", fim_semana, " ", hoje)

        if form.is_valid():
            self.object = form.save()
            return redirect(self.success_url)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        self.form_class.Meta.model.user = self.request.user
        context = super(AdicionarTimesheetView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR HORAS'
        context['return_url'] = reverse_lazy('timesheet:listatimesheet')
        return context


class AprovarTimesheetView(CustomListViewFilter):
    template_name = 'timesheet/timesheet_aprovar.html'
    model = HorasSemanais
    context_object_name = 'all_natops'
    success_url = reverse_lazy('timesheet:aprovartimesheet')
    permission_codename = 'view_naturezaoperacao'

    def get_queryset(self):
        current_user = self.request.user
        querry = HorasSemanais.objects.filter(situacao=1)
        # querry = querry.filter(submetida=False)
        return querry

    def get_object(self):
        current_user = self.request.user
        return HorasSemanais.objects.all(user=current_user)

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if value == "on":
                acao = request.POST['acao']
                if acao == 'reprovar-horas':
                    instance = self.model.objects.get(id=key)
                    instance.situacao = 3
                    instance.save()
                else:
                    instance = self.model.objects.get(id=key)
                    instance.situacao = 2
                    instance.save()

        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(AprovarTimesheetView, self).get_context_data(**kwargs, object_list=None)
        # context = self.get_object()
        context['title_complete'] = 'Sub-Grupo'
        context['add_url'] = reverse_lazy('timesheet:aprovartimesheet')
        return context


class AprovarGastosView(CustomListViewFilter):
    template_name = 'timesheet/aprovar_gastos.html'
    model = Gastos
    context_object_name = 'all_natops'
    success_url = reverse_lazy('timesheet:aprovargastos')
    permission_codename = 'view_naturezaoperacao'

    def get_queryset(self):
        current_user = self.request.user
        querry = Gastos.objects.filter(situacao='1')
        # querry = querry.filter(submetida=False)
        return querry

    def post(self, request, *args, **kwargs):
        if self.check_user_delete_permission(request, self.model):
            for key, value in request.POST.items():
                if value == "on":

                    if 'acao' in request.POST:
                        acao = request.POST['acao']
                        if acao == 'aprovar_gastos':
                            instance = self.model.objects.get(id=key)
                            instance.situacao = 2
                            instance.save()
                        elif acao == 'reprovar_gastos':
                            instance = self.model.objects.get(id=key)
                            instance.situacao = 3
                            instance.save()

        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(AprovarGastosView, self).get_context_data(**kwargs, object_list=None)
        # context = self.get_object()
        context['title_complete'] = 'Listar Gastos'
        context['add_url'] = reverse_lazy('timesheet:incluirgastos')
        return context


class ListGastosView(CustomListViewFilter):
    template_name = 'timesheet/listar_gastos.html'
    model = Gastos
    context_object_name = 'all_natops'
    success_url = reverse_lazy('timesheet:listargastos')
    permission_codename = 'view_naturezaoperacao'

    def get_queryset(self):
        current_user = self.request.user
        querry = Gastos.objects.filter(solicitante=current_user)
        # querry = querry.filter(submetida=False)
        return querry

    def post(self, request, *args, **kwargs):
        if self.check_user_delete_permission(request, self.model):
            for key, value in request.POST.items():
                if value == "on":

                    if 'acao' in request.POST:
                        acao = request.POST['acao']
                        if acao == 'submeter_gastos':
                            instance = self.model.objects.get(id=key)
                            instance.situacao = 1
                            instance.save()
                    else:
                        instance = self.model.objects.get(id=key)
                        instance.delete()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(ListGastosView, self).get_context_data(**kwargs, object_list=None)
        # context = self.get_object()
        context['title_complete'] = 'Listar Gastos'
        context['add_url'] = reverse_lazy('timesheet:incluirgastos')
        return context


class AdicionarGastoView(CustomCreateView):
    form_class = GastosForm
    template_name = 'timesheet/add_percentual.html'
    success_url = reverse_lazy('timesheet:listargastos')
    success_message = "Adicionar Exemplo <b>%(cfop)s </b>adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def post(self, request, *args, **kwargs):
        self.object = None

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.request_user = self.request.user
        if form.is_valid():
            self.object = form.save()
            return redirect(self.success_url)
        return self.form_invalid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarGastoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR EXEMPLO'
        context['return_url'] = reverse_lazy('timesheet:listargastos')
        return context


class AdicionarPercentualDiarioView(CustomCreateViewAddUser):
    form_class = PercentualDiarioForm
    template_name = "timesheet/add_percentual.html"
    success_url = reverse_lazy('timesheet:adicionarpercentualdiario')
    success_message = "Percentual de horas trabalhadas lançado com sucesso."
    permission_codename = 'add_percentualdiario'
    context_object_name = 'all_natops'

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()

        form = self.get_form(form_class)
        form.request_user = self.request.user

        data = datetime.datetime.strptime(request.POST['data'], "%d/%m/%Y").date()
        hoje = datetime.datetime.now().date()

        if data > hoje:
            form.add_error('data', 'Não é possível lança horas futuras.')

        # seleciona os laçamentos do usuário já existentes para o dia
        lancamentos_dia = PercentualDiario.objects.filter(solicitante=self.request.user, data=data)

        total_percentual_dia = 0
        for lancamento in lancamentos_dia:
            total_percentual_dia += lancamento.percentual
            if int(self.request.POST['projeto']) == lancamento.projeto_id:
                form.add_error('projeto', 'Você já lançou horas para este projeto nesta data')

        if float(total_percentual_dia) + float(self.request.POST['percentual']) > 100.00:
            form.add_error('percentual', 'O percentual diário não pode ultrapassar 100% de horas')

        if form.is_valid():
            self.object = form.save()
            return redirect(self.success_url)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        self.form_class.Meta.model.user = self.request.user
        context = super(AdicionarPercentualDiarioView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR PERCENTUAL DE HORAS'
        context['return_url'] = reverse_lazy('timesheet:listarpercentualdiario')

        lista_timesheet = PercentualDiario.objects.filter(solicitante=self.request.user)

        projetos = set()
        datas = set()

        for timesheet in lista_timesheet:
            projetos.add(timesheet.projeto)
            datas.add(str(timesheet.data))

        datas_dict = {key: None for key in datas}

        for data in datas_dict.keys():

            projetos_dict = {key: None for key in projetos}
            total_percentual_dia = 0.00
            for timesheet in lista_timesheet:

                if data == str(timesheet.data):
                    projetos_dict[timesheet.projeto] = {'percentual': timesheet.percentual, 'id': timesheet.id}
                    total_percentual_dia += float(timesheet.percentual)

            datas_dict[data] = [projetos_dict, total_percentual_dia, int(total_percentual_dia)]

        context['timesheet'] = datas_dict
        context['projetos'] = projetos

        return context


class EditarPercentualDiarioView(CustomUpdateView):
    form_class = PercentualDiarioForm
    model = PercentualDiario
    template_name = 'timesheet/edit_percentual.html'
    success_url = reverse_lazy('timesheet:listarpercentualdiario')
    success_message = "Percentual de horas Editado com Sucesso."
    permission_codename = 'cadastrar_item_viagens'

    def get_context_data(self, **kwargs):
        context = super(EditarPercentualDiarioView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Edição de percentual de horas'
        context['return_url'] = reverse_lazy('timesheet:listarpercentualdiario')
        context['id'] = self.object.id

        lista_timesheet = PercentualDiario.objects.filter(solicitante=self.request.user)

        projetos = set()
        datas = set()

        for timesheet in lista_timesheet:
            projetos.add(timesheet.projeto)
            datas.add(str(timesheet.data))

        datas_dict = {key: None for key in datas}

        for data in datas_dict.keys():

            projetos_dict = {key: None for key in projetos}
            total_percentual_dia = 0.00
            for timesheet in lista_timesheet:

                if data == str(timesheet.data):
                    projetos_dict[timesheet.projeto] = {'percentual': timesheet.percentual, 'id': timesheet.id}
                    total_percentual_dia += float(timesheet.percentual)
                    _data = timesheet.data

            datas_dict[data] = [projetos_dict, total_percentual_dia, int(total_percentual_dia), _data]

        context['timesheet'] = datas_dict
        context['projetos'] = projetos

        return context

    def post(self, request, *args, **kwargs):

        # Sobreescreve a url de sucesso considerando o pk
        self.success_url = reverse_lazy('timesheet:editarpercentualdiario', kwargs={'pk': kwargs['pk']})

        self.object = self.get_object()
        form_class = self.get_form_class()
        form = form_class(request.POST, instance=self.object)
        form.request_user = self.request.user

        data = datetime.datetime.strptime(request.POST['data'], "%d/%m/%Y").date()
        hoje = datetime.datetime.now().date()

        if data > hoje:
            form.add_error('data', 'Não é possível lança horas futuras.')

        # seleciona os laçamentos do usuário para o mesmo dia, excluindo o que está sob atualização
        lancamentos_dia = self.model.objects.filter(solicitante=self.request.user, data=data).exclude(pk=kwargs['pk'])

        total_percentual_dia = 0
        for lancamento in lancamentos_dia:
            total_percentual_dia += lancamento.percentual
            if int(self.request.POST['projeto']) == lancamento.projeto_id:
                form.add_error('projeto', 'Você já lançou horas para este projeto nesta data')

        if float(total_percentual_dia) + float(self.request.POST['percentual']) > 100.00:
            form.add_error('percentual', 'O percentual diário não pode ultrapassar 100% de horas')

        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.save()
            return self.form_valid(form)
        return self.form_invalid(form)


class ListPercentualDiarioView(CustomListViewFilter):
    template_name = 'timesheet/timesheet_percentual_list.html'
    model = PercentualDiario
    context_object_name = 'all_natops'
    success_url = reverse_lazy('timesheet:listarpercentualdiario')
    permission_codename = 'view_percentualdiario'

    def get_queryset(self):
        current_user = self.request.user
        querry = self.model.objects.filter(solicitante=current_user)
        # querry = querry.filter(submetida=False)
        return querry

    def get_object(self):
        current_user = self.request.user
        return self.model.objects.all(user=current_user)

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if value == "on":
                acao = request.POST['acao']
                if acao == 'submeter_horas':
                    instance = self.model.objects.get(id=key)
                    instance.situacao = 1
                    instance.save()
                elif acao == 'excluir':
                    instance = self.model.objects.get(id=key)
                    if instance.situacao == 0:
                        instance.delete()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(ListPercentualDiarioView, self).get_context_data(**kwargs, object_list=None)
        # context = self.get_object()
        context['title_complete'] = 'Timesheet'
        context['add_url'] = reverse_lazy('timesheet:adicionarpercentualdiario')
        return context


class ListTimesheetDiasView(CustomListViewFilter):
    template_name = 'timesheet/timesheet_dias_list.html'
    model = PercentualDiario
    context_object_name = 'all_natops'
    success_url = reverse_lazy('timesheet:listartimesheetdias')
    permission_codename = 'view_percentualdiario'

    timesheet = []

    def get_queryset(self):
        current_user = self.request.user
        query = self.model.objects.filter(solicitante=current_user)
        # querry = querry.filter(submetida=False)
        return query

    def get_object(self):
        current_user = self.request.user
        return self.model.objects.all()

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if value == "on":
                acao = request.POST['acao']
                if acao == 'submeter_horas':
                    instance = self.model.objects.get(id=key)
                    instance.situacao = 1
                    instance.save()
                elif acao == 'excluir':
                    instance = self.model.objects.get(id=key)
                    if instance.situacao == 0:
                        instance.delete()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(ListTimesheetDiasView, self).get_context_data(**kwargs, object_list=None)
        context['title_complete'] = 'Timesheet'
        context['add_url'] = reverse_lazy('timesheet:adicionarpercentualdiario')

        lista_timesheet = self.get_object()

        projetos = set()
        datas = set()

        for timesheet in lista_timesheet:
            projetos.add(timesheet.projeto)
            datas.add(str(timesheet.data))

        datas_dict = {key: None for key in datas}

        for data in datas_dict.keys():

            projetos_dict = {key: None for key in projetos}
            total_percentual_dia = 0.00
            for timesheet in lista_timesheet:

                if data == str(timesheet.data):
                    projetos_dict[timesheet.projeto] = {'percentual': timesheet.percentual, 'id': timesheet.id}
                    total_percentual_dia += float(timesheet.percentual)
                    _data = timesheet.data

            datas_dict[data] = [projetos_dict, total_percentual_dia, int(total_percentual_dia), _data]

        context['timesheet'] = datas_dict
        context['projetos'] = projetos

        return context
