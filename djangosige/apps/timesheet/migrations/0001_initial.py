# Generated by Django 3.2.10 on 2023-08-18 20:45

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('norli_projeto', '0005_alter_exemplomodel_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='PercentualDiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('percentual', models.DecimalField(decimal_places=2, max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.01')), django.core.validators.MaxValueValidator(Decimal('100.00'))])),
                ('observacao', models.CharField(blank=True, max_length=500, null=True)),
                ('situacao', models.IntegerField(default=0)),
                ('motivo_reprovacao', models.CharField(blank=True, max_length=500, null=True)),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projeto_timesheet', to='norli_projeto.exemplomodel')),
                ('solicitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timesheet_diaria_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Timesheet - Percentual',
                'permissions': (('aprovar_horas', 'Pode aprovar lançamento de horas'),),
            },
        ),
        migrations.CreateModel(
            name='OpiniaoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo', models.CharField(choices=[('1', 'Dúvida'), ('2', 'Sugestão/Opinião'), ('3', 'Elogio'), ('4', 'Crítica'), ('5', 'Reportar um problema')], default='2', max_length=1)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('opiniao', models.CharField(max_length=500)),
                ('rating', models.IntegerField(blank=True, default=0)),
                ('anexo', models.FileField(blank=True, null=True, upload_to='files/')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timesheet_opiniao_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Timesheet - Opiniões',
                'permissions': (('analisar_opinioes', 'Vizualiza todas as opiniões'),),
            },
        ),
        migrations.CreateModel(
            name='HorasSemanais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hr_seg', models.CharField(blank=True, max_length=200)),
                ('hr_ter', models.CharField(blank=True, max_length=200)),
                ('hr_qua', models.CharField(blank=True, max_length=200)),
                ('hr_qui', models.CharField(blank=True, max_length=200)),
                ('hr_sex', models.CharField(blank=True, max_length=200)),
                ('hr_sab', models.CharField(blank=True, max_length=200)),
                ('hr_dom', models.CharField(blank=True, max_length=200)),
                ('semanas', models.CharField(choices=[('30/07/2023 - 05/08/2023', '30/07/2023 - 05/08/2023'), ('06/08/2023 - 12/08/2023', '06/08/2023 - 12/08/2023'), ('13/08/2023 - 19/08/2023', '13/08/2023 - 19/08/2023'), ('20/08/2023 - 26/08/2023', '20/08/2023 - 26/08/2023'), ('27/08/2023 - 02/09/2023', '27/08/2023 - 02/09/2023')], max_length=200)),
                ('situacao', models.IntegerField(default=0)),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificados_user', to='norli_projeto.exemplomodel')),
                ('solicitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timesheet_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=500)),
                ('valor', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=15)),
                ('file', models.FileField(upload_to='files/')),
                ('situacao', models.CharField(blank=True, choices=[('3', 'REPROVADA'), ('2', 'APROVADA'), ('1', 'SUBMETIDA'), ('0', 'NÃO SUBMETIDA')], default='0', max_length=1, null=True)),
                ('data', models.DateField()),
                ('projeto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projeto_gastos', to='norli_projeto.exemplomodel')),
                ('solicitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gastos_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
