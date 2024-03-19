from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm, \
                   UserEditForm, ProfileEditForm,ContactEditForm,Contact2EditForm,LegalEditForm,LegalEdit2Form,ContactLegalEditForm,ContactLegal2EditForm,ActivityEditForm,TermsEditForm,PostulantesEditForm
from .models import Profile,Contact_Profile,contacto,legal,contacto_legal,activity,terms,edit_profile_done,Manual_inscripcion, Manual_lineasfomento_editorial,Manual_creacion_convocatoria_fomento,Manual_editar_convocatoria_fomento,Manual_editar_configuracion,postulantes_lineas_fomentos
from django.template.loader import render_to_string
import weasyprint
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.utils.safestring import mark_safe




def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    if request.user.is_authenticated:
        usuario = request.user.profile 
        contacto= request.user.contact_profile
        terminos = request.user.terms 
        
        return render(request,
                  'account/dashboard.html',
                  {'section': 'account:dashboard','usuario': usuario,'contacto': contacto,'terminos':terminos})
    else:
        return render(request, 'account/dashboard.html', {'mensaje': 'Debes iniciar sesión para ver tu perfil'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            legal.objects.create(user=new_user)
            contacto_legal.objects.create(user=new_user)
            activity.objects.create(user=new_user)
            terms.objects.create(user=new_user)
            Contact_Profile.objects.create(user=new_user)

            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})



@staff_member_required
def admin_profile_pdf(request, perfil_id):
    perfil = get_object_or_404(Profile, id=perfil_id)
    html = render_to_string('account/admin_profile_pdf/profile_pdf.html',
                            {'perfil': perfil})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=order_{}.pdf"'.format(perfil.id)
    weasyprint.HTML(string=html,  base_url=request.build_absolute_uri() ).write_pdf(response,stylesheets=[weasyprint.CSS('account/static/css/profile.css')], presentational_hints=True)
    return response

@staff_member_required
def admin_contact_pdf(request,contacto_id):
    contacto = get_object_or_404(Contact_Profile, id=contacto_id)
    html = render_to_string('account/admin_profile_pdf/contact_pdf.html',
                            {'contacto':contacto})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=order_{}.pdf"'.format(contacto.id)
    weasyprint.HTML(string=html,  base_url=request.build_absolute_uri() ).write_pdf(response,stylesheets=[weasyprint.CSS('account/static/css/profile.css')], presentational_hints=True)
    return response

@staff_member_required
def admin_legal_pdf(request,info_legal_id):
    info_legal = get_object_or_404(legal, id=info_legal_id)
    html = render_to_string('account/admin_profile_pdf/legal_pdf.html',
                            {'info_legal':info_legal})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=order_{}.pdf"'.format(info_legal.id)
    weasyprint.HTML(string=html,  base_url=request.build_absolute_uri() ).write_pdf(response,stylesheets=[weasyprint.CSS('account/static/css/profile.css')], presentational_hints=True)
    return response



@staff_member_required
def admin_contact_legal_pdf(request,contactolegal_id):
    contactolegal = get_object_or_404(contacto_legal, id=contactolegal_id)
    html = render_to_string('account/admin_profile_pdf/contact_legal_pdf.html',
                            {'contactolegal':contactolegal})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=order_{}.pdf"'.format(contactolegal.id)
    weasyprint.HTML(string=html,  base_url=request.build_absolute_uri() ).write_pdf(response,stylesheets=[weasyprint.CSS('account/static/css/profile.css')], presentational_hints=True)
    return response

@staff_member_required
def admin_activity_pdf(request,actividad_id):
    actividad = get_object_or_404(activity, id=actividad_id)
    html = render_to_string('account/admin_profile_pdf/contact_legal_pdf.html',
                            {'actividad':actividad})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=order_{}.pdf"'.format(activity.id)
    weasyprint.HTML(string=html,  base_url=request.build_absolute_uri() ).write_pdf(response,stylesheets=[weasyprint.CSS('account/static/css/profile.css')], presentational_hints=True)
    return response

@staff_member_required
def admin_terms_pdf(request,terms_id):
    terminos = get_object_or_404(terms, id=terms_id)
    html = render_to_string('account/admin_profile_pdf/contact_legal_pdf.html',
                            {'terminos':terminos})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=order_{}.pdf"'.format(terminos.id)
    weasyprint.HTML(string=html,  base_url=request.build_absolute_uri() ).write_pdf(response,stylesheets=[weasyprint.CSS('account/static/css/profile.css')], presentational_hints=True)
    return response


