# -*- coding: utf-8 -*-

from django.urls import reverse_lazy

from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView

from djangosige.apps.fiscal.forms import NaturezaOperacaoForm
from djangosige.apps.fiscal.models import NaturezaOperacao


from djangosige.apps.zeppelin.forms.FormClasse import *
from djangosige.apps.zeppelin.models.classe import *

from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers

class ListView(CustomListView):
    template_name = 'zeppelin/subgrupo_list.html'
    model = SubGrupoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listasubgrupo')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Sub-Grupo'
        context['add_url'] = reverse_lazy('zeppelin:adicionasubgrupo')
        return context

class AdicionarView(CustomCreateView):

    form_class = SubGrupoForm
    template_name = "zeppelin/subgrupo_add.html"
    success_url = reverse_lazy('zeppelin:listasubgrupo')
    success_message = "Sub-Classe adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR SUB-GRUPO'
        context['return_url'] = reverse_lazy('zeppelin:listasubgrupo')
        return context


class EditarView(CustomUpdateView):
    form_class = SubGrupoForm
    model = SubGrupoModel

    template_name = "zeppelin/subgrupo_edit.html"
    success_url = reverse_lazy('zeppelin:listasubgrupo')
    success_message = "Classe editada com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarView,
                        self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listasubgrupo')
        return context



class ListRegionalView(CustomListView):
    template_name = 'zeppelin/classe_operacao/regional_list.html'
    model = RegionalModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listaregional')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListRegionalView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Regionais'
        context['add_url'] = reverse_lazy('zeppelin:adicionaregional')

        return context


class AdicionarRegionalView(CustomCreateView):

    form_class = RegionalForm
    template_name = "zeppelin/classe_operacao/regional_add.html"
    success_url = reverse_lazy('zeppelin:listaregional')
    success_message = "Regional adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarRegionalView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR REGIONAL'
        context['return_url'] = reverse_lazy('zeppelin:listaregional')
        return context


class EditarRegionalView(CustomUpdateView):
    form_class = RegionalForm
    model = RegionalModel

    template_name = "zeppelin/classe_operacao/regional_edit.html"
    success_url = reverse_lazy('zeppelin:listaregional')
    success_message = "Regional editada com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarRegionalView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listaregional')
        return context

class ListMunicipioView(CustomListView):
    template_name = 'zeppelin/municipio_list.html'
    model = MunicipioModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listamunicipio')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListMunicipioView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Municipios'
        context['add_url'] = reverse_lazy('zeppelin:adicionamunicipio')

        return context

class AdicionarMunicipiolView(CustomCreateView):

    form_class = MunicipioForm
    template_name = "zeppelin/classe_operacao/regional_add.html"
    success_url = reverse_lazy('zeppelin:listamunicipio')
    success_message = "Municipio adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarMunicipiolView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR REGIONAL'
        context['return_url'] = reverse_lazy('zeppelin:listamunicipio')
        return context


class EditarMunicipioView(CustomUpdateView):
    form_class = MunicipioForm
    model = MunicipioModel

    template_name = "zeppelin/municipio_edit.html"
    success_url = reverse_lazy('zeppelin:listamunicipio')
    success_message = "Municipio editada com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarMunicipioView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listamunicipio')
        return context


class ListClasseView(CustomListView):
    template_name = 'zeppelin/classe_list.html'
    model = ClasseModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listaclasse')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListClasseView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Classes'
        context['add_url'] = reverse_lazy('zeppelin:adicionaclasse')

        return context


class AdicionarClasseView(CustomCreateView):

    form_class = ClasseForm
    template_name = "zeppelin/classe_add.html"
    success_url = reverse_lazy('zeppelin:listaclasse')
    success_message = "Classe adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarClasseView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR REGIONAL'
        context['return_url'] = reverse_lazy('zeppelin:listaclasse')
        return context



