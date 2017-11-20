from django.shortcuts import render, redirect
from apps.ponencias.form import EventoForm
from apps.ponencias.models import Evento
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
# Create your views here.
def registro(request):
    return render(request, 'ponencia/registro.html')
def eventos(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('inicio:principal')
    else:
        form = EventoForm()
    return render(request, 'evento/registro.html', {'form': form})

def libros(request):
    return render(request, 'libro/registro.html')
def revistas(request):
    return render(request, 'revista/registro.html')