import datetime
from django.core.management.base import BaseCommand

from djangosige.apps.util.importador_dados_legado import ImportadorLegado

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        verbose = options.get('verbosity', '0') != '0'
        dao = ImportadorLegado()
        # dao.importar_clientes(verbose)
        dao.importar_fornecedores(verbose)
