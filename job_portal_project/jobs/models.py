from django.db import models
from django.contrib.auth.models import User


# ----------------------------------------
# Job Type
# ----------------------------------------
JOB_TYPE_CHOICE = (
    ('full_time', 'Full Time'),
    ('internship', 'Internship'),
    ('part_time', 'Part Time'),
    ('contract', 'Contract'),
    ('freelance', 'Freelance'),
)


class Jobs(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    job_location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100, choices=JOB_TYPE_CHOICE)
    salary = models.CharField(max_length=100, blank=True, null=True)
    requirements = models.TextField()
    company_name = models.CharField(max_length=100)
    company_website = models.URLField(blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f"{self.job_title} at {self.company_name} by {self.employer.username}"


# ----------------------------------------
# Job Application
# ----------------------------------------
class JobApplication(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, related_name='applications')
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
    applied_at = models.DateTimeField(auto_now_add=True)
    seen_by_employer = models.BooleanField(default=False)

    # Optional for message
    message = models.TextField(blank=True, null=True)

    # status choice -> Track status like pending, rejected, selected...
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pending')

    class Meta:
        unique_together = ('job', 'job_seeker')
        ordering = ['-applied_at']

    def __str__(self):
        return f'{self.job_seeker.username} applied to {self.job.job_title}'
    
    @property
    # Return resume file from the job seeker profile 
    def resume_url(self):
        return self.job_seeker.userprofile.resume.url if self.job_seeker.userprofile.resume else None
    
    @property
    def contact_number(self):
        return self.job_seeker.userprofile.contact_number