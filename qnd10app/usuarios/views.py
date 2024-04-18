from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, \
                   UserEditForm, ProfileEditForm,Contact1EditForm, \
                    Contact2EditForm,Contact3EditForm,Contact4EditForm, \
                    LegalEditForm,Legal2EditForm, \
                    ActivityEditForm, DeclaratoriaEditForm
                    
from .models import Profile, Contacts, Legal,Activity,DeclaracionVeracidad, Dashboard, confirmacion
from editorial_literaria.models import ManualCreateConvocatoria
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
import weasyprint

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['Nombre de Usuario'],
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
            Contacts.objects.create(user=new_user)
            Legal.objects.create(user=new_user)
            Activity.objects.create(user=new_user)
            DeclaracionVeracidad.objects.create(user=new_user)
            return render(request,
                          'usuarios/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'usuarios/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'usuarios/edit_profile/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


@login_required
def edit_contact(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        contact1_form = Contact1EditForm(request.POST, instance=request.user.contacts)
        if contact1_form.is_valid():
            # Guardar los datos del formulario en la base de datos
            contact1_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('usuarios:edit_legal')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        contact1_form = Contact1EditForm(instance=request.user.contacts)
    return render(request, 'usuarios/edit_profile/edit_contact1.html', {'contact1_form': contact1_form, 'profile': profile})


@login_required
def edit_contact2(request):
    if request.method == 'POST':
        contact2_form = Contact2EditForm(instance=request.user,
                                 data=request.POST)
        if contact2_form.is_valid():
            contact2_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        contact2_form = Contact2EditForm(instance=request.user)
    return render(request,
                  'usuarios/edit_profile/edit_contact2.html',
                  {'contact2_form': contact2_form})

@login_required
def edit_contact3(request):
    if request.method == 'POST':
        contact3_form = Contact3EditForm(instance=request.user,
                                 data=request.POST)
        if contact3_form.is_valid():
            contact3_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        contact3_form = Contact3EditForm(instance=request.user)
    return render(request,
                  'usuarios/edit_profile/edit_contact3.html',
                  {'contact3_form': contact3_form})

@login_required
def edit_contact4(request):
    if request.method == 'POST':
        contact4_form = Contact4EditForm(instance=request.user,
                                 data=request.POST)
        if contact4_form.is_valid():
            contact4_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        contact4_form = Contact4EditForm(instance=request.user)
    return render(request,
                  'usuarios/edit_profile/edit_contact4.html',
                  {'contact4_form': contact4_form})

@login_required
def edit_legal(request):
    profile = get_object_or_404(Profile, user=request.user)
    legal = get_object_or_404(Legal, user=request.user)
    
    if request.method == 'POST':
        legal1_form = LegalEditForm(instance=legal, data=request.POST)
        if legal1_form.is_valid():
            legal1_form.save()
            messages.success(request, 'Un perfil legal de usuario acaba de ser grabado')
            return redirect('usuarios:edit_activity')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        legal1_form = LegalEditForm(instance=legal)
    
    return render(request, 'usuarios/edit_profile/edit_legal1.html', {'legal1_form': legal1_form, 'legal': legal, 'profile': profile })


@login_required
def edit_legal2(request):
    profile = get_object_or_404(Profile, user=request.user)
    legal = Legal.objects.get(user=request.user)
    if request.method == 'POST':
        legal2_form =  Legal2EditForm(instance=request.user.legal,
                                 data=request.POST)
        if legal2_form.is_valid():
            legal2_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('usuarios:edit_activity')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        legal2_form = LegalEditForm(instance=request.user.legal)
    return render(request,
                  'usuarios/edit_profile/edit_legal2.html',
                  {'legal2_form': legal2_form, 'legal':legal, 'profile': profile  })

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
    dashboards = Dashboard.objects.all()
    return render(request,
                  'usuarios/dashboard.html',
                  {'section': 'dashboard', 'profile': profile, 'dashboards': dashboards})

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
    return render(request, 'usuarios/profile.html', {'profile': profile,'contact': contact,'legal': legal,'activity': activity,'declaratoria': declaratoria})

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

@login_required
def Manuales(request):
    manuales = Manual.objects.all()
    terminos = DeclaracionVeracidad.objects.get(user=request.user)
    user_groups = request.user.groups.all()
    is_tecnicos_group = any(group.name == 'tecnicos' for group in user_groups)
    return render(request,
                  'usuarios/edit_profile/sidebar.html',
                  {'section': 'sidebar','manuales': 'manuales','is_tecnicos_group': is_tecnicos_group, 'terminos': terminos})


