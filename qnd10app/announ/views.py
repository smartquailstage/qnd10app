from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin
from django.forms.models import modelform_factory
from django.apps import apps
from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from .models import announ_linea_fomento_editorial, bases_linea_fomento_editorial, contenido_bases_linea_fomento_editorial,Categorias_linea_fomento_editorial,postulantes
from .forms import ModuleFormSet,AnnounEnrollForm
from django.forms import DateInput
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.core.cache import cache
from django.db.models import Count
from account.models import terms
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from .forms import CourseEnrollForm



@login_required
def dashboard(request):
    if request.user.is_authenticated:
        terminos = request.user.terms       
        return render(request,
                  'dashboard.html',
                  {'section': 'announ:dashboard','terminos':terminos})
    else:
        return render(request, 'dashboard.html', {'mensaje': 'Debes iniciar sesión para ver tu perfil'})


# Aca empieza la app de creacion de convocatorias
    
class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self ).get_queryset()
        return qs.filter(owner=self.request.user)
    
class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class OwnerAnnounMixin(OwnerMixin, LoginRequiredMixin):
    model = announ_linea_fomento_editorial
    fields = ['fomento','categoria','title', 'slug', 'overview']
    sucess_url = reverse_lazy('announ:manage_announ_list')


class OwnerAnnounEditMixin(OwnerAnnounMixin, OwnerEditMixin):
    fields = ['fomento','categoria', 'title', 'slug', 'overview']
    sucess_url = reverse_lazy('announ:manage_announ_list')
    template_name = 'announces/manage/announ/form.html'

class OwnerAnnounCreateMixin(OwnerAnnounMixin, OwnerAnnounEditMixinOwnerAnnounEditMixin):
    model = announ_linea_fomento_editorial
    fields = ['portada', 'fomento','categoria','title', 'slug', 'fecha_inicio', 'fecha_vencimiento', 'overview', 'actividad']
    success_url = reverse_lazy('announ:manage_announ_list')
    widgets = {
        'fecha_inicio': DateInput(attrs={'type': 'datetime-local'}),
        'fecha_vencimiento': DateInput(attrs={'type': 'datetime-local'})
    }



class ManageAnnounListView(OwnerAnnounMixin, ListView):
    template_name = 'announces/manage/announ/list.html'

    def get_queryset(self):
        return announ_linea_fomento_editorial.objects.filter(owner=self.request.user)

class AnnounCreateView(PermissionRequiredMixin, OwnerAnnounCreateMixin, CreateView):
    model = announ_linea_fomento_editorial 
    permission_required = 'announ.add_announ'

class AnnounUpdateView(PermissionRequiredMixin, OwnerAnnounEditMixin, UpdateView):
    model = announ_linea_fomento_editorial 
    permission_required = 'announ.change_announ'

class AnnounDeleteView(PermissionRequiredMixin, OwnerAnnounMixin, DeleteView):
    model = announ_linea_fomento_editorial 
    template_name = 'announces/manage/announ/delete.html'
    success_url = reverse_lazy('announ:manage_announ_list')
    permission_required = 'announ.delete_announ'

