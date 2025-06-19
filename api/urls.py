from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_view, name='about'),
    path('experience/', views.experience_view, name='experience'),
    path('skills/', views.skills_view, name='skills'),
    path('projects/', views.projects_view, name='projects'),
    path('certifications/', views.certifications_view, name='certifications'),
    path('education/', views.education_view, name='education'),
]