class EditarClasseView(CustomUpdateView):
    form_class = ClasseForm
    model = ClasseModel

    template_name = "zeppelin/classe_edit.html"
    success_url = reverse_lazy('zeppelin:listaclasse')
    success_message = "Classe editada com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarClasseView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listaclasse')
        return context




class ListSubClasseView(CustomListView):
    template_name = 'zeppelin/subclasse_list.html'
    model = SubClasseModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listasubclasse')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListSubClasseView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Sub-Classes'
        context['add_url'] = reverse_lazy('zeppelin:adicionasubclasse')

        return context



class AdicionarSubClasseView(CustomCreateView):

    form_class = SubClasseForm
    template_name = "zeppelin/subclasse_add.html"
    success_url = reverse_lazy('zeppelin:listasubclasse')
    success_message = "Sub-Classe adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarSubClasseView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR REGIONAL'
        context['return_url'] = reverse_lazy('zeppelin:listasubclasse')
        return context


class EditarSubClasseView(CustomUpdateView):
    form_class = SubClasseForm
    model = SubClasseModel

    template_name = "zeppelin/subclasse_edit.html"
    success_url = reverse_lazy('zeppelin:listasubclasse')
    success_message = "Sub-Classe editada com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarSubClasseView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listasubclasse')
        return context
##########################################################################################




class ListGrupoView(CustomListView):
    template_name = 'zeppelin/grupo_list.html'
    model = GrupoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listagrupo')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListGrupoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Grupo'
        context['add_url'] = reverse_lazy('zeppelin:adicionagrupo')

        return context


class AdicionarGrupoView(CustomCreateView):

    form_class = GrupoForm
    template_name = "zeppelin/grupo_add.html"
    success_url = reverse_lazy('zeppelin:listagrupo')
    success_message = "Grupo adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarGrupoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Grupo'
        context['return_url'] = reverse_lazy('zeppelin:listagrupo')
        return context



class EditarGrupoView(CustomUpdateView):
    form_class = GrupoForm
    model = GrupoModel

    template_name = "zeppelin/grupo_edit.html"
    success_url = reverse_lazy('zeppelin:listagrupo')
    success_message = "Grupo editada com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarGrupoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listagrupo')
        return context

#################################################################


class ListTipoEspecialView(CustomListView):
    template_name = 'zeppelin/tipo_especial_list.html'
    model = TipoEspecialModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listatipoespecial')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListTipoEspecialView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Tipo Especial'
        context['add_url'] = reverse_lazy('zeppelin:adicionatipoespecial')

        return context


class AdicionarTipoEspecialView(CustomCreateView):

    form_class = TipoEspecialForm
    template_name = "zeppelin/tipo_especial_add.html"
    success_url = reverse_lazy('zeppelin:listatipoespecial')
    success_message = "Tipo especial adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarTipoEspecialView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Tipo Especial'
        context['return_url'] = reverse_lazy('zeppelin:listatipoespecial')
        return context



class EditarTipoEspecialView(CustomUpdateView):
    form_class = TipoEspecialForm
    model = TipoEspecialModel

    template_name = "zeppelin/tipo_especial_edit.html"
    success_url = reverse_lazy('zeppelin:listatipoespecial')
    success_message = "Tipo especial editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarTipoEspecialView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listatipoespecial')
        return context


######################################################################################################



class ListUCView(CustomListView):
    template_name = 'zeppelin/uc_list.html'
    model = UnidadeConsumidoraModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listauc')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListUCView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Unidade Consumidora'
        context['add_url'] = reverse_lazy('zeppelin:adicionauc')

        return context


class AdicionarUCView(CustomCreateView):

    form_class = UnidadeConsumidoraForm
    template_name = "zeppelin/uc_add.html"
    success_url = reverse_lazy('zeppelin:listauc')
    success_message = "Unidade consumidora adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarUCView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Unidade Consumidora'
        context['return_url'] = reverse_lazy('zeppelin:listauc')
        return context



