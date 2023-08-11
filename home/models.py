from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
import datetime
# Create your models here.
# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='', null = True, blank = True)
    imagen_2 = models.ImageField(upload_to='', null = True, blank = True)
    detalle_principal = models.TextField(null=True, blank=True)
    detalle = models.TextField(null=True, blank=True)
    fecha = models.DateField(default=now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE,)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name='Blog'
        verbose_name_plural='Blogs'
    def __str__(self):
        return self.titulo

class Proyecto(models.Model):
    TIPO_PROYECTO = [
        ('S','Software'),
        ('D','Diseño'),
        ('F','Fotografía'),
    ]
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='', null = True, blank = True)
    rol_realizado = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    empresa = models.CharField(max_length=200)
    tipo_proyecto = models.CharField(blank=True, null=True, choices=TIPO_PROYECTO, max_length=50)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
    def __str__(self):
        return self.nombre
    
class QuienSoy(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name='QuienSoy'
        verbose_name_plural='QuienSoy'
    def __str__(self):
        return self.titulo
    

class RespuestaBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    comentario = models.TextField(null=True, blank=True)
    fecha_hora = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='RespuestaBlog'
        verbose_name_plural='RespuestasBlog'
    def __str__(self):
        return self.nombre