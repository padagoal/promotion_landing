from django.contrib import admin
from .models import Personas_voto, Personas_votante_prod
# Register your models here.


class Persona_VotanteAdmin(admin.ModelAdmin):
    list_display = (('cedula'),('matricula'),('apellido'),('nombre'),('estaHabilitado'),)
    #list_filter = (('cedula'),('matricula'),('apellido'),('nombre'),('estaHabilitado'),)
    search_fields = (('cedula'),('matricula'),('apellido'),('nombre'),('estaHabilitado'),)
    #exclude = ('created_by', 'created_at', 'modified_by', 'modified_at',)




admin.site.register(Personas_votante_prod,Persona_VotanteAdmin)