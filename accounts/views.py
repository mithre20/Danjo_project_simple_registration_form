"""
accounts/views.py  —  View Functions

Three views:
  1. register_view  — Shows the registration form; saves user on POST
  2. success_view   — Shown after successful registration
  3. login_view     — Simple login page (uses Django's built-in authenticate)
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegistrationForm


# ------------------------------------------------------------------ #
# 1. REGISTRATION VIEW
# ------------------------------------------------------------------ #
def register_view(request):
    """
    GET  → Show an empty registration form.
    POST → Validate form data; if valid, create user and redirect to success page.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)       # Bind submitted data to form
        if form.is_valid():
            form.save()                             # Saves user to SQLite db
            username = form.cleaned_data['username']
            messages.success(
                request,
                f"Account created successfully for '{username}'! You can now log in."
            )
            return redirect('accounts:success')     # Redirect to success page
        # If form is invalid, fall through and re-render with error messages
    else:
        form = RegistrationForm()                   # Empty form for GET request

    return render(request, 'accounts/register.html', {'form': form})


# ------------------------------------------------------------------ #
# 2. SUCCESS VIEW
# ------------------------------------------------------------------ #
def success_view(request):
    """Simple success/confirmation page shown after registration."""
    return render(request, 'accounts/success.html')


# ------------------------------------------------------------------ #
# 3. LOGIN VIEW
# ------------------------------------------------------------------ #
def login_view(request):
    """
    GET  → Show empty login form.
    POST → Authenticate credentials; login user and redirect to success page.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('accounts:success')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


# ------------------------------------------------------------------ #
# 4. LOGOUT VIEW
# ------------------------------------------------------------------ #
def logout_view(request):
    """Logs out the user and redirects to login page."""
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('accounts:login')
