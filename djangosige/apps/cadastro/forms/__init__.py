# -*- coding: utf-8 -*-

from .pessoa_forms import PessoaJuridicaForm, PessoaFisicaForm
from .inline_formsets import EnderecoFormSet, TelefoneFormSet, EmailFormSet, SiteFormSet, BancoFormSet, DocumentoFormSet, ContaBancariaFormSet, EnderecoUsuarioFormSet

from .empresa import EmpresaForm, MinhaEmpresaForm, DepartamentoForm
from .cliente import ClienteForm
from .fornecedor import FornecedorForm
from .transportadora import TransportadoraForm, VeiculoFormSet

from .produto import ProdutoForm, CategoriaForm, UnidadeForm, MarcaForm
