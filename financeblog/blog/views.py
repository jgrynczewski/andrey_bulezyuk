from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from . import models


# def list_blogs(request):
#     blogs = models.Blog.objects.all()
#     return render(
#         request,
#         'blog/list.html',
#         {
#             'blogs': blogs,
#         }
#     )


class BlogListView(ListView):
    model = models.Blog
    ordering = ['-date_published']
    paginate_by = 3


# def detail_blog(request, pk):
#     blog = get_object_or_404(models.Blog, pk=pk)
#     return render(
#         request,
#         'blog/detail.html',
#         {
#             'blog': blog,
#         }
#     )


class BlogDetailView(DetailView):
    model = models.Blog


class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = models.Blog
    fields = [
        'title',
        'content',
    ]
    success_message = "Blog created successfully!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = models.Blog
    fields = ['title', 'content']
    success_message = "Blog update successfully!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        else:
            return False


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Blog
    success_message = "Blog deleted successfully"
    success_url = '/'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        else:
            return False

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)
