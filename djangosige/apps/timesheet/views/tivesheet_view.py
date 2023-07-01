
from django.urls import reverse_lazy

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView, CustomListViewFilter, CustomCreateViewAddUser




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
        #context = self.get_object()
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
        #querry = querry.filter(submetida=False)
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
        #context = self.get_object()
        context['title_complete'] = 'Timesheet'
        context['add_url'] = reverse_lazy('timesheet:adicionatimesheet')
        return context

class AdicionarTimesheetView(CustomCreateViewAddUser):

    form_class = HorasSemanaisForm
    template_name = "timesheet/add.html"
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

        date_selected = request.POST['semanas'].split(" - ")
        inicio_semana = datetime.datetime.strptime(date_selected[0], "%d/%m/%Y").date()
        fim_semana = datetime.datetime.strptime(date_selected[1], "%d/%m/%Y").date()
        hoje = datetime.datetime.now().date()

        inputs_dias_semana = ['hr_seg', 'hr_ter', 'hr_qua', 'hr_qui', 'hr_sex', 'hr_sab', 'hr_dom', ]

        if hoje > fim_semana:
            return self.form_invalid(form)
        else:
            if hoje >= inicio_semana:
                for i, v in enumerate(inputs_dias_semana):
                    if i > hoje.isoweekday():
                        print(hoje.isoweekday(), " ", i, "d eu ruim")

        print(hoje <= fim_semana)

        print(inicio_semana, " ", fim_semana, " ", hoje)


        if form.is_valid():
            # self.object = form.save()
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
        #querry = querry.filter(submetida=False)
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
        #context = self.get_object()
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
        #querry = querry.filter(submetida=False)
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
        #context = self.get_object()
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
        #querry = querry.filter(submetida=False)
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
        #context = self.get_object()
        context['title_complete'] = 'Listar Gastos'
        context['add_url'] = reverse_lazy('timesheet:incluirgastos')
        return context



class AdicionarGastoView(CustomCreateView):

    form_class = GastosForm
    template_name = 'timesheet/add.html'
    success_url = reverse_lazy('timesheet:listargastos')
    success_message = "Adicionar Exemplo <b>%(cfop)s </b>adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def post(self, request, *args, **kwargs):
        self.object = None
        req_post = request.POST.copy()
        req_post['valor'] = float(
            req_post['valor'].replace('.', '').replace(',', '.'))
        request.POST = req_post

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
