from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.formulario_migrantes, name='insertar_migrantes'),
    path('<int:id>/',views.formulario_migrantes, name='actulizacion_migrante'),
    path('dlete/<int:id>/',views.eliminar_migrantes,name='eliminar_migrante'),
    path('tablaMigrantes/',views.tabla_migrantes, name='lista_migrantes')
  
]
