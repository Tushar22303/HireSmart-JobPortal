from django.urls import path
from . import views

urlpatterns = [
    path('post_jobs/', views.post_jobs, name='post_jobs'),
    path('my_posted_jobs/', views.my_posted_jobs, name='my_posted_jobs'),
    path('my_posted_jobs/<int:job_id>/edit_job/', views.edit_job_details, name='edit_job_details'),
    path('my_posted_jobs/<int:job_id>/delete_job/', views.delete_job_details, name='delete_job_details'),
    path('my_posted_jobs/view_applicants', views.view_applicants, name='view_applicants'),
    path('my_posted_jobs/view_applicants/<int:app_id>/view_details/', views.view_applicants_detail, name='view_applicants_detail'),
    path('my_posted_jobs/view_applicants/<int:app_id>/delete_application/', views.delete_application, name='delete_application'),
    path('browse_jobs/', views.browse_jobs, name='browse_jobs'),
    path('job_details/<int:job_id>/', views.job_details, name='job_details'),
    path('job_details/<int:job_id>/apply/', views.apply_to_jobs, name='apply_to_jobs'),
    path('applied_jobs/', views.applied_jobs, name='applied_jobs'),
    path('applied_jobs/<int:application_id>/withdraw/', views.withdraw_application, name='withdraw_application'),
]
