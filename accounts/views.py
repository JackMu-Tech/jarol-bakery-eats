# accounts/views.py
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from products.views import product_list  # Assuming there's a product_list view in the Products app
from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser

def register(request):
    """
    View for user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    """
    View for user profile.
    """
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})

def user_login(request):
    """
    View for user login.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to appropriate page after login
            if request.GET.get('next'):
                return redirect(request.GET['next'])
            else:
                return redirect('profile')  # Redirect to profile page by default
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')
