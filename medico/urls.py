from django.urls import path
from .views import (EspecialidadeListView, EspecialidadeCreateView, EspecialidadeUpdateView,
                    EspecialidadeDeleteView, MedicoListView, MedicoCreateView, MedicoUpdateView,
                    MedicoDeleteView)

urlpatterns = [
    path('', EspecialidadeListView.as_view(), name='especialidade_list'),
    path('create/', EspecialidadeCreateView.as_view(), name='especialidade_create'),
    path('<int:pk>/update/', EspecialidadeUpdateView.as_view(), name='especialidade_edit'),
    path('<int:pk>/delete/', EspecialidadeDeleteView.as_view(), name='especialidade_delete'),

    path('', MedicoListView.as_view(), name='medico_list'),
    path('create/', MedicoCreateView.as_view(), name='medico_create'),
    path('<int:pk>/update/', MedicoUpdateView.as_view(), name='medico_edit'),
    path('<int:pk>/delete/', MedicoDeleteView.as_view(), name='medico_delete'),
]