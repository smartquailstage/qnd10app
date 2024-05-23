from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, \
                                      DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin, \
                                       PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from django.forms.models import modelform_factory
from django.apps import apps
from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from django.db.models import Count
from .models import Subject, Project,Author,Content,BibliographicReference
from .forms import ModuleFormSet, BiblioProjectForm,BiblioProjectFormSet,WorkPlanProjectFormSet
from students.forms import CourseEnrollForm
#from students.forms import CourseEnrollForm
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from usuarios.models import Profile,DeclaracionVeracidad
from django.contrib import messages

class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)


class OwnerProjectMixin(OwnerMixin, LoginRequiredMixin):
    model = Project
    fields = ['course','subject', 'title', 'slug', 'overview','plan','cv']
    success_url = reverse_lazy('proyectos:manage_project_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar las variables adicionales al contexto
        context['author'] = self.authors()
        context['profile'] = self.profile()
        context['actividad'] = self.get_profile()
        context['acepta_terminos_condiciones'] = self.get_declaracion()
        return context
    

    
    def authors(self):
        user = self.request.user
        authors = Author.objects.filter(user=user)
        if authors.exists():
            titles = [author.title for author in authors]
            return titles
        else:
            return ["No registra autores este proyecto"] 
    
    def profile(self):
        user = self.request.user
        profile = get_object_or_404(Profile, user=user)
        return profile

    def get_profile(self):
        user = self.request.user
        profile = get_object_or_404(Profile, user=user)
        return profile.activity
    
    def get_declaracion(self):
        user = self.request.user
        declaracion = get_object_or_404(DeclaracionVeracidad, user=user)
        return declaracion.acepta_terminos_condiciones

class OwnerProjectEditMixin(OwnerProjectMixin, OwnerEditMixin):
    fields = ['course','subject', 'title', 'slug', 'overview','plan','cv']
    success_url = reverse_lazy('proyectos:manage_project_list')
    template_name = 'projects/manage/course/form.html'




class ManageProjectListView(OwnerProjectMixin, ListView):
    template_name = 'projects/manage/course/list.html'


class ProjectCreateView(
                       OwnerProjectEditMixin,
                       CreateView):
    pass


class ProjectUpdateView(
                       OwnerProjectEditMixin,
                       UpdateView):
    pass


class ProjectDeleteView(
                       OwnerProjectMixin,
                       DeleteView):
    template_name = 'projects/manage/course/delete.html'
    success_url = reverse_lazy('proyectos:manage_project_list')
    pass


class ProjectAuthorUpdateView(TemplateResponseMixin, View):
    template_name = 'projects/manage/module/formset.html'
    fields = ['title','description']
    project = None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.project, data=data)

    def dispatch(self, request, pk):
        self.project = get_object_or_404(Project,
                                        id=pk,
                                        owner=request.user)
        return super(ProjectAuthorUpdateView, self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'project': self.project,
                                        'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('proyectos:manage_project_list')
        return self.render_to_response({'project': self.project,
                                        'formset': formset})
    



class ContentCreateUpdateView(TemplateResponseMixin, View):
    author = None
    model = None
    obj = None
    template_name = 'projects/manage/content/form.html'

    def get_model(self, model_name):
        if model_name in ['cv']:
            return apps.get_model(app_label='proyectos',
                                  model_name=model_name)
        return None

    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(model, exclude=['owner',
                                                 'order',
                                                 'created',
                                                 'updated'])
        return Form(*args, **kwargs)

    def dispatch(self, request, author_id, model_name, id=None):
        self.author = get_object_or_404(Author,
                                       id=author_id,
                                       project__owner=request.user)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model,
                                         id=id,
                                         owner=request.user)
        return super(ContentCreateUpdateView,
           self).dispatch(request, author_id, model_name, id)

    def get(self, request, author_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response({'form': form,
                                        'object': self.obj})

    def post(self, request, author_id, model_name, id=None):
        form = self.get_form(self.model,
                             instance=self.obj,
                             data=request.POST,
                             files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            if not id:
                # new content
                Content.objects.create(author=self.author,
                                       item=obj)
            return redirect('proyectos:author_content_list', self.author.id)

        return self.render_to_response({'form': form,
                                        'object': self.obj})


class ContentDeleteView(View):

    def post(self, request, id):
        content = get_object_or_404(Content,
                                    id=id,
                                    author__project__owner=request.user)
        author = content.author
        content.item.delete()
        content.delete()
        return redirect('proyectos:author_content_list', author.id)


class AuthorContentListView(TemplateResponseMixin, View):
    template_name = 'projects/manage/module/content_list.html'

    def get(self, request, author_id):
        author = get_object_or_404(Author,
                                   id=author_id,
                                   project__owner=request.user)

        return self.render_to_response({'author': author})


class AuthorOrderView(CsrfExemptMixin,
                      JsonRequestResponseMixin,
                      View):
    def post(self, request):
        for id, order in self.request_json.items():
            Author.objects.filter(id=id,
                   project__owner=request.user).update(order=order)
        return self.render_json_response({'saved': 'OK'})


class ContentOrderView(CsrfExemptMixin,
                       JsonRequestResponseMixin,
                       View):
    def post(self, request):
        for id, order in self.request_json.items():
            Content.objects.filter(id=id,
                       author__project__owner=request.user) \
                       .update(order=order)
        return self.render_json_response({'saved': 'OK'})


class ProjectListView(TemplateResponseMixin, View):
    model = Project
    template_name = 'projects/course/list.html'

    def get(self, request, subject=None):
        profile = Profile.objects.get(user=request.user)
        subjects = Subject.objects.annotate(total_projects=Count('projects'))
        actividad = profile.activity
        declaracion = DeclaracionVeracidad.objects.get(user=request.user)
        acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
      #  projects = Project.objects.annotate(total_authors=Count('authors'))

        if subject:
            subject = get_object_or_404(Subject,slug=subject)
            projects = projects.filter(subject=subject)       
        return self.render_to_response({'subjects': subjects,
                                        'projects': projects, 
                                        'profile':profile,
                                        'actividad':actividad,
                                        'acepta_terminos_condiciones':acepta_terminos_condiciones,})


class ProjectDetailView(DetailView):
     model = Project
     template_name = 'projects/course/detail.html'

     def get_context_data(self, **kwargs):
        context = super(ProjectDetailView,
                        self).get_context_data(**kwargs)
        context['enroll_form'] = CourseEnrollForm(
                                   initial={'project':self.object})
   #     context['project_enroll_form'] = ProjectEnrollForm(
   #                                initial={'project':self.object})
        return context
     

class ProjectBibliographicReferenceUpdateView(TemplateResponseMixin, View):
    template_name = 'projects/manage/module/bibliographic_reference_formset.html'
    project = None

    def get_formset(self, data=None):
        return BiblioProjectFormSet(instance=self.project, data=data)

    def dispatch(self, request, pk):
        self.project = get_object_or_404(Project, id=pk, owner=request.user)
        return super(ProjectBibliographicReferenceUpdateView, self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'project': self.project, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('proyectos:manage_project_list')
        return self.render_to_response({'project': self.project, 'formset': formset})




class WorkPlanUpdateView(TemplateResponseMixin, View):
    template_name = 'projects/manage/module/work_plan_formset.html'
    project = None

    def get_formset(self, data=None):
        return WorkPlanProjectFormSet(instance=self.project, data=data)

    def dispatch(self, request, pk):
        self.project = get_object_or_404(Project, id=pk, owner=request.user)
        return super(WorkPlanUpdateView, self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'project': self.project, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('proyectos:manage_project_list')
        return self.render_to_response({'project': self.project, 'formset': formset})