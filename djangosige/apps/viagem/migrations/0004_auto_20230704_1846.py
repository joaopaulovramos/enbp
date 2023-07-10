# Generated by Django 3.2.10 on 2023-07-04 21:46

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viagem', '0003_alter_viagemmodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='viagemmodel',
            name='recusado_dus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='viagemmodel',
            name='recusado_sup',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='arquivos',
            name='cotacao',
            field=models.DecimalField(decimal_places=2, max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='arquivos',
            name='valor_pago',
            field=models.DecimalField(decimal_places=2, max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='arquivos',
            name='valor_pago_reais',
            field=models.DecimalField(decimal_places=2, max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]