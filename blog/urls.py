from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import api_views

router = DefaultRouter()
router.register('posts', api_views.PostViewSet, basename='post')

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('posts/', views.get_all_posts, name='get-all-posts'),
    path('posts/create/', views.create_post, name='create-post'),
    path('posts/<int:id>/', views.get_post, name='post-detail'),
    path('posts/<int:id>/edit/', views.edit_post, name='edit-post'),
    path('posts/<int:id>/delete/', views.delete_post, name='delete-post'),
    path('api/login/', api_views.api_login, name='api-login'),
    path('api/', include(router.urls)),
]