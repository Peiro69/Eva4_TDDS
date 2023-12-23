from django.contrib import admin
from Cliente.models import Cliente, Pedido

# Register your models here.

class AdminCliente(admin.ModelAdmin):
    list_display = ['nombre','correo']
admin.site.register(Cliente, AdminCliente)

class AdminPedido(admin.ModelAdmin):
    list_display = ['descripcion', 'tipo_de_carga', 'cliente']
admin.site.register(Pedido, AdminPedido)
