from django.urls import path
from . import views

urlpatterns = [
    # aca conecto la ruta raiz al catalogo principal
    path('', views.index, name='inicio'),

    # aca defino la ruta para crear un curso nuevo (va antes del slug para que no choque)
    path('curso/nuevo/', views.curso_crear, name='curso_crear'),

    # aca defino la ruta para ver el detalle de cada curso segun su slug
    path('curso/<slug:slug>/', views.detalle_curso, name='detalle_curso'),

    # aca defino la ruta para editar los datos de un curso
    path('curso/<slug:slug>/editar/', views.curso_editar, name='curso_editar'),

    # aca defino la ruta para borrar un curso con confirmacion
    path('curso/<slug:slug>/eliminar/', views.curso_eliminar, name='curso_eliminar'),
]

