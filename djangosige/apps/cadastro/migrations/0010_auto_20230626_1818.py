# Generated by Django 3.2.10 on 2023-06-26 21:18

from django.db import migrations, models
import django.db.models.deletion
import django_cpf_cnpj.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0009_auto_20230622_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='CNAE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='empresa',
            name='inativo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pessoajuridica',
            name='cnpj',
            field=django_cpf_cnpj.fields.CNPJField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cnae',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empresa_cnae', to='cadastro.cnae'),
        ),
    ]
