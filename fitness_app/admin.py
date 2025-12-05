from django.contrib import admin
from .models import Entrenador, Gimnasio, Articulo, Habito

@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especialidad', 'experiencia']
    list_filter = ['especialidad']
    search_fields = ['nombre', 'especialidad']

@admin.register(Gimnasio)
class GimnasioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion', 'telefono']
    filter_horizontal = ['entrenadores']

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'fecha_publicacion']
    list_filter = ['fecha_publicacion']
    search_fields = ['titulo', 'contenido']

@admin.register(Habito)
class HabitoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'fecha', 'ejercicio_realizado', 'duracion_minutos']
    list_filter = ['fecha', 'usuario']