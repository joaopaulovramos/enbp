# Generated by Django 3.2.10 on 2023-08-02 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viagem', '0004_auto_20230704_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viagemmodel',
            name='crianca_colo',
        ),
        migrations.AddField(
            model_name='viagemmodel',
            name='duracao',
            field=models.CharField(choices=[('0', 'Inferior a 6hs'), ('1', 'Igual/Superior a 6hs')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viagemmodel',
            name='justificativa_cancelamento',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='viagemmodel',
            name='itinerario',
            field=models.CharField(choices=[('0', 'Ida'), ('1', 'Ida e Volta'), ('2', 'Em trânsito')], max_length=2),
        ),
        migrations.CreateModel(
            name='TrechoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio_trecho', models.DateTimeField()),
                ('data_fim_trecho', models.DateTimeField(blank=True, null=True)),
                ('origem_trecho', models.CharField(max_length=200)),
                ('destino_trecho', models.CharField(max_length=200)),
                ('tipo_transporte_trecho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viagem_trecho_transporte', to='viagem.tipodetransportemodel')),
                ('viagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viagem_trechos', to='viagem.viagemmodel')),
            ],
        ),
    ]
