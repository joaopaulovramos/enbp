# Generated by Django 3.2.10 on 2023-06-20 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0008_auto_20230620_1701'),
        ('norli_projeto', '0002_auto_20230417_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filialmodel',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='filial_empresa', to='cadastro.empresa'),
        ),
    ]
