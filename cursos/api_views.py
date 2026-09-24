from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Categoria, Instructor, Curso
from .serializers import CategoriaSerializer, InstructorSerializer, CursoSerializer
from .services import obtener_conversion_monedas

# aca defino el ViewSet de Categoria: gestiona automaticamente GET (listar/detalle), POST, PUT, DELETE
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('nombre')
    serializer_class = CategoriaSerializer
    search_fields = ['nombre']
    filter_backends = [filters.SearchFilter]


# aca defino el ViewSet de Instructor: gestiona automaticamente el CRUD completo para instructores
class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all().order_by('nombre')
    serializer_class = InstructorSerializer
    search_fields = ['nombre', 'especialidad', 'email']
    filter_backends = [filters.SearchFilter]


# aca defino el ViewSet de Curso: agrupa el CRUD de cursos con optimizacion select_related, filtros y busqueda
class CursoViewSet(viewsets.ModelViewSet):
    # uso select_related para traer Categoria e Instructor en una sola consulta SQL optimizada
    queryset = Curso.objects.select_related('categoria', 'instructor').all().order_by('-id')
    serializer_class = CursoSerializer

    # backends para permitir filtros por categoria/nivel, busqueda por texto y ordenamiento
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['categoria', 'nivel']
    search_fields = ['titulo', 'descripcion']
    ordering_fields = ['precio', 'duracion_horas', 'id']


# aca defino el endpoint que expone la conversion monetaria consumiendo la API externa de mindicador.cl
class IndicadoresEconomicosView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        precio = request.query_params.get('precio', '29990')
        try:
            precio_num = float(precio)
        except ValueError:
            precio_num = 29990.0

        datos = obtener_conversion_monedas(precio_num)
        return Response(datos)
