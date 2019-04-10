from django.shortcuts import render, get_object_or_404, redirect 
from django.utils import timezone

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Blog


def index(request):

    blogs = Blog.objects.all

    tmpb = Blog.objects

    return render(request, 'index.html', {'blogs':blogs, 'tmpb':tmpb})


def new(request):
    if request.method == 'POST':
        blog = Blog()
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        img = request.FILES['image']
        fs = FileSystemStorage()
        blog.image = fs.save(img.name, img)
        blog.date = timezone.datetime.now()
        blog.save()

        return redirect('/blog/'+str(blog.id))

    else:
        return render(request, 'new.html')


def detail(request, blog_id):

    blog = get_object_or_404(Blog, pk = blog_id)
    #blog = Blog.objects.get(pk=blog_id)

    return render(request, 'detail.html', {'blog':blog})


def edit(request, blog_id):

    blog = get_object_or_404(Blog, pk = blog_id)
    
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()

        return redirect('/blog/'+str(blog.id))

    else:
        
        return render(request, 'edit.html', {'blog':blog})


def delete(request, blog_id):

    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()

    return redirect('/')