class EditarUCView(CustomUpdateView):
    # form_class = TipoEspecialForm
    # model = TipoEspecialModel
    form_class = UnidadeConsumidoraForm
    model = UnidadeConsumidoraModel

    # template_name = "zeppelin/tipo_especial_edit.html"
    template_name = "zeppelin/uc_edit.html"
    # success_url = reverse_lazy('zeppelin:listatipoespecial')
    success_url = reverse_lazy('zeppelin:listauc')
    success_message = "Unidade Consumidora editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarUCView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listauc')
        return context



#################################################################


class ListMedidorView(CustomListView):
    template_name = 'zeppelin/medidor_list.html'
    model = MedidorModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listamedidor')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListMedidorView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Medidores'
        context['add_url'] = reverse_lazy('zeppelin:adicionamedidor')

        return context


class AdicionarMedidorView(CustomCreateView):

    form_class = MedidorlForm
    template_name = "zeppelin/medidor_add.html"
    success_url = reverse_lazy('zeppelin:listamedidor')
    success_message = "Medidor adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarMedidorView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Medidor'
        context['return_url'] = reverse_lazy('zeppelin:listamedidor')
        return context



class EditarMedidorView(CustomUpdateView):
    form_class = MedidorlForm
    model = MedidorModel

    template_name = "zeppelin/medidor_edit.html"
    success_url = reverse_lazy('zeppelin:listamedidor')
    success_message = "Medidor editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarMedidorView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listamedidor')
        return context





#################################################################


class ListDesligamentoView(CustomListView):
    template_name = 'zeppelin/desligamento_list.html'
    model = MotivoDesligamento
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listadesligamento')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListDesligamentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Motivo de Desligamento'
        context['add_url'] = reverse_lazy('zeppelin:adicionadesligamento')

        return context


class AdicionarDesligamentoView(CustomCreateView):

    form_class = MotivoDesligamentoForm
    template_name = "zeppelin/desligamento_add.html"
    success_url = reverse_lazy('zeppelin:listadesligamento')
    success_message = "Desligamento adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarDesligamentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Motivo de Desligamento'
        context['return_url'] = reverse_lazy('zeppelin:listadesligamento')
        return context



class EditarDesligamentoView(CustomUpdateView):
    form_class = MotivoDesligamentoForm
    model = MotivoDesligamento

    template_name = "zeppelin/desligamento_edit.html"
    success_url = reverse_lazy('zeppelin:listadesligamento')
    success_message = "Desligamento editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarDesligamentoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listadesligamento')
        return context




######################################################################################################



class ListServicoView(CustomListView):
    template_name = 'zeppelin/servico_list.html'
    model = ServicoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listaservico')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListServicoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Serviços'
        context['add_url'] = reverse_lazy('zeppelin:adicionaservico')

        return context


class AdicionarServicoView(CustomCreateView):

    form_class = ServicoForm
    template_name = "zeppelin/servico_add.html"
    success_url = reverse_lazy('zeppelin:listaservico')
    success_message = "Serviço especial adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarServicoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Tipo Especial'
        context['return_url'] = reverse_lazy('zeppelin:listatipoespecial')
        return context



class EditarServicoView(CustomUpdateView):
    form_class = ServicoForm
    model = ServicoModel

    template_name = "zeppelin/servico_edit.html"
    success_url = reverse_lazy('zeppelin:listaservico')
    success_message = "Serviço editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarServicoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listaservico')
        return context

#########################################################################################################


class ListGrupoEquipamentoView(CustomListView):
    template_name = 'zeppelin/grupo_equipamento_list.html'
    model = GrupoEquipamentoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listagrupoequipamento')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListGrupoEquipamentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Grupo de Equipamento'
        context['add_url'] = reverse_lazy('zeppelin:adicionagrupoequipamento')

        return context


