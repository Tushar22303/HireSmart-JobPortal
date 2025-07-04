from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Jobs
from .forms import Post_Job_Form
from django.http import HttpResponseForbidden
from django.db.models import Q

# ==================================
# post job view
# ==================================
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
            return redirect('browse_jobs')
    else:
        form = Post_Job_Form()
    return render(request, 'jobs/post_jobs.html', {'form': form})


# ==================================
# my posted jobs view
# ==================================
@login_required
def my_posted_jobs(request):
    if request.user.userprofile.role != 'employer':
        return HttpResponseForbidden("You are not authorized to access the my posted job page.")

    my_jobs = Jobs.objects.filter(employer=request.user).order_by('-posted_at')
    return render(request, 'jobs/my_posted_jobs.html', {'my_jobs':my_jobs})



# ==================================
# Browse jobs view
# ==================================
def browse_jobs(request):
    job_title = request.GET.get('job_title', '')
    job_location = request.GET.get('job_location', '')
    company_name = request.GET.get('company_name', '')
    job_type = request.GET.get('job_type', '')

    jobs = Jobs.objects.all()

    if job_title:
        jobs = jobs.filter(job_title__icontains=job_title)
    if job_location:
        jobs = jobs.filter(job_location__icontains=job_location)
    if company_name:
        jobs = jobs.filter(company_name__icontains=company_name)
    if job_type:
        jobs = jobs.filter(job_type__icontains=job_type)

    context = {
        'job_list': jobs.order_by('-posted_at'),
        'job_count': jobs.count(),
        'filters':{
            'job_title': job_title,
            'job_location': job_location,
            'company_name': company_name,
            'job_type': job_type
        }
    }

    return render(request, 'jobs/browse_jobs.html', context)


# ==================================
# View Job Detail 
# ==================================
@login_required
def job_details(request):
    return render(request, 'jobs/job_detail.html')