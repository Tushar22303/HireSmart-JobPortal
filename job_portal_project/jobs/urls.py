from django.urls import path
from . import views

urlpatterns = [
    path('post_jobs/', views.post_jobs, name='post_jobs'),
    path('my_posted_jobs/', views.my_posted_jobs, name='my_posted_jobs'),
    path('browse_jobs/', views.browse_jobs, name='browse_jobs'),
    path('job_details/<int:job_id>/', views.job_details, name='job_details'),
]
