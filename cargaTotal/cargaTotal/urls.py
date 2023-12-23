"""
URL configuration for cargaTotal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Chofer import views as Chofer
from Cliente import views as Cliente


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Cliente.indexPrincipal),
    path('inicioChofer/', Chofer.indexChofer),
    path('inicioCliente/', Cliente.indexCliente),
    path('registrarPedido/', Cliente.formularioPedido),
    path('registrarCliente/', Cliente.formularioCliente),
    path('pedidosRegistrados/', Cliente.listaPedidos),
    path('pedidosDisponibles/', Cliente.listaPedidosChofer),
    path('pedidos/<int:id>', Cliente.modificarPedido),
    path('pedidosAceptados/', Cliente.pedidosAceptados),
    path('pedidosEntregados/', Cliente.pedidosEntregados),
]
