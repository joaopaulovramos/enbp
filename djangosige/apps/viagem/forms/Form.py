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


class TiposNecessidadeEspecialForm(forms.ModelForm):
    class Meta:
        model = TiposNecessidadeEspecialModel
        fields = ('descricao',)
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
        }
        labels = {
            'descricao': _('Descrição'),
        }


class LocalidadeForm(forms.ModelForm):
    class Meta:
        model = LocalidadeModel
        fields = ('descricao',)
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'size': '400'}),
        }
        labels = {
            'descricao': _('Descrição'),
        }

class TabelaDiariaForm(forms.ModelForm):
    class Meta:
        model = TabelaDiariaModel
        fields = ('grupo_funcional',
                  'localidade_destino',
                  'moeda',
                  'valor_diaria')
        widgets = {
            'grupo_funcional': forms.Select(attrs={'class': 'form-control select-cod-descricao'}),
            'localidade_destino': forms.Select(attrs={'class': 'form-control select-cod-descricao'}),
            'moeda': forms.Select(attrs={'class': 'form-control select-cod-descricao'}),
            'valor_diaria': forms.NumberInput(attrs={'class': 'form-control', 'id': 'valor_passagem_viagem'}),
        }
        labels = {
            'grupo_funcional': _('Grupo Funcional'),
            'localidade_destino': _('Localidade'),
            'moeda': _('Moeda'),
            'valor_diaria': _('Valor Diária'),
        }


class ViagemForm(forms.ModelForm):
    # valor_passagem = forms.DecimalField(max_digits=16, decimal_places=2, localize=True, widget=forms.TextInput(
    #     attrs={'id': 'valor_passagem_viagem', 'class': 'form-control', 'placeholder': 'R$ 0,00'}), initial=Decimal('0.00'),
    #                                     label='Valor da Passagem', required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ViagemForm, self).__init__(*args, **kwargs)
        self.fields['dada_inicio'].input_formats = ('%d/%m/%Y %H:%M',)

    class Meta:
        model = ViagemModel
        fields = (
            'valor_passagem',
            'itinerario',
            'escalas',
            'dada_inicio',
            'dada_fim',
            'origem',
            'destino',
            'localidade_destino',
            'acompanhante',
            'necessidade_especial',
            'objetivo',
            'justificativa',
            'tipo_viagem',
            'tipo_solicitacao',
            'motivo',
            'tipo_transporte',
            'categoria_passagem',
            'horario_preferencial',
            'bagagem_tecnica',
            'bagagem_despachada',
            'crianca_colo',
            'local_risco',
            'exige_vacina',
            'reservar_hotel',
            'alimentacao_terceiros',
            'qtd_diarias',
            'valor_diaria',
            'valor_total_diarias',
        )
        widgets = {
            'valor_passagem': forms.NumberInput(attrs={'class': 'form-control', 'id': 'valor_passagem_viagem'}),
            'itinerario': forms.RadioSelect(attrs={'class': 'form-control'}),
            'escalas': forms.RadioSelect(attrs={'class': 'form-control'}),
            'dada_inicio': forms.TextInput(attrs={'class': 'form-control datetimepicker', 'size': '200'}),
            'dada_fim': forms.TextInput(attrs={'class': 'form-control datetimepicker', 'size': '200'}),
            'origem': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'destino': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'acompanhante': forms.Select(attrs={'class': 'form-control select-cod-descricao'}),
            'necessidade_especial': forms.Select(attrs={'class': 'form-control select-cod-descricao'}),
            'objetivo': forms.Textarea(attrs={'class': 'form-control', 'size': '200'}),
            'justificativa': forms.Textarea(attrs={'class': 'form-control', 'size': '200'}),
            'tipo_viagem': forms.Select(attrs={'class': 'form-control select-cod-descricao'}),
            'localidade_destino': forms.Select(attrs={'class': 'form-control select-cod-descricao'}),
            'tipo_solicitacao': forms.Select(attrs={'class': 'form-control select-cod-descricao'}),
            'motivo': forms.Select(attrs={'class': 'form-control select-cod-descricao'}),
            'tipo_transporte': forms.Select(attrs={'class': 'form-control select-cod-descricao'}),
            'categoria_passagem': forms.Select(attrs={'class': 'form-control select-cod-descricao'}),
            'horario_preferencial': forms.Select(attrs={'class': 'form-control select-cod-descricao'}),
            'bagagem_tecnica': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'bagagem_despachada': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'crianca_colo': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'local_risco': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'exige_vacina': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'reservar_hotel': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'alimentacao_terceiros': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'qtd_diarias': forms.NumberInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'valor_diaria': forms.NumberInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'valor_total_diarias': forms.NumberInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),

        }
        labels = {
            'itinerario': _('Itinerário'),
            'escalas': _('Escalas'),
            'dada_inicio': _('Data Inicio'),
            'dada_fim': _('Data Fim'),
            'origem': _('Origem'),
            'destino': _('Destino'),
            'localidade_destino': _('Localidade'),
            'acompanhante': _(''),
            'necessidade_especial': _(''),
            'objetivo': _('Objetivo'),
            'justificativa': _('Justificativa de Excepcionalidade'),
            'tipo_viagem': _('Tipo de Viagem'),
            'tipo_solicitacao': _('Tipo de Solicitação'),
            'motivo': _('Motivo'),
            'tipo_transporte': _('Tipo de Transporte'),
            'categoria_passagem': _('Catergoria da Passagem'),
            'horario_preferencial': _('Horário Preferencial'),
            'bagagem_tecnica': _('Bagagem Técnica'),
            'bagagem_despachada': _('Bagagem Despachada'),
            'crianca_colo': _('Criança de Colo'),
            'local_risco': _('Local de risco'),
            'exige_vacina': _('Exige comprovante de vacina'),
            'reservar_hotel': _('Reservar hotel'),
            'alimentacao_terceiros': _('Alimentação Terceiros'),
            'qtd_diarias': _('Qtd. de Diárias'),
            'valor_diaria': _('Valor diária'),
            'valor_total_diarias': _('Valor Total'),

        }

    def save(self, commit=True):
        instance = super(ViagemForm, self).save(commit=False)
        instance.solicitante = self.request_user
        if commit:
            instance.save()
        return instance


class VerViagemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(VerViagemForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ViagemModel
        fields = (
            'valor_passagem',
            'itinerario',
            'escalas',
            'dada_inicio',
            'dada_fim',
            'origem',
            'destino',
            'acompanhante',
            'necessidade_especial',
            'objetivo',
            'justificativa',
            'tipo_viagem',
            'tipo_solicitacao',
            'motivo',
            'tipo_transporte',
            'categoria_passagem',
            'horario_preferencial',
            'bagagem_tecnica',
            'bagagem_despachada',
            'crianca_colo',
            'local_risco',
            'exige_vacina',
            'reservar_hotel',
            'alimentacao_terceiros',
            'qtd_diarias',
            'valor_diaria',
            'valor_total_diarias',
        )
        widgets = {
            'valor_passagem': forms.NumberInput(
                attrs={'class': 'form-control', 'id': 'valor_passagem_viagem', 'disabled': 'disabled'}),
            'itinerario': forms.RadioSelect(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'escalas': forms.RadioSelect(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'dada_inicio': forms.TextInput(attrs={'class': 'form-control datepicker', 'size': '200', 'disabled': 'disabled'}),
            'dada_fim': forms.TextInput(attrs={'class': 'form-control', 'size': '200', 'disabled': 'disabled'}),
            'origem': forms.TextInput(attrs={'class': 'form-control', 'size': '200', 'disabled': 'disabled'}),
            'destino': forms.TextInput(attrs={'class': 'form-control', 'size': '200', 'disabled': 'disabled'}),
            'acompanhante': forms.Select(attrs={'class': 'form-control select-cod-descricao', 'disabled': 'disabled'}),
            'necessidade_especial': forms.Select(
                attrs={'class': 'form-control select-cod-descricao', 'disabled': 'disabled'}),
            'objetivo': forms.Textarea(attrs={'class': 'form-control', 'size': '200', 'disabled': 'disabled'}),
            'justificativa': forms.Textarea(attrs={'class': 'form-control', 'size': '200', 'disabled': 'disabled'}),
            'tipo_viagem': forms.Select(attrs={'class': 'form-control select-cod-descricao', 'disabled': 'disabled'}),
            'tipo_solicitacao': forms.Select(
                attrs={'class': 'form-control select-cod-descricao', 'disabled': 'disabled'}),
            'motivo': forms.Select(attrs={'class': 'form-control select-cod-descricao', 'disabled': 'disabled'}),
            'tipo_transporte': forms.Select(
                attrs={'class': 'form-control select-cod-descricao', 'disabled': 'disabled'}),
            'categoria_passagem': forms.Select(
                attrs={'class': 'form-control select-cod-descricao', 'disabled': 'disabled'}),
            'horario_preferencial': forms.Select(
                attrs={'class': 'form-control select-cod-descricao', 'disabled': 'disabled'}),
            'bagagem_tecnica': forms.CheckboxInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'bagagem_despachada': forms.CheckboxInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'crianca_colo': forms.CheckboxInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'local_risco': forms.CheckboxInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'exige_vacina': forms.CheckboxInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'reservar_hotel': forms.CheckboxInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'alimentacao_terceiros': forms.CheckboxInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'qtd_diarias': forms.NumberInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'valor_diaria': forms.NumberInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'valor_total_diarias': forms.NumberInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),

        }
        labels = {
            'itinerario': _('Itinerário'),
            'escalas': _('Escalas'),
            'dada_inicio': _('Data Inicio'),
            'dada_fim': _('Data Fim'),
            'origem': _('Origem'),
            'destino': _('Destino'),
            'acompanhante': _(''),
            'necessidade_especial': _(''),
            'objetivo': _('Objetivo'),
            'justificativa': _('Justificativa de Excepcionalidade'),
            'tipo_viagem': _('Tipo de Viagem'),
            'tipo_solicitacao': _('Tipo de Solicitação'),
            'motivo': _('Motivo'),
            'tipo_transporte': _('Tipo de Transporte'),
            'categoria_passagem': _('Catergoria da Passagem'),
            'horario_preferencial': _('Horário Preferencial'),
            'bagagem_tecnica': _('Bagagem Técnica'),
            'bagagem_despachada': _('Bagagem Despachada'),
            'crianca_colo': _('Criança de Colo'),
            'local_risco': _('Local de risco'),
            'exige_vacina': _('Exige comprovante de vacina'),
            'reservar_hotel': _('Reservar hotel'),
            'alimentacao_terceiros': _('Alimentação Terceiros'),
            'qtd_diarias': _('Qtd. de Diárias'),
            'valor_diaria': _('Valor diária'),
            'valor_total_diarias': _('Valor Total'),

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

    def __int__(self, *args, **kwargs):
        super(ArquivosForm, self).__int__(*args, **kwargs)
        self.fields['data_evento'].input_formats = ('%d/%m/%Y',)

    class Meta:
        model = Arquivos
        # 'viagem',
        fields = ('descricao',
                  'file',
                  'numero_item',
                  'tipo_despesa',
                  'moeda',
                  'data_evento',
                  'pagamento',
                  'valor_pago',
                  'cotacao',
                  'valor_pago_reais',
                  )

        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'size': '250'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'numero_item': forms.NumberInput(attrs={'class': 'form-control', 'size': '200'}),
            'tipo_despesa': forms.Select(attrs={'class': 'form-control select-cod-descricao'}),
            'moeda': forms.Select(attrs={'class': 'form-control select-cod-descricao'}),
            # 'data_evento': DateInput(format='%d/%m/%Y', attrs={'class': 'form-control datepicker', 'size': '200'}),
            'data_evento': forms.TextInput(attrs={'class': 'form-control datepicker', 'size': '200'}),
            'pagamento': forms.Select(attrs={'class': 'form-control'}),
            'valor_pago': forms.NumberInput(attrs={'class': 'form-control', 'size': '200'}),
            'cotacao': forms.NumberInput(attrs={'class': 'form-control', 'size': '200'}),
            'valor_pago_reais': forms.NumberInput(attrs={'class': 'form-control', 'size': '200', 'readonly': 'readonly'}),
        }
        labels = {
            'descricao': _('Descrição do Item'),
            'file': _('Arquivo'),
            'numero_item': _('Item'),
            'tipo_despesa': _('Tipo de Despesa'),
            'moeda': _('Moeda'),
            'data_evento': _('Data do evento'),
            'pagamento': _('Forma de Pagamento'),
            'valor_pago': _('Valor Pago'),
            'cotacao': _('Cotação do Dia'),
            'valor_pago_reais': _('Valor pago em Reais'),
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
