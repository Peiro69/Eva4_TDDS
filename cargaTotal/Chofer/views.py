from django.shortcuts import render

# Create your views here.

def indexChofer(request):
    return render(request, 'Chofer/inicioChofer.html')

def verPedidos(request):
    return render(request, 'Chofer')
