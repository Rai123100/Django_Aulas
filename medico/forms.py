from django import forms
from .models import medico, especialidade

class MedicoForm(forms.ModelForm):
    class Meta:
        model = medico
        fields = ['id_medico', 'nome', 'endereco', 'telefone', 'email', 'data_nascimento', 'id_especialidade']
        
# ----------------------------------------------------------------------------

class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = especialidade
        fields = ['id_especialidade', 'nome', 'descricao']

