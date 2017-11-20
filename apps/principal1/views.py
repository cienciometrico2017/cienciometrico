from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'base1/inicio.html')
def produccion(request):
    return render(request, 'base1/produccioncientifica.html')
def similares(request):
    return render(request, 'base1/similares.html')
def sesiones(request):
    return render(request, 'base1/sesion.html')