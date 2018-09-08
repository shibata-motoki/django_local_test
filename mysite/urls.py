"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('anything/', include('anything.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('blog/', include('blog.urls')),
    path('memo/', include('memo.urls')),
    path('todo/', include('todo.urls')),
    # path('sougi/', include('sougi.urls')),
    # path('api_test/', include('api_test.urls')),
    path('anything/', include('anything.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns