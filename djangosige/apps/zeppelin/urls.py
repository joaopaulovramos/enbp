# -*- coding: utf-8 -*-



from django.conf.urls import url
from . import views

app_name = 'zeppelin'
urlpatterns = [

    url(r'zeppelin/lista/$', views.ListView.as_view(), name='listasubgrupo'),
    url(r'zeppelin/adicionar/$', views.AdicionarView.as_view(), name='adicionasubgrupo'),
    url(r'zeppelin/editar/(?P<pk>[0-9]+)/$', views.EditarView.as_view(), name='editarsubgrupo'),

    url(r'regional/lista/$', views.ListRegionalView.as_view(), name='listaregional'),
    url(r'regional/adicionar/$', views.AdicionarRegionalView.as_view(), name='adicionaregional'),
    url(r'regional/editar/(?P<pk>[0-9]+)/$', views.EditarRegionalView.as_view(), name='editarregional'),

    url(r'municipio/lista/$', views.ListMunicipioView.as_view(), name='listamunicipio'),
    url(r'municipio/adicionar/$', views.AdicionarMunicipiolView.as_view(), name='adicionamunicipio'),
    url(r'municipio/editar/(?P<pk>[0-9]+)/$', views.EditarMunicipioView.as_view(), name='editarmunicipio'),

    url(r'classe/lista/$', views.ListClasseView.as_view(), name='listaclasse'),
    url(r'classe/adicionar/$', views.AdicionarClasseView.as_view(), name='adicionaclasse'),
    url(r'classe/editar/(?P<pk>[0-9]+)/$', views.EditarClasseView.as_view(), name='editarclasse'),


    url(r'subclasse/lista/$', views.ListSubClasseView.as_view(), name='listasubclasse'),
    url(r'subclasse/adicionar/$', views.AdicionarSubClasseView.as_view(), name='adicionasubclasse'),
    url(r'subclasse/editar/(?P<pk>[0-9]+)/$', views.EditarSubClasseView.as_view(), name='editarsubclasse'),

    url(r'grupo/lista/$', views.ListGrupoView.as_view(), name='listagrupo'),
    url(r'grupo/adicionar/$', views.AdicionarGrupoView.as_view(), name='adicionagrupo'),
    url(r'grupo/editar/(?P<pk>[0-9]+)/$', views.EditarGrupoView.as_view(), name='editargrupo'),

    url(r'tipoespecial/lista/$', views.ListTipoEspecialView.as_view(), name='listatipoespecial'),
    url(r'tipoespecial/adicionar/$', views.AdicionarTipoEspecialView.as_view(), name='adicionatipoespecial'),
    url(r'tipoespecial/editar/(?P<pk>[0-9]+)/$', views.EditarTipoEspecialView.as_view(), name='editartipoespecial'),

    url(r'uc/lista/$', views.ListUCView.as_view(), name='listauc'),
    url(r'uc/adicionar/$', views.AdicionarUCView.as_view(), name='adicionauc'),
    url(r'uc/editar/(?P<pk>[0-9]+)/$', views.EditarUCView.as_view(), name='editaruc'),

    url(r'medidor/lista/$', views.ListMedidorView.as_view(), name='listamedidor'),
    url(r'medidor/adicionar/$', views.AdicionarMedidorView.as_view(), name='adicionamedidor'),
    url(r'medidor/editar/(?P<pk>[0-9]+)/$', views.EditarMedidorView.as_view(), name='editarmedidor'),

    url(r'desligamento/lista/$', views.ListDesligamentoView.as_view(), name='listadesligamento'),
    url(r'desligamento/adicionar/$', views.AdicionarDesligamentoView.as_view(), name='adicionadesligamento'),
    url(r'desligamento/editar/(?P<pk>[0-9]+)/$', views.EditarDesligamentoView.as_view(), name='editardesligamento'),

    url(r'servico/lista/$', views.ListServicoView.as_view(), name='listaservico'),
    url(r'servico/adicionar/$', views.AdicionarServicoView.as_view(), name='adicionaservico'),
    url(r'servico/editar/(?P<pk>[0-9]+)/$', views.EditarServicoView.as_view(), name='editarservico'),

    url(r'grupoequipamento/lista/$', views.ListGrupoEquipamentoView.as_view(), name='listagrupoequipamento'),
    url(r'grupoequipamento/adicionar/$', views.AdicionarGrupoEquipementoView.as_view(), name='adicionagrupoequipamento'),
    url(r'grupoequipamento/editar/(?P<pk>[0-9]+)/$', views.EditarGrupoEquipamentoView.as_view(), name='editargrupoequipamento'),

    url(r'equipamento/lista/$', views.ListEquipamentoView.as_view(), name='listaequipamento'),
    url(r'equipamento/adicionar/$', views.AdicionarEquipementoView.as_view(), name='adicionaequipamento'),
    url(r'equipamento/editar/(?P<pk>[0-9]+)/$', views.EditarEquipamentoView.as_view(), name='editarequipamento'),

    url(r'cnae/lista/$', views.ListCNAEView.as_view(), name='listacnae'),
    url(r'cnae/adicionar/$', views.AdicionarCNAEView.as_view(), name='adicionacnae'),
    url(r'cnae/editar/(?P<pk>[0-9]+)/$', views.EditarCNAEView.as_view(), name='editarcnae'),

    url(r'historicopadrao/lista/$', views.ListHistoricoPadraoView.as_view(), name='listahistoricopadrao'),
    url(r'historicopadrao/adicionar/$', views.AdicionarHistoricoPadraoView.as_view(), name='adicionahistoricopadrao'),
    url(r'historicopadrao/editar/(?P<pk>[0-9]+)/$', views.EditarHistoricoPadraoView.as_view(), name='editarhistoricopadrao'),

    url(r'tipoboletimafericao/lista/$', views.ListTipoBoletimAfericaoView.as_view(), name='listatipoboletimafericao'),
    url(r'tipoboletimafericao/adicionar/$', views.AdicionarTipoBoletimAfericaoView.as_view(), name='adicionatipoboletimafericao'),
    url(r'tipoboletimafericao/editar/(?P<pk>[0-9]+)/$', views.EditarTipoBoletimAfericaoView.as_view(), name='editartipoboletimafericao'),

    url(r'tipodocumento/lista/$', views.ListTipoDocumentoView.as_view(), name='listatipodocumento'),
    url(r'tipodocumento/adicionar/$', views.AdicionarTipoDocumentoView.as_view(), name='adicionatipodocumento'),
    url(r'tipodocumento/editar/(?P<pk>[0-9]+)/$', views.EditarTipoDocumentoView.as_view(), name='editartipodocumento'),

    url(r'tiposervicoessencial/lista/$', views.ListServicoEssencialView.as_view(), name='listatiposervicoessencial'),
    url(r'tiposervicoessencial/adicionar/$', views.AdicionarServicoEssencialView.as_view(), name='adicionatiposervicoessencial'),
    url(r'tiposervicoessencial/editar/(?P<pk>[0-9]+)/$', views.EditarServicoEssencialView.as_view(), name='editartiposervicoessencial'),

    url(r'cadastrofinalidade/lista/$', views.ListCadastroDeFinalidadeView.as_view(), name='listacadastrodefinalidade'),
    url(r'cadastrofinalidade/adicionar/$', views.AdicionarCadastroDeFinalidadeView.as_view(), name='adicionacadastrodefinalidade'),
    url(r'cadastrofinalidade/editar/(?P<pk>[0-9]+)/$', views.EditarCadastroDeFinalidadeView.as_view(), name='editarcadastrodefinalidade'),

    url(r'motivoreprovacaovistoria/lista/$', views.ListMotivoReprovacaoVistoriaView.as_view(), name='listamotivoreprovacaovistoria'),
    url(r'motivoreprovacaovistoria/adicionar/$', views.AdicionarMotivoReprovacaoVistoriaView.as_view(), name='adicionamotivoreprovacaovistoria'),
    url(r'motivoreprovacaovistoria/editar/(?P<pk>[0-9]+)/$', views.EditarMotivoReprovacaoVistoriaView.as_view(), name='editarmotivoreprovacaovistoria'),

    url(r'motivocancelamentovistoria/lista/$', views.ListMotivoCancelamentoView.as_view(), name='listamotivocancelamento'),
    url(r'motivocancelamentovistoria/adicionar/$', views.AdicionarMotivoCancelamentoView.as_view(), name='adicionamotivocancelamento'),
    url(r'motivocancelamentovistoria/editar/(?P<pk>[0-9]+)/$', views.EditarMotivoCancelamentoVistoriaView.as_view(), name='editarmotivocancelamento'),

    url(r'motivoreprovacaoanalise/lista/$', views.ListMotivoReprovacaoAnaliseView.as_view(), name='listamotivoreprovacaoanalise'),
    url(r'motivoreprovacaoanalise/adicionar/$', views.AdicionarMotivoReprovacaoAnaliseView.as_view(), name='adicionamotivoreprovacaoanalise'),
    url(r'motivoreprovacaoanalise/editar/(?P<pk>[0-9]+)/$', views.EditarMotivoReprovacaoAnaliseView.as_view(),name='editarmotivoreprovacaoanalise'),

    url(r'deferimentobaixarenda/lista/$', views.ListMotivoDeferimentoBaixaRendaView.as_view(), name='listamotivodeferimentobaixarenda'),
    url(r'deferimentobaixarenda/adicionar/$', views.AdicionarMotivoDeferimentoBaixaRendaView.as_view(), name='adicionamotivodeferimentobaixarenda'),
    url(r'deferimentobaixarenda/editar/(?P<pk>[0-9]+)/$', views.EditarMotivoDeferimentoBaixaRendaView.as_view(), name='editarmotivodeferimentobaixarenda'),

    url(r'criteriobaixarenda/lista/$', views.ListCriterioBaixaRendaView.as_view(), name='listcriteriobaixarenda'),
    url(r'criteriobaixarenda/adicionar/$', views.AdicionarCriterioBaixaRendaView.as_view(), name='adicionacriteriobaixarenda'),
    url(r'criteriobaixarenda/editar/(?P<pk>[0-9]+)/$', views.EditarCriterioRendaView.as_view(), name='editarcriteriobaixarenda'),

]
