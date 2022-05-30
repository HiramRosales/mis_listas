from django.urls import path
from carros import views


urlpatterns = [
    path('', views.index_carro, name="index_carro"),
    path('agregar_carro/', views.agregar_carro, name="agregar_carro"),
    path('borrar_carro/<identificador>', views.borrar_carro, name="borrar_carro"),
    path('actualizar_carro/', views.actualizar_carro, name="actualizar_action_carro"),
    path('actualizar_carro/<identificador>', views.actualizar_carro, name="actualizar_carro"),
    path('buscar_carro/', views.buscar_carro, name="buscar_carro"),
]
