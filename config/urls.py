from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# aca defino las rutas principales de todo el proyecto django
urlpatterns = [
    # aca redirijo el favicon para que no tire error 404 en el navegador
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),

    # aca conecto el panel de administracion nativo de django
    path('admin/', admin.site.urls),

    # aca conecto el sistema de login y logout nativo de django
    path('accounts/', include('django.contrib.auth.urls')),

    # aca conecto los endpoints de autenticacion stateless con JSON Web Tokens (Simple JWT)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # aca conecto las rutas de la API RESTful versionada (/api/v1/cursos/, /api/v1/categorias/, etc.)
    path('api/v1/', include('cursos.api_urls')),

    # aca incluyo las rutas de mi aplicacion cursos (interfaz web tradicional)
    path('', include('cursos.urls')),
]


