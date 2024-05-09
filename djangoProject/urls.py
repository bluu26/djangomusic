"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mjuzik_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('add_article/', views.add_article, name='add_article'),
    path('bands/', views.bands, name='bands'),
    path('add_band/', views.add_band, name='add_band'),
    path('delete_band/<int:pk>/', views.delete_band, name='delete_band'),
    path('albums/', views.albums, name='albums'),
    path('add_album/', views.add_album, name='add_album'),
    path('admin/', admin.site.urls),
]
