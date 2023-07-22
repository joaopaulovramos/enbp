# -*- coding: utf-8 -*-

from djangosige.apps.vendas.models import ItensVenda, Pagamento

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

from geraldo import Report, ReportBand, SubReport
from geraldo.widgets import Label, SystemField, ObjectValue
from geraldo.graphics import Image, Line
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

REPORT_FONT = 'Times'
REPORT_FONT_BOLD = REPORT_FONT + '-Bold'

class DocumentoUnicoFinaceiroReport(Report):

    def __init__(self, *args, **kargs):
        super(DocumentoUnicoFinaceiroReport, self).__init__(*args, **kargs)
        self.title = 'Documento Único'

        self.page_size = A4
        self.margin_left = 0.8 * cm
        self.margin_top = 0.8 * cm
        self.margin_right = 0.8 * cm
        self.margin_bottom = 0.8 * cm

        # Bandas
        self.topo_pagina = TopoPagina()
        self.dados_cliente = DadosCliente()
        self.observacoes = Observacoes()
        self.banda_foot = BandaFoot()


class TopoPagina(ReportBand):

    def __init__(self):
        super(TopoPagina, self).__init__()
        self.elements = []
        txt = SystemField(expression='%(report_title)s', top=0.65 *
                          cm, left=0 * cm, width=19.4 * cm, height=0.8 * cm)
        txt.style = {'fontName': REPORT_FONT_BOLD,
                     'fontSize': 15, 'alignment': TA_CENTER, 'leading': 15}
        self.elements.append(txt)

        txt = SystemField(expression='Página %(page_number)s de %(last_page_number)s',
                          top=3.1 * cm, left=0 * cm, width=19.4 * cm, height=0.5 * cm)
        txt.style = {'fontName': REPORT_FONT, 'fontSize': 8.5,
                     'alignment': TA_RIGHT, 'leading': 8.5}
        self.elements.append(txt)

        self.elements.append(Line(top=3.6 * cm, bottom=3.6 *
                                  cm, left=0 * cm, right=19.4 * cm, stroke_width=0.3))

        self.height = 3.65 * cm

    def inserir_data_emissao(self, data_emissao):
        if data_emissao:
            txt = ObjectValue(attribute_name='format_data_emissao', display_format='Data: %s',
                              top=1.45 * cm, left=0 * cm, width=19.4 * cm, height=0.5 * cm)
        else:
            txt = SystemField(expression='Data: %(now:%d/%m/%Y)s',
                              top=1.45 * cm, left=0 * cm, width=19.4 * cm, height=0.5 * cm)
        txt.style = {'fontName': REPORT_FONT_BOLD,
                     'fontSize': 9, 'alignment': TA_CENTER, 'leading': 9}
        self.elements.append(txt)
 
    def inserir_logo(self, path_imagem):
        logo = Image(left=0.5 * cm, top=0.3 * cm, right=10 * cm, bottom=0.5 *
                     cm, width=5.5 * cm, height=5.5 * cm, filename=path_imagem)
        self.elements.append(logo)


