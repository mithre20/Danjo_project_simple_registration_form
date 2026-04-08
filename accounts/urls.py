"""
accounts/urls.py  —  App-level URL Configuration

Maps URL paths to view functions within the 'accounts' app.
The 'app_name' enables namespacing so we can use {% url 'accounts:register' %}
in templates instead of hardcoding paths.
"""

from django.urls import path
from . import views

app_name = 'accounts'   # Namespace for URL reversing

urlpatterns = [
    # /accounts/register/  →  registration form
    path('register/', views.register_view, name='register'),

    # /accounts/login/     →  login form
    path('',    views.login_view,    name='login'),

    # /accounts/logout/    →  log out and redirect
    path('logout/',   views.logout_view,   name='logout'),

    # /accounts/success/   →  post-registration success page
    path('success/',  views.success_view,  name='success'),
]
