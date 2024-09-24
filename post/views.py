from django import forms
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404

class InicioView(TemplateView):
    template_name = 'inicio.html'

@login_required
def crear_publicacion(request):
        if request.method == 'POST':
            titulo = request.POST.get('titulo')
            contenido = request.POST.get('contenido')
            nueva_publicacion = Post.objects.create(
                titulo=titulo,
                contenido=contenido,
                autor=request.user
            )
            nueva_publicacion.save()
            ##Mensaje de éxito de la creación de la publicación de django
            messages.success(request, 'La publicación se ha creado con éxito.')
            return redirect('listar_post')
        return render(request, 'crear_publicacion.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión ha cerrado la sesión.')
    return redirect('inicio_view')


def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

from django.shortcuts import render
from .models import Post

def listar_post(request):
    publicaciones = Post.objects.all()
    return render(request, 'listar_post.html', {'publicaciones': publicaciones})

@login_required
def detalle_post(request, id):
    publicacion = get_object_or_404(Post, id=id)
    return render(request, 'detalle_post.html', {'publicacion': publicacion})

@login_required
def eliminar_post(request, id):
    publicacion = get_object_or_404(Post, id=id, autor=request.user)  # Solo permite eliminar si es el autor
    if request.method == 'POST':
        publicacion.delete()
        messages.success(request, 'Publicación eliminada con éxito.')
        return redirect('listar_post')
    return render(request, 'eliminar_confirmacion.html', {'publicacion': publicacion})


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido']

@login_required
def editar_post(request, id):
    publicacion = get_object_or_404(Post, id=id, autor=request.user)  # Solo permite editar si es el autor
    ## Si el método es POST, se actualiza la publicación
    if request.method == 'POST':
        form = PublicacionForm(request.POST, instance=publicacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publicación actualizada con éxito.')
            return redirect('detalle_post', id=publicacion.id)
    ## Si no se muestra el formulario con los datos del post
    else:
        form = PublicacionForm(instance=publicacion)
    return render(request, 'editar_post.html', {'form': form, 'publicacion': publicacion})