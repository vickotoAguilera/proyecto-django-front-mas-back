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

        # aca defino la ruta para la consola tecnica de la evaluacion 3 en el panel administrativo
    path('panel-admin/evaluacion-3/', views.consola_evaluacion_3, name='consola_evaluacion_3'),


    # aca defino la ruta para el catalogo interactivo frontend consumido por API REST con JavaScript
    path('catalogo-api/', views.catalogo_api, name='catalogo_api'),
]

