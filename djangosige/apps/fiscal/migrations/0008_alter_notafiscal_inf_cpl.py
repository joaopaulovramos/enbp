# Generated by Django 3.2.10 on 2023-08-17 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiscal', '0007_merge_20230816_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notafiscal',
            name='inf_cpl',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
    ]
