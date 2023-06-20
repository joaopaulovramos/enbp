# Generated by Django 3.2.10 on 2023-06-20 19:58

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20230614_1213'),
        ('viagem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalidadeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=400)),
            ],
        ),
        migrations.AlterModelOptions(
            name='viagemmodel',
            options={'permissions': (('solicitar_viagens', 'Pode solicitar viagens'), ('autorizar_viagens_sup', 'Pode autorizar viagens - Superintendente'), ('autorizar_viagens_dus', 'Pode autorizar viagens - Diretor de Unidade de Serviço'), ('homologar_viagens', 'Pode homologar viagens'), ('cadastrar_item_viagens', 'Cadastrar Items de Viagem')), 'verbose_name': 'Viagens'},
        ),
        migrations.RenameField(
            model_name='viagemmodel',
            old_name='autorizada',
            new_name='autorizada_dus',
        ),
        migrations.AddField(
            model_name='arquivos',
            name='cotacao',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AddField(
            model_name='arquivos',
            name='data_evento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='arquivos',
            name='moeda',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='arquivos_moeda', to='viagem.moedamodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arquivos',
            name='numero_item',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arquivos',
            name='pagamento',
            field=models.CharField(blank=True, choices=[('RECURSOS DA EMPRESA', 'Recursos da Empresa'), ('RECURSOS PRÓPRIOS', 'Recursos Próprios')], max_length=50),
        ),
        migrations.AddField(
            model_name='arquivos',
            name='tipo_despesa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='arquivos_despesa', to='viagem.tipodedespesamodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arquivos',
            name='valor_pago',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AddField(
            model_name='arquivos',
            name='valor_pago_reais',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AddField(
            model_name='viagemmodel',
            name='autorizada_sup',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='viagemmodel',
            name='motivo_reprovacao_pc',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='viagemmodel',
            name='qtd_diarias',
            field=models.FloatField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viagemmodel',
            name='valor_diaria',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=16, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
        migrations.AddField(
            model_name='viagemmodel',
            name='valor_total_diarias',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=16, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
        migrations.AlterField(
            model_name='viagemmodel',
            name='acompanhante',
            field=models.ForeignKey(blank=True, limit_choices_to={'grupo_funcional': '0'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='viagem_acompanhante', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='viagemmodel',
            name='dada_fim',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='viagemmodel',
            name='pagamento',
            field=models.CharField(blank=True, choices=[('RECURSOS DA EMPRESA', 'Recursos da Empresa'), ('RECURSOS PRÓPRIOS', 'Recursos Próprios')], max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='TabelaDiariaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo_funcional', models.CharField(choices=[('0', 'A - DIRETORES e CONSELHEIROS'), ('1', 'B – PROFISSIONAIS')], default='1', max_length=1)),
                ('valor_diaria', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=16, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('localidade_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diaria_localidade', to='viagem.localidademodel')),
                ('moeda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diaria_moeda', to='viagem.moedamodel')),
            ],
        ),
        migrations.AddField(
            model_name='viagemmodel',
            name='localidade_destino',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='viagem_localidade_destino', to='viagem.localidademodel'),
            preserve_default=False,
        ),
    ]