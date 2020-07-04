from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Personas_votante

# Register your models here.

from import_export import resources


class PersonaVotanteAdminResource(resources.ModelResource):

    class Meta:
        model   =   Personas_votante
        import_id_fields = ('cedula',)
        use_bulk = True
        skip_unchanged = True
        
class CustomPersonaVotanteAdmin(ImportExportModelAdmin):
    resource_class = PersonaVotanteAdminResource
    list_display = (('cedula'),('matricula'),('apellido'),('nombre'),('estaHabilitado'))
    search_fields = (('cedula'),('matricula'),('apellido'),('nombre'),('estaHabilitado'))
    actions = ['remove_all', ]

    def remove_all(self, request, queryset):
        queryset = Personas_votante.objects.all()
        queryset.delete()
    remove_all.short_description = "Delete all %(verbose_name_plural)s WARNING"
    remove_all.acts_on_all = True

    def changelist_view(self, request, extra_context=None):
        try:
            action = self.get_actions(request)[request.POST['action']][0]
            action_acts_on_all = action.acts_on_all
        except (KeyError, AttributeError):
            action_acts_on_all = False

        if action_acts_on_all:
            post = request.POST.copy()
            post.setlist(admin.helpers.ACTION_CHECKBOX_NAME,
                        self.model.objects.values_list('cedula', flat=True))
            request.POST = post
                
        return super().changelist_view(request, extra_context)


admin.site.register(Personas_votante,CustomPersonaVotanteAdmin)
