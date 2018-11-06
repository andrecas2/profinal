from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ComicsForm
from comics.models import Comic, Editorial, Autor
from django.contrib.auth.decorators import login_required


@login_required
def comic_nueva(request):
    if request.method == 'POST':
        formulario = ComicsForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listado_comics')
            messages.add_message(request, messages.SUCCESS, 'comic Guardada Exitosamente')
    else:
        formulario = ComicsForm()
    return render(request, 'comics/comic_editar.html', {'formulario': formulario})

def listado_comics(request):
    comic = Comic.objects.all()
    return render(request, 'comics/listadocomics.html', {'comic': comic})

def detalle_comic(request, pk):
    comic = get_object_or_404(Comic, pk=pk)
    editorial = Editorial.objects.all()
    autor = Autor.objects.all()
    return render(request, 'comics/detallecomic.html', {'comic': comic, 'editorial': editorial, 'autor': autor})

def eliminar_comic(request, pk):
    comic = get_object_or_404(Comic, pk=pk)
    comic.delete()
    return redirect('listado_comics')

def editar_comic(request, pk):
    comic = get_object_or_404(Comic, pk=pk)
    if request.method == 'POST':
        formulario = ComicsForm(request.POST, request.FILES, instance=comic)
        if formulario.is_valid():
            comic = formulario.save()
            comic.save()
            return redirect('detalle_comic', pk=comic.pk)

    else:
        formulario = ComicsForm(instance=comic)
    return render(request, 'comics/comic_editar.html', {'formulario': formulario})
