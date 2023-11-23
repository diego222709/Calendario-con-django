from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('fecha/',views.fecha, name='fecha'),
    path('calendario/',views.calendario, name='calendario'),

    path('registrarfechas/', views.registrar_fechas, name='registrar_fechas'),
]