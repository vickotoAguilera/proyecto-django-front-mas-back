from django.contrib import admin
from .models import Categoria, Instructor, Curso

# aca personalizo el titulo del panel de administracion para que no salga el de django por defecto
admin.site.site_header = "Directorio de Cursos — Panel Administrativo"
admin.site.site_title = "Directorio de Cursos"
admin.site.index_title = "Gestión del Catálogo y Personal"


# aca creo la tabla en linea (inline) para ver y gestionar los cursos que pertenecen a una categoria
class CursoCategoriaInline(admin.TabularInline):
    model = Curso
    extra = 0                                     # aca evito que cree filas vacias de mas
    fields = ['titulo', 'nivel', 'precio', 'duracion_horas']
    show_change_link = True                       # aca coloco un boton directo para ir a la ficha del curso

# aca creo la tabla en linea (inline) para ver y gestionar los cursos asignados a un instructor
class CursoInstructorInline(admin.TabularInline):
    model = Curso
    extra = 0
    fields = ['titulo', 'categoria', 'nivel', 'precio', 'duracion_horas']
    show_change_link = True


# aca configuro el modelo Categoria en el panel de administracion extendido con inlines
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']
    ordering = ['nombre']
    inlines = [CursoCategoriaInline]              # aca incrusto la coleccion de cursos dentro de la categoria


# aca configuro el modelo Instructor en el panel de administracion extendido con inlines
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especialidad', 'email', 'anios_experiencia']
    list_filter = ['especialidad', 'anios_experiencia']
    search_fields = ['nombre', 'email', 'especialidad']
    ordering = ['nombre']
    inlines = [CursoInstructorInline]             # aca incrusto los cursos asignados a este instructor


# aca configuro el modelo Curso en el panel de administracion
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'instructor', 'nivel', 'precio_formateado', 'duracion_horas']
    list_filter = ['categoria', 'nivel', 'instructor']
    search_fields = ['titulo', 'descripcion']
    prepopulated_fields = {'slug': ('titulo',)}  # aca hago que el slug se escriba solo al tipear el titulo
    ordering = ['-id']                            # aca ordeno para ver los mas nuevos primero
    list_per_page = 10                            # aca limito a 10 cursos por pagina

    # aca formateo el precio con moneda chilena para que se lea ordenado en la grilla del admin
    @admin.display(description='Precio (CLP)')
    def precio_formateado(self, obj):
        return f"${obj.precio:,.0f} CLP".replace(",", ".")


