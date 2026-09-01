from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('curso/<slug:slug>/', views.detalle_curso, name='detalle_curso'),
]
