from django.shortcuts import render

from blog.models import Blog


def blog_list(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog_list.html', context)