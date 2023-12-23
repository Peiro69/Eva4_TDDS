from django.db import models

# Create your models here.


OPCIONES_TIPO_CARGA = [('Carga Liviana','Carga Liviana'), ('Carga Media','Carga Media'), ('Carga Pesada','Carga Pesada')]

OPCIONES_TIPO_USUARIO = [('Cliente','Cliente'), ('Chofer','Chofer')]

OPCIONES_TIPO_ESTADO_PEDIDO = [('En Espera', 'En Espera'), ('Aceptada', 'Aceptada'), ('Entregada', 'Entregada')]


class Cliente(models.Model):
    
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)

    def __str__(self):
        return f'{self.nombre}, {self.correo}'


class Pedido(models.Model):
    descripcion = models.CharField(max_length=50)
    tipo_de_carga = models.CharField(max_length=50, choices=OPCIONES_TIPO_CARGA)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=OPCIONES_TIPO_ESTADO_PEDIDO, default='En Espera')
    
    def __str__(self):
        return f'{self.descripcion}, {self.tipo_de_carga}, {self.cliente}'
