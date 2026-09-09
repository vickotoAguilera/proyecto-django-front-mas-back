from django.contrib import admin
from .models import Categoria, Instructor, Curso

# aca personalizo el titulo del panel de administracion para que no salga el de django por defecto
admin.site.site_header = "Directorio de Cursos — Panel Administrativo"
admin.site.site_title = "Directorio de Cursos"
admin.site.index_title = "Gestión del Catálogo y Personal"


# aca configuro el modelo Categoria en el panel de administracion
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']
    ordering = ['nombre']


# aca configuro el modelo Instructor en el panel de administracion
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especialidad', 'email', 'anios_experiencia']
    list_filter = ['especialidad', 'anios_experiencia']
    search_fields = ['nombre', 'email', 'especialidad']
    ordering = ['nombre']


# aca configuro el modelo Curso en el panel de administracion
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'instructor', 'nivel', 'precio', 'duracion_horas']
    list_filter = ['categoria', 'nivel', 'instructor']
    search_fields = ['titulo', 'descripcion']
    prepopulated_fields = {'slug': ('titulo',)}  # aca hago que el slug se escriba solo al tipear el titulo
    ordering = ['-id']                            # aca ordeno para ver los mas nuevos primero
    list_per_page = 10                            # aca limito a 10 cursos por pagina

