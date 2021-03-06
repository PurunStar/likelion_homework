from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs' :blogs, 'posts':posts})

def details(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'details.html', {'detail': details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def edit(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/' + str(blog.id))
    return render(request,'edit.html',{'blog':blog})


def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('/')
