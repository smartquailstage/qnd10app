from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm, \
                   UserEditForm, ProfileEditForm,ContactEditForm,Contact2EditForm,LegalEditForm,ContactLegalEditForm,ContactLegal2EditForm,ActivityEditForm,Activity2EditForm,TermsEditForm
from .models import Profile,contacto,legal,contacto_legal,activity,terms


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
        contacto= request.user.contacto
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
            contacto.objects.create(user=new_user)
            legal.objects.create(user=new_user)
            contacto_legal.objects.create(user=new_user)
            activity.objects.create(user=new_user)
            terms.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})




@login_required
def edit(request):
    if request.method == 'POST':
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
                  {'user_form': user_form,
                   'profile_form': profile_form})

@login_required
def edit_contact(request):
    if request.method == 'POST':
        contact_form = ContactEditForm(instance=request.user.contacto,
                                       data=request.POST,
                                       files=request.FILES)
        contact2_form = Contact2EditForm(instance=request.user.contacto,
                                       data=request.POST,
                                       files=request.FILES)
      
        
        if  contact_form.is_valid() and contact2_form.is_valid() :
            contact_form.save()
            contact2_form.save()


            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        contact_form = ContactEditForm(instance=request.user.contacto)
        contact2_form = Contact2EditForm(instance=request.user.contacto)
 
    return render(request,
                  'account/edit_profiles/edit_contact_profile.html',
                  {'contact_form': contact_form,
                   'contact2_form': contact2_form,})

@login_required
def edit_legal(request):
    if request.method == 'POST':
        legal_form = LegalEditForm(instance=request.user.legal,
                                       data=request.POST,
                                       files=request.FILES)
        legal_contact_form = ContactLegalEditForm(instance=request.user.contacto_legal,
                                       data=request.POST,
                                       files=request.FILES)
        legal_contact2_form = ContactLegal2EditForm(instance=request.user.contacto_legal,
                                       data=request.POST,
                                       files=request.FILES)
      
        
        if  legal_form.is_valid() and legal_contact_form.is_valid() and legal_contact_form.is_valid() :
            legal_form.save()
            legal_contact_form.save()
            legal_contact2_form.save()


            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        legal_form = ContactLegalEditForm(instance=request.user.legal)
        legal_contact_form = Contact2EditForm(instance=request.contacto_legal)
        legal_contact2_form = ContactLegal2EditForm(instance=request.contacto_legal)
 
    return render(request,
                  'account/edit_profiles/edit_legal_profile.html',
                  {'legal_form': legal_form,
                   'legal_contact_form': legal_contact_form,
                   'legal_contact2_form': legal_contact2_form,})

@login_required
def edit_activity(request):
    if request.method == 'POST':
        activity_form = ActivityEditForm(instance=request.user.activity,
                                       data=request.POST,
                                       files=request.FILES)
        activity2_form = Activity2EditForm(instance=request.user.activity,
                                       data=request.POST,
                                       files=request.FILES)
      
        
        if   activity_form.is_valid() and activity2_form.is_valid()  :
            activity_form.save()
            activity2_form.save()
          


            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        activity_form = ActivityEditForm(instance=request.user.activity)
        activity2_form = Activity2EditForm(instance=request.user.activity)

 
    return render(request,
                  'account/edit_profiles/edit_activity_profile.html',
                  {'activity_form': activity_form,
                   'activity2_form': activity2_form})

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



@login_required
def perfil_usuario(request):
    # Verificar si el usuario está autenticado
    if request.user.is_authenticated:
        usuario = request.user.profile 
        contacto= request.user.contacto
        terminos = request.user.terms  # Suponiendo que el perfil de usuario está relacionado con el modelo de usuario
        return render(request, 'account/profile/profile.html','account/dashboard.html', {'usuario': usuario,'contacto': contacto,'terminos':terminos})
    else:
        # Redirigir al usuario a la página de inicio de sesión o mostrar un mensaje de error
        return render(request, 'account/profile/profile.html', {'mensaje': 'Debes iniciar sesión para ver tu perfil'})
    
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


