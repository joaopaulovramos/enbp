# Generated by Django 3.2.10 on 2022-11-15 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiscal', '0003_auto_20170915_0904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='configuracaonotafiscal',
            options={'default_permissions': (), 'permissions': (('configurar_nfe', 'Pode modificar configuração de NF-e'),), 'verbose_name': 'Configuração NF-e'},
        ),
        migrations.AlterModelOptions(
            name='grupofiscal',
            options={'verbose_name': 'Grupo Fiscal'},
        ),
        migrations.AlterModelOptions(
            name='naturezaoperacao',
            options={'verbose_name': 'Natureza da Operação'},
        ),
        migrations.AlterModelOptions(
            name='notafiscalentrada',
            options={'verbose_name': 'Nota Fiscal de Fornecedor'},
        ),
        migrations.AlterModelOptions(
            name='notafiscalsaida',
            options={'permissions': (('emitir_notafiscal', 'Pode emitir notas fiscais'), ('cancelar_notafiscal', 'Pode cancelar notas fiscais'), ('gerar_danfe', 'Pode gerar DANFE/DANFCE'), ('consultar_cadastro', 'Pode consultar cadastro no SEFAZ'), ('inutilizar_notafiscal', 'Pode inutilizar notas fiscais'), ('consultar_notafiscal', 'Pode consultar notas fiscais'), ('baixar_notafiscal', 'Pode baixar notas fiscais'), ('manifestacao_destinatario', 'Pode efetuar manifestação do destinatário')), 'verbose_name': 'Nota Fiscal'},
        ),
    ]