class AnnounBasesUpdateView(TemplateResponseMixin, View):
    template_name = 'announces/manage/base/formset.html'
    announ = None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.announ, data=data)

    def dispatch(self, request, pk):
        self.announ = get_object_or_404(announ_linea_fomento_editorial, id=pk, owner=request.user)
        return super(AnnounBasesUpdateView, self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'announ': self.announ, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('announ:manage_announ_list')
        return self.render_to_response({'announ': self.announ, 'formset': formset})

class ContenidoCreateUpdateView(TemplateResponseMixin, View):
    base = None
    model = None
    obj = None
    template_name = 'announces/manage/content/form.html'

    def get_model(self, model_name):
        if model_name in ['text', 'video', 'image', 'file']:
            return apps.get_model(app_label='announces', model_name=model_name)
        return None

    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(model, exclude=['owner', 'order', 'created', 'updated'])
        return Form(*args, **kwargs)

    def dispatch(self, request, base_id, model_name, id=None):
        self.base = get_object_or_404(bases_linea_fomento_editorial,
                                       id=base_id,
                                       announ__owner=request.user)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model,
                                         id=id,
                                         owner=request.user)
        return super(ContenidoCreateUpdateView,
           self).dispatch(request, base_id, model_name, id)

    
  

    def get(self, request, base_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response({'form': form, 'object': self.obj})

    def post(self, request, base_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj, data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            if not id:
                contenido_bases_linea_fomento_editorial.objects.create(base=self.base, item=obj)
            return redirect('announ:base_contenido_list', self.base.id)
        return self.render_to_response({'form': form, 'object': self.obj})

class ContenidoDeleteView(View):
    def post(self, request, id):
        contenido = get_object_or_404(contenido_bases_linea_fomento_editorial, id=id, base__announ__owner=request.user)
        base = contenido.base
        contenido.item.delete()
        contenido.delete()
        return redirect('announ:bases_contenido_list', base.id)

class BaseContenidoListView(TemplateResponseMixin, View):
    template_name = 'announces/manage/base/contenido_list.html'

    def get(self, request, base_id):
        base = get_object_or_404(bases_linea_fomento_editorial, id=base_id, base__owner=request.user)
        return self.render_to_response({'base': base})

class BaseOrderView(CsrfExemptMixin, JsonRequestResponseMixin, View):
    def post(self, request):
        for id, order in self.request_json.items():
            bases_linea_fomento_editorial.objects.filter(id=id, announ__owner=request.user).update(order=order)
        return self.render_json_response({'saved': 'OK'})

class ContenidoOrderView(CsrfExemptMixin, JsonRequestResponseMixin, View):
    def post(self, request):
        for id, order in self.request_json.items():
            contenido_bases_linea_fomento_editorial.objects.filter(id=id, base__announ__owner=request.user).update(order=order)
        return self.render_json_response({'saved': 'OK'})




class AnnounListView(View):
    model = announ_linea_fomento_editorial
    template_name = 'announces/announ/list.html'

    def get(self, request, categoria=None): 
        terminos = None
        if request.user.is_authenticated:
            terminos = request.user.terms 
        categorias = Categorias_linea_fomento_editorial.objects.annotate(
            total_announces=Count('announces'))
        announces = announ_linea_fomento_editorial.objects.annotate(
            total_bases=Count('bases'))

        if categoria:
            categoria = get_object_or_404(Categorias_linea_fomento_editorial, slug=categoria)
            announces = announces.filter(categoria=categoria)

        return TemplateResponse(request, self.template_name, {'categorias': categorias,
                                        'categoria': categoria,
                                        'announces': announces, 'terminos':terminos})

class AnnounDetailView(LoginRequiredMixin, DetailView):
    model = announ_linea_fomento_editorial
    template_name = 'announces/announ/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enroll_form'] = AnnounEnrollForm(initial={'announ': self.object})
        if self.request.user.is_authenticated:
            terminos = self.request.user.terms
            context['terminos'] = terminos
        return context

  
    

class PostulantesEnrollAnnounView(LoginRequiredMixin, FormView):
    announ = None
    template_name = 'postulantes/announ/detail.html'
    form_class = AnnounEnrollForm


    def form_valid(self, form):
        self.announ = form.cleaned_data['announ']
        self.announ.postulantes.add(self.request.user)
        return super(PostulantesEnrollAnnounView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('announ:postulante_announ_detail', args=[self.announ.id])


class PostulantesAnnounListView(LoginRequiredMixin, ListView):

    model = announ_linea_fomento_editorial
    template_name = 'postulantes/announ/list.html'
  

    
    def get_queryset(self):
        qs = super(PostulantesAnnounListView,self).get_queryset()
        return qs.filter(postulantes__in=[self.request.user])



class PostulantesAnnounDetailView(DetailView):
    model = announ_linea_fomento_editorial
    template_name = 'postulantes/announ/detail.html'

    def get_queryset(self):
        qs = super(PostulantesAnnounDetailView, self).get_queryset()
        return qs.filter(postulantes=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(PostulantesAnnounDetailView, self).get_context_data(**kwargs)
        announ = self.get_object()
        if 'base_id' in self.kwargs:
            context['base'] = announ.bases.get(id=self.kwargs['base_id'])
        else:
            context['base'] = announ.bases.first()  # Use first() instead of all()[0]
        return context
    




