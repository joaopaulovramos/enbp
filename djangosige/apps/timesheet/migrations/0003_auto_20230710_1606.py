# Generated by Django 3.2.10 on 2023-07-10 19:06

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('norli_projeto', '0003_alter_filialmodel_empresa'),
        ('timesheet', '0002_auto_20230704_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastos',
            name='projeto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projeto_gastos', to='norli_projeto.exemplomodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gastos',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=15),
        ),
    ]