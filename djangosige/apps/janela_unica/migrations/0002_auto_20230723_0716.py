# Generated by Django 3.2.10 on 2023-07-23 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('janela_unica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='data_finalizacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documentounicofinanceiro',
            name='numero',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]
