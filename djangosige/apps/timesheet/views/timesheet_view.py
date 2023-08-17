import os.path
import random
import string
from collections import defaultdict
from django.contrib import messages
import locale

import requests
from django.db.models import Avg, Sum, Count
from django.urls import reverse_lazy

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView, CustomListViewFilter, \
    CustomCreateViewAddUser, CustomView
from djangosige.apps.login.models import Usuario

from djangosige.apps.norli_projeto.models import ExemploModel

from djangosige.apps.timesheet.forms.timesheet_forms import *
from djangosige.apps.timesheet.models.timesheet_model import *

from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect

from pypdf import PdfWriter
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template

from djangosige.configs import settings


LIMITE_HORAS_DIA = 8

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')


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
            if value == "on" and key != 'selecionar_todos':
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
            if value == "on" and key != 'selecionar_todos':
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
                if value == "on" and key != 'selecionar_todos':
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


class AprovarTimesheetPercentualView(CustomListViewFilter):
    template_name = 'timesheet/timesheet_percentual_aprovar.html'
    model = PercentualDiario
    context_object_name = 'all_natops'
    success_url = reverse_lazy('timesheet:aprovarpercentuaisdiarios')
    permission_codename = 'aprovar_horas'
    _ano = datetime.datetime.now().year
    _mes = datetime.datetime.now().month
    _user = 'Todos'

    def get_queryset(self):

        # tratamento do filtro de seleção ano e mês
        if self.request.GET.get('mes'):
            self.request.session['mes_select'] = self.request.GET.get('mes')
        if 'mes_select' in self.request.session:
            self._mes = self.request.session['mes_select']

        if self.request.GET.get('ano'):
            self.request.session['ano_select'] = self.request.GET.get('ano')
        if 'ano_select' in self.request.session:
            self._ano = self.request.session['ano_select']

        if self.request.GET.get('user'):
            self.request.session['user_select'] = self.request.GET.get('user')
        if 'user_select' in self.request.session:
            self._user = self.request.session['user_select']

        self._user_list = list(User.objects.filter(pk__in=list(PercentualDiario.objects.filter(situacao=1, data__month=self._mes, data__year=self._ano).values_list(
            'solicitante', flat=True).distinct())).order_by('username').values_list('username', flat=True))
        self._user_list.insert(0, 'Todos')
        PercentualDiario.objects.filter(situacao=1, data__month=self._mes, data__year=self._ano).values_list(
            'solicitante', flat=True).distinct()

        current_user = self.request.user
        if current_user.usuario.perfil != '2' and current_user.usuario.perfil != '1' and not current_user.is_superuser:
            return
        query = PercentualDiario.objects.filter(situacao=1, data__month=self._mes, data__year=self._ano)
        if self._user != 'Todos':
            query = query.filter(solicitante__username=self._user)
        if not current_user.is_superuser and current_user.usuario.perfil != '1':
            query = query.filter(solicitante__usuario__departamento=current_user.usuario.departamento)
        return query

    # def get_object(self):
    #     current_user = self.request.user
    #     return HorasSemanais.objects.all(user=current_user)

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if value == "on" and key != 'selecionar_todos':
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
        context = super(AprovarTimesheetPercentualView, self).get_context_data(**kwargs, object_list=None)
        ano_atual = datetime.datetime.now().year
        context['mes_selecionado'] = str(self._mes)
        context['ano_selecionado'] = str(self._ano)
        context['anos_disponiveis'] = [str(ano_atual), str(int(ano_atual) - 1), str(int(ano_atual) - 2)]
        if (self._user):
            context['user_selecionado'] = str(self._user)
        context['users_disponiveis'] = self._user_list
        context['title_complete'] = 'Aprovar Horas - Percentual'
        context['add_url'] = reverse_lazy('timesheet:aprovartimesheet')
        return context


