# Generated by Django 3.2.10 on 2023-07-25 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('janela_unica', '0004_alter_documentounicofinanceiro_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentounicofinanceiro',
            name='tipo_arquivo',
            field=models.CharField(blank=True, choices=[('0', 'Nota Fiscal (NF-e)'), ('1', 'DANFE'), ('2', 'Boleto'), ('3', 'Comprovante de Pagamento'), ('9', 'Outros')], max_length=1, null=True),
        ),
    ]
