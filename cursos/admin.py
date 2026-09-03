from django.contrib import admin
from .models import Categoria, Instructor, Curso


# aca configuro como se administra el modelo Categoria en el panel /admin/
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion'] # columnas visibles en la tabla
    search_fields = ['nombre']               # barra de busqueda por nombre


# aca configuro el modelo Instructor en el panel de administracion
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especialidad', 'email', 'anios_experiencia'] # datos visibles
    list_filter = ['especialidad', 'anios_experiencia']                     # filtros laterales
    search_fields = ['nombre', 'email']                                     # busqueda por nombre o correo


# aca configuro el modelo Curso en el panel de administracion
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'instructor', 'nivel', 'precio', 'duracion_horas']
    list_filter = ['categoria', 'instructor', 'nivel']  # filtros laterales rapidos
    search_fields = ['titulo', 'descripcion']           # buscador por texto
    prepopulated_fields = {'slug': ('titulo',)}         # hace que el slug se escriba solo al tipear el titulo


