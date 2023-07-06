import datetime
from django.core.management.base import BaseCommand

from djangosige.apps.util.importador_dados_legado import ImportadorLegado

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        verbose = options.get('verbosity', '0') != '0'
        dao = ImportadorLegado()
        # dao.importar_usuarios(verbose)
        # dao.importar_clientes(verbose)
        # dao.importar_fornecedores(verbose)
        # dao.importar_transportadoras(verbose)
        # dao.importar_contas_lancamentos(verbose)
        # dao.importar_produtos_faturados(verbose)
        # dao.importar_notas_faturadas(verbose)
        dao.importar_lancamentos_apagar(verbose)
        dao.importar_lancamentos_areceber(verbose)
