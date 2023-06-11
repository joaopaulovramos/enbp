# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangosige.apps.viagem.models import *


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)


class TipoViagemForm(forms.ModelForm):
    class Meta:
        model = TiposDeViagemModel
        fields = ('nome',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),

        }
        labels = {
            'nome': _('Descrição'),
        }


class TipoDeSolicitacaoForm(forms.ModelForm):
    class Meta:
        model = TiposDeSolicitacaoModel
        fields = ('nome',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),

        }
        labels = {
            'nome': _('Descrição'),
        }


class TipoDeTransporteForm(forms.ModelForm):
    class Meta:
        model = TipoDeTransporteModel
        fields = ('nome',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),

        }
        labels = {
            'nome': _('Descrição'),
        }


class TipoMotivoForm(forms.ModelForm):
    class Meta:
        model = MotivoDeViagemModel
        fields = ('nome',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
        }
        labels = {
            'nome': _('Descrição'),
        }


class TipoDespesaForm(forms.ModelForm):
    class Meta:
        model = TipoDeDespesaModel
        fields = ('sigla', 'descricao',)
        widgets = {
            'sigla': forms.TextInput(attrs={'class': 'form-control', 'size': '10'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'size': '300'}),
        }
        labels = {
            'sigla': _('Silga'),
            'descricao': _('Descrição'),
        }


class MoedaForm(forms.ModelForm):
    class Meta:
        model = MoedaModel
        fields = ('descricao',)
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'size': '300'}),
        }
        labels = {
            'descricao': _('Descrição'),
        }


class CategoriaPassagemForm(forms.ModelForm):
    class Meta:
        model = CategoriaPassagemModel
        fields = ('descricao',)
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
        }
        labels = {
            'descricao': _('Descrição'),
        }


class HorarioPreferencialForm(forms.ModelForm):
    class Meta:
        model = HorarioPreferencialModel
        fields = ('descricao',)
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
        }
        labels = {
            'descricao': _('Descrição'),
        }


class ViagemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ViagemForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ViagemModel
        fields = ('valor_passagem',
                  'dada_inicio',
                  'dada_fim',
                  'origem',
                  'destino',
                  'objetivo',
                  'tipo_viagem',
                  'tipo_solicitacao',
                  'motivo',
                  'tipo_transporte',
                  'categoria_passagem',
                  'horario_preferencial',)
        widgets = {
            'valor_passagem': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'dada_inicio': DateInput(format=["%d-%m-%Y"], attrs={'class': 'form-control', 'size': '200'}),
            'dada_fim': DateInput(format=["%d-%m-%Y"], attrs={'class': 'form-control', 'size': '200'}),
            'origem': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'destino': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'objetivo': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'tipo_viagem': forms.Select(attrs={'class': 'form-control select-produto'}),
            'tipo_solicitacao': forms.Select(attrs={'class': 'form-control select-produto'}),
            'motivo': forms.Select(attrs={'class': 'form-control select-produto'}),
            'tipo_transporte': forms.Select(attrs={'class': 'form-control select-produto'}),
            'categoria_passagem': forms.Select(attrs={'class': 'form-control select-produto'}),
            'horario_preferencial': forms.Select(attrs={'class': 'form-control select-produto'}),
        }
        labels = {
            'valor_passagem': _('Valor da Passagem'),
            'dada_inicio': _('Data Inicio'),
            'dada_fim': _('Data Fim'),
            'origem': _('Origem'),
            'destino': _('Destino'),
            'objetivo': _('Objetivo'),
            'tipo_viagem': _('Tipo de Viagem'),
            'tipo_solicitacao': _('Tipo de Solicitação'),
            'motivo': _('Motivo'),
            'tipo_transporte': _('Tipo de Transporte'),
            'categoria_passagem': _('Catergoria da Passagem'),
            'horario_preferencial': _('Horário Preferencial'),

        }

    def save(self, commit=True):
        instance = super(ViagemForm, self).save(commit=False)
        instance.solicitante = self.request_user
        if commit:
            instance.save()
        return instance


class PrestacaoContaForm(forms.ModelForm):
    '''
     dada_inicio_realizada = models.DateTimeField()
    dada_fim_realizada   = models.DateField()
    remarcacao_interesse_particular = models.BooleanField(default=False)

    '''

    class Meta:
        model = ViagemModel
        fields = ('pagamento',
                  'dada_inicio_realizada',
                  'dada_fim_realizada',
                  'remarcacao_interesse_particular',
                  'descricao',
                  'finalizar_pc',

                  )
        widgets = {
            'pagamento': forms.Select(attrs={'class': 'form-control select-produto'}),
            'dada_inicio_realizada': DateInput(format=["%d-%m-%Y"], attrs={'class': 'form-control', 'size': '200'}),
            'dada_fim_realizada': DateInput(format=["%d-%m-%Y"], attrs={'class': 'form-control', 'size': '200'}),
            'remarcacao_interesse_particular': forms.Select(attrs={'class': 'form-control select-produto'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'size': '200'}),
            'finalizar_pc': forms.Select(attrs={'class': 'form-control select-produto'}),

        }
        labels = {
            'pagamento': _('Forma de Pagamento'),
            'dada_inicio_realizada': _('Data realizada de inicio'),
            'dada_fim_realizada': _('Data realizada de fim'),
            'remarcacao_interesse_particular': _('Remarcação por interesse particular'),
            'descricao': _('Descrição da Viagem'),
            'finalizar_pc': _('Finalizar Prestação de Contas'),

        }


class ArquivosForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(ArquivosForm, self).__init__(*args, **kwargs)
    #     self.fields['viagem'].initial = ViagemModel.objects.get(id=45)

    class Meta:
        model = Arquivos
        # 'viagem',
        fields = ('descricao', 'file',)

        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            # 'viagem': forms.Select(attrs={'class': 'form-control select-produto'}),
        }
        labels = {
            'descricao': _('Descrição'),
            'file': _('Arquivo'),
            # 'viagem': _('Viagem'),
        }


class AvaliarPrestacaoContaForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AvaliarPrestacaoContaForm, self).__init__(*args, **kwargs)
    #     self.fields['<field_to_disable>'].disabled = True
    '''
        dada_inicio_realizada = models.DateTimeField()
       dada_fim_realizada   = models.DateField()
       remarcacao_interesse_particular = models.BooleanField(default=False)

       '''

    class Meta:
        model = ViagemModel
        fields = ('pagamento',
                  'dada_inicio_realizada',
                  'dada_fim_realizada',
                  'remarcacao_interesse_particular',
                  'descricao',
                  'finalizar_pc',

                  )
        widgets = {
            'pagamento': forms.Select(attrs={'class': 'form-control select-produto', "disabled": "disabled"}),
            'dada_inicio_realizada': DateInput(format=["%d-%m-%Y"],
                                               attrs={'class': 'form-control', 'size': '200', "disabled": "disabled"}),
            'dada_fim_realizada': DateInput(format=["%d-%m-%Y"],
                                            attrs={'class': 'form-control', 'size': '200', 'style': 'disabled: true;',
                                                   "disabled": "disabled"}),
            'remarcacao_interesse_particular': forms.Select(
                attrs={'class': 'form-control select-produto', 'style': 'disabled: true;', "disabled": "disabled"}),
            'descricao': forms.Textarea(
                attrs={'class': 'form-control', 'size': '200', 'style': 'disabled: true;', "disabled": "disabled"}),
            'finalizar_pc': forms.Select(
                attrs={'class': 'form-control select-produto', 'style': 'disabled: true;', "disabled": "disabled"}),

        }
        labels = {
            'pagamento': _('Forma de Pagamento'),
            'dada_inicio_realizada': _('Data realizada de inicio'),
            'dada_fim_realizada': _('Data realizada de fim'),
            'remarcacao_interesse_particular': _('Remarcação por interesse particular'),
            'descricao': _('Descrição da Viagem'),
            'finalizar_pc': _('Finalizar Prestação de Contas'),

        }


class AvaliarSolicitacaoViagemForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AvaliarPrestacaoContaForm, self).__init__(*args, **kwargs)
    #     self.fields['<field_to_disable>'].disabled = True
    '''
        dada_inicio_realizada = models.DateTimeField()
       dada_fim_realizada   = models.DateField()
       remarcacao_interesse_particular = models.BooleanField(default=False)

       '''

    class Meta:
        model = ViagemModel
        fields = ('valor_passagem',
                  'dada_inicio',
                  'dada_fim',
                  'origem',
                  'destino',
                  'objetivo',
                  'tipo_viagem',
                  'tipo_solicitacao',
                  'motivo',
                  'tipo_transporte',)
        widgets = {

            'valor_passagem': forms.TextInput(attrs={'class': 'form-control', 'size': '200', "disabled": "disabled"}),
            'dada_inicio': DateInput(format=["%d-%m-%Y"],
                                     attrs={'class': 'form-control', 'size': '200', "disabled": "disabled"}),
            'dada_fim': DateInput(format=["%d-%m-%Y"],
                                  attrs={'class': 'form-control', 'size': '200', "disabled": "disabled"}),
            'origem': forms.TextInput(attrs={'class': 'form-control', 'size': '200', "disabled": "disabled"}),
            'destino': forms.TextInput(attrs={'class': 'form-control', 'size': '200', "disabled": "disabled"}),
            'objetivo': forms.TextInput(attrs={'class': 'form-control', 'size': '200', "disabled": "disabled"}),
            'tipo_viagem': forms.Select(attrs={'class': 'form-control select-produto', "disabled": "disabled"}),
            'tipo_solicitacao': forms.Select(attrs={'class': 'form-control select-produto, "disabled":"disabled"'}),
            'motivo': forms.Select(attrs={'class': 'form-control select-produto', "disabled": "disabled"}),
            'tipo_transporte': forms.Select(attrs={'class': 'form-control select-produto, "disabled":"disabled"'}),
        }
        labels = {
            'valor_passagem': _('Valor da Passagem'),
            'dada_inicio': _('Data Inicio'),
            'dada_fim': _('Data Fim'),
            'origem': _('Origem'),
            'destino': _('Destino'),
            'objetivo': _('Objetivo'),
            'tipo_viagem': _('Tipo de Viagem'),
            'tipo_solicitacao': _('Tipo de Solicitação'),
            'motivo': _('Motivo'),
            'tipo_transporte': _('Tipo de Transporte'),

        }