@login_required
def edit(request):
    if request.user.is_authenticated:
        usuario = request.user.profile 
        contacto= request.user.contact_profile
        legal_profile = request.user.legal 
        terminos = request.user.terms
    if request.method  == 'POST' and request.user.is_authenticated :
        terminos = request.user.terms
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)        
        if user_form.is_valid() and profile_form.is_valid() :
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

 
    return render(request,
                  'account/edit_profiles/edit_profile.html',
                  {'terminos': terminos,
                   'user_form': user_form,
                   'profile_form': profile_form})


def edit_contact(request):
    if request.method == 'POST':
        contact_form =  ContactEditForm(instance=request.user.contact_profile,
                                 data=request.POST)       
        if contact_form .is_valid() :
            contact_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        contact_form =ContactEditForm(instance=request.user.contact_profile) 
    return render(request,
                  'account/edit_profiles/edit_contact_profile.html',
                  {'contact_form': contact_form })


@login_required
def edit_legal(request): 
    if request.method == 'POST' and request.user.is_authenticated:
        legal_form = LegalEditForm(instance=request.user.legal,
                                       data=request.POST,
                                       files=request.FILES)
        
        legal_profile = request.user.legal 
        if  legal_form.is_valid():
            
            legal_form.save()
            
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        legal_form = LegalEditForm(instance=request.user.legal)
        legal_profile = request.user.legal
    return render(request,
                  'account/edit_profiles/edit_legal_profile.html',
                  {'legal_form': legal_form,'legal_profile':legal_profile})
    


@login_required
def edit2_legal(request):
    if request.method == 'POST':
        legal2_form = LegalEdit2Form(instance=request.user.legal,
                                       data=request.POST,
                                       files=request.FILES)
        legal_contact = ContactLegalEditForm(instance=request.user.contacto_legal,
                                       data=request.POST,
                                       files=request.FILES)
        if  legal2_form.is_valid() and legal_contact.is_valid() :
            legal2_form.save()
            legal_contact.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        legal2_form = LegalEdit2Form(instance=request.user.legal)
        legal_contact = ContactLegalEditForm(instance=request.user.contacto_legal)
      
 
    return render(request,
                  'account/edit_profiles/edit_legal_contact.html',
                  {'legal2_form': legal2_form, 'legal_contact':legal_contact})



@login_required
def edit_activity(request):
    if request.method == 'POST':
        activity_form = ActivityEditForm(instance=request.user.activity,
                                       data=request.POST,
                                       files=request.FILES)
        if  activity_form.is_valid():
            activity_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        activity_form = ActivityEditForm(instance=request.user.activity)
    return render(request,
                  'account/edit_profiles/edit_activity_profile.html',
                  {'activity_form': activity_form})


@login_required
def edit_terms(request):
    if request.method == 'POST':
        terms_form = TermsEditForm(instance=request.user.terms,
                                       data=request.POST,
                                       files=request.FILES)
        if  terms_form.is_valid():
            terms_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        terms_form = TermsEditForm(instance=request.user.terms)

    return render(request,
                  'account/edit_profiles/edit_terms_profile.html',
                  {'terms_form':terms_form})

#MANEJADORES

@login_required
def perfil_usuario(request):
    # Verificar si el usuario está autenticado
    if request.user.is_authenticated:
        usuario = request.user.profile 
        contacto= request.user.contact_profile
        legal_profile = request.user.legal 
        terminos = request.user.terms  # Suponiendo que el perfil de usuario está relacionado con el modelo de usuario
        return render(request, 'account/profile/profile.html', {'usuario': usuario,'contacto': contacto,'terminos':terminos, 'legal_profile':legal_profile,})
    else:
        # Redirigir al usuario a la página de inicio de sesión o mostrar un mensaje de error
        return render(request, 'account/profile/profile.html', {'mensaje': 'Debes iniciar sesión para ver tu perfil'})
    

    
def sidebar(request):
    # Verificar si el usuario está autenticado
    if request.user.is_authenticated:
        usuario = request.user.profile 
        contacto= request.user.contact_profile
        legal_profile = request.user.legal 
        terminos = request.user.terms  # Suponiendo que el perfil de usuario está relacionado con el modelo de usuario
        return render(request, 'account/header.html', {'usuario': usuario,'contacto': contacto,'terminos':terminos, 'legal_profile':legal_profile,})
    else:
        # Redirigir al usuario a la página de inicio de sesión o mostrar un mensaje de error
        return render(request, 'account/header.html', {'mensaje': 'Debes iniciar sesión para ver tu perfil'})
    
    
    
@login_required
def perfil_legal(request):
    # Verificar si el usuario está autenticado
    if request.user.is_authenticated:
       usuario = request.user.profile
       legal_profile = request.user.legal 
       terminos = request.user.terms # Suponiendo que el perfil de usuario está relacionado con el modelo de usuario
       return render(request, 'account/edit_profiles/edit_legal_profile.html', {'legal_profile': legal_profile, 'usuario': usuario, 'terminos':terminos })
    else:
        # Redirigir al usuario a la página de inicio de sesión o mostrar un mensaje de error
        return render(request, 'account/edit_profiles/edit_legal_profile.html', {'mensaje': 'Debes iniciar sesión para ver tu perfil'})
    