class AdicionarGrupoEquipementoView(CustomCreateView):

    form_class = GrupoEquipamentoForm
    template_name = "zeppelin/grupo_equipamento_add.html"
    success_url = reverse_lazy('zeppelin:listagrupoequipamento')
    success_message = "Grupo de equipementos adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarGrupoEquipementoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Grupo de Equipamento'
        context['return_url'] = reverse_lazy('zeppelin:listagrupoequipamento')
        return context





class EditarGrupoEquipamentoView(CustomUpdateView):
    form_class = GrupoEquipamentoForm
    model = GrupoEquipamentoModel

    template_name = "zeppelin/grupo_equipamento_edit.html"
    success_url = reverse_lazy('zeppelin:listagrupoequipamento')
    success_message = "Grupo de equipamentos editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarGrupoEquipamentoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listagrupoequipamento')
        return context

#########################################################################################################




class ListEquipamentoView(CustomListView):
    template_name = 'zeppelin/equipamento_list.html'
    model = EquipamentoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listaequipamento')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListEquipamentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Equipamento'
        context['add_url'] = reverse_lazy('zeppelin:adicionaequipamento')

        return context


class AdicionarEquipementoView(CustomCreateView):

    form_class = EquipamentoForm
    template_name = "zeppelin/equipamento_add.html"
    success_url = reverse_lazy('zeppelin:listaequipamento')
    success_message = "Equipementos adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarEquipementoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Equipamento'
        context['return_url'] = reverse_lazy('zeppelin:listaequipamento')
        return context





class EditarEquipamentoView(CustomUpdateView):
    form_class = EquipamentoForm
    model = EquipamentoModel

    template_name = "zeppelin/equipamento_edit.html"
    success_url = reverse_lazy('zeppelin:listaequipamento')
    success_message = "Equipamentos editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarEquipamentoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listaequipamento')
        return context



#########################################################################################################




class ListCNAEView(CustomListView):
    template_name = 'zeppelin/cnae_list.html'
    model = cnaeModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listacnae')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListCNAEView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Equipamento'
        context['add_url'] = reverse_lazy('zeppelin:adicionacnae')

        return context


class AdicionarCNAEView(CustomCreateView):

    form_class = CnaeForm
    template_name = "zeppelin/cnae_add.html"
    success_url = reverse_lazy('zeppelin:listacnae')
    success_message = "CNAE adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarCNAEView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar CNAE'
        context['return_url'] = reverse_lazy('zeppelin:listacnae')
        return context





class EditarCNAEView(CustomUpdateView):
    form_class = CnaeForm
    model = cnaeModel

    template_name = "zeppelin/cnae_edit.html"
    success_url = reverse_lazy('zeppelin:listacnae')
    success_message = "CNAE editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarCNAEView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listacnae')
        return context




#########################################################################################################




class ListHistoricoPadraoView(CustomListView):
    template_name = 'zeppelin/historicopadrao_list.html'
    model = HistoricoPadraoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listahistoricopadrao')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListHistoricoPadraoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Histórico Padrão'
        context['add_url'] = reverse_lazy('zeppelin:adicionahistoricopadrao')

        return context


class AdicionarHistoricoPadraoView(CustomCreateView):

    form_class = HistoricoPadraoForm
    template_name = "zeppelin/historicopadrao_add.html"
    success_url = reverse_lazy('zeppelin:listahistoricopadrao')
    success_message = "Histórico do padrão adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarHistoricoPadraoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Histórico do padrão'
        context['return_url'] = reverse_lazy('zeppelin:listahistoricopadrao')
        return context





class EditarHistoricoPadraoView(CustomUpdateView):
    form_class = HistoricoPadraoForm
    model = HistoricoPadraoModel

    template_name = "zeppelin/historicopadrao_edit.html"
    success_url = reverse_lazy('zeppelin:listahistoricopadrao')
    success_message = "Histórico do padrão editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarHistoricoPadraoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listahistoricopadrao')
        return context


#########################################################################################################




