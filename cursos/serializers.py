from rest_framework import serializers
from django.utils.text import slugify
import uuid
from .models import Categoria, Instructor, Curso

# aca defino el serializador de Categoria (convierte el modelo Categoria a JSON y viceversa)
# regla de oro para la defensa: NUNCA usar fields = '__all__' para evitar la exposicion silenciosa de datos sensibles
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion']


# aca defino el serializador de Instructor
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'nombre', 'especialidad', 'email', 'anios_experiencia']


# aca defino el serializador de Curso con validaciones de negocio en el servidor
class CursoSerializer(serializers.ModelSerializer):
    # aca agrego campos calculados de solo lectura para enriquecer la respuesta JSON sin necesidad de hacer queries extras
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')
    instructor_nombre = serializers.ReadOnlyField(source='instructor.nombre')

    class Meta:
        model = Curso
        fields = [
            'id',
            'titulo',
            'slug',
            'descripcion',
            'nivel',
            'duracion_horas',
            'precio',
            'categoria',
            'categoria_nombre',
            'instructor',
            'instructor_nombre',
        ]
        # el slug lo autogenera el servidor para garantizar formato URL valido
        read_only_fields = ['slug']

    # validacion en servidor: el precio no puede ser negativo
    def validate_precio(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio del curso no puede ser un valor negativo.")
        return value

    # validacion en servidor: la duracion debe ser mayor a 0 horas
    def validate_duracion_horas(self, value):
        if value <= 0:
            raise serializers.ValidationError("La duración debe ser mayor a 0 horas.")
        return value

    # si se crea un curso por API y no trae slug, lo generamos automaticamente a partir del titulo
    def create(self, validated_data):
        if not validated_data.get('slug'):
            base_slug = slugify(validated_data.get('titulo', 'curso'))
            # agregamos sufijo unico para evitar colisiones de slug en base de datos
            validated_data['slug'] = f"{base_slug}-{uuid.uuid4().hex[:6]}"
        return super().create(validated_data)
