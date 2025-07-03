from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile
from .forms import CustomUserRegistrationForm
from django.contrib.auth.decorators import login_required


# -----------------------------------
# Register View
# -----------------------------------
def register(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

            # Save the Profile
            role = form.cleaned_data['role']
            profile = user.userprofile
            profile.role = role.lower()

            if role == "employer":
                profile.company_name = form.cleaned_data['company_name']
                profile.company_location = form.cleaned_data['company_location']
                profile.company_email = form.cleaned_data['company_email']
                profile.company_contact = form.cleaned_data['company_contact']
                profile.company_website = form.cleaned_data['company_website']

            profile.save()

            messages.success(request, "Account created successfully")
            login(request, user)
            return redirect('dashboard')
        
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'registration/login.html')


# Logout View
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return redirect('home_page')


# Dashboard View
@login_required
def dashboard(request):
    return render(request, 'core/home_page.html')