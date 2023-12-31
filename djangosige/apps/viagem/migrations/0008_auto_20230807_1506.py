# Generated by Django 3.2.10 on 2023-08-07 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_usuario_departamento'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viagem', '0007_auto_20230807_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprovarpagamentodiariasmodel',
            name='autorizado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='aprovarpagamentodiariasmodel',
            name='tipo_pagamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='viagem.tipodepagamentomodel'),
        ),
        migrations.AlterField(
            model_name='aprovarpagamentodiariasmodel',
            name='viagem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='viagem.viagemmodel'),
        ),
        migrations.AlterField(
            model_name='aprovarpagamentoreembolsomodel',
            name='autorizado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='aprovarpagamentoreembolsomodel',
            name='tipo_pagamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='viagem.tipodepagamentomodel'),
        ),
        migrations.AlterField(
            model_name='aprovarpagamentoreembolsomodel',
            name='viagem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='viagem.viagemmodel'),
        ),
        migrations.AlterField(
            model_name='arquivos',
            name='moeda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='arquivos_moeda', to='viagem.moedamodel'),
        ),
        migrations.AlterField(
            model_name='arquivos',
            name='tipo_despesa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='arquivos_despesa', to='viagem.tipodedespesamodel'),
        ),
        migrations.AlterField(
            model_name='arquivos',
            name='viagem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='arquivos_viagem', to='viagem.viagemmodel'),
        ),
        migrations.AlterField(
            model_name='tabeladiariamodel',
            name='localidade_destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='diaria_localidade', to='viagem.localidademodel'),
        ),
        migrations.AlterField(
            model_name='tabeladiariamodel',
            name='moeda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='diaria_moeda', to='viagem.moedamodel'),
        ),
        migrations.AlterField(
            model_name='trechomodel',
            name='categoria_passagem_trecho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='viagem_trecho_passagem', to='viagem.categoriapassagemmodel'),
        ),
        migrations.AlterField(
            model_name='trechomodel',
            name='localidade_trecho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='viagem_trecho_localidade_destino', to='viagem.localidademodel'),
        ),
        migrations.AlterField(
            model_name='trechomodel',
            name='motivo_trecho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='viagem_trecho_motivo', to='viagem.motivodeviagemmodel'),
        ),
        migrations.AlterField(
            model_name='trechomodel',
            name='tipo_transporte_trecho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='viagem_trecho_transporte', to='viagem.tipodetransportemodel'),
        ),
        migrations.AlterField(
            model_name='trechomodel',
            name='viagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='viagem_trechos', to='viagem.viagemmodel'),
        ),
        migrations.AlterField(
            model_name='viagemmodel',
            name='acompanhante',
            field=models.ForeignKey(blank=True, limit_choices_to={'grupo_funcional': '0'}, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='viagem_acompanhante', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='viagemmodel',
            name='horario_preferencial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='viagem_horario', to='viagem.horariopreferencialmodel'),
        ),
        migrations.AlterField(
            model_name='viagemmodel',
            name='necessidade_especial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='viagem_necessidade_especial', to='viagem.tiposnecessidadeespecialmodel'),
        ),
        migrations.AlterField(
            model_name='viagemmodel',
            name='solicitante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='viagem_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='viagemmodel',
            name='tipo_solicitacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='viagem_solicitacao', to='viagem.tiposdesolicitacaomodel'),
        ),
        migrations.AlterField(
            model_name='viagemmodel',
            name='tipo_viagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='viagem_tipo', to='viagem.tiposdeviagemmodel'),
        ),
    ]
