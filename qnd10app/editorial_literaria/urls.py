from django.urls import path
from . import views

app_name = 'editorial_literaria'

urlpatterns = [
    path('mine/', views.ManageCourseListView.as_view(), name='manage_course_list'),
    path('create/', views.CourseCreateView.as_view(), name='course_create'),
    path('<pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('<pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('<pk>/module/', views.CourseModuleUpdateView.as_view(), name='course_module_update'),
    path('module/<int:module_id>/content/<model_name>/create/', views.ContentCreateUpdateView.as_view(), name='module_content_create'),
    path('module/<int:module_id>/content/<model_name>/<id>/', views.ContentCreateUpdateView.as_view(), name='module_content_update'),
    path('content/<int:id>/delete/', views.ContentDeleteView.as_view(), name='module_content_delete'),
    path('module/<int:module_id>/', views.ModuleContentListView.as_view(), name='module_content_list'),
    path('module/order/', views.ModuleOrderView.as_view(), name='module_order'),
    path('content/order/', views.ContentOrderView.as_view(), name='content_order'),

   # path('subject/<slug:subject>/', views.CourseListView.as_view(), name='course_list_subject'),
   # path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),

    # Uncomment and correct the following paths if needed
    path('subject/<slug:subject>/', views.CourseListView.as_view(), name='course_list_subject'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
path('enroll-course/', views.StudentEnrollCourseView.as_view(),name='student_enroll_course'),
    path('courses/',views.StudentCourseListView.as_view(),name='student_course_list'),
    path('course/<pk>/',views.StudentCourseDetailView.as_view(),name='student_course_detail'),
    path('course/<pk>/<module_id>/', views.StudentCourseDetailView.as_view(), name='student_course_detail_module'),

    path('inicio_crear_convocatoria/', views.manual_crear_convocatoria, name='inicio_crear_convocatoria'),
    path('inicio_editar_convocatoria/', views.manual_editar_convocatoria, name='inicio_editar_convocatoria'),
    path('inicio_Mis_convocatoria/', views.manual_mis_convocatoria, name='inicio_mis_convocatoria'),
    path('inicio_Inscripciones/', views.manual_inscripcion, name='inicio_inscripcion'),
   # path('inicio_postulacion/', views.manual_postulation, name='inicio_postulation'),  # Corrected name
    path('inicio_Mis_postulaciones/', views.manual_mis_postulaciones, name='inicio_mis_postulaciones'),
    path('inicio_crear_Proyecto/', views.manual_crear_proyecto, name='inicio_crear_proyecto'),
    path('inicio_editar_Proyecto/', views.manual_editar_proyecto, name='inicio_editar_proyecto'),
    path('inicio_Mis_Proyecto/', views.manual_mis_proyectos, name='inicio_mis_proyectos'),
   
]
