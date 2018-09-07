from django.urls import path

from . import views

app_name = 'memo'

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.memo_list, name='memo_list'),
    path('<int:pk>', views.memo_detail, name='memo_detail'),
    path('<int:pk>/del', views.memo_del, name='memo_del'),
    path('<int:pk>/edit', views.memo_edit, name='memo_edit'),
]