from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Evento
from .forms import Evento30000Form, Evento20000Form, Evento10000Form, Circulacion5000Form
from .models import Evento_30000, Evento_20000, Evento_10000, Evento_5000,Subject
from usuarios.models import Profile,DeclaracionVeracidad
from django.shortcuts import get_object_or_404
from django.http import HttpResponse



@login_required
def listar_categorias(request):
    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    categorias = Subject.objects.all()


    return render(request, 'listar_categorias.html', {'categorias': categorias, 
                                                      'actividad': actividad,
                                                      'acepta_terminos_condiciones': acepta_terminos_condiciones})
@login_required
def evento(request, categoria_slug):
    # Obtener el objeto Subject basado en el slug de la categoría
    categoria = get_object_or_404(Subject, slug=categoria_slug)

    # Seleccionar el formulario correspondiente a la categoría
    if categoria.categoria == 30000:
        form_class = Evento30000Form
    elif categoria.categoria == 20000:
        form_class = Evento20000Form
    elif categoria.categoria == 10000:
        form_class = Evento10000Form
    elif categoria.categoria == 5000:
        form_class = Circulacion5000Form
    else:
        # Manejar el caso donde la categoría no tiene un formulario correspondiente
        return HttpResponse("No se encontró un formulario para esta categoría.")

    if request.method == 'POST':
        # Crear una instancia del formulario correspondiente y procesar los datos
        form = form_class(request.POST)
        if form.is_valid():
            # Guardar el formulario y redirigir a la página de éxito
            form.save()
            return redirect('success_page')  # Reemplaza 'success_page' con el nombre de la URL de tu página de éxito
    else:
        # Crear una instancia del formulario correspondiente
        form = form_class()

    return render(request, f'eventos/{categoria.categoria}.html', {'categoria': categoria, 'form': form})

@login_required
def Evento_30000(request):
    if request.method == 'POST':
        form = Evento30000Form(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a alguna página de éxito o hacer alguna acción adicional
    else:
        form = Evento30000Form()
    return render(request, 'eventos/30000.html', {'form': form})

@login_required
def Evento_20000(request):
    if request.method == 'POST':
        form = SubjectEvento(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a alguna página de éxito o hacer alguna acción adicional
    else:
        form = SubjectEvento()
    return render(request, '20000.html', {'form': form})

@login_required
def Evento_10000(request):
    if request.method == 'POST':
        form = SubjectEvento(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a alguna página de éxito o hacer alguna acción adicional
    else:
        form = SubjectEvento()
    return render(request, '10000.html', {'form': form})

@login_required
def Evento_5000(request):
    if request.method == 'POST':
        form = SubjectEvento(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a alguna página de éxito o hacer alguna acción adicional
    else:
        form = SubjectEvento()
    return render(request, '5000.html', {'form': form})



