from django.shortcuts import render
from Cliente.forms import PedidoForm, ClienteForm
from Cliente.models import Pedido, Cliente


# Create your views here.

def indexPrincipal(request):
    return render(request,'Cliente/inicioProyecto.html')

def indexCliente(request):
    return render(request, 'Cliente/inicioCliente.html')

def formularioPedido(request):
    form = PedidoForm()
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
        return indexCliente(request)
    data = {'form':form}
    return render(request, 'Cliente/PedidosCliente.html', data)

def listaPedidos(request):
    pedidos = Pedido.objects.all()
    data = {'pedidos': pedidos}
    return render(request, 'Cliente/listaPedidos.html', data)

def listaPedidosChofer(request):
    pedidos = Pedido.objects.all()
    data = {'pedidos' : pedidos}
    return render(request, 'Chofer/pedidosDisponibles.html', data)

def modificarPedido(request, id):
    pedido = Pedido.objects.get( id = id)
    form = PedidoForm(instance=pedido)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
        return listaPedidosChofer(request)
    data = {'form': form}
    return render(request, 'Cliente/PedidosCliente.html', data)
    
def pedidosAceptados(request):
    pedidos_aceptados = Pedido.objects.filter(estado='Aceptada')
    data = {'pedidos_aceptados': pedidos_aceptados}
    return render(request, 'Chofer/pedidosAceptados.html', data)

def pedidosEntregados(request):
    pedidos_entregados = Pedido.objects.filter(estado='Entregada')
    data = {'pedidos_entregados': pedidos_entregados}
    return render(request, 'Chofer/pedidosEntregados.html', data)

def formularioCliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return indexCliente(request)
    data = {'form':form}
    return render(request, 'Cliente/formularioCliente.html', data)