import json
from django.core.management.base import BaseCommand
from django.conf import settings
from cursos.models import Categoria, Instructor, Curso


class Command(BaseCommand):
    help = "Carga los datos iniciales desde front/data/cursos.json hacia la base de datos"

    def handle(self, *args, **options):
        # 1. Ruta al archivo JSON
        ruta_json = settings.BASE_DIR / 'front' / 'data' / 'cursos.json'

        # 2. Abrir y leer el JSON
        with open(ruta_json, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 3. Cargar Categorías
        for cat in data['categorias']:
            Categoria.objects.update_or_create(
                id=cat['id'],
                defaults={
                    'nombre': cat['nombre'],
                    'descripcion': cat['descripcion']
                }
            )
        self.stdout.write(self.style.SUCCESS('Categorías cargadas con éxito'))

        # 4. Cargar Instructores
        for inst in data['instructores']:
            Instructor.objects.update_or_create(
                id=inst['id'],
                defaults={
                    'nombre': inst['nombre'],
                    'especialidad': inst['especialidad'],
                    'email': inst['email'],
                    'anios_experiencia': inst['anios_experiencia']
                }
            )
        self.stdout.write(self.style.SUCCESS('Instructores cargados con éxito'))

        # 5. Cargar Cursos
        for cur in data['cursos']:
            categoria_obj = Categoria.objects.get(id=cur['categoria_id'])
            instructor_obj = Instructor.objects.get(id=cur['instructor_id'])

            Curso.objects.update_or_create(
                id=cur['id'],
                defaults={
                    'titulo': cur['titulo'],
                    'slug': cur['slug'],
                    'descripcion': cur['descripcion'],
                    'nivel': cur['nivel'],
                    'duracion_horas': cur['duracion_horas'],
                    'precio': cur['precio'],
                    'categoria': categoria_obj,
                    'instructor': instructor_obj
                }
            )
        self.stdout.write(self.style.SUCCESS('Cursos cargados con éxito'))
