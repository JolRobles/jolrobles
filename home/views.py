from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # user = form.save()
            # user.is_staff = True
            # user.is_superuser = True
            # user.active = True
            # user.save()
            # Iniciar sesión al usuario después del registro
            # login(request, user)
            return redirect('home:list_blog')  # Cambia 'home' por el nombre de tu vista de inicio
    else:
        form = UserCreationForm()
    context = { 
        'title':"Register",
        'form':form
    }
    return render(request, 'home/register.html', context)

def index(request):
    quien_soy = QuienSoy.objects.filter()
    context = {
        'quien_soy':quien_soy
    }
    return render(request, 'index.html', context)

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
    blog_object = Blog.objects.get(pk=pk)
    respuestas = RespuestaBlog.objects.filter(blog=blog_object)
    blogs = Blog.objects.all()
    respuesta_formulario = RespuestaBlogForm()
    if request.method == 'POST':
        respuesta_formulario = RespuestaBlogForm(request.POST, request.FILES)
        if respuesta_formulario.is_valid():
            respuesta = respuesta_formulario.save(commit=False)
            respuesta.blog = blog_object
            respuesta.save()
            messages.success(request, f'Respuesta Creada, ¡Muchas gracias!')
            return redirect('home:blog', blog_object.pk)
        else:
            context = {
                'blog_object':blog_object,
                'blogs':blogs,
                'respuesta_form':respuesta_formulario,
                'respuestas':respuestas,
            }
            messages.error(request, 'Corrija los errores')
            print(respuesta_formulario.errors)
            return render(request, 'home/blog.html', context)
    context = {
        'blog_object':blog_object,
        'blogs':blogs,
        'respuesta_form':respuesta_formulario,
        'respuestas':respuestas
    }
    return render(request, 'home/blog.html', context)

def list_blog(request):
    blogs = Blog.objects.filter(activo=True)
    context = {
        'blogs':blogs
    }
    return render(request, 'home/blog_list.html', context)
