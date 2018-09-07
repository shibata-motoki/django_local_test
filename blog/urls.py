from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('post', views.post_list, name='post_list'),
    path('', views.index, name='blog'),
]