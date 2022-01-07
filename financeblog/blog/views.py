from django.shortcuts import render
from django.shortcuts import get_object_or_404

from . import models

def list_blogs(request):
    blogs = models.Blog.objects.all()
    return render(
        request,
        'blog/list.html',
        {
            'blogs': blogs,
        }
    )


def detail_blog(request, pk):
    blog = get_object_or_404(models.Blog, pk=pk)
    return render(
        request,
        'blog/detail.html',
        {
            'blog': blog,
        }
    )
