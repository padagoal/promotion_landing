from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Personas_votante

# Register your models here.

from import_export import resources


class PersonaVotanteAdminResource(resources.ModelResource):

    class Meta:
        model   =   Personas_votante
        import_id_fields = ('cedula',)
        
class CustomPersonaVotanteAdmin(ImportExportModelAdmin):
    resource_class = PersonaVotanteAdminResource
    list_display = (('cedula'),('matricula'),('apellido'),('nombre'),('estaHabilitado'))
    search_fields = (('cedula'),('matricula'),('apellido'),('nombre'),('estaHabilitado'))
    


admin.site.register(Personas_votante,CustomPersonaVotanteAdmin)
