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