class VerTimesheetPercentualAprovadoView(CustomListViewFilter):
    template_name = 'timesheet/timesheet_percentual_ver_aprovados.html'
    model = PercentualDiario
    context_object_name = 'all_natops'
    success_url = reverse_lazy('timesheet:verpercentuaisdiariosaprovados')
    permission_codename = 'aprovar_horas'
    _ano = datetime.datetime.now().year
    _mes = datetime.datetime.now().month

    def get_queryset(self):
        current_user = self.request.user

        # tratamento do filtro de seleção ano e mês
        if self.request.GET.get('mes'):
            self.request.session['mes_select'] = self.request.GET.get('mes')
        if 'mes_select' in self.request.session:
            self._mes = self.request.session['mes_select']

        if self.request.GET.get('ano'):
            self.request.session['ano_select'] = self.request.GET.get('ano')
        if 'ano_select' in self.request.session:
            self._ano = self.request.session['ano_select']

        # consulta dos lançamentos aprovados considerando ano e mês
        query = PercentualDiario.objects.filter(situacao=2, data__month=self._mes, data__year=self._ano)

        # limita a lista ao departamento para quem não for root ou perfil diretor
        # TODO: checar se o diretor realmente deveria ver tudo
        if not current_user.is_superuser and current_user.usuario.perfil != '1':
            query = query.filter(solicitante__usuario__departamento=current_user.usuario.departamento)

        # simulando uma agregação de soma agrupando por solicitante e projeto
        query = query.values('solicitante', 'projeto').annotate(total_percentual=Sum('percentual'))

        # simulando uma agregação de contagem dias distintos agrupando por solicitante
        dias_trabalhados_query = query.values('solicitante').annotate(dias_trabalhados=Count('data', distinct=True))

        registros_transposed = defaultdict(dict)
        projetos = set()

        # criando um dicionario pivotando solicitante pelos projetos
        # na prática, fazendo os projetos virarem colunas
        for registro in query:
            _user = User.objects.get(pk=registro['solicitante'])
            nome = f'{_user.first_name} {_user.last_name}'
            solicitante = f'{_user.pk} - {nome}'
            projeto = ExemploModel.objects.get(pk=registro['projeto']).nome
            projetos.add(projeto)

            dias_trabalhados_solicitante = dias_trabalhados_query.get(solicitante=registro['solicitante'])[
                'dias_trabalhados']

            registros_transposed[solicitante][projeto] = float(registro['total_percentual']) / int(
                dias_trabalhados_solicitante)

        projetos = list(projetos)
        projetos.sort()

        # adicionando ao dicionário os projetos nos quais o solicitante não trabalhou
        # para facilitar a impressão no template
        for key, values in registros_transposed.items():
            for projeto in projetos:
                if not projeto in values.keys():
                    registros_transposed[key][projeto] = 0.0

        # ordenando os projetos de cada solicitante
        # opcionalmente, seria possível usar OrderedDict, mas o retorno como lista atrapalharia a remontagem no template
        # ex. registros_transposed[key] = OrderedDict(sorted(values.items()))
        ordered_data = {}
        total_percentuais = 0.0
        for key, values in registros_transposed.items():
            ordered_values = {}
            soma = 0.0

            for prj in sorted(values.keys()):
                ordered_values[prj] = values[prj]
                soma += values[prj]

            ordered_values['total'] = soma
            ordered_data[key] = ordered_values
            total_percentuais += soma

        self.projetos = projetos

        # somatório dos percentuais por projeto
        percentual_por_projetos = {}
        for _, value in ordered_data.items():
            for projeto, percentual in value.items():
                if projeto in percentual_por_projetos.keys():
                    percentual_por_projetos[projeto] += float(percentual)
                else:
                    percentual_por_projetos[projeto] = float(percentual)

        # por algum motivo, o arredondamento não funcionado fazendo a divisão no loop anterior
        for key, value in percentual_por_projetos.items():
            percentual_por_projetos[key] /= total_percentuais * .01

        if ordered_data:
            ordered_data['Percentual por projeto'] = percentual_por_projetos

        return ordered_data

    def get_context_data(self, **kwargs):
        context = super(VerTimesheetPercentualAprovadoView, self).get_context_data(**kwargs, object_list=None)
        ano_atual = datetime.datetime.now().year
        context['mes_selecionado'] = str(self._mes)
        context['ano_selecionado'] = str(self._ano)
        context['anos_disponiveis'] = [str(ano_atual), str(int(ano_atual) - 1), str(int(ano_atual) - 2)]
        context['title_complete'] = 'Horas Aprovadas - Percentual'
        context['projetos'] = self.projetos
        context['add_url'] = reverse_lazy('timesheet:gerarpdfpercentualaprovados')
        return context


