from django.urls import path
from .views import forum_posts

urlpatterns = [
    path('api/posts/', forum_posts, name='forum_api'),
]