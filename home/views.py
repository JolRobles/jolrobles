from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def proyectos(request):
    proyectos = Proyecto.objects.filter(activo=True)
    context = {
        'proyectos':proyectos
    }
    return render(request, 'home/proyectos.html', context)
def proyecto_detail(request, pk):
    proyecto = Proyecto.objects.get(pk=pk)
    proyectos = Proyecto.objects.filter(activo=True)
    context = {
        'proyecto':proyecto,
        'proyectos':proyectos
    }
    return render(request, 'home/proyecto_detail.html', context)

def contactos(request):

    return render(request, 'home/contacto.html')

def blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    blogs = Blog.objects.all()
    context = {
        'blog':blog,
        'blogs':blogs,
    }
    return render(request, 'home/blog.html', context)

def list_blog(request):
    blogs = Blog.objects.filter(activo=True)
    context = {
        'blogs':blogs
    }
    return render(request, 'home/blog_list.html', context)
