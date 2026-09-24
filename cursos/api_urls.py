from django.urls import path
from rest_framework.routers import DefaultRouter
from .api_views import CategoriaViewSet, InstructorViewSet, CursoViewSet, IndicadoresEconomicosView

# aca instancio el enrutador predeterminado de DRF que genera automaticamente todas las rutas REST
# buenas practicas: recursos nombrados con sustantivos en plural (/categorias/, /instructores/, /cursos/)
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='api-categoria')
router.register(r'instructores', InstructorViewSet, basename='api-instructor')
router.register(r'cursos', CursoViewSet, basename='api-curso')

# aca exporto las URLs del router sumando el endpoint de la API externa
urlpatterns = [
    # aca expongo el endpoint REST que consume la API externa de mindicador.cl
    path('indicadores/', IndicadoresEconomicosView.as_view(), name='api-indicadores'),
] + router.urls
