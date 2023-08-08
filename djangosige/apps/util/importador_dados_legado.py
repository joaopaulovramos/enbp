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
from djangosige.apps.cadastro.models.produto import Produto, Unidade
from djangosige.apps.cadastro.models.transportadora import Transportadora
from djangosige.apps.financeiro.models.lancamento import Entrada, Saida
from djangosige.apps.vendas.models import Pagamento as Pagamento
from djangosige.apps.financeiro.models.plano import TIPO_GRUPO_ESCOLHAS, PlanoContasGrupo, PlanoContasSubgrupo
from djangosige.apps.fiscal.models.natureza_operacao import NaturezaOperacao
from djangosige.apps.fiscal.models.tributos import COFINS, ICMS, IPI, PIS, GrupoFiscal, ICMSUFDest
from djangosige.apps.vendas.models.vendas import PedidoVenda


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

    def importar_lancamentos_areceber(self, verbose=True):
        sql = """
            select pc.DT_VENCIMENTO, pc.VL_PARCELA, pc.CD_ID as id_parcela, pg.cd_lancamento,
            pg.cd_carteira, cart.DS_CARTEIRA, 
            pg.CD_CLIENTE, forn.NR_CPFCNPJ, 
            pg.cd_forma_pagamento, fp.DS_FORMA_PAGAMENTO,
            pg.ds_obs, pg.ds_especie, 
            pg.nr_documento, pg.nr_parcelas, pg.vl_titulo
        from TBL_FINANCEIRO_TITULOS_ARECEBER pg
            inner join TBL_FINANCEIRO_TITULOS_ARECEBER_PARCELAS pc on pc.CD_LANCAMENTO = pg.CD_LANCAMENTO
            inner join TBL_FINANCEIRO_CARTEIRA cart on cart.cd_carteira = pg.CD_CARTEIRA
            inner join TBL_ENTIDADES forn on forn.CD_ENTIDADE = pg.CD_CLIENTE
            inner join TBL_FINANCEIRO_FORMAS_PAGAMENTO fp on fp.CD_FORMA_PAGAMENTO = pg.CD_FORMA_PAGAMENTO;
            """
        cur = self.get_connection().cursor()
        cur.execute(sql)

        row = cur.fetchone()

        while row:
            rpagamento = {
                'codigo': str(row['id_parcela']).title(),
                'numero_pessoa': row['NR_CPFCNPJ'],
            }
            if not Entrada.objects.filter(codigo_legado=rpagamento['codigo']).exists():
                # Criar lancamento com data futura (sem movimentos)
                saida = Entrada()
                saida.descricao = 'referente documento: ' + str(row['nr_documento'])
                saida.codigo_legado = rpagamento['codigo']
                saida.data_vencimento = row['DT_VENCIMENTO']
                saida.valor_total = row['VL_PARCELA']
                saida.movimentar_caixa = False
                saida.valor_liquido = row['VL_PARCELA']
                qf = Cliente.objects.filter(pessoa_jur_info__cnpj=rpagamento['numero_pessoa'])
                if qf.exists():
                    saida.cliente = qf.first()
                saida.save()
            row = cur.fetchone()
        cur.close()
        if verbose:
            stdout.write("\rImportando contas a receber: 100%\r\n")

    def importar_lancamentos_apagar(self, verbose=True):
        sql = """
            select pc.DT_VENCIMENTO, pc.VL_PARCELA, pc.CD_ID as id_parcela, pg.cd_lancamento,
            pg.cd_carteira, cart.DS_CARTEIRA, 
            pg.cd_fornecedor, forn.NR_CPFCNPJ, 
            pg.cd_entrada_compra,
            pg.cd_forma_pagamento, fp.DS_FORMA_PAGAMENTO,
            pg.ds_obs, pg.ds_especie, 
            pg.nr_documento, pg.nr_parcelas, pg.vl_titulo
        from TBL_FINANCEIRO_TITULOS_APAGAR pg
            inner join TBL_FINANCEIRO_TITULOS_APAGAR_PARCELAS pc on pc.CD_LANCAMENTO = pg.CD_LANCAMENTO
            inner join TBL_FINANCEIRO_CARTEIRA cart on cart.cd_carteira = pg.CD_CARTEIRA
            inner join TBL_ENTIDADES forn on forn.CD_ENTIDADE = pg.CD_FORNECEDOR
            inner join TBL_FINANCEIRO_FORMAS_PAGAMENTO fp on fp.CD_FORMA_PAGAMENTO = pg.CD_FORMA_PAGAMENTO;
            """
        cur = self.get_connection().cursor()
        cur.execute(sql)

        row = cur.fetchone()

        while row:
            rpagamento = {
                'codigo': str(row['id_parcela']).title(),
                'numero_pessoa': row['NR_CPFCNPJ'],
            }
            if not Saida.objects.filter(codigo_legado=rpagamento['codigo']).exists():
                # Criar lancamento com data futura (sem movimentos)
                saida = Saida()
                saida.descricao = 'referente documento: ' + str(row['nr_documento'])
                saida.codigo_legado = rpagamento['codigo']
                saida.data_vencimento = row['DT_VENCIMENTO']
                saida.valor_total = row['VL_PARCELA']
                saida.movimentar_caixa = False
                saida.valor_liquido = row['VL_PARCELA']
                qf = Fornecedor.objects.filter(pessoa_jur_info__cnpj=rpagamento['numero_pessoa'])
                if qf.exists():
                    saida.fornecedor = qf.first()
                saida.save()
            row = cur.fetchone()
        cur.close()
        if verbose:
            stdout.write("\rImportando contas a pagar: 100%\r\n")
    
    def importar_contas_lancamentos(self, verbose=True):
        sql = """
            Select pc.cd_conta, pc.ds_classificacao, pc.ds_conta, pc.ds_abreviacao, pc.nr_natureza, pc.nr_conta_vinculada_agco, pc.nr_cpfcnpj, pc.x_tipo as tipo
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
                'codigo_legado': row['cd_conta'],
                'codigo': str(row['ds_classificacao']).title(),
                'descricao': str(row['ds_conta']),
                'tipo_grupo': natureza[row['nr_natureza']],
                'observacao': 'Abreviação: ' + str(row['ds_abreviacao']) + ' CNPJ: ' + str(row['nr_cpfcnpj']),
            }
            # print(rcliente)
            if not PlanoContasGrupo.objects.filter(codigo_legado=rcliente['codigo_legado']).exists():
                if '.' not in rcliente['codigo']:
                    ct = PlanoContasGrupo.objects.create(codigo=rcliente['codigo'], descricao=rcliente['descricao'], tipo_grupo=rcliente['tipo_grupo'], observacao=rcliente['observacao'], codigo_legado=rcliente['codigo_legado'])
                    ct.save()
                else:
                    codigo_pai = rcliente['codigo'][:rcliente['codigo'].rindex('.')]
                    codigo_filho = rcliente['codigo'][rcliente['codigo'].rindex('.')+1:]
                    print(codigo_pai)
                    try:
                        pt = PlanoContasGrupo.objects.filter(codigo=codigo_pai)[:1].get()
                    except PlanoContasGrupo.DoesNotExist:
                        print('Grupo não encontrado: ' + codigo_pai)
                        #print('registrado não sera migrado: ' + str(rcliente))
                        pt = PlanoContasGrupo.objects.create(codigo=codigo_pai, descricao='Conta: ' + codigo_pai, tipo_grupo=rcliente['tipo_grupo'], observacao='Gerado automaticamente conta ' + codigo_pai + ' não encontrado no legado', codigo_legado=rcliente['codigo_legado'])        
                    ct = PlanoContasSubgrupo.objects.create(codigo=rcliente['codigo'], descricao=rcliente['descricao'], tipo_grupo=rcliente['tipo_grupo'], grupo=pt, observacao=rcliente['observacao'], codigo_legado=rcliente['codigo_legado'])        
                        

            row = cur.fetchone()
        cur.close()


    def importar_detalhes_venda(self, venda, verbose=True):
        sql = """
        select pg.CD_LANCAMENTO, pg.VL_VALOR, pg.CD_LANCAMENTO_TRIBUTARIO,
            pc.NR_PARCELA, pc.VL_PARCELA, pc.DT_VENCIMENTO
            from TBL_NOTAS_FATURAMENTO_FORMAS_PAGAMENTO pg
            inner join TBL_NOTAS_FATURAMENTO_PARCELAS pc on pc.CD_PAGAMENTO = pg.CD_PAGAMENTO
            where pg.CD_PAGAMENTO = {};
            """
        cur = self.get_connection().cursor()
        cur.execute(sql.format(venda.codigo_legado))

        row = cur.fetchone()
        while row:
            pagamento = Pagamento()
            pagamento.venda_id = venda
            pagamento.indice_parcela = row['NR_PARCELA']
            pagamento.vencimento = row['DT_VENCIMENTO']
            pagamento.valor_parcela = row['VL_PARCELA']
            pagamento.save()

            row = cur.fetchone()

        cur.close()

    def importar_notas_faturadas(self, verbose=True):
        sql = """
            select nf.CD_LANCAMENTO as codigo, 
            nf.CD_CLIENTE, cli.NR_CPFCNPJ,
            nf.CD_STATUS, nf.CD_STATUS_NFE_RETORNO,
            nf.DT_EMISSAO, DT_SAIDA, HR_SAIDA,
            nf.DT_EMISSAO_NFSE,
            nf.DT_GERACAO_NSU, nf.NR_NSU, nf.NR_DOCUMENTO,
            nf.NR_PARCELAS, nf.NR_QUANTIDADE,
            nf.DS_OBS,
            nf.DS_DIGEST_VALUE_NFE, 
            nf.NR_LOTE_NFE, nf.NR_RECIBO_NFE,
            nf.NR_CHAVE_NFE, nf.NR_PROTOCOLO_NFE,
            nf.NR_ITENS, nf.DS_VERSAO_NFE,
            nf.VL_PRODUTOS, nf.VL_TOTAL, nf.VL_pis, nf.VL_COFINS,  (nf.VL_pis + nf.VL_COFINS) as total_impostos
        from TBL_NOTAS_FATURAMENTO nf
            inner join TBL_ENTIDADES cli on cli.CD_ENTIDADE = nf.CD_CLIENTE
            where nf.CD_STATUS in (1,2); -- Pendente ou Faturado
            """
        cur = self.get_connection().cursor()
        cur.execute(sql)

        row = cur.fetchone()

        while row:
            rvenda = {
                'codigo': str(row['codigo']),
                'numero_pessoa': row['NR_CPFCNPJ'],
                'numero_pessoa_clean': re.sub('[./-]', '', row['NR_CPFCNPJ']),
                'data_emissao': row['DT_EMISSAO'],
                'valor_total': row['VL_TOTAL'],
                'impostos': row['total_impostos'],
                'status': row['CD_STATUS']-1,
            }
            if not PedidoVenda.objects.filter(codigo_legado=rvenda['codigo']).exists():
                venda = PedidoVenda()
                venda.status = rvenda['status']
                venda.codigo_legado=rvenda['codigo']
                venda.data_emissao = rvenda['data_emissao']
                venda.cliente = Cliente.objects.filter(
                tipo_pessoa='PJ').filter(pessoa_jur_info__cnpj=rvenda['numero_pessoa'])[0]
                venda.valor_total = rvenda['valor_total']
                venda.impostos = rvenda['impostos']
                venda.save()
                self.importar_detalhes_venda(venda, verbose)
            row = cur.fetchone()

        cur.close()
        if verbose:
            stdout.write("\rImportando vendas: 100%\r\n")

    def importar_produtos_faturados(self, verbose=True):
        sql = """
            select min(nf.CD_NOTA) as codigo, 
                nfi.DS_MATERIAL as descricao_produto,
                nfi.VL_ICMS_ST_DESONERADO, nfi.PR_REDUCAO, 
                nfi.PR_REDUCAO_ST,
                mt.CD_CODBARRA as cod_barra, mt.CD_CEST as cest, mt.CD_NCM as ncm,
                nfi.DS_CFOP, nfi.DS_UNIDADE,
                nfi.DS_INFO_ADICIONAL_NFE as info_adicional, nfi.DS_SITTRIBUTARIA as cst
            from TBL_NOTAS_EMITIDAS_ITENS nfi
            inner join TBL_NOTAS_EMITIDAS nf on nf.CD_NOTA = nfi.CD_NOTA
            inner join TBL_MATERIAIS mt on mt.CD_MATERIAL = nfi.CD_MATERIAL
            where nf.CD_STATUS in (2) group by  nfi.DS_MATERIAL, nfi.VL_ICMS_ST_DESONERADO, 
            nfi.PR_REDUCAO, nfi.PR_REDUCAO_ST,
            mt.CD_CODBARRA, mt.CD_CEST, mt.CD_NCM,
            nfi.DS_CFOP, nfi.DS_UNIDADE,
            nfi.DS_INFO_ADICIONAL_NFE, nfi.DS_SITTRIBUTARIA
            union select min(nf.CD_LANCAMENTO) as codigo, 
                nfi.DS_MATERIAL as descricao_produto, nfi.VL_ICMS_ST_DESONERADO, nfi.PR_REDUCAO, 
                nfi.PR_REDUCAO_ST,
                mt.CD_CODBARRA as cod_barra, mt.CD_CEST as cest, mt.CD_NCM as ncm,
                nfi.DS_CFOP, nfi.DS_UNIDADE,
                nfi.DS_INFO_ADICIONAL_NFE as info_adicional, nfi.DS_SITTRIBUTARIA as cst
            from TBL_NOTAS_FATURAMENTO_ITENS nfi
            inner join TBL_NOTAS_FATURAMENTO nf on nf.CD_LANCAMENTO = nfi.CD_LANCAMENTO
            inner join TBL_MATERIAIS mt on mt.CD_MATERIAL = nfi.CD_MATERIAL
            where nf.CD_STATUS in (2)
            group by  nfi.DS_MATERIAL, nfi.VL_ICMS_ST_DESONERADO, 
                nfi.PR_REDUCAO, nfi.PR_REDUCAO_ST,
                mt.CD_CODBARRA, mt.CD_CEST, mt.CD_NCM,
                nfi.DS_CFOP, nfi.DS_UNIDADE,
                nfi.DS_INFO_ADICIONAL_NFE, nfi.DS_SITTRIBUTARIA 
            union select min(nf.CD_ENTRADA) as codigo, 
                nfi.DS_MATERIAL as descricao_produto, 0 as VL_ICMS_ST_DESONERADO, nfi.PR_REDUCAO,  nfi.PR_REDUCAO_ST,
                mt.CD_CODBARRA as cod_barra, mt.CD_CEST as cest, mt.CD_NCM as ncm,
                nfi.DS_CFOP, nfi.DS_UNIDADE, null as info_adicional, nfi.CD_SITTRIBUTARIA as cst
            from TBL_COMPRAS_NOTAFISCAL_ENTRADA_ITENS nfi
                inner join TBL_COMPRAS_NOTAFISCAL_ENTRADA nf on nf.CD_ENTRADA = nfi.CD_ENTRADA
                inner join TBL_MATERIAIS mt on mt.CD_MATERIAL = nfi.CD_MATERIAL
            where nf.CD_STATUS in (2)
            group by  nfi.DS_MATERIAL, 
                nfi.PR_REDUCAO, nfi.PR_REDUCAO_ST,
                mt.CD_CODBARRA, mt.CD_CEST, mt.CD_NCM,
                nfi.DS_CFOP, nfi.DS_UNIDADE, nfi.CD_SITTRIBUTARIA; 
            """
        cur = self.get_connection().cursor()
        cur.execute(sql)

        row = cur.fetchone()

        while row:
            rproduto = {
                'codigo': row['codigo'],
                'descricao_produto': row['descricao_produto'],
                'cod_barra': row['cod_barra'],
                'cfop': str(re.sub('[./-]', '', row['DS_CFOP'])),
                'cest': row['cest'],
                'ncm': row['ncm']
            }
            if not Produto.objects.filter(descricao=rproduto['descricao_produto']).exists():
                produto = Produto()
                produto.descricao = rproduto['descricao_produto']
                produto.codigo = rproduto['codigo']
                produto.codigo_legado = rproduto['codigo']
                produto.codigo_barras = rproduto['cod_barra']
                produto.cest = rproduto['cest']
                produto.ncm = rproduto['ncm']
                produto.inf_adicionais = row['info_adicional']
                produto.controlar_estoque = False
                # Natureza Operacao
                nat_ops = NaturezaOperacao.objects.filter(
                    cfop=rproduto['cfop'])
                if len(nat_ops):
                    nat_op = nat_ops[0]
                else:
                    nat_op = NaturezaOperacao()
                    nat_op.cfop = rproduto['cfop']
                    nat_op.set_values_by_cfop()
                    nat_op.save()
                # importar unidade de comercialização
                #produto.venda = det.prod.vUnCom.valor
                produto.cfop_padrao = nat_op
                grupo_fiscal = GrupoFiscal()
                grupo_fiscal.descricao = 'Produto: ' + rproduto['descricao_produto'] + ' (Importado)'
                grupo_fiscal.regime_trib = '0'  # Normal
                grupo_fiscal.save()
                grupo_icms = ICMS()
                grupo_icms.grupo_fiscal = grupo_fiscal
                grupo_icms.cst = row['cst']
                grupo_icms.p_red_bc = row['PR_REDUCAO']
                # grupo_icms.mod_bcst = row['VL_BASE_CREDITO_ICMS_ST_RETIDO']
                # grupo_icms.p_icms = row['VL_ICMS_ST_DESONERADO']
                # grupo_icms.mod_bc = str(det.imposto.ICMS.modBC.valor)
                # grupo_icms.p_mvast = det.imposto.ICMS.pMVAST.valor
                # grupo_icms.p_red_bcst = row['PR_REDUCAO_ST']
                # grupo_icms.p_icmsst = det.imposto.ICMS.pICMSST.valor
                # grupo_icms.mot_des_icms = str(det.imposto.ICMS.motDesICMS.valor)
                # grupo_icms.p_dif = det.imposto.ICMS.pDif.valor
                # grupo_icms.p_bc_op = det.imposto.ICMS.pBCOp.valor
                # grupo_icms.ufst = str(det.imposto.ICMS.UFST.valor)
                grupo_icms.save()

                grupo_icmsufdest = ICMSUFDest()
                grupo_icmsufdest.grupo_fiscal = grupo_fiscal
                # grupo_icmsufdest.p_fcp_dest = pFCPUFDest
                # grupo_icmsufdest.p_icms_dest =ICMSUFDest.pICMSUFDest
                # grupo_icmsufdest.p_icms_inter = ICMSUFDest.pICMSInter
                # grupo_icmsufdest.p_icms_inter_part = ICMSUFDest.pICMSInterPart
                grupo_icmsufdest.save()

                # IPI
                grupo_ipi = IPI()
                grupo_ipi.grupo_fiscal = grupo_fiscal
                # grupo_ipi.cst = str(det.imposto.IPI.CST.valor)
                # grupo_ipi.cl_enq = str(det.imposto.IPI.clEnq.valor)
                # grupo_ipi.c_enq = str(det.imposto.IPI.cEnq.valor)
                # grupo_ipi.cnpj_prod = str(det.imposto.IPI.CNPJProd.valor)
                # if det.imposto.IPI.qUnid.valor or det.imposto.IPI.vUnid.valor:
                #     grupo_ipi.tipo_ipi = u'1'
                #     grupo_ipi.valor_fixo = det.imposto.IPI.vUnid.valor
                # elif det.imposto.IPI.vBC.valor or det.imposto.IPI.pIPI.valor:
                #     grupo_ipi.tipo_ipi = u'2'
                #     grupo_ipi.p_ipi = det.imposto.IPI.pIPI.valor
                # else:
                #     grupo_ipi.tipo_ipi = u'0'
                grupo_ipi.save()

                # PIS
                grupo_pis = PIS()
                grupo_pis.grupo_fiscal = grupo_fiscal
                # if det.imposto.PIS.CST.valor:
                #     grupo_pis.cst = det.imposto.PIS.CST.valor
                #     grupo_pis.p_pis = det.imposto.PIS.pPIS.valor
                #     grupo_pis.valiq_pis = det.imposto.PIS.vAliqProd.valor
                grupo_pis.save()

                # COFINS
                grupo_cofins = COFINS()
                grupo_cofins.grupo_fiscal = grupo_fiscal
                # if det.imposto.COFINS.CST.valor:
                #     grupo_cofins.cst = det.imposto.COFINS.CST.valor
                #     grupo_cofins.p_cofins = det.imposto.COFINS.pCOFINS.valor
                #     grupo_cofins.valiq_cofins = det.imposto.COFINS.vAliqProd.valor
                grupo_cofins.save()
                grupo_fiscal.save()

                produto.grupo_fiscal = grupo_fiscal

                # Unidade
                rquery = Unidade.objects.filter(sigla_unidade=row['DS_UNIDADE'])
                if not rquery.exists():
                    unidade = Unidade()
                    unidade.unidade_desc = row['DS_UNIDADE']
                    unidade.sigla_unidade = row['DS_UNIDADE']
                    unidade.save()
                else:
                    unidade = rquery[0]
                produto.unidade = unidade
                produto.save()
                
            row = cur.fetchone()

        cur.close()
        if verbose:
            stdout.write("\rImportando produtos: 100%\r\n")
