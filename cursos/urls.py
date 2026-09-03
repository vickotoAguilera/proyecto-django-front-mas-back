from django.urls import path
from . import views

# aca defino las rutas (URLs) especificas de mi aplicacion 'cursos'
urlpatterns = [
    # ruta raiz ('') -> llama a mi vista index (el catalogo general con buscador)
    path('', views.index, name='inicio'),

    # ruta dinamica por slug ('curso/<slug>/') -> llama a mi vista detalle_curso
    # <slug:slug> captura el texto de la URL (ej: 'python-desde-cero') y se lo pasa como argumento a la funcion
    path('curso/<slug:slug>/', views.detalle_curso, name='detalle_curso'),
]


