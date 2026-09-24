from rest_framework.routers import DefaultRouter
from .api_views import CategoriaViewSet, InstructorViewSet, CursoViewSet

# aca instancio el enrutador predeterminado de DRF que genera automaticamente todas las rutas REST
# buenas practicas: recursos nombrados con sustantivos en plural (/categorias/, /instructores/, /cursos/)
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='api-categoria')
router.register(r'instructores', InstructorViewSet, basename='api-instructor')
router.register(r'cursos', CursoViewSet, basename='api-curso')

# aca exporto las URLs generadas por el router
urlpatterns = router.urls
