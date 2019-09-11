from django.db import models

from cliente.models import Cliente

class ListaDeDesejos(models.Model):

    produto = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente',
                             on_delete=models.PROTECT, related_name='lista_de_desejos')

    class Meta:
        verbose_name = u'ListaDeDesejo'
        verbose_name_plural = u'ListaDeDesejos'
        unique_together = [['produto', 'cliente']]

    def __str__(self):
        return '{}-{}'.format(self.cliente, self.produto)