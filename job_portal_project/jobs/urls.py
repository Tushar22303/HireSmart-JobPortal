from django.urls import path
from . import views

urlpatterns = [
    path('post_jobs/', views.post_jobs, name='post_jobs'),
    path('my_posted_jobs/', views.my_posted_jobs, name='my_posted_jobs')
]
