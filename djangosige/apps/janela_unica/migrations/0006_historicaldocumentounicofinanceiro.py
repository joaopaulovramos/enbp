# Generated by Django 3.2.10 on 2023-07-26 00:20

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_cpf_cnpj.fields
import django_fsm
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('norli_projeto', '0003_alter_filialmodel_empresa'),
        ('financeiro', '0004_auto_20221115_1505'),
        ('cadastro', '0014_departamentomodel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('janela_unica', '0005_alter_documentounicofinanceiro_tipo_arquivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalDocumentoUnicoFinanceiro',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('arquivo', models.TextField(blank=True, max_length=100, null=True)),
                ('situacao', django_fsm.FSMField(choices=[('Edição Responsável', 'Edição Responsável'), ('Aguardando avaliação Gerência', 'Aguardando avaliação Gerência'), ('Aguardando avaliação Superintendencia', 'Aguardando avaliação Superintendencia'), ('Aguardando avaliação Diretoria', 'Aguardando avaliação Diretoria'), ('Aguardando Análise Fiscal', 'Aguardando Análise Fiscal'), ('Aguardando Análise Financeira', 'Aguardando Análise Financeira'), ('Reprovado', 'Reprovado'), ('Finalizado', 'Finalizado'), ('Cancelado', 'Cancelado'), ('Aprovado', 'Aprovado')], default='Edição Responsável', max_length=50, protected=True, verbose_name='Situação')),
                ('data_inclusao', models.DateTimeField(blank=True, editable=False)),
                ('data_finalizacao', models.DateTimeField(blank=True, null=True)),
                ('tipo_arquivo', models.CharField(blank=True, choices=[('0', 'Nota Fiscal (NF-e)'), ('1', 'DANFE'), ('2', 'Boleto'), ('3', 'Comprovante de Pagamento'), ('9', 'Outros')], max_length=1, null=True)),
                ('tipo_anexo', models.CharField(blank=True, choices=[('0', '.xml'), ('1', '.pdf'), ('2', '.doc'), ('3', 'Outros')], max_length=1, null=True)),
                ('numero', models.CharField(blank=True, max_length=9, null=True)),
                ('chave', models.CharField(blank=True, max_length=44, null=True)),
                ('mod', models.CharField(blank=True, choices=[('55', 'NF-e (55)'), ('65', 'NFC-e (65)')], max_length=2, null=True)),
                ('serie', models.CharField(blank=True, max_length=3, null=True)),
                ('cnpj', django_cpf_cnpj.fields.CNPJField(blank=True, max_length=18, null=True)),
                ('data_emissao', models.DateField(blank=True, null=True)),
                ('cfop', models.CharField(blank=True, max_length=5, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('rateio', models.BooleanField(blank=True, null=True)),
                ('observacoes', models.CharField(blank=True, max_length=1055, null=True)),
                ('banco', models.CharField(blank=True, choices=[('001', '001 - BANCO DO BRASIL S.A.'), ('003', '003 - BANCO DA AMAZONIA S.A.'), ('004', '004 - BANCO DO NORDESTE DO BRASIL S.A.'), ('012', '012 - BANCO STANDARD DE INVESTIMENTOS S.A.'), ('014', '014 - NATIXIS BRASIL S.A. BANCO MÚLTIPLO'), ('019', '019 - BANCO AZTECA DO BRASIL S.A.'), ('021', '021 - BANESTES S.A. BANCO DO ESTADO DO ESPIRITO SANTO'), ('024', '024 - BANCO DE PERNAMBUCO S.A. - BANDEPE'), ('025', '025 - BANCO ALFA S.A.'), ('029', '029 - BANCO BANERJ S.A.'), ('031', '031 - BANCO BEG S.A.'), ('033', '033 - BANCO SANTANDER (BRASIL) S.A.'), ('036', '036 - BANCO BRADESCO BBI S.A.'), ('037', '037 - BANCO DO ESTADO DO PARÁ S.A.'), ('040', '040 - BANCO CARGILL S.A.'), ('041', '041 - BANCO DO ESTADO DO RIO GRANDE DO SUL S.A.'), ('044', '044 - BANCO BVA S.A.'), ('045', '045 - BANCO OPPORTUNITY S.A.'), ('047', '047 - BANCO DO ESTADO DE SERGIPE S.A.'), ('062', '062 - HIPERCARD BANCO MÚLTIPLO S.A.'), ('063', '063 - BANCO IBI S.A. - BANCO MÚLTIPLO'), ('065', '065 - BANCO LEMON S.A.'), ('066', '066 - BANCO MORGAN STANLEY S.A.'), ('069', '069 - BPN BRASIL BANCO MÚLTIPLO S.A.'), ('070', '070 - BRB - BANCO DE BRASILIA S.A.'), ('072', '072 - BANCO RURAL MAIS S.A.'), ('073', '073 - BB BANCO POPULAR DO BRASIL S.A.'), ('074', '074 - BANCO J. SAFRA S.A.'), ('075', '075 - BANCO CR2 S/A'), ('076', '076 - BANCO KDB DO BRASIL S.A.'), ('077', '077 - BANCO INTERMEDIUM S/A'), ('078', '078 - BES INVESTIMENTO DO BRASIL S.A. - BANCO DE INVESTIMENTO'), ('079', '079 - JBS BANCO S/A'), ('081', '081 - CONCÓRDIA BANCO S.A.'), ('082', '082 - BANCO TOPÁZIO S.A.'), ('083', '083 - BANCO DA CHINA BRASIL S.A'), ('096', '096 - BANCO BM&F DE SERVIÇOS DE LIQUIDAÇÃO E CUSTÓDIA S.A.'), ('104', '104 - CAIXA ECONOMICA FEDERAL'), ('107', '107 - BANCO BBM S/A'), ('151', '151 - BANCO NOSSA CAIXA S.A.'), ('184', '184 - BANCO ITAÚ BBA S.A.'), ('204', '204 - BANCO BRADESCO CARTÕES S.A.'), ('208', '208 - BANCO UBS PACTUAL S.A.'), ('212', '212 - BANCO MATONE S.A.'), ('213', '213 - BANCO ARBI S.A.'), ('214', '214 - BANCO DIBENS S.A.'), ('215', '215 - BANCO COMERCIAL E DE INVESTIMENTO SUDAMERIS S.A.'), ('217', '217 - BANCO JOHN DEERE S.A.'), ('218', '218 - BANCO BONSUCESSO S.A.'), ('222', '222 - BANCO CALYON BRASIL S.A.'), ('224', '224 - BANCO FIBRA S.A.'), ('225', '225 - BANCO BRASCAN S.A.'), ('229', '229 - BANCO CRUZEIRO DO SUL S.A.'), ('230', '230 - UNICARD BANCO MÚLTIPLO S.A.'), ('233', '233 - BANCO GE CAPITAL S.A.'), ('237', '237 - BANCO BRADESCO S.A.'), ('241', '241 - BANCO CLASSICO S.A.'), ('243', '243 - BANCO MÁXIMA S.A.'), ('246', '246 - BANCO ABC BRASIL S.A.'), ('248', '248 - BANCO BOAVISTA INTERATLANTICO S.A.'), ('249', '249 - BANCO INVESTCRED UNIBANCO S.A.'), ('250', '250 - BANCO SCHAHIN S.A.'), ('254', '254 - PARANÁ BANCO S.A.'), ('260', '260 - NU PAGAMENTOS S.A.'), ('263', '263 - BANCO CACIQUE S.A.'), ('265', '265 - BANCO FATOR S.A.'), ('266', '266 - BANCO CEDULA S.A.'), ('300', '300 - BANCO DE LA NACION ARGENTINA'), ('318', '318 - BANCO BMG S.A.'), ('320', '320 - BANCO INDUSTRIAL E COMERCIAL S.A.'), ('341', '341 - BANCO ITAÚ S.A.'), ('366', '366 - BANCO SOCIETE GENERALE BRASIL S.A.'), ('370', '370 - BANCO WESTLB DO BRASIL S.A.'), ('376', '376 - BANCO J.P. MORGAN S.A.'), ('389', '389 - BANCO MERCANTIL DO BRASIL S.A.'), ('394', '394 - BANCO FINASA BMC S.A.'), ('399', '399 - HSBC BANK BRASIL S.A. - BANCO MULTIPLO'), ('409', '409 - UNIBANCO-UNIAO DE BANCOS BRASILEIROS S.A.'), ('412', '412 - BANCO CAPITAL S.A.'), ('422', '422 - BANCO SAFRA S.A.'), ('453', '453 - BANCO RURAL S.A.'), ('456', '456 - BANCO DE TOKYO-MITSUBISHI UFJ BRASIL S/A'), ('464', '464 - BANCO SUMITOMO MITSUI BRASILEIRO S.A.'), ('473', '473 - BANCO CAIXA GERAL - BRASIL S.A.'), ('477', '477 - CITIBANK N.A.'), ('479', '479 - BANCO ITAUBANK S.A.'), ('487', '487 - DEUTSCHE BANK S.A. - BANCO ALEMAO'), ('488', '488 - JPMORGAN CHASE BANK, NATIONAL ASSOCIATION'), ('492', '492 - ING BANK N.V.'), ('494', '494 - BANCO DE LA REPUBLICA ORIENTAL DEL URUGUAY'), ('495', '495 - BANCO DE LA PROVINCIA DE BUENOS AIRES'), ('505', '505 - BANCO CREDIT SUISSE (BRASIL) S.A.'), ('600', '600 - BANCO LUSO BRASILEIRO S.A.'), ('604', '604 - BANCO INDUSTRIAL DO BRASIL S.A.'), ('610', '610 - BANCO VR S.A.'), ('611', '611 - BANCO PAULISTA S.A.'), ('612', '612 - BANCO GUANABARA S.A.'), ('613', '613 - BANCO PECUNIA S.A.'), ('623', '623 - BANCO PANAMERICANO S.A.'), ('626', '626 - BANCO FICSA S.A.'), ('630', '630 - BANCO INTERCAP S.A.'), ('633', '633 - BANCO RENDIMENTO S.A.'), ('634', '634 - BANCO TRIANGULO S.A.'), ('637', '637 - BANCO SOFISA S.A.'), ('638', '638 - BANCO PROSPER S.A.'), ('641', '641 - BANCO ALVORADA S.A.'), ('643', '643 - BANCO PINE S.A.'), ('652', '652 - ITAÚ UNIBANCO BANCO MÚLTIPLO S.A.'), ('653', '653 - BANCO INDUSVAL S.A.'), ('654', '654 - BANCO A.J. RENNER S.A.'), ('655', '655 - BANCO VOTORANTIM S.A.'), ('707', '707 - BANCO DAYCOVAL S.A.'), ('719', '719 - BANIF - BANCO INTERNACIONAL DO FUNCHAL (BRASIL), S.A.'), ('721', '721 - BANCO CREDIBEL S.A.'), ('734', '734 - BANCO GERDAU S.A'), ('735', '735 - BANCO POTTENCIAL S.A.'), ('738', '738 - BANCO MORADA S.A'), ('739', '739 - BANCO BGN S.A.'), ('740', '740 - BANCO BARCLAYS S.A.'), ('741', '741 - BANCO RIBEIRAO PRETO S.A.'), ('743', '743 - BANCO SEMEAR S.A.'), ('745', '745 - BANCO CITIBANK S.A.'), ('746', '746 - BANCO MODAL S.A.'), ('747', '747 - BANCO RABOBANK INTERNATIONAL BRASIL S.A.'), ('748', '748 - BANCO COOPERATIVO SICREDI S.A.'), ('749', '749 - BANCO SIMPLES S.A.'), ('751', '751 - DRESDNER BANK BRASIL S.A. BANCO MULTIPLO'), ('752', '752 - BANCO BNP PARIBAS BRASIL S.A.'), ('753', '753 - NBC BANK BRASIL S. A. - BANCO MÚLTIPLO'), ('756', '756 - BANCO COOPERATIVO DO BRASIL S.A. - BANCOOB'), ('757', '757 - BANCO KEB DO BRASIL S.A.')], max_length=3, null=True)),
                ('agencia', models.CharField(blank=True, max_length=8, null=True)),
                ('conta', models.CharField(blank=True, max_length=32, null=True)),
                ('digito', models.CharField(blank=True, max_length=8, null=True)),
                ('possui_parcelamento', models.BooleanField(blank=True, null=True)),
                ('possui_contrato', models.BooleanField(blank=True, null=True)),
                ('extra_orcamentaria', models.BooleanField(blank=True, null=True)),
                ('antecipacao_pagamento', models.BooleanField(blank=True, null=True)),
                ('pagamento_boleto', models.BooleanField(blank=True, null=True)),
                ('aprovado_gerencia', models.BooleanField(blank=True, null=True)),
                ('observacao_gerencia', models.CharField(blank=True, max_length=1055, null=True)),
                ('aprovado_superintendencia', models.BooleanField(blank=True, null=True)),
                ('observacao_superintendencia', models.CharField(blank=True, max_length=1055, null=True)),
                ('aprovado_diretoria', models.BooleanField(blank=True, null=True)),
                ('observacao_diretoria', models.CharField(blank=True, max_length=1055, null=True)),
                ('aprovado_analise_financeira', models.BooleanField(blank=True, null=True)),
                ('observacao_analise_financeira', models.CharField(blank=True, max_length=1055, null=True)),
                ('comprovante_lancamento', models.TextField(blank=True, max_length=100, null=True)),
                ('aprovado_analise_fiscal', models.BooleanField(blank=True, null=True)),
                ('observacao_analise_fiscal', models.CharField(blank=True, max_length=1055, null=True)),
                ('comprovante_pagamento', models.TextField(blank=True, max_length=100, null=True)),
                ('descricao', models.CharField(blank=True, max_length=1055, null=True)),
                ('usuario_lancamento', models.CharField(blank=True, max_length=255, null=True)),
                ('data_lancamento', models.DateField(blank=True, null=True)),
                ('numero_lancamento', models.CharField(blank=True, max_length=255, null=True)),
                ('pagamento_realizado', models.BooleanField(blank=True, null=True)),
                ('observacao_pagamento', models.CharField(blank=True, max_length=1055, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('fornecedor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='cadastro.pessoa')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('plano_conta', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='financeiro.planocontasgrupo')),
                ('projeto', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='norli_projeto.exemplomodel')),
                ('responsavel', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_analise_financeira', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_analise_fiscal', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_diretoria', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_gerencia', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_superintencencia', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Documento Janela Única',
                'verbose_name_plural': 'historical Documento Janela Únicas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
