from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_inscripcion, name='agregar_inscripcion'),
    path('', views.listar_inscripciones, name='listar_inscripciones'),
    path('modificar/<int:id>/', views.modificar_inscripcion, name='modificar_inscripcion'),
    path('eliminar/<int:id>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
]
