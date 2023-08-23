from simple_menu import Menu, MenuItem
from django.urls import reverse

janela_unica_children = [
    MenuItem("Caixa de entrada", reverse("janela_unica:caixaentrada"), weight=10, icon="user"),
    MenuItem("Documentos", '/admin/janela_unica/contrato/', weight=20, icon="user", check=lambda r: r.user.has_perm('janela_unica.view_contrato')),
    MenuItem("Adicionar Documento", '/admin/janela_unica/documentounicofinanceiro/', weight=20, icon="user"),
    #MenuItem("Adicionar", reverse("janela_unica:adicionar_documento_unico"), weight=20, icon="user"),
]

Menu.add_item("main", MenuItem("Janela Única", '#',
                               weight=10, icon="insert_drive_file",
                               children=janela_unica_children))
