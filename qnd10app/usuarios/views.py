from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserEditForm2,UserRegistrationForm, \
                   UserEditForm, ProfileEditForm,Contact1EditForm, \
                    Contact2EditForm,Contact3EditForm,ContactForm, \
                    LegalEditForm,Legal2EditForm, \
                    ActivityEditForm, DeclaratoriaEditForm
                    
from .models import Profile, edit_contact1,edit_contact2,Contacts, Legal,Activity,DeclaracionVeracidad, Dashboard, confirmacion
from editorial_literaria.models import ManualCreateConvocatoria
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
import weasyprint
from django.core.cache import cache
from editorial_literaria.models import ManualCreateConvocatoria, ManualEditConvocatoria,ManualInscripcion
from .models import PrivacyPolicy, TermsOfUse, ActivityPrivacyPolicy,ActivityTermsOfUse
from actividades_espacio_publico.models import Evento_30000, Evento_20000, Evento_10000, Evento_5000

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
                    user_profile = Profile.objects.get(user=user)
                    return redirect('usuarios:dashboard')
                else:
                    return HttpResponse('Disabled account')
            else:
                form = LoginForm()
                return render(request, 'registration/editorial_literario/login_fail.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'registration/editorial_literario/login.html', {'form': form})


def user_activity_login(request):
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
                    user_profile = Profile.objects.get(user=user)
                    return redirect('usuarios:dashboard')
                else:
                    return HttpResponse('Disabled account')
            else:
                form = LoginForm()
                return render(request, 'registration/actividades_espacio_publico/login_fail.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'registration/actividades_espacio_publico/login.html', {'form': form})




def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
  
            
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
           

            # Create the user profile and related objects
            Profile.objects.create(user=new_user)
            Contacts.objects.create(user=new_user)
            #edit_contact1.objects.create(user=new_user)
            #edit_contact2.objects.create(user=new_user)
            Legal.objects.create(user=new_user)
            Activity.objects.create(user=new_user)
            DeclaracionVeracidad.objects.create(user=new_user)
            #Espacio publico
            Evento_30000.objects.create(user=new_user)
            Evento_20000.objects.create(user=new_user)
            Evento_10000.objects.create(user=new_user)
            Evento_5000.objects.create(user=new_user)

            return render(request, 'usuarios/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'usuarios/register.html', {'user_form': user_form})


def activity_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
  
            
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            group = Group.objects.get(name='Postular_a_convocatorias')
            new_user.groups.add(group)

            # Create the user profile and related objects
            Profile.objects.create(user=new_user)
            Contacts.objects.create(user=new_user)
            #edit_contact1.objects.create(user=new_user)
            #edit_contact2.objects.create(user=new_user)
            Legal.objects.create(user=new_user)
            Activity.objects.create(user=new_user)
            DeclaracionVeracidad.objects.create(user=new_user)
            return render(request, 'usuarios/activity_register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'usuarios/activity_register.html', {'user_form': user_form})





@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
       # user_form2 = UserEditForm2(instance=request.name, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid()  :
            user_form.save()
            profile_form.save()
           
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
       # UserEditForm2 = UserEditForm2(instance=request.name)
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'usuarios/edit_profile/edit.html',
                  {'user_form': user_form,
                 #  'user_form2': user_form2,
                   'profile_form': profile_form})


@login_required
def edit_contact(request):
    contacts = get_object_or_404(Contacts, user=request.user)
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        # Utiliza la instancia correcta para el formulario
        contact_form = ContactForm(request.POST, instance=contacts)
        if contact_form.is_valid():
            contact_instance = contact_form.save(commit=False)
            paises_residencias = contact_instance.pais_residencias

            if 'EC' in paises_residencias:  # Condición para Ecuador en la lista de países
                # Redireccionar a una URL específica para Ecuador
                return redirect('usuarios:edit_contact2')
            else:
                # Redireccionar a una URL predeterminada si no cumple ninguna condición
                return redirect('usuarios:edit_contact4')
        else:
            messages.error(request, 'Error actualizando tu perfil')
    else:
        contact_form = ContactForm(instance=contacts)
    return render(request, 'usuarios/edit_profile/edit_contact1.html', {'contact_form': contact_form, 'contacts': contacts, 'profile': profile})

@login_required
def edit_contact2(request):
    contacts = get_object_or_404(Contacts, user=request.user)
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        # Utiliza la instancia correcta para el formulario
        contact2_form = Contact1EditForm(request.POST, instance=contacts)
        if contact2_form.is_valid():
            contact2_instance = contact2_form.save(commit=False)
            provincia_cantones_ecuador = contact2_instance.provincia_cantones_ecuador

            if 'Quito' in provincia_cantones_ecuador:  # Condición para Ecuador en la lista de países
                # Redireccionar a una URL específica para Ecuador
                return redirect('usuarios:edit_contact3')
            else:
                # Redireccionar a una URL predeterminada si no cumple ninguna condición
                return redirect('usuarios:edit_contact4')
        else:
            messages.error(request, 'Error actualizando tu perfil')
    else:
        contact2_form = Contact1EditForm(instance=contacts)
    return render(request, 'usuarios/edit_profile/edit_contact2.html', {'contact2_form': contact2_form, 'contacts': contacts, 'profile': profile})


@login_required
def edit_contact3(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        contact3_form = Contact2EditForm(request.POST, instance=request.user.contacts)
        if contact3_form.is_valid():
            # Guardar los datos del formulario en la base de datos
            contact3_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('usuarios:edit_legal')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        contact3_form = Contact2EditForm(instance=request.user.contacts)
    return render(request, 'usuarios/edit_profile/edit_contact3.html', {'contact3_form': contact3_form, 'profile': profile})


@login_required
def edit_contact4(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        contact4_form = Contact3EditForm(request.POST, instance=request.user.contacts)
        if contact4_form.is_valid():
            # Guardar los datos del formulario en la base de datos
            contact4_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('usuarios:edit_legal')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        contact4_form = Contact2EditForm(instance=request.user.contacts)
    return render(request, 'usuarios/edit_profile/edit_contact4.html', {'contact4_form': contact4_form, 'profile': profile})







@login_required
def edit_legal(request):
    profile = get_object_or_404(Profile, user=request.user)
    legal = get_object_or_404(Legal, user=request.user)
    
    if request.method == 'POST':
        legal_form = LegalEditForm(instance=legal, data=request.POST)
        if legal_form.is_valid():
            legal_instance = legal_form.save(commit=False)
            # Obtener el valor de tipo_personeria del formulario
            tipo_personeria = legal_instance.tipo_personeria
            
            if tipo_personeria == 'Natural':  # Condición para el primer valor
                # Redireccionar a una URL específica para valor1
                return redirect('usuarios:edit_activity')
            elif tipo_personeria == 'Jurídico':  # Condición para el segundo valor
                # Redireccionar a una URL específica para valor2
                return redirect('usuarios:edit_legal2')
            else:
                # Redireccionar a una URL predeterminada si no cumple ninguna condición
                return redirect('usuarios:edit_activity')
        else:
            messages.error(request, 'Error actualizando tu perfil')
    else:
        legal_form = LegalEditForm(instance=legal)
    
    return render(request, 'usuarios/edit_profile/edit_legal1.html', {'legal_form': legal_form, 'legal': legal, 'profile': profile })


@login_required
def edit_legal2(request):
    profile = get_object_or_404(Profile, user=request.user)
    legal = get_object_or_404(Legal, user=request.user)
    if request.method == 'POST':
        legal2_form = Legal2EditForm(instance=legal, data=request.POST)
        if legal2_form.is_valid():
            legal2_form.save()
            messages.success(request, 'Perfil actualizado exitosamente')
            return redirect('usuarios:edit_activity')
        else:
            messages.error(request, 'Error actualizando tu perfil')
    else:
        legal2_form = Legal2EditForm(instance=legal)
    return render(request, 'usuarios/edit_profile/edit_legal2.html', {'legal2_form': legal2_form, 'legal': legal, 'profile': profile })

@login_required
def edit_activity(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        activity_form =  ActivityEditForm(instance=request.user.activity,
                                 data=request.POST)
        if activity_form.is_valid():
            activity_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('usuarios:edit_declaratoria')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        activity_form = ActivityEditForm(instance=request.user.activity)
    return render(request,
                  'usuarios/edit_profile/edit_activity.html',
                  {'activity_form':  activity_form , 'profile': profile })

@login_required
def edit_declaratoria(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        declaratoria_form =  DeclaratoriaEditForm(instance=request.user.declaracionveracidad,
                                 data=request.POST)
        if declaratoria_form.is_valid():
            declaratoria_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('usuarios:confirmacion')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        declaratoria_form = DeclaratoriaEditForm(instance=request.user.declaracionveracidad)
    return render(request,
                  'usuarios/edit_profile/edit_declaratoria.html',
                  {'declaratoria_form':   declaratoria_form, 'profile': profile  })


@login_required
def confirmacion(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'usuarios/edit_profile/confirmacion.html', {'profile': profile})

@login_required
def contact_profile(request):
    contact = Contacts.objects.get(user=request.user)
    return render(request,
                  'usuarios/edit_profile/edit_contact1.html',
                  {'contact': 'contact'})



@login_required
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    actividad = profile.activity
    try:
        declaracion = DeclaracionVeracidad.objects.get(user=request.user)
        acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    except DeclaracionVeracidad.DoesNotExist:
        # Si no hay declaración existente, establece el valor de acepta_terminos_condiciones en False
        acepta_terminos_condiciones = False
    
    manuales = Dashboard.objects.all()
    user_groups = request.user.groups.all()
    is_tecnicos_group = any(group.name == 'Administrar' for group in user_groups)
    
    return render(request, 'usuarios/dashboard.html', {
        'section': 'dashboard',
        'profile': profile,
        'actividad': actividad,
        'acepta_terminos_condiciones': acepta_terminos_condiciones,
        'manuales': manuales,
        'is_tecnicos_group': is_tecnicos_group
    })



@login_required
def nav_bar(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,
                  'usuarios/header.html',
                  {'profile':'profile'})

@login_required
def profile_view(request):
    # Obtener el perfil del usuario actualmente autenticado
    profile = Profile.objects.get(user=request.user)
    contact = Contacts.objects.get(user=request.user)
    legal = Legal.objects.get(user=request.user)
    activity = Activity.objects.get(user=request.user)
    declaratoria = DeclaracionVeracidad.objects.get(user=request.user)
    terminos  = DeclaracionVeracidad.objects.get(user=request.user)
    user_groups = request.user.groups.all()
    is_tecnicos_group = any(group.name == 'tecnicos' for group in user_groups)
    return render(request, 'usuarios/profile.html', {'profile': profile,'contact': contact,'legal': legal,'activity': activity,'declaratoria': declaratoria, 'terminos': terminos, 'is_tecnicos_group':is_tecnicos_group })

@login_required
def config_view(request):
    # Obtener el perfil del usuario actualmente autenticado
    profile = Profile.objects.get(user=request.user)
    return render(request, 'usuarios/config.html', {'profile': profile})


@staff_member_required
def admin_profile_pdf(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    html = render_to_string('usuarios/pdf_profiles/pdf.html',
                            {'profile': profile})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=order_{}.pdf"'.format(profile.id)
    weasyprint.HTML(string=html,  base_url=request.build_absolute_uri() ).write_pdf(response,stylesheets=[weasyprint.CSS('static/assets/css/profiles.css')], presentational_hints=True)
    return response

def sidebar(request):
    terminos  = DeclaracionVeracidad.objects.get(user=request.user)
    user_groups = request.user.groups.all()
    is_tecnicos_group = any(group.name == 'tecnicos' for group in user_groups)
    return render(request,
                  'usuarios/edit_profile/sidebar.html',
                  {'section': 'sidebar', 'is_tecnicos_group': is_tecnicos_group, 'terminos': terminos})


@login_required
def manual_crear_convocatoria(request):
    manuales = ManualCreateConvocatoria.objects.all()
    return render(request,
                   'editorial_literaria/manuales/crear_convocatoria.html',
                     {'manuales': manuales})



@login_required
def manual_editar_convocatoria(request):
    manuales = ManualEditConvocatoria.objects.all()
    return render(request,
                   'editorial_literaria/manuales/edit_convocatoria.html',
                     {'manuales': manuales})


@login_required
def manual_inscripcion(request):
    manuales = ManualInscripcion.objects.all()
    return render(request,
                  'editorial_literaria/manuales/inscripcion.html',
                  {'manuales': manuales})

def privacy_policy_view(request):
    privacy_policy_items = PrivacyPolicy.objects.all()
    return render(request, 'legal/privacy_policy.html', {'items': privacy_policy_items})

def terms_of_use_view(request):
    terms_of_use_items = TermsOfUse.objects.all()
    return render(request, 'legal/terms_of_use.html', {'items': terms_of_use_items})


def activity_privacy_policy_view(request):
    privacy_policy_items = ActivityPrivacyPolicy.objects.all()
    return render(request, 'legal/activity_privacy_policy.html', {'items': privacy_policy_items})

def activity_terms_of_use_view(request):
    terms_of_use_items = ActivityTermsOfUse.objects.all()
    return render(request, 'legal/activity_terms_of_use.html', {'items': terms_of_use_items})


