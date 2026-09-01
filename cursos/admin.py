from django.contrib import admin
from .models import Categoria, Instructor, Curso


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especialidad', 'email', 'anios_experiencia']
    list_filter = ['especialidad', 'anios_experiencia']
    search_fields = ['nombre', 'email']


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'instructor', 'nivel', 'precio', 'duracion_horas']
    list_filter = ['categoria', 'instructor', 'nivel']
    search_fields = ['titulo', 'descripcion']
    prepopulated_fields = {'slug': ('titulo',)}
