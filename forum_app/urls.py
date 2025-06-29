from django.urls import path
from .views import forum_list, create_post

urlpatterns = [
    path('', forum_list, name='forum_list'),
    path('create/', create_post, name='create_post'),
]