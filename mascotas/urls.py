from django.urls import path
from mascotas import views


urlpatterns = [
    path('', views.index_mascotas, name="index_mascotas"),
    path('agregar_mascotas/', views.agregar_mascotas, name="agregar_mascotas"),
    path('borrar_mascotas/<identificador>', views.borrar_mascotas, name="borrar_mascotas"),
    path('actualizar_mascotas/', views.actualizar_mascotas, name="actualizar_action_mascotas"),
    path('actualizar_mascotas/<identificador>', views.actualizar_mascotas, name="actualizar_mascotas"),
    path('buscar_mascotas/', views.buscar_mascotas, name="buscar_mascotas"),
]