class ListTipoBoletimAfericaoView(CustomListView):
    template_name = 'zeppelin/tipoboletimafericao_list.html'
    model = TipoBoletimAfericaoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listatipoboletimafericao')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListTipoBoletimAfericaoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Tipo Boletim Afericao Padrão'
        context['add_url'] = reverse_lazy('zeppelin:adicionatipoboletimafericao')

        return context


class AdicionarTipoBoletimAfericaoView(CustomCreateView):

    form_class = TipoBoletimAfericaoForm
    template_name = "zeppelin/tipoboletimafericao_add.html"
    success_url = reverse_lazy('zeppelin:listatipoboletimafericao')
    success_message = "adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarTipoBoletimAfericaoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Tipo Boletim Aferição'
        context['return_url'] = reverse_lazy('zeppelin:listatipoboletimafericao')
        return context





class EditarTipoBoletimAfericaoView(CustomUpdateView):
    form_class = TipoBoletimAfericaoForm
    model = TipoBoletimAfericaoModel

    template_name = "zeppelin/tipoboletimafericao_edit.html"
    success_url = reverse_lazy('zeppelin:listatipoboletimafericao')
    success_message = "Tipo Boletim Afericao editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarTipoBoletimAfericaoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listatipoboletimafericao')
        return context


#########################################################################################################




class ListTipoDocumentoView(CustomListView):
    template_name = 'zeppelin/tipodocumento_list.html'
    model = TipoDocumentoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listatipodocumento')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListTipoDocumentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Tipo Documetno'
        context['add_url'] = reverse_lazy('zeppelin:adicionatipodocumento')

        return context


class AdicionarTipoDocumentoView(CustomCreateView):

    form_class = TipoDocumentoForm
    template_name = "zeppelin/tipodocumento_add.html"
    success_url = reverse_lazy('zeppelin:listatipodocumento')
    success_message = "adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarTipoDocumentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Tipo de Documento'
        context['return_url'] = reverse_lazy('zeppelin:listatipodocumento')
        return context





class EditarTipoDocumentoView(CustomUpdateView):
    form_class = TipoDocumentoForm
    model = TipoDocumentoModel

    template_name = "zeppelin/tipodocumento_edit.html"
    success_url = reverse_lazy('zeppelin:listatipodocumento')
    success_message = "Tipo de Documento editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarTipoDocumentoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listatipodocumento')
        return context




#########################################################################################################




class ListServicoEssencialView(CustomListView):
    template_name = 'zeppelin/tiposervicoessencial_list.html'
    model = TipoServicoEssencialModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listatiposervicoessencial')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListServicoEssencialView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Tipo Serviço Essencial'
        context['add_url'] = reverse_lazy('zeppelin:adicionatiposervicoessencial')

        return context


class AdicionarServicoEssencialView(CustomCreateView):

    form_class = TipoServicoEssencialForm
    template_name = "zeppelin/tiposervicoessencial_add.html"
    success_url = reverse_lazy('zeppelin:listatiposervicoessencial')
    success_message = "adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarServicoEssencialView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Serviço Essencial'
        context['return_url'] = reverse_lazy('zeppelin:listatiposervicoessencial')
        return context





class EditarServicoEssencialView(CustomUpdateView):
    form_class = TipoServicoEssencialForm
    model = TipoServicoEssencialModel

    template_name = "zeppelin/tiposervicoessencial_edit.html"
    success_url = reverse_lazy('zeppelin:listatiposervicoessencial')
    success_message = "Serviço Essencial editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarServicoEssencialView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listatiposervicoessencial')
        return context



#########################################################################################################




class ListCadastroDeFinalidadeView(CustomListView):
    template_name = 'zeppelin/cadastrodefinalidade_list.html'
    model = CadastroDeFinalidadeModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listacadastrodefinalidade')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListCadastroDeFinalidadeView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Cadastro de Finalidade'
        context['add_url'] = reverse_lazy('zeppelin:adicionacadastrodefinalidade')

        return context


