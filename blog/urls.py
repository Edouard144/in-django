from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('posts/<int:id>/', views.get_post, name='get-post'),
    path('posts/', views.get_all_posts, name='get-all-posts'),
    path('posts/<int:id>/', views.get_post, name='post-detail'),
]