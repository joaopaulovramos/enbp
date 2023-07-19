from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangosige.apps.timesheet.models.timesheet_model import HorasSemanais, Gastos, PercentualDiario, OpiniaoModel
from decimal import Decimal


class HorasSemanaisForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(HorasSemanaisForm, self).__init__(*args, **kwargs)

    class Meta:
        model = HorasSemanais

        # 'projeto'
        fields = ('projeto', 'semanas', 'hr_seg', 'hr_ter', 'hr_qua', 'hr_qui', 'hr_sex', 'hr_sab', 'hr_dom',)

        widgets = {

            'semanas': forms.Select(attrs={'class': 'form-control'}),
            'projeto': forms.Select(attrs={'class': 'form-control'}),

            'hr_seg': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control decimal-mask'}),
            'hr_ter': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control decimal-mask'}),
            'hr_qua': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control decimal-mask'}),
            'hr_qui': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control decimal-mask'}),
            'hr_sex': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control decimal-mask'}),
            'hr_sab': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control decimal-mask'}),
            'hr_dom': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control decimal-mask'}),

        }
        labels = {
            'projeto': _('Projeto'),
            'horas': _('Horas Trabalhadas'),
            'semanas': _('Semana'),
            'hr_seg': _('Horas Trabalhadas na Segunda'),
            'hr_ter': _('Horas Trabalhadas na Terça'),
            'hr_qua': _('Horas Trabalhadas na Quarta'),
            'hr_qui': _('Horas Trabalhadas na Quinta'),
            'hr_sex': _('Horas Trabalhadas na Sexta'),
            'hr_sab': _('Horas Trabalhadas na Sabado'),
            'hr_dom': _('Horas Trabalhadas na Domingo'),
        }

    def save(self, commit=True):
        instance = super(HorasSemanaisForm, self).save(commit=False)
        instance.solicitante = self.request_user
        if commit:
            instance.save()
        return instance


class GastosForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(GastosForm, self).__init__(*args, **kwargs)
        self.fields['valor'].localize = True
        self.fields['data'].input_formats = ('%d/%m/%Y',)
        if (self.instance.situacao != '0' and self.instance.situacao != '3'):
            self.fields['projeto'].widget.attrs['disabled'] = True
            self.fields['descricao'].widget.attrs['disabled'] = True
            self.fields['valor'].widget.attrs['disabled'] = True
            self.fields['file'].widget.attrs['disabled'] = True
            self.fields['data'].widget.attrs['disabled'] = True
            self.fields['data'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Gastos
        #
        # descricao = models.CharField(max_length=500, null=False, blank=False)
        # # projeto = models.ForeignKey('norli_projeto.ExemploModel', related_name="certificados_user", on_delete=models.CASCADE, null=True, blank=True)
        # solicitante = models.ForeignKey(User, related_name="gastos_user", on_delete=models.CASCADE, null=True,
        #                                 blank=True)
        # valor = models.CharField(max_length=10, null=False, blank=False)
        # file = models.FileField(upload_to='files/', null=False, blank=False)

        fields = ('projeto', 'descricao', 'valor', 'file', 'data', 'situacao',)

        widgets = {
            'projeto': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'size': '500'}),
            'valor': forms.TextInput(attrs={'class': 'form-control decimal-mask'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control datepicker'}),
            'situacao': forms.Select(attrs={'class': 'form-control', 'disabled': True}),

        }
        labels = {
            'projeto': _('Projeto'),
            'descricao': _('Descrição'),
            'valor': _('Valor (R$)'),
            'file': _('Comprovante'),
            'data': _('Data'),
            'situacao': _('Situação'),
        }

    def save(self, commit=True):
        instance = super(GastosForm, self).save(commit=False)
        instance.solicitante = self.request_user
        if commit:
            instance.save()
        return instance


class PercentualDiarioForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PercentualDiarioForm, self).__init__(*args, **kwargs)
        self.fields['data'].input_formats = ('%d/%m/%Y',)

    class Meta:
        model = PercentualDiario

        # 'projeto'
        fields = ('data', 'projeto', 'percentual', 'observacao',)

        widgets = {

            'data': forms.DateInput(attrs={'class': 'form-control', 'size': '200'}),
            'projeto': forms.Select(attrs={'class': 'form-control'}),
            'percentual': forms.NumberInput(attrs={'class': 'form-control percentual'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control', 'size': '250'}),

        }
        labels = {
            'data': _('Dia'),
            'projeto': _('Projeto'),
            'percentual': _('Percentual da atividade'),
            'observacao': _('Observação'),
        }

    def save(self, commit=True):
        instance = super(PercentualDiarioForm, self).save(commit=False)
        instance.solicitante = self.request_user
        if commit:
            instance.save()
        return instance

class OpiniaoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(OpiniaoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = OpiniaoModel

        fields = ('opiniao',)

        widgets = {

            'opiniao': forms.Textarea(attrs={'class': 'form-control', 'size': '512'}),

        }
        labels = {
            'opiniao': _('Observação/crítica/sugestão'),
        }

    def save(self, commit=True):
        instance = super(OpiniaoForm, self).save(commit=False)
        instance.usuario = self.request_user
        if commit:
            instance.save()
        return instance