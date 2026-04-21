from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('posts/', views.get_all_posts, name='get-all-posts'),
    path('posts/create/', views.create_post, name='create-post'),
    path('posts/<int:id>/', views.get_post, name='post-detail'),
    path('posts/<int:id>/edit/', views.edit_post, name='edit-post'),
    path('posts/<int:id>/delete/', views.delete_post, name='delete-post'),
]