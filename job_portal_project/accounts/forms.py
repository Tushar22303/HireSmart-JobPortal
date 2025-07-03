from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# -----------------------------------
# Custom User Registration Form
# -----------------------------------
class CustomUserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=UserProfile._meta.get_field('role').choices, required=True)

    # Company basic details or Employer specific field
    company_name = forms.CharField(required=False)
    company_location = forms.CharField(required=False)
    company_email = forms.EmailField(required=False)
    company_contact = forms.CharField(required=False)
    company_website = forms.URLField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'role', 'password1', 'password2', 'company_name', 'company_location', 'company_email', 'company_contact', 'company_website']

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        if role == 'employer':
            required_field = ['company_name', 'company_location','company_email', 'company_contact']
            for field in required_field:
                if not cleaned_data.get(field):
                    self.add_error(field, f"{field.replace('_', ' ').title()} is required for employer!")
        else:
            # Clear employer fields if job seeker, to avoid confusion
            cleaned_data['company_name'] = ''
            cleaned_data['company_location'] = ''
            cleaned_data['company_email'] = ''
            cleaned_data['company_contact'] = ''
            cleaned_data['company_website'] = ''

        return cleaned_data