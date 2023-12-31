# Generated by Django 3.2.10 on 2023-06-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_delete_exemplo'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='codigo_legado',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='data_sit_cadastral',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='forma_tributacao',
            field=models.CharField(blank=True, choices=[('1', 'Lucro Real'), ('2', 'Lucro Real/Arbitrado'), ('3', 'Lucro Presumido/Real'), ('4', 'Lucro Presumido/Real/Arbitrado'), ('5', 'Lucro Presumido'), ('6', 'Lucro Arbitrado'), ('7', 'Lucro Presumido/Arbitrado'), ('8', 'Imune do IRPJ'), ('9', 'Isenta do IRPJ')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='inativo',
            field=models.CharField(blank=True, choices=[('1', 'SIM'), ('0', 'NÃO')], default=1, max_length=1),
        ),
        migrations.AddField(
            model_name='empresa',
            name='indi_ini_periodo',
            field=models.CharField(blank=True, choices=[('0', '0 - Regular (Início no primeiro dia do ano)'), ('1', '1 - Abertura (Início de atividades no ano-calendário)'), ('2', '2 - Resultante de cisão/fusão ou remanescente de cisão, ou realizou incorporação'), ('3', '3 - Resultante de Mudança de Qualificação da Pessoa Jurídica'), ('4', '4 - Início de obrigatoriedade da entrega no curso do ano calendário')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='indi_sit_especial',
            field=models.CharField(blank=True, choices=[('0', '0 - Normal (Sem ocorrência de situação especial ou evento)'), ('1', '1 - Extinção'), ('2', '2 - Fusão'), ('3', '3 - Incorporação \\ Incorporada'), ('4', '4 - Incorporação \\ Incorporadora'), ('5', '5 - Cisão Total'), ('6', '6 - Cisão Parcial'), ('7', '7 - Mudança de Qualificação da Pessoa Jurídica'), ('8', '8 - Desenquadramento de Imune/Isenta'), ('9', '9 - Inclusão no Simples Nacional')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='ini_atividades',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='qualificacao',
            field=models.CharField(blank=True, choices=[('001', '001 - Pessoa Jurídica (e-CNPJ ou e-PJ)'), ('203', '203 - Diretor'), ('204', '204 - Conselheiro de Administração'), ('205', '205 - Administrador'), ('206', '206 - Administrador do Grupo'), ('207', '207 - Administrador de Sociedade Filiada'), ('220', '220 - Administrador Judicial – Pessoa Física'), ('222', '222 - Administrador Judicial – Pessoa Jurídica - Profissional Responsável'), ('223', '223 - Administrador Judicial/Gestor'), ('226', '226 - Gestor Judicial'), ('309', '309 - Procurador'), ('312', '312 - Inventariante'), ('313', '313 - Liquidante'), ('315', '315 - Interventor'), ('401', '401 - Titular – Pessoa Física - EIRELI'), ('801', '801 - Empresário'), ('900', '900 - Contador/Contabilista'), ('940', '940 - Auditor Independente'), ('999', '999 - Outros')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='sit_cadastral',
            field=models.CharField(blank=True, choices=[('1', 'Ativa'), ('2', 'Suspensa'), ('3', 'Inapta'), ('4', 'Baixada'), ('5', 'Nula'), ('6', 'Inativa')], max_length=2, null=True),
        ),
    ]
