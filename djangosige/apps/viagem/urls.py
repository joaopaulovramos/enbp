# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'viagem'
urlpatterns = [

    # Tipo de Viagns
    url(r'viagem/listatipo/$', views.ListTipoViagensView.as_view(), name='listatiposviagens'),
    url(r'viagem/adicionartipo/$', views.AdicionarTipoViagemView.as_view(), name='adicionartiposviagens'),
    url(r'viagem/editartipo/(?P<pk>[0-9]+)/$', views.EditarTipoViagemView.as_view(), name='editartiposviagens'),

    # Tipo de Solicitação
    url(r'viagem/listatiposolicitacao/$', views.ListTipoSolicitacaoView.as_view(), name='listatiposolicitacao'),
    url(r'viagem/adicionartiposolicitacao/$', views.AdicionarTipoSolicitacaoView.as_view(), name='adicionartiposolicitacao'),
    url(r'viagem/editartiposolicitacao/(?P<pk>[0-9]+)/$', views.EditarTipoSolicitacaoView.as_view(), name='editartiposolicitacao'),

    # Tipo de Transporte
    url(r'viagem/listatipotransporte/$', views.ListTipoTransporteView.as_view(), name='listatipotransporte'),
    url(r'viagem/adicionartipotransporte/$', views.AdicionarTipoTransporteView.as_view(), name='adicionartipotransporte'),
    url(r'viagem/editartipotransporte/(?P<pk>[0-9]+)/$', views.EditarTipoTransporteView.as_view(),name='editartipotransporte'),

    # Motivos de Transporte
    url(r'viagem/listamotivos/$', views.ListMotivosView.as_view(), name='listamotivos'),
    url(r'viagem/adicionarmotivo/$', views.AdicionarMotivoView.as_view(), name='adicionarmotivo'),
    url(r'viagem/editarmotivo/(?P<pk>[0-9]+)/$', views.EditarMotivoView.as_view(), name='editarmotivo'),

    # Tipo de Despesa
    url(r'viagem/listatipodespesa/$', views.ListTipoDespesaView.as_view(), name='listatipodespesa'),
    url(r'viagem/adicionartipodespesa/$', views.AdicionarTipoDespesaView.as_view(), name='adicionartipodespesa'),
    url(r'viagem/editartipodespesa/(?P<pk>[0-9]+)/$', views.EditarTipoDespesaView.as_view(), name='editartipodespesa'),

    # Moeda
    url(r'viagem/listamoeda/$', views.ListMoedaView.as_view(), name='listamoeda'),
    url(r'viagem/adicionarmoeda/$', views.AdicionarMoedaView.as_view(), name='adicionarmoeda'),
    url(r'viagem/editarmoeda/(?P<pk>[0-9]+)/$', views.EditarMoedaView.as_view(), name='editarmoeda'),

    # Tipo de Pagamento
    url(r'viagem/listatipopagamento/$', views.ListTipoPagamentoView.as_view(), name='listatipopagamento'),
    url(r'viagem/adicionartipopagamento/$', views.AdicionarTipoPagamentoView.as_view(), name='adicionartipopagamento'),
    url(r'viagem/editartipopagamento/(?P<pk>[0-9]+)/$', views.EditarTipoPagamentoView.as_view(),name='editartipopagamento'),

    # Categoria de passagem
    url(r'viagem/listacategoriapassagem/$', views.ListCategoriaPassagemView.as_view(), name='listacategoriapassagem'),
    url(r'viagem/adicionarcategoriapassagem/$', views.AdicionarCategoriaPassagemView.as_view(), name='adicionarcategoriapassagem'),
    url(r'viagem/editarcategoriapassagem/(?P<pk>[0-9]+)/$', views.EditarCategoriaPassagemView.as_view(), name='editarcategoriapassagem'),

    # Horário Prefencial
    url(r'viagem/listahorariopreferencial/$', views.ListHorarioPreferencialView.as_view(), name='listahorariopreferencial'),
    url(r'viagem/adicionarhorariopreferencial/$', views.AdicionarHorarioPreferencialView.as_view(), name='adicionarhorariopreferencial'),
    url(r'viagem/editarhorariopreferencial/(?P<pk>[0-9]+)/$', views.EditarHorarioPreferencialView.as_view(), name='editarhorariopreferencial'),

    # Necessidades Especiais
    url(r'viagem/listatiposnecessidadeespecial/$', views.ListTiposNecessidadeEspecialView.as_view(), name='listatiposnecessidadeespecial'),
    url(r'viagem/adicionartiponecessidadeespecial/$', views.AdicionarTipoNecessidadeEspecialView.as_view(), name='adicionartiponecessidadeespecial'),
    url(r'viagem/editartiponecessidadeespecial/(?P<pk>[0-9]+)/$', views.EditarTipoNecessidadeEspecialView.as_view(), name='editartiponecessidadeespecial'),

    # Localidades
    url(r'viagem/listalocalidade/$', views.ListLocalidadeView.as_view(), name='listalocalidades'),
    url(r'viagem/adicionarlocalidade/$', views.AdicionarLocalidadeView.as_view(), name='adicionarlocalidade'),
    url(r'viagem/editarlocalidade/(?P<pk>[0-9]+)/$', views.EditarLocalidadeView.as_view(), name='editarlocalidade'),

    # Tabela Diárias
    url(r'viagem/listatabeladiaria/$', views.ListTabelaDiariaView.as_view(), name='listatabeladiarias'),
    url(r'viagem/adicionartabeladiaria/$', views.AdicionarTabelaDiariaView.as_view(), name='adicionartabeladiaria'),
    url(r'viagem/editartabeladiaria/(?P<pk>[0-9]+)/$', views.EditarTabelaDiariaView.as_view(), name='editartabeladiaria'),

    # Viagens
    url(r'viagem/listarviagem/$', views.ListViagensView.as_view(), name='listaviagem'),
    url(r'viagem/adicionarviagem/$', views.AdicionarViagemView.as_view(), name='adicionarviagem'),
    url(r'viagem/editarviagem/(?P<pk>[0-9]+)/$', views.EditarViagemView.as_view(), name='editarviagem'),
    url(r'viagem/ver_solicitacao_viagem/(?P<pk>[0-9]+)/$', views.VerSolicitacaoViagem.as_view(), name='ver_solicitacao_viagem'),

    url(r'viagem/listasupautorizarviagem/$', views.ListSupAutorizarViagensView.as_view(), name='listasupautorizarviagem'),

    url(r'viagem/listarautorizarviagem/$', views.ListAutorizarViagensView.as_view(), name='listaautorizarviagem'),
    url(r'viagem/listarhomologarviagem/$', views.ListHomologarViagensView.as_view(), name='listahomologacaoviagem'),
    url(r'viagem/listapagamentodiarias/$', views.ListPagamentoDiariasView.as_view(), name='listapagamentodiarias'),
    url(r'viagem/aprovarpagamentodiarias/(?P<pk>[0-9]+)/$', views.AprovarPagamentoDiariasView.as_view(), name='aprovarpagamentodiarias'),
    url(r'viagem/listapagamentoreembolso/$', views.ListPagamentoReembolsoView.as_view(), name='listapagamentoreembolso'),
    url(r'viagem/aprovarpagamentoreembolso/(?P<pk>[0-9]+)/$', views.AprovarPagamentoReembolsoView.as_view(), name='aprovarpagamentoreembolso'),
    url(r'viagem/prestar_contas/(?P<pk>[0-9]+)/$', views.PrestarContasView.as_view(), name='prestar_contas'),
    url(r'viagem/prestar_contas_arquivos/(?P<pk>[0-9]+)/$', views.PrestarContasArquivosView.as_view(), name='prestar_contas_arquivos'),

    url(r'viagem/remover_arquivo/(?P<pk>[0-9]+)/(?P<viagem>[0-9]+)/$', views.RemoverArquivoView.as_view(), name='remover_arquivo'),

    url(r'viagem/enviar_arquivos/$', views.EnviarArquivosView.as_view(), name='enviar_arquivos'),
   # url(r'viagem/arquivosviagem/(?P<pk>[0-9]+)/$', views.ArquivosViagemView.as_view(), name='arquivosviagem'),
    url(r'viagem/arquivosviagem/$', views.ArquivosViagemView.as_view(), name='arquivosviagem'),

    url(r'viagem/listaraprovarpcviagem/$', views.ListAprovarPCViagensView.as_view(), name='listaaprovarpcviagem'),

    url(r'viagem/avaliar_prestacao_de_contas/(?P<pk>[0-9]+)/$', views.AvaliarPrestacaoDeContas.as_view(), name='avaliar_prestacao_de_contas'),
    url(r'viagem/avaliar_solicitacao_viagem/(?P<pk>[0-9]+)/$', views.AvaliarSolicitacaoViagem.as_view(), name='avaliar_solicitacao_viagem'),
    url(r'viagem/avaliar_arquivos/(?P<pk>[0-9]+)/$', views.AvaliarArquivosView.as_view(), name='avaliar_arquivos'),


]
