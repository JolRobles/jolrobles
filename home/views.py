from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    blogs = Blog.objects.all()
    context = {
        'blog':blog,
        'blogs':blogs,
    }
    return render(request, 'home/blog.html', context)

def list_blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request, 'home/blog_list.html', context)
