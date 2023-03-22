from django.contrib import admin
from django.urls import path
from . import views

########################################################################################################################

urlpatterns = [
    path('crear_equipo/', views.crear_equipo, name="crear_equipo"),
    path('modificar_equipo/<int:id>', views.modificar_equipo, name="modificar_equipo"),
    path('eliminar_equipo/<int:id>', views.eliminar_equipo, name="eliminar_equipo"),
    path('consultar_equipo/', views.consultar_equipo, name="consultar_equipo"),
    path('buscar_equipo/', views.buscar_equipo, name="buscar_equipo"),

########################################################################################################################

    path('crear_trofeo/', views.crear_trofeo, name="crear_trofeo"),
    path('modificar_trofeo/<int:id>', views.modificar_trofeo, name="modificar_trofeo"),
    path('eliminar_trofeo/<int:id>', views.eliminar_trofeo, name="eliminar_trofeo"),
    path('consultar_trofeo/', views.consultar_trofeo, name="consultar_trofeo"),
    path('buscar_trofeo/', views.buscar_trofeo, name="buscar_trofeo"),

########################################################################################################################

    path('crear_torneo/', views.crear_torneo, name="crear_torneo"),
    path('modificar_torneo/<int:id>', views.modificar_torneo, name="modificar_torneo"),
    path('eliminar_torneo/<int:id>', views.eliminar_torneo, name="eliminar_torneo"),
    path('consultar_torneo/', views.consultar_torneo, name="consultar_torneo"),
    path('buscar_torneo/', views.buscar_torneo, name="buscar_torneo"),
]