# Generated by Django 3.2.10 on 2023-04-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0002_horassemanais_submetida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horassemanais',
            name='hr_dom',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='horassemanais',
            name='hr_qua',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='horassemanais',
            name='hr_qui',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='horassemanais',
            name='hr_sab',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='horassemanais',
            name='hr_seg',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='horassemanais',
            name='hr_sex',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='horassemanais',
            name='hr_ter',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
