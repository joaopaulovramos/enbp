# Generated by Django 3.2.10 on 2023-04-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='horassemanais',
            name='submetida',
            field=models.BooleanField(default=False),
        ),
    ]
