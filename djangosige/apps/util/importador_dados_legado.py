import copy
import datetime
import re
from decimal import Decimal
from sys import stdout
from django.conf import settings
from djangosige.apps.cadastro.models import Cliente, PessoaFisica, PessoaJuridica, Endereco, Telefone, Fornecedor


class ImportadorLegado:
    def get_connection(self):
        """Conexão com SQL Server"""
        import pymssql

        return pymssql.connect(
            host=settings.LEGADO['DATABASE_HOST'],
            user=settings.LEGADO['DATABASE_USER'],
            password=settings.LEGADO['DATABASE_PASSWORD'],
            database=settings.LEGADO['DATABASE_NAME'],
            as_dict=True,
        )

    def clean_data(self, row):
        rcliente = {
            'id_legado': row['id_legado'],
            'numero_pessoa': row['nr_cpfcnpj'],
            'numero_pessoa_clean': re.sub('[./-]', '', row['nr_cpfcnpj']),
            'nome': row['ds_entidade'],
            'nome_razao_social': row['ds_entidade'],
            'nome_fantasia': row['ds_fantasia'],
            'inscricao_estadual': row['inscricao_estadual'],
            'classificacao': row['cd_classificacao'],
            'ddd_telefone': row['nr_ddd'],
            'numero_telefone': row['nr_telefone'],
            'endereco_logradouro': row['ds_endereco'],
            'endereco_bairro': row['ds_bairro'],
            'endereco_numero': row['nr_numero'],
            'endereco_complemento': row['ds_complemento'],
            'endereco_cep': row['nr_cep'],
            'endereco_cidade': row['ds_cidade'],
            'endereco_uf': row['ds_uf'],
        }

        return rcliente

    def importar_pessoa(self, rcliente, pessoa):
        pessoa.nome_razao_social = rcliente['nome_razao_social']
        # cliente.indicador_ie = rcliente['inscricao_estadual']

        # PJ
        pessoa.tipo_pessoa = 'PJ'
        info_cliente = PessoaJuridica()
        info_cliente.nome_fantasia = rcliente['nome_fantasia']
        info_cliente.cnpj = rcliente['numero_pessoa']
        # info_cliente.suframa = rcliente['suframa']
        info_cliente.inscricao_estadual = rcliente['inscricao_estadual']

        ender_cliente = Endereco()

        ender_cliente.logradouro = rcliente['endereco_logradouro']
        ender_cliente.numero = rcliente['endereco_numero']
        ender_cliente.bairro = rcliente['endereco_bairro']
        ender_cliente.complemento = rcliente['endereco_complemento']
        # ender_cliente.pais =
        # ender_cliente.cpais =
        ender_cliente.municipio = rcliente['endereco_cidade']
        # ender_cliente.cmun =
        ender_cliente.cep = rcliente['endereco_cep']
        ender_cliente.uf = rcliente['endereco_uf']

        pessoa.save()
        info_cliente.pessoa_id = pessoa
        info_cliente.save()
        ender_cliente.pessoa_end = pessoa
        ender_cliente.save()
        pessoa.endereco_padrao = ender_cliente
        if rcliente['numero_telefone']:
            tel_cliente = Telefone()
            tel_cliente.telefone = rcliente['ddd_telefone'] + rcliente['numero_telefone']
            tel_cliente.pessoa_tel = pessoa
            tel_cliente.save()
            pessoa.telefone_padrao = tel_cliente

    def importar_clientes(self, verbose=True):
        sql = """
            Select et.cd_entidade as id_legado, 
            et.nr_cpfcnpj, et.nr_ie as inscricao_estadual, et.cd_classificacao, et.dt_abertura,
            et.ds_entidade, et.ds_fantasia, 
            et.nr_ddd, et.nr_telefone,
            et.ds_endereco, et.ds_bairro, et.nr_cep, et.nr_numero, et.ds_complemento, cid.ds_cidade, cid.ds_uf
            from tbl_entidades et 
            left join TBL_ENDERECO_CIDADES cid on cid.CD_CIDADE = et.CD_CIDADE
            where X_CLIENTE = 1 and X_ATIVO = 1;
            """
        cur = self.get_connection().cursor()
        cur.execute(sql)

        row = cur.fetchone()
        while row:
            rcliente = self.clean_data(row)

            # CNPJ
            if len(rcliente['numero_pessoa_clean']) == 14:
                clientepj = PessoaJuridica.objects.filter(cnpj=rcliente['numero_pessoa'])
                if not clientepj.exists():
                    cliente = Cliente()
                    self.importar_pessoa(rcliente, cliente)
                    cliente.save()
            # TODO: Importar cliente PF
            row = cur.fetchone()

        cur.close()
        if verbose:
            stdout.write("\rImportando clientes: 100%\r\n")

    def importar_fornecedores(self, verbose=True):
        sql = """
            Select et.cd_entidade as id_legado, 
            et.nr_cpfcnpj, et.nr_ie as inscricao_estadual, et.cd_classificacao, et.dt_abertura,
            et.ds_entidade, et.ds_fantasia, 
            et.nr_ddd, et.nr_telefone,
            et.ds_endereco, et.ds_bairro, et.nr_cep, et.nr_numero, et.ds_complemento, cid.ds_cidade, cid.ds_uf
            from tbl_entidades et 
            left join TBL_ENDERECO_CIDADES cid on cid.CD_CIDADE = et.CD_CIDADE
            where X_FORNECEDOR = 1 and X_ATIVO = 1;
            """
        cur = self.get_connection().cursor()
        cur.execute(sql)

        row = cur.fetchone()
        while row:
            rcliente = self.clean_data(row)

            # CNPJ
            if len(rcliente['numero_pessoa_clean']) == 14:
                clientepj = PessoaJuridica.objects.filter(cnpj=rcliente['numero_pessoa'])
                if not clientepj.exists():
                    fornecedor = Fornecedor()
                    self.importar_pessoa(rcliente, fornecedor)
                    fornecedor.save()
            # TODO: Importar fornecedor PF
            row = cur.fetchone()

        cur.close()
        if verbose:
            stdout.write("\rImportando fornecedor: 100%\r\n")