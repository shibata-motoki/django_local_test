from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('/<int:pk>/detail', views.todo_detail, name='todo_detail'),
    path('/<int:pk>/update', views.todo_update, name='todo_update'),
    path('/<int:pk>/delete', views.todo_delete, name='todo_delete'),
]