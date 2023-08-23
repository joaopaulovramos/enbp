# Generated by Django 3.2.10 on 2023-08-21 02:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_fsm
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0016_merge_20230818_1651'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viagem', '0012_auto_20230818_1745'),
        ('login', '0007_usuario_departamento'),
        ('janela_unica', '0011_auto_20230818_1745'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentounicofinanceiro',
            options={'permissions': (('gerencia_documento_unico', 'Aprovar documentos janela única - Gerência'), ('superintendencia_documento_unico', 'Aprovar documentos janela única - Superintendencia'), ('diretoria_documento_unico', 'Aprovar documentos janela única - Diretoria'), ('analise_fiscal_documento_unico', 'Analise Fiscal'), ('analise_financeira_documento_unico', 'Analise Financeira'), ('processamento_financeiro_documento_unico', 'Processamento Financeiro'), ('analise_orcamentaria_documento_unico', 'Analise Orçamentária'), ('retorno_financeiro_documento_unico', 'Retorno financeiro')), 'verbose_name': 'Documento Janela Única'},
        ),
        migrations.AddField(
            model_name='avaliacaodocumentounico',
            name='data_avaliacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='detalhe_pagamento',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empresa_contrato', to='cadastro.empresa'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='forma_pagamento',
            field=models.CharField(choices=[('0', 'Boleto'), ('1', 'TED'), ('2', 'PIX'), ('9', 'Outros')], default='9', max_length=1),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='aprovado_analise_orcamentaria',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='aprovado_processamento_financeiro',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='aprovado_retorno_financeiro',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='comprovante_retorno',
            field=models.FileField(blank=True, null=True, upload_to='janela_unica/documentos/retorno'),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='conta_pagadora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conta_pagadora_documento_unico', to='cadastro.banco'),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='conta_recebedora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conta_recebedora_documento_unico', to='cadastro.banco'),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='cotacao',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='data_analise_fiscal',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='data_cotacao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='data_pagamento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='data_vencimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='descricacao_pagamento',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='descricao_pagamento',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='documento_remessa_pagamento',
            field=models.FileField(blank=True, null=True, upload_to='janela_unica/documentos/remessa'),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empresa_documento_unico', to='cadastro.empresa'),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='moeda_pagamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='moeda_pagamento_documento_unico', to='viagem.moedamodel'),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='observacao_analise_orcamentaria',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='observacao_processamento_financeiro',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='observacao_retorno_financeiro',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='usuario_analise_orcamentaria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documento_unico_usuario_analise_orcamentaria', to='login.usuario'),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='usuario_processamento_financeiro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documento_unico_usuario_processamento_financeiro', to='login.usuario'),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='usuario_retorno_financeiro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documento_unico_usuario_retorno_financiero', to='login.usuario'),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='valor_bruto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='valor_desconto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='valor_juros',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='valor_juros_mora',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='valor_multa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='documentounicofinanceiro',
            name='valor_outros',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='aprovado_analise_orcamentaria',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='aprovado_processamento_financeiro',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='aprovado_retorno_financeiro',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='comprovante_retorno',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='conta_pagadora',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='cadastro.banco'),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='conta_recebedora',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='cadastro.banco'),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='cotacao',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='data_analise_fiscal',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='data_cotacao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='data_pagamento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='data_vencimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='descricacao_pagamento',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='descricao_pagamento',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='documento_remessa_pagamento',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='empresa',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='cadastro.empresa'),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='moeda_pagamento',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='viagem.moedamodel'),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='observacao_analise_orcamentaria',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='observacao_processamento_financeiro',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='observacao_retorno_financeiro',
            field=models.CharField(blank=True, max_length=1055, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='usuario_analise_orcamentaria',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='login.usuario'),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='usuario_processamento_financeiro',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='login.usuario'),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='usuario_retorno_financeiro',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='login.usuario'),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='valor_bruto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='valor_desconto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='valor_juros',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='valor_juros_mora',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='valor_multa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='historicaldocumentounicofinanceiro',
            name='valor_outros',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='aprovadorcontrato',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aprovador_usuario_contrato', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='avaliacaodocumentounico',
            name='usuario_avaliador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documento_unico_usuario_avaliador', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='documentomodel',
            name='dono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dono_doc', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='documentounicofinanceiro',
            name='responsavel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsavel_documento_unico', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='documentounicofinanceiro',
            name='situacao',
            field=django_fsm.FSMField(choices=[('Edição Responsável', 'Edição Responsável'), ('Aguardando avaliação', 'Aguardando avaliação'), ('Aguardando Análise Orçamentária', 'Aguardando Análise Orçamentária'), ('Aguardando Análise Fiscal', 'Aguardando Análise Fiscal'), ('Aguardando Análise Financeira', 'Aguardando Análise Financeira'), ('Aguardando Processamento (Taticca)', 'Aguardando Processamento (Taticca)'), ('Aguardando Retorno Financeiro', 'Aguardando Retorno Financeiro'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado'), ('Aprovado', 'Aprovado'), ('Devolvido (Responsável)', 'Devolvido (Responsável)')], default='Edição Responsável', max_length=50, verbose_name='Situação'),
        ),
        migrations.AlterField(
            model_name='documentounicofinanceiro',
            name='usuario_analise_financeira',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documento_unico_usuario_analise_financeira', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='documentounicofinanceiro',
            name='usuario_analise_fiscal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documento_unico_usuario_analise_fiscal', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='documentounicofinanceiro',
            name='usuario_diretoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documento_unico_usuario_diretoria', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='documentounicofinanceiro',
            name='usuario_gerencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documento_unico_usuario_gerencia', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='documentounicofinanceiro',
            name='usuario_superintencencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documento_unico_usuario_superintendencia', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='documentounicofinanceiro',
            name='valor_liquido',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='historicaldocumentounicofinanceiro',
            name='responsavel',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='historicaldocumentounicofinanceiro',
            name='situacao',
            field=django_fsm.FSMField(choices=[('Edição Responsável', 'Edição Responsável'), ('Aguardando avaliação', 'Aguardando avaliação'), ('Aguardando Análise Orçamentária', 'Aguardando Análise Orçamentária'), ('Aguardando Análise Fiscal', 'Aguardando Análise Fiscal'), ('Aguardando Análise Financeira', 'Aguardando Análise Financeira'), ('Aguardando Processamento (Taticca)', 'Aguardando Processamento (Taticca)'), ('Aguardando Retorno Financeiro', 'Aguardando Retorno Financeiro'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado'), ('Aprovado', 'Aprovado'), ('Devolvido (Responsável)', 'Devolvido (Responsável)')], default='Edição Responsável', max_length=50, verbose_name='Situação'),
        ),
        migrations.AlterField(
            model_name='historicaldocumentounicofinanceiro',
            name='usuario_analise_financeira',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='historicaldocumentounicofinanceiro',
            name='usuario_analise_fiscal',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='historicaldocumentounicofinanceiro',
            name='usuario_diretoria',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='historicaldocumentounicofinanceiro',
            name='usuario_gerencia',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='historicaldocumentounicofinanceiro',
            name='usuario_superintencencia',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='historicaldocumentounicofinanceiro',
            name='valor_liquido',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='tramitacaomodel',
            name='user_enviado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_enviado', to='login.usuario'),
        ),
        migrations.AlterField(
            model_name='tramitacaomodel',
            name='user_recebido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_recebido', to='login.usuario'),
        ),
        migrations.CreateModel(
            name='HistoricalContrato',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_change_reason', models.TextField(null=True)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('arquivo', models.TextField(blank=True, max_length=100, null=True)),
                ('data_inclusao', models.DateTimeField(blank=True, editable=False)),
                ('data_validade', models.DateTimeField(blank=True, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('forma_pagamento', models.CharField(choices=[('0', 'Boleto'), ('1', 'TED'), ('2', 'PIX'), ('9', 'Outros')], default='9', max_length=1)),
                ('detalhe_pagamento', models.CharField(blank=True, max_length=1055, null=True)),
                ('situacao', django_fsm.FSMField(choices=[('Rascunho', 'Rascunho'), ('Em Execução', 'Em Execução'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado')], default='Rascunho', max_length=50, protected=True, verbose_name='Situação')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('empresa', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='cadastro.empresa')),
                ('fornecedor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='cadastro.pessoa')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('tipo_contrato', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='janela_unica.tipocontrato')),
            ],
            options={
                'verbose_name': 'historical Contrato',
                'verbose_name_plural': 'historical Contratos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]