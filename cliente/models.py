from django.db import models

class Cliente(models.Model):

    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = u'Cliente'
        verbose_name_plural = u'Clientes'

    def __str__(self):
        return '{}-{}'.format(self.nome, self.email)