from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Jobs, JobApplication
from .forms import Post_Job_Form
from django.http import HttpResponseForbidden
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone

# ===============================================================
# post job view -> Employer Side -> Employer posting new jobs
# ===============================================================
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


# ===============================================================
# my posted jobs view -> Employer Side -> Employer can all the jobs posted by him/her
# ===============================================================
@login_required
def my_posted_jobs(request):
    if request.user.userprofile.role != 'employer':
        return HttpResponseForbidden("You are not authorized to access the my posted job page.")

    my_jobs = Jobs.objects.filter(employer=request.user).order_by('-posted_at')
    return render(request, 'jobs/my_posted_jobs.html', {'my_jobs':my_jobs})



# ===============================================================
# Browse jobs view -> all job list posted -> can see both job_seeker and Employer
# ===============================================================
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


# ===============================================================
# View Job Detail -> Both Job seeker and Employer 
# ===============================================================
@login_required
def job_details(request, job_id):
    job = get_object_or_404(Jobs, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job':job})


# ===============================================================
# Apply to Job View -> Only Job seeker can apply to the jobs
# ===============================================================
@login_required
def apply_to_jobs(request, job_id):
    if request.user.userprofile.role != 'job_seeker':
        return HttpResponseForbidden("Only Job Seeker can apply to jobs")
    
    job = get_object_or_404(Jobs, id=job_id)

    # check if already applied
    already_applied = JobApplication.objects.filter(
        job=job,
        job_seeker=request.user
    ).exists()

    if already_applied:
        messages.info(request, "You already have applied to the job")
        return redirect('job_details', job_id=job.id)
    
    if request.method == "POST":
        message = request.POST.get('message', '')
        JobApplication.objects.create(
            job=job, 
            job_seeker=request.user,
            applied_at=timezone.now(),
            message=message
        )
        messages.success(request, "You have successfully applied to the job")
        return redirect('job_details', job_id=job.id)
    
    return render(request, 'jobs/apply_to_jobs.html', {'job':job, 'already_applied':already_applied})


# ===============================================================
# Applied Jobs -> Only Job seeker can view their jobs
# ===============================================================
@login_required
def applied_jobs(request):
    if request.user.userprofile.role != 'job_seeker':
        return HttpResponseForbidden("You are not authorized to view this page.")
    
    applications = JobApplication.objects.filter(job_seeker=request.user).select_related('job')
    return render(request, 'jobs/applied_jobs.html', {'applied_jobs':applications})


# ===============================================================
# View applicants -> Only Employer can see the applicants who applied for job
# ===============================================================
@login_required
def view_applicants(request):
    if request.user.userprofile.role != 'employer':
        return HttpResponseForbidden("You are not authorized to access this page.")
    
    # Get jobs posted by this employer
    employer_jobs = Jobs.objects.filter(employer=request.user)

    # Get all applcations to those jobs
    applications = JobApplication.objects.filter(job__in=employer_jobs).select_related('job', 'job_seeker__userprofile')

    return render(request, 'jobs/view_applicants.html', {'applications': applications})