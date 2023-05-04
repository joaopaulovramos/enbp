# Generated by Django 3.2.10 on 2022-11-15 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_merge_20170625_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='localestoque',
            options={'verbose_name': 'Local de Estoque'},
        ),
        migrations.AlterModelOptions(
            name='movimentoestoque',
            options={'permissions': (('consultar_estoque', 'Pode consultar estoque'),), 'verbose_name': 'Movimento de Estoque'},
        ),
        migrations.AlterField(
            model_name='entradaestoque',
            name='local_dest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='entrada_estoque_local', to='estoque.localestoque'),
        ),
        migrations.AlterField(
            model_name='saidaestoque',
            name='local_orig',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='saida_estoque_local', to='estoque.localestoque'),
        ),
    ]
