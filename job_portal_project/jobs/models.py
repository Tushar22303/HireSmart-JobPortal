from django.db import models
from django.contrib.auth.models import User


# Job Type
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
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    requirements = models.TextField()
    company_name = models.CharField(max_length=100)
    company_website = models.URLField(blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f"{self.job_title} at {self.company_name} by {self.employer.username}"