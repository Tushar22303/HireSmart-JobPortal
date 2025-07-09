from jobs.models import JobApplication

def notification_count(request):
    if request.user.is_authenticated and hasattr(request.user, 'userprofile'):
        if request.user.userprofile.role == 'employer':
            count = JobApplication.objects.filter(job__employer=request.user, seen_by_employer=False).count()
            return {'notification_count': count}
    return {} 