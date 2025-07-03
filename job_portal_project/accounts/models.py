from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# -----------------------------------
# Choices for user roles
# -----------------------------------
USER_ROLE = (
    ('job_seeker', 'Job Seeker'),
    ('employer', 'Employer'),
)

# -----------------------------------
# Profile Model
# -----------------------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(choices=USER_ROLE, max_length=20)

    # common field
    profile_picture = models.ImageField(upload_to='profile_pic/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)

    # employee specific field
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_location = models.CharField(max_length=255, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)
    company_contact = models.CharField(max_length=15, blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.get_role_display()}'
    

# Signal to create/update the UserProfile automatically
@receiver(post_save,sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()