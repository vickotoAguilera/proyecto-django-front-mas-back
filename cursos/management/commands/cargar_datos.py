import json
from django.core.management.base import BaseCommand
from django.conf import settings
from cursos.models import Categoria, Instructor, Curso


# aca creo mi comando personalizado para ejecutarlo desde la terminal: python manage.py cargar_datos
class Command(BaseCommand):
    help = "Carga los datos iniciales desde front/data/cursos.json hacia la base de datos SQLite"

    def handle(self, *args, **options):
        # 1. aca busco la ruta absoluta hacia el archivo JSON que generamos con IA
        ruta_json = settings.BASE_DIR / 'front' / 'data' / 'cursos.json'

        # 2. aca abro y leo el archivo JSON con codificacion UTF-8 para no perder caracteres especiales
        with open(ruta_json, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 3. aca recorro la lista de categorias del JSON y las guardo en mi base de datos
        # uso update_or_create para que si el registro ya existe lo actualice, y si no existe lo cree
        # de esta forma evito duplicar registros si llego a ejecutar el comando mas de una vez
        for cat in data['categorias']:
            Categoria.objects.update_or_create(
                id=cat['id'],
                defaults={
                    'nombre': cat['nombre'],
                    'descripcion': cat['descripcion']
                }
            )
        self.stdout.write(self.style.SUCCESS('Categorías cargadas con éxito'))

        # 4. aca recorro la lista de instructores del JSON y los guardo en la base de datos
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

        # 5. aca recorro la lista de cursos del JSON
        for cur in data['cursos']:
            # como Curso tiene claves foraneas (ForeignKey), aca primero busco los objetos
            # reales de Categoria e Instructor en la base de datos usando sus IDs
            categoria_obj = Categoria.objects.get(id=cur['categoria_id'])
            instructor_obj = Instructor.objects.get(id=cur['instructor_id'])

            # ahora creo o actualizo el curso asignandole los objetos relacionados
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


