from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .forms import  SignUpForm, PasswordChangingForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .forms import  ProfileForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from .models import Profile
from workout.models import UserWorkoutPlan
from datetime import date
from django.shortcuts import get_object_or_404

def home(request):# renders the homepage
    return render(request, 'home.html')
def dashboard(request):# dashboard
    if request.user.is_authenticated:
        
        profile = get_object_or_404(Profile, user=request.user)
        workout_plan= UserWorkoutPlan.objects.filter(user=profile, date_created=date.today())
        workouts = UserWorkoutPlan.objects.filter(user=profile, date_created=date.today())
        context= {'workouts': workouts, 'profile': profile}
        return render(request, 'dashboard.html', context)
    return redirect('login')
    

def user_signup(request):# user signup logic
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created' )
            return redirect('login')
    
    return render(request, 'registration/signup.html', {'form': form})


# login page
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page, e.g., home page
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def password_change(request): # change password
    if request.method == 'POST':
        form = PasswordChangingForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully changed!')
            return redirect('login')
    else:
        form = PasswordChangingForm(request.user)
    return render(request, 'password_change.html', {'form': form})


@login_required
def profile(request):# function to create profile each time you create a user
    user=request.user
    
    profiles = Profile.objects.filter(user=request.user)
    if profiles.exists():
        profiles = get_object_or_404(Profile, user=request.user)
    else:
        profile=None


    
    return render(request, 'profile.html',{'user':user, 'profile': profiles})

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):# function to create profile each time you create a user
    if not created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):# saves user profile
    try:
        profile = Profile.objects.get(user=instance.id)
        if profile:
            profile.save()
    except (Profile.DoesNotExist, Profile.MultipleObjectsReturned):
        pass

@login_required
def update_profile(request):# update profile form
    
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
       
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')  # Redirect to the profile page
    else:
       
        form = ProfileForm(instance=profile)

    return render(request, 'profile_update.html', {'form': form})
