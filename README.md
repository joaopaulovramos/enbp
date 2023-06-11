pyt # DjangoSIGE [![Build Status](https://travis-ci.org/thiagopena/djangoSIGE.svg?branch=master)](https://travis-ci.org/thiagopena/djangoSIGE)

Sistema Integrado de Gestão Empresarial baseado em Django

## Instalação:
## atualização zeppelin

0. Instalar as bibliotecas/pacotes (no Linux):

```bash
sudo apt install -y libxml2 gcc python3-dev libxml2-dev libxslt1-dev zlib1g-dev python3-pip
sudo apt update
```

1. Instalar dependências:

```bash
pip install -r requirements.txt
```

2. Edite o conteúdo do arquivo **djangosige/configs/configs.py**

3. Gere um `.env` local

```bash
python contrib/env_gen.py
```


4. Sincronize a base de dados:

```bash
python manage.py migrate
```
teste

5. Crie um usuário (Administrador do sistema):

```bash
python manage.py createsuperuser
```

5.1 carregar dados iniciais 
```
python manage.py loaddata djangosige/tests/fixtures/test_db_backup.json

python manage.py loaddata djangosige/tests/fixtures/municipios.json

python manage.py loaddata djangosige/tests/fixtures/grupos.json 

python manage.py loaddata djangosige/tests/fixtures/classes.json

python manage.py loaddata djangosige/tests/fixtures/sub_classes.json 
```

6. Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):

```bash
python manage.py runserver
```

## Implementações

- Cadastro de produtos, clientes, empresas, fornecedores e transportadoras
- Login/Logout
- Criação de perfil para cada usuário.
- Definição de permissões para usuários.
- Criação e geração de PDF para orçamentos e pedidos de compra/venda
- Módulo financeiro (Plano de Contas, Fluxo de Caixa e Lançamentos)
- Módulo para controle de estoque
- Módulo fiscal:
    - Geração e armazenamento de notas fiscais
    - Validação do XML de NF-e/NFC-es
    - Emissão, download, consulta e cancelamento de NF-e/NFC-es **(Testar em ambiente de homologação)**
    - Comunicação com SEFAZ (Consulta de cadastro, inutilização de notas, manifestação do destinatário)
- Interface simples e em português



