from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile
from .forms import CustomUserRegistrationForm, AdditionalDataForm, EditProfileForm, EditUserForm, DeleteAccountForm
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


# -----------------------------------
# Login View
# -----------------------------------
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


# -----------------------------------
# Logout View
# -----------------------------------
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return redirect('home_page')


# -----------------------------------
# Dashboard View
# -----------------------------------
@login_required
def dashboard(request):
    return render(request, 'core/home_page.html')


# -----------------------------------
# Profile View
# -----------------------------------
@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')


# -----------------------------------
# additional profile data view
# -----------------------------------
def additional_profile_data(request):
    profile = request.user.userprofile

    if request.method == "POST":
        form = AdditionalDataForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = AdditionalDataForm(instance=profile, user=request.user)        
    return render(request, 'registration/additional_data_form.html', {'form': form})


# -----------------------------------
# edit profile view
# -----------------------------------
@login_required
def edit_profile_view(request):
    user = request.user
    profile = user.userprofile

    if request.method == "POST":
        user_form = EditUserForm(request.POST, instance=user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_view')
    else:
        user_form = EditUserForm(instance=user)
        profile_form = EditProfileForm(instance=profile) 
    return render(request, 'registration/edit_profile_form.html', {'user_form':user_form, 'profile_form':profile_form, 'role': profile.role})


# -----------------------------------
# Delete the User Account (employee and job_seeker)
# -----------------------------------
@login_required
def delete_account(request):
    if request.method == "POST":
        form = DeleteAccountForm(request.POST)
        if form.is_valid():
            confirmation_text = form.cleaned_data['confirmation_text']
            captcha_answer = form.cleaned_data['captcha_answer']

            if confirmation_text != 'DELETE':
                form.add_error('confirmation_text', 'You must type DELETE to confirm.')
            elif captcha_answer != 5:
                form.add_error('captcha_answer', 'Incorrect Captcha Answer.')
            else:
                user = request.user
                logout(request)
                user.delete()
                messages.success(request, "Your account has been deleted successfully.")
                return redirect("home_page")
    else:
        form = DeleteAccountForm()   
    return render(request, 'registration/delete_account_confirm.html', {'form': form})
    