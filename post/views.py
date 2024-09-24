from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView


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
            return redirect('listar_post')
        return render(request, 'crear_publicacion.html')




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

