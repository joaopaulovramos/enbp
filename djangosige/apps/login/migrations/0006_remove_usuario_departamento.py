# Generated by Django 3.2.10 on 2023-07-20 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_usuario_departamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='departamento',
        ),
    ]
