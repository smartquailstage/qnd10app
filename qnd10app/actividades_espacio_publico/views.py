from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Evento
from .forms import Evento30000Form, Evento20000Form, Evento10000Form, Evento5000Form
from .models import Evento_30000, Evento_20000, Evento_10000, Evento_5000,Subject
from usuarios.models import Profile,DeclaracionVeracidad
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages


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
def evento_30000(request):

    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    try:
        event = Evento_30000.objects.get(user=request.user)
    except Evento_30000.DoesNotExist:
        event = None

    if request.method == 'POST':
        if event:
            event_30000_form = Evento30000Form(instance=event, data=request.POST)
        else:
            event_30000_form = Evento30000Form(data=request.POST)

        if event_30000_form.is_valid():
            event = event_30000_form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event updated successfully')
            return redirect('usuarios:edit_declaratoria')
        else:
            messages.error(request, 'Error updating your event')
    else:
        event_30000_form = Evento30000Form(instance=event)
    return render(request, 'eventos/30000.html', {'event_30000_form': event_30000_form, 'profile': profile, 'event': event,
                                                   'actividad': actividad,
                                                      'acepta_terminos_condiciones': acepta_terminos_condiciones})

@login_required
def evento_20000(request):
    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    
    try:
        event = Evento_20000.objects.get(user=request.user)
        event_20000_form = Evento20000Form(instance=event)
    except Evento_20000.DoesNotExist:
        event = None
        event_20000_form = Evento20000Form()

    if request.method == 'POST':
        if event:
            event_20000_form = Evento20000Form(instance=event, data=request.POST)
        else:
            event_20000_form = Evento20000Form(data=request.POST)

        if event_20000_form.is_valid():
            event = event_20000_form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event updated successfully')
            return redirect('usuarios:edit_declaratoria')
        else:
            messages.error(request, 'Error updating your event')

    return render(request, 'eventos/20000.html', {'event_20000_form': event_20000_form, 'profile': profile, 'event': event,
                                                   'actividad': actividad, 'acepta_terminos_condiciones': acepta_terminos_condiciones})

@login_required
def evento_10000(request):
    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    
    try:
        event = Evento_10000.objects.get(user=request.user)
        event_10000_form = Evento10000Form(instance=event)
    except Evento_10000.DoesNotExist:
        event = None
        event_10000_form = Evento10000Form()

    if request.method == 'POST':
        if event:
            event_10000_form = Evento10000Form(instance=event, data=request.POST)
        else:
            event_10000_form = Evento10000Form(data=request.POST)

        if event_10000_form.is_valid():
            event = event_10000_form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event updated successfully')
            return redirect('usuarios:edit_declaratoria')
        else:
            messages.error(request, 'Error updating your event')

    return render(request, 'eventos/10000.html', {'event_10000_form': event_10000_form, 'profile': profile, 'event': event,
                                                   'actividad': actividad, 'acepta_terminos_condiciones': acepta_terminos_condiciones})


@login_required
def evento_5000(request):
    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    
    try:
        event = Evento_5000.objects.get(user=request.user)
        event_5000_form = Evento5000Form(instance=event)
    except Evento_5000.DoesNotExist:
        event = None
        event_5000_form = Evento5000Form()

    if request.method == 'POST':
        if event:
            event_5000_form = Evento5000Form(instance=event, data=request.POST)
        else:
            event_5000_form = Evento5000Form(data=request.POST)

        if event_5000_form.is_valid():
            event = event_5000_form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event updated successfully')
            return redirect('usuarios:edit_declaratoria')
        else:
            messages.error(request, 'Error updating your event')

    return render(request, 'eventos/5000.html', {'event_5000_form': event_5000_form, 'profile': profile, 'event': event,
                                                   'actividad': actividad, 'acepta_terminos_condiciones': acepta_terminos_condiciones})