class AdicionarCadastroDeFinalidadeView(CustomCreateView):

    form_class = CadastroDeFinalidadeForm
    template_name = "zeppelin/cadastrodefinalidade_add.html"
    success_url = reverse_lazy('zeppelin:listacadastrodefinalidade')
    success_message = "adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):

        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarCadastroDeFinalidadeView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Finalidade'
        context['return_url'] = reverse_lazy('zeppelin:listacadastrodefinalidade')
        return context





class EditarCadastroDeFinalidadeView(CustomUpdateView):
    form_class = CadastroDeFinalidadeForm
    model = CadastroDeFinalidadeModel

    template_name = "zeppelin/cadastrodefinalidade_edit.html"
    success_url = reverse_lazy('zeppelin:listacadastrodefinalidade')
    success_message = "Finalidade editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarCadastroDeFinalidadeView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listacadastrodefinalidade')
        return context



#########################################################################################################




class ListMotivoReprovacaoVistoriaView(CustomListView):
    template_name = 'zeppelin/motivoreprovacaovistoria_list.html'
    model = MotivoReprovacaoVistoriaModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listamotivoreprovacaovistoria')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListMotivoReprovacaoVistoriaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Motivos de Reprovação em vistoria'
        context['add_url'] = reverse_lazy('zeppelin:adicionamotivoreprovacaovistoria')

        return context


class AdicionarMotivoReprovacaoVistoriaView(CustomCreateView):

    form_class = MotivoReprovacaoVistoriaForm
    template_name = "zeppelin/motivoreprovacaovistoria_add.html"
    success_url = reverse_lazy('zeppelin:listamotivoreprovacaovistoria')
    success_message = "Motivo de reprovação em vistoria adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):

        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarMotivoReprovacaoVistoriaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Motivos de Reprovação em Vistoria'
        context['return_url'] = reverse_lazy('zeppelin:listamotivoreprovacaovistoria')
        return context





class EditarMotivoReprovacaoVistoriaView(CustomUpdateView):
    form_class = MotivoReprovacaoVistoriaForm
    model = MotivoReprovacaoVistoriaModel

    template_name = "zeppelin/motivoreprovacaovistoria_edit.html"
    success_url = reverse_lazy('zeppelin:listamotivoreprovacaovistoria')
    success_message = "Motivo de reprovação em vistoria editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarMotivoReprovacaoVistoriaView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listamotivoreprovacaovistoria')
        return context






#########################################################################################################




class ListMotivoCancelamentoView(CustomListView):
    template_name = 'zeppelin/motivocancelamento_list.html'
    model = MotivoCancelamentoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listamotivocancelamento')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListMotivoCancelamentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Motivos de Cancelamento de Vistoria'
        context['add_url'] = reverse_lazy('zeppelin:adicionamotivocancelamento')

        return context


class AdicionarMotivoCancelamentoView(CustomCreateView):

    form_class = MotivoCancelamentoForm
    template_name = "zeppelin/add.html"
    success_url = reverse_lazy('zeppelin:listamotivocancelamento')
    success_message = "Motivo de Cancelamento de vistoria adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):

        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarMotivoCancelamentoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Motivos de Cancelamento de Vistoria'
        context['return_url'] = reverse_lazy('zeppelin:listamotivocancelamento')
        return context





class EditarMotivoCancelamentoVistoriaView(CustomUpdateView):
    form_class = MotivoCancelamentoForm
    model = MotivoCancelamentoModel

    template_name = "zeppelin/edit.html"
    success_url = reverse_lazy('zeppelin:listamotivocancelamento')
    success_message = "Motivo de cancelamento de vistoria editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarMotivoCancelamentoVistoriaView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listamotivocancelamento')
        return context


#########################################################################################################




class ListMotivoReprovacaoAnaliseView(CustomListView):
    template_name = 'zeppelin/motivoreprovacaoanalise_list.html'
    model = MotivoReprovacaoAnaliseModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listamotivoreprovacaoanalise')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListMotivoReprovacaoAnaliseView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Motivos de Reprocação em Análise'
        context['add_url'] = reverse_lazy('zeppelin:adicionamotivoreprovacaoanalise')

        return context