def fetch_resources(uri, rel):
    return uri.replace(settings.MEDIA_URL, "")


class GerarPDFTimesheetPercentualAprovadoView(CustomView):
    permission_codename = 'aprovar_horas'
    template_name = 'timesheet/PDF_timesheet_percentual_aprovados.html'
    _ano = datetime.datetime.now().year
    _mes = datetime.datetime.now().month

    def get(self, request, *args, **kwargs):
        current_user = self.request.user

        # tratamento do filtro de seleção ano e mês
        if self.request.GET.get('mes'):
            self.request.session['mes_select'] = self.request.GET.get('mes')
        if 'mes_select' in self.request.session:
            self._mes = self.request.session['mes_select']

        if self.request.GET.get('ano'):
            self.request.session['ano_select'] = self.request.GET.get('ano')
        if 'ano_select' in self.request.session:
            self._ano = self.request.session['ano_select']

        # consulta dos lançamentos aprovados considerando ano e mês
        query = PercentualDiario.objects.filter(situacao=2, data__month=self._mes, data__year=self._ano)

        # limita a lista ao departamento para quem não for root ou perfil diretor
        # TODO: checar se o diretor realmente deveria ver tudo
        if not current_user.is_superuser and current_user.usuario.perfil != '1':
            query = query.filter(solicitante__usuario__departamento=current_user.usuario.departamento)

        # simulando uma agregação de soma agrupando por solicitante e projeto
        query = query.values('solicitante', 'projeto').annotate(total_percentual=Sum('percentual'))

        # simulando uma agregação de contagem dias distintos agrupando por solicitante
        dias_trabalhados_query = query.values('solicitante').annotate(dias_trabalhados=Count('data', distinct=True))

        registros_transposed = defaultdict(dict)
        projetos = set()

        # criando um dicionario pivotando solicitante pelos projetos
        # na prática, fazendo os projetos virarem colunas
        for registro in query:
            _user = User.objects.get(pk=registro['solicitante'])
            nome = f'{_user.first_name} {_user.last_name}'
            solicitante = f'{_user.pk} - {nome}'
            projeto = ExemploModel.objects.get(pk=registro['projeto']).nome
            projetos.add(projeto)

            dias_trabalhados_solicitante = dias_trabalhados_query.get(solicitante=registro['solicitante'])[
                'dias_trabalhados']

            registros_transposed[solicitante][projeto] = float(registro['total_percentual']) / int(
                dias_trabalhados_solicitante)

        projetos = list(projetos)
        projetos.sort()

        # adicionando ao dicionário os projetos nos quais o solicitante não trabalhou
        # para facilitar a impressão no template
        for key, values in registros_transposed.items():
            for projeto in projetos:
                if not projeto in values.keys():
                    registros_transposed[key][projeto] = 0.0

        # ordenando os projetos de cada solicitante
        # opcionalmente, seria possível usar OrderedDict, mas o retorno como lista atrapalharia a remontagem no template
        # ex. registros_transposed[key] = OrderedDict(sorted(values.items()))
        ordered_data = {}
        total_percentuais = 0.0
        for key, values in registros_transposed.items():
            ordered_values = {}
            soma = 0.0

            for prj in sorted(values.keys()):
                ordered_values[prj] = values[prj]
                soma += values[prj]

            ordered_values['total'] = soma
            ordered_data[key] = ordered_values
            total_percentuais += soma

        # somatório dos percentuais por projeto
        percentual_por_projetos = {}
        for _, value in ordered_data.items():
            for projeto, percentual in value.items():
                if projeto in percentual_por_projetos.keys():
                    percentual_por_projetos[projeto] += float(percentual)
                else:
                    percentual_por_projetos[projeto] = float(percentual)

        # por algum motivo, o arredondamento não funcionado fazendo a divisão no loop anterior
        for key, value in percentual_por_projetos.items():
            percentual_por_projetos[key] /= total_percentuais * .01

        ordered_data['Projeto (%)'] = percentual_por_projetos

        current_user = self.request.user
        aprovador = f'{User.objects.get(pk=current_user.id).first_name} {User.objects.get(pk=current_user.id).last_name}'

        template = get_template(self.template_name)
        context = {
            "all_natops": ordered_data,
            "projetos": projetos,
            "ano": self._ano,
            "mes": calendar.month_name[int(self._mes)],
            "aprovador": aprovador,
            "perfil": Usuario.PERFIS[int(current_user.usuario.perfil)][1]
        }
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result, link_callback=fetch_resources)

        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        else:
            return None


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
                if value == "on" and key != 'selecionar_todos':
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
        context['title_complete'] = 'ADICIONAR GASTO'
        context['return_url'] = reverse_lazy('timesheet:listargastos')
        return context


