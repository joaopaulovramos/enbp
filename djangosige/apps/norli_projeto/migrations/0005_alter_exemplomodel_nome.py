# Generated by Django 3.2.10 on 2023-08-17 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('norli_projeto', '0004_alter_exemplomodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exemplomodel',
            name='nome',
            field=models.CharField(default='projeto', max_length=50, unique=True),
        ),
    ]
