from django.urls import path
from . import views

app_name = 'proyectos'

urlpatterns = [
    path('mine/', views.ManageProjectListView.as_view(), name='manage_project_list'),
    path('create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('<pk>/edit/', views.ProjectUpdateView.as_view(), name='project_edit'),
    path('<pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('<pk>/module/', views.ProjectAuthorUpdateView.as_view(), name='project_author_update'),
    path('module/<int:author_id>/content/<model_name>/create/', views.ContentCreateUpdateView.as_view(), name='module_content_create'),
    path('module/<int:author_id>/content/<model_name>/<id>/', views.ContentCreateUpdateView.as_view(), name='module_content_update'),
    path('content/<int:id>/delete/', views.ContentDeleteView.as_view(), name='module_content_delete'),
    path('module/<int:author_id>/', views.AuthorContentListView.as_view(), name='module_content_list'),
    path('module/order/', views.AuthorOrderView.as_view(), name='module_order'),
    path('content/order/', views.ContentOrderView.as_view(), name='content_order'),

   # path('subject/<slug:subject>/', views.CourseListView.as_view(), name='course_list_subject'),
   # path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),

    # Uncomment and correct the following paths if needed
    path('subject/<slug:subject>/', views.ProjectListView.as_view(), name='course_list_subject'),
    path('<slug:slug>/', views.ProjectDetailView.as_view(), name='course_detail'),
    #path('enroll-course/', views.StudentEnrollCourseView.as_view(),name='student_enroll_course'),
    #path('courses/',views.StudentCourseListView.as_view(),name='student_course_list'),
    #path('course/<pk>/',views.StudentCourseDetailView.as_view(),name='student_course_detail'),
    #path('course/<pk>/<module_id>/', views.StudentCourseDetailView.as_view(), name='student_course_detail_module'),

  
   
]