class AdicionarMotivoReprovacaoAnaliseView(CustomCreateView):

    form_class = MotivoReprovacaoAnaliseForm
    template_name = "zeppelin/add.html"
    success_url = reverse_lazy('zeppelin:listamotivoreprovacaoanalise')
    success_message = "Motivo de Reprovação em Análise adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarMotivoReprovacaoAnaliseView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Motivos de Cancelamento de Vistoria'
        context['return_url'] = reverse_lazy('zeppelin:listamotivocancelamento')
        return context





class EditarMotivoReprovacaoAnaliseView(CustomUpdateView):
    form_class = MotivoReprovacaoAnaliseForm
    model = MotivoReprovacaoAnaliseModel

    template_name = "zeppelin/edit.html"
    success_url = reverse_lazy('zeppelin:listamotivoreprovacaoanalise')
    success_message = "Motivo de Reprovação de Análise editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarMotivoReprovacaoAnaliseView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listamotivoreprovacaoanalise')
        return context


#########################################################################################################




class ListMotivoDeferimentoBaixaRendaView(CustomListView):
    template_name = 'zeppelin/motivodeferimentobaixarenda_list.html'
    model = MotivoDeferimentoBaixaRendaModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listamotivodeferimentobaixarenda')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListMotivoDeferimentoBaixaRendaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Motivos Deferimento de Baixa Renda'
        context['add_url'] = reverse_lazy('zeppelin:adicionamotivodeferimentobaixarenda')

        return context


class AdicionarMotivoDeferimentoBaixaRendaView(CustomCreateView):

    form_class = MotivoDeferimentoBaixaRendaForm
    template_name = "zeppelin/add.html"
    success_url = reverse_lazy('zeppelin:listamotivodeferimentobaixarenda')
    success_message = "Motivo Deferimento Baixa Renda Adicionado Com Sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarMotivoDeferimentoBaixaRendaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Motivos de Deferimento Baixa Renda'
        context['return_url'] = reverse_lazy('zeppelin:listamotivodeferimentobaixarenda')
        return context





class EditarMotivoDeferimentoBaixaRendaView(CustomUpdateView):
    form_class = MotivoDeferimentoBaixaRendaForm
    model = MotivoDeferimentoBaixaRendaModel

    template_name = "zeppelin/edit.html"
    success_url = reverse_lazy('zeppelin:listamotivodeferimentobaixarenda')
    success_message = "Motivo de Deferimento Baixa Renda editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarMotivoDeferimentoBaixaRendaView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listamotivodeferimentobaixarenda')
        return context



#########################################################################################################




class ListCriterioBaixaRendaView(CustomListView):
    template_name = 'zeppelin/criteriobaixarenda_list.html'
    model = CriterioBaixaRendaModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('zeppelin:listcriteriobaixarenda')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListCriterioBaixaRendaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Critérios de Baixa Renda'
        context['add_url'] = reverse_lazy('zeppelin:adicionacriteriobaixarenda')

        return context


class AdicionarCriterioBaixaRendaView(CustomCreateView):

    form_class = CriterioBaixaRendaForm
    template_name = "zeppelin/add.html"
    success_url = reverse_lazy('zeppelin:listcriteriobaixarenda')
    success_message = "Critério de Renda Adicionado Com Sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarCriterioBaixaRendaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Adicionar Critério de Baixa Renda'
        context['return_url'] = reverse_lazy('zeppelin:listcriteriobaixarenda')
        return context





class EditarCriterioRendaView(CustomUpdateView):
    form_class = CriterioBaixaRendaForm
    model = CriterioBaixaRendaModel

    template_name = "zeppelin/edit.html"
    success_url = reverse_lazy('zeppelin:listcriteriobaixarenda')
    success_message = "Critério de Baixa Renda editado com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarCriterioRendaView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('zeppelin:listcriteriobaixarenda')
        return context


