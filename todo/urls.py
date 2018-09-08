from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:pk>/detail', views.todo_detail, name='todo_detail'),
    path('add', views.todo_add, name='todo_add'),
    path('<int:pk>/del', views.todo_delete, name='todo_delete'),
]