class EditarGastoView(CustomUpdateView):
    form_class = GastosForm
    template_name = 'timesheet/edit_gasto.html'
    success_url = reverse_lazy('timesheet:listargastos')
    success_message = "Gasto editado com sucesso."
    permission_codename = 'change_naturezaoperacao'
    context_object_name = 'all_natops'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        req_post = request.POST.copy()
        req_post['valor'] = float(
            req_post['valor'].replace('.', '').replace(',', '.'))
        request.POST = req_post

        form_class = self.get_form_class()
        form = form_class(request.POST, instance=self.object)
        form.request_user = self.request.user
        form.files['file'] = Gastos.objects.get(pk=self.kwargs['pk']).file
        if form.is_valid():
            form.instance.pessoa_id = self.object
            self.object = form.save()
            return self.form_valid(form)
        return self.form_invalid(form)

    def get_queryset(self):
        current_user = self.request.user
        querry = Gastos.objects.filter(solicitante=current_user, id=self.kwargs['pk'])
        # querry = querry.filter(submetida=False)
        return querry

    def get_context_data(self, **kwargs):
        context = super(EditarGastoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'EDITAR GASTO'
        context['return_url'] = reverse_lazy('timesheet:listargastos')
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        # form_class.prefix = "empresa_form"
        form = self.get_form(form_class)
        form.files['file'] = Gastos.objects.get(pk=self.object.pk).file
        return super(EditarGastoView, self).get(request, form, *args, **kwargs)


class AdicionarPercentualDiarioView(CustomCreateViewAddUser):
    form_class = PercentualDiarioForm
    template_name = "timesheet/add_percentual.html"
    success_url = reverse_lazy('timesheet:adicionarpercentualdiario')
    success_message = "Percentual de horas trabalhadas lançado com sucesso."
    permission_codename = 'add_percentualdiario'
    context_object_name = 'all_natops'

    def post(self, request, *args, **kwargs):

        datas_selecionadas = str(request.POST['data']).split(', ')

        post = request.POST.copy()  # to make it mutable

        for dt in datas_selecionadas:

            post['data'] = dt.strip()
            request.POST = post

            self.object = None
            form_class = self.get_form_class()

            form = self.get_form(form_class)
            form.request_user = self.request.user

            data = datetime.datetime.strptime(dt.strip(), "%d/%m/%Y").date()
            hoje = datetime.datetime.now().date()

            if data > hoje:
                form.add_error('data', 'Não é possível lança horas futuras.')

            # seleciona os laçamentos do usuário já existentes para o dia
            lancamentos_dia = PercentualDiario.objects.filter(solicitante=self.request.user, data=data)

            total_percentual_dia = 0
            for lancamento in lancamentos_dia:
                total_percentual_dia += lancamento.percentual
                if int(self.request.POST['projeto']) == lancamento.projeto_id:
                    form.add_error('projeto', f'Você já lançou horas para este projeto em {dt}')

            if float(total_percentual_dia) + float(self.request.POST['percentual']) > 100.00:
                form.add_error('percentual', 'O percentual diário não pode ultrapassar 100% de horas')

            if form.is_valid():
                self.object = form.save()
            else:
                return self.form_invalid(form)

        return redirect(self.success_url)

        # if form.is_valid():
        #     self.object = form.save()
        #     return redirect(self.success_url)
        # return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        self.form_class.Meta.model.user = self.request.user
        context = super(AdicionarPercentualDiarioView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Percentual de Horas'
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
                    projetos_dict[timesheet.projeto] = {
                        'percentual': timesheet.percentual,
                        'id': timesheet.id,
                        'situacao': timesheet.situacao,
                        'obs': timesheet.observacao,
                    }
                    total_percentual_dia += float(timesheet.percentual)

            data_formatada = f'{data.split("-")[2]}/{data.split("-")[1]}/{data.split("-")[0]}'
            datas_dict[data] = [projetos_dict, total_percentual_dia, int(total_percentual_dia), data_formatada]

        context['timesheet'] = datas_dict
        context['projetos'] = projetos

        return context


class EditarPercentualDiarioView(CustomUpdateView):
    form_class = PercentualDiarioForm
    model = PercentualDiario
    template_name = 'timesheet/edit_percentual.html'
    success_url = reverse_lazy('timesheet:listarpercentualdiario')
    success_message = "Percentual de horas Editado com Sucesso."
    permission_codename = 'change_percentualdiario'

    def get_context_data(self, **kwargs):
        context = super(EditarPercentualDiarioView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Editar Percentual de Horas'
        context['return_url'] = reverse_lazy('timesheet:listarpercentualdiario')
        context['id'] = self.object.id
        context['motivo_reprovacao'] = self.object.motivo_reprovacao

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
                    projetos_dict[timesheet.projeto] = {
                        'percentual': timesheet.percentual,
                        'id': timesheet.id,
                        'situacao': timesheet.situacao,
                        'obs': timesheet.observacao,
                    }
                    total_percentual_dia += float(timesheet.percentual)

            data_formatada = f'{data.split("-")[2]}/{data.split("-")[1]}/{data.split("-")[0]}'
            datas_dict[data] = [projetos_dict, total_percentual_dia, int(total_percentual_dia), data_formatada]

        context['timesheet'] = datas_dict
        context['projetos'] = projetos

        return context

    def post(self, request, *args, **kwargs):

        if ('excluir_timesheet' in request.POST):
            instance = self.model.objects.get(id=self.kwargs['pk'])
            if instance.situacao == 0:
                instance.delete()
                return redirect(self.success_url)
            # self.model.delete(self)

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


class VerPercentualDiarioView(CustomUpdateView):
    form_class = PercentualDiarioForm
    model = PercentualDiario
    template_name = 'timesheet/ver_percentual.html'
    success_url = reverse_lazy('timesheet:aprovarpercentuaisdiarios')
    success_message = "Percentual de horas Editado com Sucesso."
    permission_codename = 'aprovar_horas'

    def get_context_data(self, **kwargs):
        context = super(VerPercentualDiarioView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Visualizando lançamento de horas'
        context['return_url'] = reverse_lazy('timesheet:aprovarpercentuaisdiarios')
        context['id'] = self.object.id
        context['projeto'] = self.object.projeto

        lancamentos = self.model.objects.filter(data=self.object.data)
        lancamentos = lancamentos.filter(situacao=1)
        context['lancamentos_do_dia'] = lancamentos

        return context

    def post(self, request, *args, **kwargs):

        if 'acao' in request.POST.keys():
            acao = request.POST['acao']
            instance = self.model.objects.get(pk=kwargs['pk'])
            if acao == 'aprovar_timesheet':
                instance.situacao = 2
                instance.save()
                print("aprovando Timesheet")
            if acao == 'reprovar_timesheet':
                instance.situacao = 3
                instance.motivo_reprovacao = request.POST['motivo']
                instance.save()

        return redirect(self.success_url)


class ListPercentualDiarioView(CustomListViewFilter):
    template_name = 'timesheet/timesheet_percentual_list.html'
    model = PercentualDiario
    context_object_name = 'all_natops'
    success_url = reverse_lazy('timesheet:listarpercentualdiario')
    permission_codename = 'view_percentualdiario'
    _ano = datetime.datetime.now().year
    _mes = datetime.datetime.now().month

    def get_queryset(self):

        # tratamento do filtro de seleção ano e mês
        if self.request.GET.get('mes'):
            self.request.session['mes_select'] = self.request.GET.get('mes')
        if 'mes_select' in self.request.session:
            self._mes = self.request.session['mes_select']

        if self.request.GET.get('ano'):
            self.request.session['ano_select'] = self.request.GET.get('ano')
        if 'ano_select' in self.request.session:
            self._ano = self.request.session['ano_select']

        current_user = self.request.user
        querry = self.model.objects.filter(solicitante=current_user, data__month=self._mes, data__year=self._ano)




        return querry

    def get_object(self):
        current_user = self.request.user
        return self.model.objects.all(user=current_user)

    def post(self, request, *args, **kwargs):
        current_user = self.request.user
        mes = self.request.POST['select_mes']
        ano =  self.request.POST['select_ano']
        querry = self.model.objects.filter(solicitante=current_user, situacao=0, data__month=mes,
                                           data__year=ano)

        days = {}
        for lancamento in querry:
            # lancamento.full = False
            retVal = days.get(lancamento.data)
            if retVal is not None:
                days[lancamento.data] = days[lancamento.data] + lancamento.percentual
            else:
                days[lancamento.data] = lancamento.percentual
        incompleto = False
        for key, value in request.POST.items():
            if value == "on" and key != 'selecionar_todos':
                acao = request.POST['acao']

                if acao == 'submeter_horas':

                    instance = self.model.objects.get(id=key)
                    if days[instance.data] == 100.00:
                        instance.situacao = 1
                        instance.save()
                    else:
                        incompleto = True


                elif acao == 'excluir':
                    if key == 'selecionar_todos':
                        continue
                    instance = self.model.objects.get(id=key)
                    if instance.situacao == 0:
                        instance.delete()

        if incompleto:
            messages.success(self.request,
                         f' Não é possivel submeter percentuais incompletos')
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(ListPercentualDiarioView, self).get_context_data(**kwargs, object_list=None)
        ano_atual = datetime.datetime.now().year
        context['mes_selecionado'] = str(self._mes)
        context['ano_selecionado'] = str(self._ano)
        context['anos_disponiveis'] = [str(ano_atual), str(int(ano_atual) - 1), str(int(ano_atual) - 2)]
        context['title_complete'] = 'Minhas Horas - Percentual'
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
        return self.model.objects.filter(solicitante=current_user)

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if value == "on" and key != 'selecionar_todos':
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


class ListOpiniaoView(CustomListViewFilter):
    template_name = 'timesheet/opiniao_list.html'
    model = OpiniaoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('timesheet:listaropinioes')
    permission_codename = 'view_opiniaomodel'

    def get_queryset(self):
        return OpiniaoModel.objects.filter(usuario=self.request.user)

    def get_object(self):
        return OpiniaoModel.objects.all(usuario=self.request.user)

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            if value == "on" and key != 'selecionar_todos':
                acao = request.POST['acao']
                if acao == 'excluir':
                    instance = self.model.objects.get(id=key)
                    instance.delete()

        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(ListOpiniaoView, self).get_context_data(**kwargs, object_list=None)
        context['title_complete'] = 'Opiniões sobre Timesheet'
        context['add_url'] = reverse_lazy('timesheet:adicionaopiniao')
        return context


class AdicionarOpiniaoView(CustomCreateView):
    form_class = OpiniaoForm
    template_name = "timesheet/add_feedback.html"
    success_url = reverse_lazy('timesheet:adicionaopiniao')
    success_message = "Feedback Adicionado com Sucesso."
    permission_codename = 'add_opiniaomodel'
    context_object_name = 'all_natops'

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()

        form = OpiniaoForm(request.POST, request.FILES, instance=self.object)
        form.request_user = self.request.user

        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(20))
        nome_antigo = request.FILES['anexo'].name
        nome_antigo = nome_antigo.split('.')
        ext = nome_antigo[-1]

        if form.is_valid():
            request.FILES['anexo'].name = name + '.' + ext

            self.object = form.save(commit=False)
            # self.object.rating = 5
            self.object.save()
            return redirect(self.success_url)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        self.form_class.Meta.model.user = self.request.user
        context = super(AdicionarOpiniaoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR FEEDBACK'
        context['return_url'] = reverse_lazy('timesheet:adicionaopiniao')
        return context


class EditarOpiniaoView(CustomUpdateView):
    form_class = OpiniaoForm
    model = OpiniaoModel
    template_name = 'timesheet/edit.html'
    success_url = reverse_lazy('timesheet:listaropinioes')
    success_message = "Opinião editada com sucesso."
    permission_codename = 'change_opiniaomodel'
    context_object_name = 'all_natops'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.request_user = self.request.user

        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.save()
            return redirect(self.success_url)
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(EditarOpiniaoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'EDITAR OPINIÃO'
        context['return_url'] = reverse_lazy('timesheet:listaropinioes')
        return context
