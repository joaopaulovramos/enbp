# Generated by Django 3.2.10 on 2023-08-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0004_auto_20221115_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='lancamento',
            name='codigo_legado',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='planocontasgrupo',
            name='codigo',
            field=models.CharField(max_length=20),
        ),
    ]
