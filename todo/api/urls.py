from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('/<int:pk>/detail', views.todo_detail, name='todo_detail'),
]