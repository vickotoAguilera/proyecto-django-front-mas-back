from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

# aca defino las rutas principales de todo el proyecto django
urlpatterns = [
    # aca redirijo el favicon para que no tire error 404 en el navegador
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),

    # aca conecto el panel de administracion nativo de django
    path('admin/', admin.site.urls),

    # aca conecto el sistema de login y logout nativo de django
    path('accounts/', include('django.contrib.auth.urls')),

    # aca incluyo las rutas de mi aplicacion cursos
    path('', include('cursos.urls')),
]


