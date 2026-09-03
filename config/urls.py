from django.contrib import admin
from django.urls import path, include

# aca defino las rutas principales de todo el proyecto Django
urlpatterns = [
    # ruta del panel de administracion nativo de Django
    path('admin/', admin.site.urls),

    # aca conecto e incluyo todas las URLs de mi app 'cursos' para que respondan desde la raiz ('')
    path('', include('cursos.urls')),
]



