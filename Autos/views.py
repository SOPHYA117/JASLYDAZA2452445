from django.shortcuts import render

def autos(request):
    contexto={}
    return render(request,'autos.html',contexto)

def clientes(request):
    contexto={}
    return render(request,'clientes.html',contexto)

