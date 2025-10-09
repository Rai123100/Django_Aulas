from django.shortcuts import render, redirect
from .models import medico, especialidade
from .forms import MedicoForm, EspecialidadeForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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

# ---------------------------------------------------------------------------------------------------------------

class EspecialidadeListView(ListView):
    model = especialidade
    template_name = 'especialidade_view.html'

class EspecialidadeCreateView(CreateView):
    model = especialidade
    form_class = EspecialidadeForm
    template_name = 'especialidade_form.html'
    success_url = reverse_lazy('especialidade_view')

class EspecialidadeUpdateView(UpdateView):
    model = especialidade
    form_class = EspecialidadeForm
    template_name = 'especialidade_form.html'
    success_url = reverse_lazy('especialidade_view')

class EspecialidadeDeleteView(DeleteView):
    model = especialidade
    template_name = 'especialidade_confirm_delete.html'
    success_url = reverse_lazy('especialidade_view')

class MedicoListView(ListView):
    model = medico
    template_name = 'medico_view.html'

class MedicoCreateView(CreateView):
    model = medico
    form_class = MedicoForm
    template_name = 'medico_form.html'
    success_url = reverse_lazy('medico_view')

class MedicoUpdateView(UpdateView):
    model = medico
    form_class = MedicoForm
    template_name = 'medico_form.html'
    success_url = reverse_lazy('medico_view')

class MedicoDeleteView(DeleteView):
    model = medico
    template_name = 'medico_confirm_delete.html'
    success_url = reverse_lazy('medico_view')