from django.contrib import admin

# Register your models here.
from .models import especialidade, medico

admin.site.register(medico)
admin.site.register(especialidade)