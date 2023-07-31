# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangosige.apps.zeppelin.models import *



#ClasseForm
class SubGrupoForm(forms.ModelForm):

    class Meta:
        model = SubGrupoModel
        fields = ('nome', 'tensao_maxima', 'tensao_minima', 'carga')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'tensao_maxima': forms.TextInput(attrs={'class': 'form-control'}),
            'tensao_minima': forms.TextInput(attrs={'class': 'form-control'}),
            'carga': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RegionalForm(forms.ModelForm):

    class Meta:
        model = RegionalModel
        fields = ('nome_regional', 'funcionarios_proprios', 'funcionarios_terceirizados')

        widgets = {
            'nome_regional': forms.TextInput(attrs={'class': 'form-control'}),
            'funcionarios_proprios': forms.TextInput(attrs={'class': 'form-control'}),
            'funcionarios_terceirizados': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MunicipioForm(forms.ModelForm):

    class Meta:
        model = MunicipioModel
        fields = ('nome_municipio', 'codigo_ibge', 'conta_cosip', 'conta_ativo', 'provisao', 'uf_nome', 'uf_cod')

        widgets = {
            'nome_municipio': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_ibge': forms.TextInput(attrs={'class': 'form-control'}),
            'conta_cosip': forms.TextInput(attrs={'class': 'form-control'}),
            'conta_ativo': forms.TextInput(attrs={'class': 'form-control'}),
            'provisao': forms.TextInput(attrs={'class': 'form-control'}),
            'uf_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'uf_cod': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ClasseForm(forms.ModelForm):

    class Meta:
        model = ClasseModel
        fields = ('nome', )

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }




class SubClasseForm(forms.ModelForm):



   class Meta:
        model = SubClasseModel
        fields = ('nome', 'classe',)

        widgets = {
            'classe': forms.Select(attrs={'class': 'form-control select-produto'}),
            'nome': forms.TextInput(attrs={'class': 'form-control decimal-mask'}),

        }

        labels = {
            'nome': _('Nome'),
            'Classe': _('Classe'),
        }




class GrupoForm(forms.ModelForm):

    class Meta:
        model = GrupoModel
        fields = ('nome', 'numero', 'conjunto_aneel',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'conjunto_aneel': forms.TextInput(attrs={'class': 'form-control'}),
        }



class TipoEspecialForm(forms.ModelForm):

    class Meta:
        model = TipoEspecialModel
        fields = ('nome', 'codigo',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MedidorlForm(forms.ModelForm):

    class Meta:
        model = MedidorModel
        fields = ('codigo',)

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UnidadeConsumidoraForm(forms.ModelForm):

    class Meta:
        model = UnidadeConsumidoraModel


        fields = ('numero', 'cliente', 'grupo', 'modalidade_tarifaria',
                  'subgrupo', 'sub_classe', 'tipo_fornecimento', 'tipo_especial', 'tipo_contabilidade', 'medidor', )

        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control', 'id': 'uc_numero'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control', 'id': 'id_grupo'}),
            'modalidade_tarifaria': forms.Select(attrs={'class': 'form-control', 'id': 'id_modalidade_tarifaria'}),
            'subgrupo': forms.Select(attrs={'class': 'form-control'}),
            'sub_classe': forms.Select(attrs={'class': 'form-control'}),
            'tipo_fornecimento': forms.Select(attrs={'class': 'form-control'}),
            'tipo_especial': forms.Select(attrs={'class': 'form-control'}),
            'tipo_contabilidade': forms.Select(attrs={'class': 'form-control'}),
            'medidor': forms.Select(attrs={'class': 'form-control'}),
        }



class ServicoForm(forms.ModelForm):

    class Meta:
        model = ServicoModel
        fields = ('nome', 'codigo',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MotivoDesligamentoForm(forms.ModelForm):

    class Meta:
        model = MotivoDesligamento
        fields = ('nome', 'sai_ficha_de_leitura', 'exporta_carga_mensal', 'gera_solicitacao_desligamento' , 'servico', 'situacao', 'crm', 'tipo')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sai_ficha_de_leitura': forms.Select(attrs={'class': 'form-control'}),
            'exporta_carga_mensal': forms.Select(attrs={'class': 'form-control'}),
            'gera_solicitacao_desligamento': forms.Select(attrs={'class': 'form-control'}),
            'servico': forms.Select(attrs={'class': 'form-control'}),
            'situacao': forms.TextInput(attrs={'class': 'form-control'}),
            'crm': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }



class GrupoEquipamentoForm(forms.ModelForm):

    class Meta:
        model = GrupoEquipamentoModel
        fields = ('codigo', 'descricao', 'ativo',)

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'ativo': forms.Select(attrs={'class': 'form-control'}),
        }


class EquipamentoForm(forms.ModelForm):

    class Meta:
        model = EquipamentoModel
        fields = ('codigo', 'nome', 'grupo',   'potencia', 'hora_dia', 'dia_mes', 'classe', )

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),
            'potencia': forms.TextInput(attrs={'class': 'form-control'}),
            'hora_dia': forms.TextInput(attrs={'class': 'form-control'}),
            'dia_mes': forms.TextInput(attrs={'class': 'form-control'}),
            'classe': forms.SelectMultiple(attrs={'class': 'form-control','style': 'height:130px;'}),

        }


class CnaeForm(forms.ModelForm):

    class Meta:
        model = cnaeModel
        fields = ('codigo', 'descricao', 'prioridade', 'permite_rural',)

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'prioridade': forms.TextInput(attrs={'class': 'form-control'}),
            'permite_rural': forms.Select(attrs={'class': 'form-control'}),
        }





class HistoricoPadraoForm(forms.ModelForm):

    class Meta:
        model = HistoricoPadraoModel
        fields = ('codigo', 'nome', 'alertar',)

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'alertar': forms.Select(attrs={'class': 'form-control'}),
        }



class TipoBoletimAfericaoForm(forms.ModelForm):

    class Meta:
        model = TipoBoletimAfericaoModel
        fields = ('codigo', 'nome', 'motivo',)

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'motivo': forms.Select(attrs={'class': 'form-control'}),
        }



class TipoDocumentoForm(forms.ModelForm):

    class Meta:
        model = TipoDocumentoModel
        fields = ('codigo', 'nome', 'ativo',)

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ativo': forms.Select(attrs={'class': 'form-control'}),
        }





class TipoServicoEssencialForm(forms.ModelForm):

    class Meta:
        model = TipoServicoEssencialModel
        fields = ('codigo', 'definicao', 'ativo', 'descricao_completa', 'tipo',)

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'definicao': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao_completa': forms.TextInput(attrs={'class': 'form-control'}),
            'ativo': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }


class CadastroDeFinalidadeForm(forms.ModelForm):

    class Meta:
        model = CadastroDeFinalidadeModel
        fields = ('codigo', 'nome', 'descricao',)

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),

        }

#MotivoReprovacaoVistoriaModel


class MotivoReprovacaoVistoriaForm(forms.ModelForm):

    class Meta:
        model = MotivoReprovacaoVistoriaModel
        fields = ('codigo', 'ativo', 'descricao', 'motivo' , 'finalidade_obra',)

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'ativo': forms.Select(attrs={'class': 'form-control'}),
            'motivo': forms.TextInput(attrs={'class': 'form-control'}),
            'finalidade_obra': forms.Select(attrs={'class': 'form-control'}),

        }

class MotivoCancelamentoForm(forms.ModelForm):

    class Meta:
        model = MotivoCancelamentoModel
        fields = ('codigo', 'descricao',)

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),

        }


class MotivoReprovacaoAnaliseForm(forms.ModelForm):

    class Meta:
        model = MotivoReprovacaoAnaliseModel
        fields = ('codigo', 'descricao', 'motivo_cancelamento' , 'motivo_reprovacao',)

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'motivo_cancelamento': forms.Select(attrs={'class': 'form-control'}),
            'motivo_reprovacao': forms.Select(attrs={'class': 'form-control'}),
        }





class MotivoDeferimentoBaixaRendaForm(forms.ModelForm):

    class Meta:
        model = MotivoDeferimentoBaixaRendaModel
        fields = ('codigo', 'descricao', 'origem_solicitacao',)

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'origem_solicitacao': forms.TextInput(attrs={'class': 'form-control'}),
        }



class CriterioBaixaRendaForm(forms.ModelForm):

    class Meta:
        model = CriterioBaixaRendaModel
        fields = ('codigo', 'descricao', 'tipo', 'ativo',)

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'ativo': forms.Select(attrs={'class': 'form-control'}),
        }