class DadosCliente(ReportBand):

    def __init__(self):
        super(DadosCliente, self).__init__()
        self.ender_info = False
        self.elements = []
        txt = ObjectValue(attribute_name='fornecedor.nome_razao_social',
                          top=0.3 * cm, left=0.3 * cm, width=8 * cm, height=0.5 * cm)
        txt.style = {'fontName': REPORT_FONT_BOLD,
                     'fontSize': 12, 'leading': 12}
        self.elements.append(txt)

        self.height = 2.7 * cm

    def inserir_informacoes_pj(self):
        txt = ObjectValue(attribute_name='fornecedor.pessoa_jur_info.format_cnpj',
                          top=0.3 * cm, left=8.1 * cm, width=4 * cm, height=0.5 * cm)
        txt.style = {'fontName': REPORT_FONT_BOLD,
                     'fontSize': 10, 'leading': 10}
        self.elements.append(txt)

        txt = ObjectValue(attribute_name='fornecedor.pessoa_jur_info.format_ie',
                          top=0.3 * cm, left=13 * cm, width=6.4 * cm, height=0.5 * cm)
        txt.style = {'fontName': REPORT_FONT_BOLD,
                     'fontSize': 10, 'leading': 10}
        self.elements.append(txt)

    def inserir_informacoes_banco(self):
        atributos = ['banco', 'agencia', 'conta', 'digito']
        for atributo in atributos:
            txt = ObjectValue(attribute_name= atributo,
                              top=0.3 * cm, left=8.1 * cm,
                              width=4 * cm,
                              height=0.5 * cm
            )
            txt.style = {'fontName': REPORT_FONT_BOLD,
                         'fontSize': 10, 'leading': 10}
            self.elements.append(txt)

    def inserir_informacoes_pf(self):
        txt = ObjectValue(attribute_name='fornecedor.pessoa_fis_info.format_cpf',
                          top=0.3 * cm, left=8.1 * cm, width=4 * cm, height=0.5 * cm)
        txt.style = {'fontName': REPORT_FONT_BOLD,
                     'fontSize': 10, 'leading': 10}
        self.elements.append(txt)

        txt = ObjectValue(attribute_name='fornecedor.pessoa_fis_info.format_rg',
                          top=0.3 * cm, left=13 * cm, width=6.4 * cm, height=0.5 * cm)
        txt.style = {'fontName': REPORT_FONT_BOLD,
                     'fontSize': 10, 'leading': 10}
        self.elements.append(txt)

    def inserir_aprovado(self):
        aprovadores = ["gerencia", "superitendencia", "diretoria", "analise_financeira", "analise_fiscal"]
        for aprovador in aprovadores:
            txt = ObjectValue(attribute_name=f'aprovado_{aprovador}',
                              top=1.5 * cm, left=0.3 * cm,
                              width=8 * cm, height=0.5 * cm,
                              get_value=lambda instance: instance.aprovado_gerencia and "SIM" or "Não"
                             )
            txt.style = {'fontName': REPORT_FONT_BOLD,
                         'fontSize': 12, 'leading': 12}
            self.elements.append(txt)
            txt = ObjectValue(attribute_name=f'observacao_{aprovador}',
                              top=1.5 * cm, left=0.3 * cm,
                              width=8 * cm, height=0.5 * cm
                              )
            txt.style = {'fontName': REPORT_FONT_BOLD,
                         'fontSize': 12, 'leading': 12}
            self.elements.append(txt)


class Observacoes(ReportBand):

    def __init__(self):
        super(Observacoes, self).__init__()
        self.elements = []

        self.elements.append(Line(top=0.1 * cm, bottom=0.1 *
                                  cm, left=0 * cm, right=19.4 * cm, stroke_width=0.3))

        txt = Label(text='Observações', top=0.2 * cm, left=0 *
                    cm, width=19.4 * cm, height=0.5 * cm)
        txt.style = {'fontName': REPORT_FONT_BOLD,
                     'fontSize': 11, 'alignment': TA_CENTER, 'leading': 11}
        self.elements.append(txt)

        txt = ObjectValue(attribute_name='observacoes', top=0.8 *
                          cm, left=0.5 * cm, width=19.4 * cm, height=2 * cm)
        txt.style = {'fontName': REPORT_FONT, 'fontSize': 9, 'leading': 9}
        self.elements.append(txt)

        self.height = 2 * cm

class BandaFoot(ReportBand):

    def __init__(self):
        super(BandaFoot, self).__init__()
        self.ender_info = False
        self.elements = []

        self.elements.append(Line(top=1.5 * cm, bottom=1.5 *
                                  cm, left=0 * cm, right=19.4 * cm, stroke_width=0.3))

        txt = Label(text='Gerado por Norli', top=1.5 * cm,
                    left=0 * cm, width=19.4 * cm, height=0.5 * cm)
        txt.style = {'fontName': REPORT_FONT_BOLD,
                     'fontSize': 8, 'alignment': TA_LEFT, 'leading': 8}
        self.elements.append(txt)

        txt = SystemField(expression='Data da impressão: %(now:%d/%m/%Y)s',
                          top=1.5 * cm, left=0 * cm, width=19.4 * cm, height=0.5 * cm)
        txt.style = {'fontName': REPORT_FONT, 'fontSize': 8,
                     'alignment': TA_RIGHT, 'leading': 8}
        self.elements.append(txt)

        self.height = 2 * cm

    def inserir_nome_empresa(self, nome):
        txt = Label(text=nome, top=0 * cm, left=0 * cm,
                    width=19.4 * cm, height=0.5 * cm)
        txt.style = {'fontName': REPORT_FONT, 'fontSize': 9,
                     'alignment': TA_CENTER, 'leading': 9}
        self.elements.append(txt)
