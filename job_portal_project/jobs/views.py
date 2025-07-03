from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Jobs
from .forms import Post_Job_Form
from django.http import HttpResponseForbidden


# post job view
@login_required
def post_jobs(request):
    if request.user.userprofile.role != 'employer':
        return HttpResponseForbidden("You are not authorized to post jobs.")
    
    if request.method == "POST":
        form = Post_Job_Form(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            return redirect('my_posted_jobs')
    else:
        form = Post_Job_Form()
    return render(request, 'jobs/post_jobs.html', {'form': form})


# my posted jobs view
@login_required
def my_posted_jobs(request):
    if request.user.userprofile.role != 'employer':
        return HttpResponseForbidden("You are not authorized to access the my posted job page.")

    my_jobs = Jobs.objects.filter(employer=request.user).order_by('-posted_at')
    return render(request, 'jobs/my_posted_jobs.html', {'my_jobs':my_jobs})