from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin
from django.forms.models import modelform_factory
from django.apps import apps
from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from .models import announ_linea_fomento_editorial, bases_linea_fomento_editorial, contenido_bases_linea_fomento_editorial
from .forms import ModuleFormSet
from django.forms import DateInput


 
class OwnerAnnounMixin(LoginRequiredMixin):
    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

class OwnerEditAnnounMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class OwnerAnnounCreateMixin(OwnerAnnounMixin, OwnerEditAnnounMixin):
    model = announ_linea_fomento_editorial
    fields = ['portada', 'categoria', 'title', 'slug', 'fecha_inicio', 'fecha_vencimiento', 'overview', 'actividad']
    success_url = reverse_lazy('announ:manage_announ_list')
    widgets = {
        'fecha_inicio': DateInput(attrs={'type': 'datetime-local'})
    }

class OwnerAnnounEditMixin(OwnerAnnounMixin, OwnerEditAnnounMixin):
    fields = ['portada', 'categoria', 'title', 'slug', 'fecha_inicio', 'fecha_vencimiento', 'overview', 'actividad']
    success_url = reverse_lazy('announ:manage_announ_list')
    template_name = 'announces/manage/announ/form.html'
    widgets = {
        'fecha_inicio': DateInput(attrs={'type': 'datetime-local'})
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

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.announ, data=data)

    def dispatch(self, request, pk):
        self.announ = get_object_or_404(announ_linea_fomento_editorial, id=pk, owner=request.user)
        return super().dispatch(request, pk)

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
    template_name = 'announces/manage/content/form.html'

    def get_model(self, model_name):
        if model_name in ['text', 'video', 'image', 'file']:
            return apps.get_model(app_label='announces', model_name=model_name)
        return None

    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(model, exclude=['owner', 'order', 'created', 'updated'])
        return Form(*args, **kwargs)

    def dispatch(self, request, base_id, model_name, id=None):
        self.base = get_object_or_404(bases_linea_fomento_editorial, id=base_id, announ__owner=request.user)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model, id=id, owner=request.user)
        return super().dispatch(request, base_id, model_name, id)

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
