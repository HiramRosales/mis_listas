from django.urls import path
from familia import views


urlpatterns = [
    path('', views.index_familia, name="index_familia"),
    path('agregar_familia/', views.agregar_familia, name="agregar_familia"),
    path('borrar_familia/<identificador>', views.borrar_familia, name="borrar_familia"),
    path('actualizar_familia/', views.actualizar_familia, name="actualizar_action_familia"),
    path('actualizar_familia/<identificador>', views.actualizar_familia, name="actualizar_familia"),
    path('buscar_familia/', views.buscar_familia, name="buscar_familia"),
]
