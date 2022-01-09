from django.urls import path

from . import views

app_name = 'advice'

urlpatterns = [
    path('create/', views.QuestionCreateView.as_view(), name='question_create'),
    path('<int:pk>/delete', views.QuestionDeleteView.as_view(), name='question_delete'),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('', views.QuestionListView.as_view(), name='question_list'),
]