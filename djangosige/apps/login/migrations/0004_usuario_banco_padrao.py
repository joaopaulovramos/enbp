# Generated by Django 3.2.10 on 2023-06-22 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0009_auto_20230622_1707'),
        ('login', '0003_auto_20230614_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='banco_padrao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banco_usuario', to='cadastro.contabancaria'),
        ),
    ]
