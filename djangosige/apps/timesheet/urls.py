# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'timesheet'
urlpatterns = [

    url(r'timesheet/lista/$', views.ListTimesheetView.as_view(), name='listatimesheet'),
    url(r'timesheet/adicionar/$', views.AdicionarTimesheetView.as_view(), name='adicionatimesheet'),
    url(r'timesheet/aprovar/$', views.AprovarTimesheetView.as_view(), name='aprovartimesheet'),

    url(r'timesheet/listargastos/$', views.ListGastosView.as_view(), name='listargastos'),
    url(r'timesheet/incluirgastos/$', views.AdicionarGastoView.as_view(), name='incluirgastos'),
    url(r'timesheet/editargastos/(?P<pk>[0-9]+)$', views.EditarGastoView.as_view(), name='editargastos'),
    url(r'timesheet/aprovargastos/$', views.AprovarGastosView.as_view(), name='aprovargastos'),

    # Timesheet percentual
    url(r'timesheet/listarpercentualdiario/$', views.ListPercentualDiarioView.as_view(), name='listarpercentualdiario'),
    url(r'timesheet/adicionarpercentualdiario/$', views.AdicionarPercentualDiarioView.as_view(), name='adicionarpercentualdiario'),
    url(r'timesheet/editarpercentualdiario/(?P<pk>[0-9]+)$', views.EditarPercentualDiarioView.as_view(), name='editarpercentualdiario'),
    url(r'timesheet/aprovarpercentuaisdiarios/$', views.AprovarTimesheetPercentualView.as_view(), name='aprovarpercentuaisdiarios'),
    url(r'timesheet/verpercentuaisdiariosaprovados/$', views.VerTimesheetPercentualAprovadoView.as_view(), name='verpercentuaisdiariosaprovados'),
    url(r'timesheet/verpercentuaisdiario/(?P<pk>[0-9]+)$', views.VerPercentualDiarioView.as_view(), name='verpercentuaisdiario'),


    url(r'timesheet/listartimesheetdias/$', views.ListTimesheetDiasView.as_view(), name='listartimesheetdias'),


]
