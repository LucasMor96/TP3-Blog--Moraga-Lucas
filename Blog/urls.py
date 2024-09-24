"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from post import views
from post.views import InicioView, logout_view, registro_usuario, crear_publicacion, detalle_post, eliminar_post, editar_post
from post.views import listar_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioView.as_view(), name='inicio_view'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registro/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', registro_usuario, name='registro'),
    path('crear/', views.crear_publicacion, name='crear_publicacion'),
    path('listar/', views.listar_post, name='listar_post'),
    path('accounts/logout/', logout_view, name='logout'),
    path('publicacion/<int:id>/', detalle_post, name='detalle_post'),
    path('publicacion/eliminar/<int:id>/', eliminar_post, name='eliminar_post'),
    path('publicacion/editar/<int:id>/', editar_post, name='editar_post'), 
]

