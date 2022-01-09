from django.urls import path

from . import views

urlpatterns = [
    # path('', views.list_blogs, name='list_blogs'),
    path('', views.BlogListView.as_view(), name='list_blogs'),
    # path('blog/<int:pk>', views.detail_blog, name='detail_blog'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='detail_blog'),
    path('blog/create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
]