# Generated by Django 3.2.10 on 2023-06-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarroModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('placa', models.CharField(max_length=200)),
                ('chaci', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Exemplo Carro',
            },
        ),
        migrations.CreateModel(
            name='ExemploModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('apelido', models.CharField(max_length=200)),
            ],
        ),
    ]
