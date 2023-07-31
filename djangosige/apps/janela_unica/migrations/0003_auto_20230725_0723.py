# Generated by Django 3.2.10 on 2023-07-25 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('janela_unica', '0002_auto_20230723_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='comprovante_lancamento',
            field=models.FileField(blank=True, null=True, upload_to='janela_unica/documentos'),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='comprovante_pagamento',
            field=models.FileField(blank=True, null=True, upload_to='janela_unica/documentos'),
        ),
    ]
