from django import forms
from .models import especialidade, medico

class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = especialidade
        fields = ['nome', 'descricao']

class MedicoForm(forms.ModelForm):
    class Meta:
        model = medico
        fields = ['nome', 'endereco', 'telefone', 'email', 'data_nascimento', 'crm', 'especialidade']