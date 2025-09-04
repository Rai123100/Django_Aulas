from django.urls import path
from .views import lista_medicos, lista_especialidades, cadastrar_medico, cadastrar_especialidade

urlpatterns = [
    path("medicos", lista_medicos, name="lista_medicos"),  # <- vazio aqui
    path("especialidades", lista_especialidades, name="lista_especialidades"),
    path("adicionar_especialidade", cadastrar_especialidade, name="cadastrar_especialidade"),
    path("adicionar_medico", cadastrar_medico, name="cadastrar_medico"),
]