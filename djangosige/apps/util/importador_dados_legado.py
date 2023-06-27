import copy
import datetime
import re
from decimal import Decimal
from sys import stdout

from django.conf import settings
from django.contrib.auth.models import User

from djangosige.apps.cadastro.models import (Cliente, Endereco, Fornecedor,
                                             PessoaFisica, PessoaJuridica,
                                             Telefone, Email)
from djangosige.apps.cadastro.models.transportadora import Transportadora
from djangosige.apps.financeiro.models.plano import TIPO_GRUPO_ESCOLHAS, PlanoContasGrupo, PlanoContasSubgrupo


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
            'email': row['ds_email'],
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
        if rcliente['endereco_cidade']:
            ender_cliente.municipio = str(rcliente['endereco_cidade']).title()
        # ender_cliente.cmun =
        ender_cliente.cep = rcliente['endereco_cep']
        ender_cliente.uf = rcliente['endereco_uf']

        pessoa.save()
        info_cliente.pessoa_id = pessoa
        info_cliente.save()
        ender_cliente.pessoa_end = pessoa
        ender_cliente.save()
        pessoa.endereco_padrao = ender_cliente
        if rcliente['email']:
            email_cliente = Email()
            email_cliente.email = rcliente['email']
            email_cliente.pessoa_email = pessoa
            email_cliente.save()
            pessoa.email_padrao = email_cliente
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
            et.nr_ddd, et.nr_telefone, ds_email,
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

    def importar_transportadoras(self, verbose=True):
        sql = """
            Select et.cd_entidade as id_legado, 
            et.nr_cpfcnpj, et.nr_ie as inscricao_estadual, et.cd_classificacao, et.dt_abertura,
            et.ds_entidade, et.ds_fantasia, 
            et.nr_ddd, et.nr_telefone, ds_email,
            et.ds_endereco, et.ds_bairro, et.nr_cep, et.nr_numero, et.ds_complemento, cid.ds_cidade, cid.ds_uf
            from tbl_entidades et 
            left join TBL_ENDERECO_CIDADES cid on cid.CD_CIDADE = et.CD_CIDADE
            where X_TRANSPORTADOR = 1 and X_ATIVO = 1;
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
                    transportadora = Transportadora()
                    self.importar_pessoa(rcliente, transportadora)
                    transportadora.save()
            # TODO: Importar fornecedor PF
            row = cur.fetchone()

        cur.close()
        if verbose:
            stdout.write("\rImportando transportadoras: 100%\r\n")

    def importar_fornecedores(self, verbose=True):
        sql = """
            Select et.cd_entidade as id_legado, 
            et.nr_cpfcnpj, et.nr_ie as inscricao_estadual, et.cd_classificacao, et.dt_abertura,
            et.ds_entidade, et.ds_fantasia, 
            et.nr_ddd, et.nr_telefone, ds_email,
            et.ds_endereco, et.ds_bairro, et.nr_cep, et.nr_numero, et.ds_complemento, cid.ds_cidade, cid.ds_uf
            from tbl_entidades et 
            left join TBL_ENDERECO_CIDADES cid on cid.CD_CIDADE = et.CD_CIDADE
            where (X_FORNECEDOR = 1 OR X_FORNECEDOR_DESPESA = 1) and X_ATIVO = 1;
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

    def importar_usuarios(self, verbose=True):
        sql = """
            Select u.ds_usuario as usuario, u.ds_login as login, u.ds_senha as senha, u.ds_email as email
            from TBL_USUARIOS u 
            where X_ATIVO = 1
            """
        cur = self.get_connection().cursor()
        cur.execute(sql)

        row = cur.fetchone()
        
        while row:
            rcliente = {
                'usuario': str(row['usuario']).title(),
                'login': str(row['login']).lower(),
                'senha': row['senha'],
                'email': row['email']
            }
            if not User.objects.filter(username=rcliente['login']).exists():
                user = User.objects.create_user(username=rcliente['login'], email=rcliente['email'], password=rcliente['senha'])
                user.first_name = rcliente['usuario']
                user.save()
            row = cur.fetchone()

        cur.close()
        if verbose:
            stdout.write("\rImportando usuarios: 100%\r\n")

    def importar_lancamentos(self, verbose=True):
        # Criar lancamento com data futura (sem movimentos)
        data_pagamento_futura = datetime.strptime(
            '01/01/2099', "%d/%m/%Y").date()
        obj = Entrada.objects.create(status='0', movimentar_caixa=False, valor_total='120.00', valor_liquido='120.00', data_pagamento=data_pagamento_futura)

    def importar_contas_lancamentos(self, verbose=True):
        sql = """
            Select pc.cd_conta, pc.ds_classificacao, pc.ds_conta, pc.ds_abreviacao, pc.nr_natureza, pc.nr_conta_vinculada_agco, pc.nr_cpfcnpj 
            from TBL_CONTABIL_PLANO_CONTAS pc INNER JOIN
                (SELECT tb.cd_conta, ds_classificacao, sum(ordf) as ord
                from (SELECT CD_CONTA, DS_CLASSIFICACAO, ordinal, value, cast(value as int) as value_int, -(power(10, ordinal) * cast(value as int))  as ordf 
                FROM TBL_CONTABIL_PLANO_CONTAS 
                CROSS APPLY STRING_SPLIT(DS_CLASSIFICACAO, '.', 1)
                ) as tb
                group by tb.cd_conta, tb.ds_classificacao
                ) tmp on tmp.cd_conta = pc.cd_conta
            WHERE X_ATIVO = 1
            order by tmp.ord desc;
            """
        cur = self.get_connection().cursor()
        cur.execute(sql)

        row = cur.fetchone()

        natureza = {
            'C': TIPO_GRUPO_ESCOLHAS[0][0],
            'D': TIPO_GRUPO_ESCOLHAS[1][0]
        }
        
        while row:
            rcliente = {
                'codigo': str(row['ds_classificacao']).title(),
                'descricao': str(row['ds_conta']).lower(),
                'tipo_grupo': natureza[row['nr_natureza']] 
            }
            if not PlanoContasGrupo.objects.filter(codigo=rcliente['codigo']).exists():
                if '.' not in rcliente['codigo']:
                    ct = PlanoContasGrupo.objects.create(codigo=rcliente['codigo'], descricao=rcliente['descricao'], tipo_grupo=rcliente['tipo_grupo'])
                    ct.save()
                else:
                    codigo_pai = rcliente['codigo'][rcliente['codigo'].rindex('.')+1:]
                    print(codigo_pai)
                    pt = PlanoContasGrupo.objects.get(codigo=codigo_pai)
                    ct = PlanoContasSubgrupo.objects.create(codigo=rcliente['codigo'], descricao=rcliente['descricao'], tipo_grupo=rcliente['tipo_grupo'], grupo=pt)

            row = cur.fetchone()

        cur.close()
        if verbose:
            stdout.write("\rImportando contas: 100%\r\n")