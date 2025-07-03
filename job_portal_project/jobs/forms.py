from django import forms
from .models import Jobs

class Post_Job_Form(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = [
            'job_title',
            'job_description',
            'job_location',
            'job_type',
            'salary',
            'requirements',
            'company_name',
            'company_website',
        ]

        common_classes = 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white text-gray-800'

        widgets = {
            'job_title': forms.TextInput(attrs={'class': common_classes}),
            'job_description': forms.Textarea(attrs={'class': common_classes, 'rows': 4}),
            'job_location': forms.TextInput(attrs={'class': common_classes}),
            'job_type': forms.Select(attrs={'class': common_classes}),
            'salary': forms.TextInput(attrs={'class': common_classes}),
            'requirements': forms.Textarea(attrs={'class': common_classes, 'rows': 4}),
            'company_name': forms.TextInput(attrs={'class': common_classes}),
            'company_website': forms.URLInput(attrs={'class': common_classes}),
        }
