from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', views.cover, name='cover'),
    path('about/', views.about, name='about'),
    path('home/', PostListView.as_view(), name='home'),
    path('blogpost/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('blogpost/new/', PostCreateView.as_view(), name='post-create'),
    path('blogpost/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), 
    path('blogpost/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
]
