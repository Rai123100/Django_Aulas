from django.shortcuts import render, redirect
from .models import medico, especialidade
from .forms import MedicoForm, EspecialidadeForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

# Create your views here.
# def lista_medicos(request):
#     medicos = medico.objects.all()
#     return render(request, "medico/medico_view.html", {"medicos": medicos})

# def lista_especialidades(request):
#     especialidades = especialidade.objects.all()
#     return render(request, "medico/especialidade_view.html", {"especialidades": especialidades})

# -----------------------------------------------Form de Cadastrar medico
# def cadastrar_medico(request):
#     if request.method == "POST":
#         form = MedicoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lista_medicos')
#     else:
#         form = MedicoForm()

#     return render(request, "medico/adicionar_medico.html", {"form": form})

# -----------------------------------------------Form de Cadastrar especialidade
# def cadastrar_especialidade(request):
#     if request.method == "POST":
#         form = EspecialidadeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lista_especialidades')
#     else:
#         form = EspecialidadeForm()

#     return render(request, "medico/adicionar_especialidade.html", {"form": form})



# ----------------------- ESPECIALIDADE -----------------------

class EspecialidadeListView(LoginRequiredMixin, ListView):
    model = especialidade
    context_object_name = "especialidades"
    template_name = "medico/especialidade_view.html"

class EspecialidadeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'medico.add_especialidade'
    model = especialidade
    form_class = EspecialidadeForm
    template_name = 'medico/especialidade_form.html'
    success_url = reverse_lazy('especialidade_view')

class EspecialidadeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'medico.change_especialidade'
    model = especialidade
    form_class = EspecialidadeForm
    template_name = 'medico/especialidade_form.html'
    success_url = reverse_lazy('especialidade_view')

class EspecialidadeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'medico.delete_especialidade'
    model = especialidade
    template_name = 'medico/especialidade_confirm_delete.html'
    success_url = reverse_lazy('especialidade_view')


# ----------------------- MÉDICO -----------------------

class MedicoListView(LoginRequiredMixin, ListView):
    model = medico
    context_object_name = "medicos"
    template_name = 'medico/medico_view.html'

class MedicoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'medico.add_medico'
    model = medico
    form_class = MedicoForm
    template_name = 'medico/medico_form.html'
    success_url = reverse_lazy('medico_view')

class MedicoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'medico.change_medico'
    model = medico
    form_class = MedicoForm
    template_name = 'medico/medico_form.html'
    success_url = reverse_lazy('medico_view')

class MedicoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'medico.delete_medico'
    model = medico
    template_name = 'medico/medico_confirm_delete.html'
    success_url = reverse_lazy('medico_view')