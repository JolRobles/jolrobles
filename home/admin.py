from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.
@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    '''Admin View for Blog'''

    list_display = (
        'id',
        'titulo',
        'imagen',
        'fecha',
        'autor',
        'activo',
        )

@admin.register(Proyecto)
class ProyectoAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = (
        'id',
        'nombre',
        'activo',
        )

@admin.register(QuienSoy)
class QuienSoyAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = (
        'id',
        'titulo',
        )
    
@admin.register(RespuestaBlog)
class RespuestaBlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = (
        'id',
        'nombre',
        )