from django.db import models

# Create your models here.

class especialidade(models.Model):
    id_especialidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    crm = models.CharField(max_length=50, unique=True)
    especialidade = models.ForeignKey(especialidade, on_delete=models.CASCADE, related_name="especialidades")

    def __str__(self):
        return f"{self.nome} - {self.especialidade.nome}"
