# Generated by Django 3.2.10 on 2023-08-14 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opiniao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opiniaomodel',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
