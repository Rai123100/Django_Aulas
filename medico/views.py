from django.shortcuts import render, redirect
from .models import medico, especialidade
from .forms import MedicoForm, EspecialidadeForm

# Create your views here.
def lista_medicos(request):
    medicos = medico.objects.all()
    return render(request, "medico/medico_view.html", {"medicos": medicos})

def lista_especialidades(request):
    especialidades = especialidade.objects.all()
    return render(request, "medico/especialidade_view.html", {"especialidades": especialidades})

# -----------------------------------------------Form de Cadastrar medico
def cadastrar_medico(request):
    if request.method == "POST":
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_medicos')
    else:
        form = MedicoForm()

    return render(request, "medico/adicionar_medico.html", {"form": form})

# -----------------------------------------------Form de Cadastrar especialidade
def cadastrar_especialidade(request):
    if request.method == "POST":
        form = EspecialidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_especialidades')
    else:
        form = EspecialidadeForm()

    return render(request, "medico/adicionar_especialidade.html", {"form": form})