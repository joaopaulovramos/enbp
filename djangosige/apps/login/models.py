# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver





def user_directory_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    return 'imagens/usuarios/fotos_perfil/{0}_{1}{2}'.format(instance.user.username, instance.user.id, extension)


class Usuario(models.Model):
    PERFIS = [
        ('0', 'Solicitante'),
        ('1', 'Diretor da Unidade Solicitante (DUS)'),
        ('2', 'Superintendente'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_foto = models.ImageField(upload_to=user_directory_path, default='imagens/user.png', blank=True)
    data_inclusao = models.DateTimeField(auto_now_add=True, null=True, blank=True,)
    date_ultima_modificacao = models.DateTimeField(auto_now=True, null=True, blank=True,)
    data_inativacao = models.DateTimeField(auto_now_add=True, null=True, blank=True,)
    perfil = models.CharField(max_length=50, null=True, blank=True, choices=PERFIS, default=PERFIS[0][0])

    def save(self, *args, **kwargs):
        # Deletar user_foto se ja existir uma
        try:
            obj = Usuario.objects.get(id=self.id)
            if obj.user_foto != self.user_foto and obj.user_foto != 'imagens/user.png':
                obj.user_foto.delete(save=False)
        except:
            pass

        super(Usuario, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.user

    def __str__(self):
        return u'%s' % self.user


@receiver(post_delete, sender=Usuario)
def foto_post_delete_handler(sender, instance, **kwargs):
    # Nao deletar a imagem default 'user.png'
    if instance.user_foto != 'imagens/user.png':
        instance.user_foto.delete(False)
