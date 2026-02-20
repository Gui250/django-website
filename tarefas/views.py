from django.shortcuts import render, redirect
from .forms import TarefaForm
from .models import Tarefa
def home(request):
    lista = Tarefa.objects.all()
    return render(request, 'tarefas/home.html', {'tarefas': lista})

def adicionar(request): 
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else: 
        form = TarefaForm()
    return render(request, 'tarefas/add.html', {'form': form})