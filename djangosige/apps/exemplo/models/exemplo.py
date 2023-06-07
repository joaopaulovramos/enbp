from django.db import models


class ExemploModel(models.Model):
    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=200)





#select * from auth_permission where  auth_permission.codename LIKE '%carro%'
class CarroModel(models.Model):
    nome = models.CharField(max_length=200)
    placa = models.CharField(max_length=200)
    chaci = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Exemplo Carro"
        # permissions = (
        #     ("listar_carro", "Pode listar carros"),
        #     ("cadastrar_carro", "Pode cadastrar carro"),
        #     ("editar_carro", "Pode editar carro"),
        # )