@login_required
def perfil_activity(request):
    # Verificar si el usuario está autenticado
    if request.user.is_authenticated:
       usuario = request.user.profile
       activity_profile = request.user.legal 
       terminos = request.user.terms
        # Suponiendo que el perfil de usuario está relacionado con el modelo de usuario
       return render(request, 'account/edit_profiles/edit_activity_profile.html', {'activity_profile': activity_profile, 'usuario': usuario,'terminos':terminos })
    else:
        # Redirigir al usuario a la página de inicio de sesión o mostrar un mensaje de error
        return render(request, 'account/edit_profiles/edit_activity_profile.html', {'mensaje': 'Debes iniciar sesión para ver tu perfil'})
    
@login_required
def edit_done(request):
    # Verificar si el usuario está autenticado
    if request.user.is_authenticated:
       terminos = request.user.terms
       tecnico = edit_profile_done.objects.all()[0]
       # Suponiendo que el perfil de usuario está relacionado con el modelo de usuario
       return render(request, 'account/edit_profiles/edit_done.html', {'terminos':terminos, 'tecnico':tecnico })
    else:
        # Redirigir al usuario a la página de inicio de sesión o mostrar un mensaje de error
        return render(request, 'account/edit_profiles/edit_done.html', {'mensaje': 'Debes iniciar sesión para ver tu perfil'})
    

@login_required
def terminos_usuario(request):
    # Verificar si el usuario está autenticado
    if request.user.is_authenticated:
        terminos = request.user.terms  # Suponiendo que el perfil de usuario está relacionado con el modelo de usuario
        return render(request, 'account/sidebar.html', {'terminos':terminos})
    else:
        # Redirigir al usuario a la página de inicio de sesión o mostrar un mensaje de error
        return render(request, 'account/sidebar.html', {'mensaje': 'Debes iniciar sesión para ver tu perfil'})
    

@login_required
def user_detail(request, username):
    user = get_object_or_404(User,
                             username=username,
                             is_active=True)
    return render(request,
                  'account/profile/profile.html',
                  {'section': 'user',
                   'user': user})

@login_required
def detalle_manual(request):
    if request.user.is_authenticated:
        terminos = request.user.terms 
        manual = Manual_inscripcion.objects.first()
        return render(request, 'account/manuales/detalle_manual.html', {'manual': manual, 'terminos':terminos})
    else:
        # Redirigir al usuario a la página de inicio de sesión o mostrar un mensaje de error
        return render(request, 'account/manuales/detalle_manual.html', {'mensaje': 'Debes iniciar sesión para ver tu perfil'})

@login_required
def detalle_manual_lineafomento(request):
    if request.user.is_authenticated:
        terminos = request.user.terms 
        manual= Manual_lineasfomento_editorial.objects.first()  # Suponiendo que solo hay un manual, ajusta esto según tus necesidades
        return render(request, 'account/manuales/detalle_manual_lineafomento.html', {'manual': manual, 'terminos': terminos})
    else:
        # Redirigir al usuario a la página de inicio de sesión o mostrar un mensaje de error
        return render(request, 'account/manuales/detalle_manual_lineafomento.html', {'mensaje': 'Debes iniciar sesión para ver tu perfil'})

@login_required
def detalle_manual_creacion_convocatoria_fomento(request):
    # Obtener el objeto del manual de inscripción
    manual = Manual_creacion_convocatoria_fomento.objects.first()  # Suponiendo que solo hay un manual, ajusta esto según tus necesidades

    # Renderizar la plantilla con los detalles del manual
    return render(request, 'account/manuales/detalle_manual_creacion_convocatoria_fomento.html', {'manual': manual})

@login_required
def detalle_manual_editar_convocatoria_fomento(request):
    # Obtener el objeto del manual de inscripción
    manual = Manual_editar_convocatoria_fomento.objects.first()  # Suponiendo que solo hay un manual, ajusta esto según tus necesidades

    # Renderizar la plantilla con los detalles del manual
    return render(request, 'account/manuales/detalle_manual_editar_convocatoria_fomento.html', {'manual': manual})

@login_required
def detalle_manual_editar_configuracion(request):
    # Obtener el objeto del manual de inscripción
    manual = Manual_editar_configuracion.objects.first()  # Suponiendo que solo hay un manual, ajusta esto según tus necesidades

    # Renderizar la plantilla con los detalles del manual
    return render(request, 'account/manuales/detalle_manual_editar_configuracion.html', {'manual': manual})



