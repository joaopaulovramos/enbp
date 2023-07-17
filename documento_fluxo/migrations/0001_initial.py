# Generated by Django 3.2.10 on 2023-07-16 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_alter_tag_slug'),
        ('viewflow', '0011_alter_task_created_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DistribuirDocumentoProcess',
            fields=[
            ],
            options={
                'verbose_name': 'Distribuir documento',
                'verbose_name_plural': 'Distribuição de documentos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('viewflow.process',),
        ),
        migrations.CreateModel(
            name='DistribuirDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('despacho', models.TextField(blank=True, null=True)),
                ('data_despacho', models.DateField(auto_now_add=True)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.document')),
                ('usuario_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
