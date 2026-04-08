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
    # /  or /login/        →  login form (root redirects here too)
    path('',         views.login_view,    name='login'),
    path('login/',   views.login_view,    name='login_explicit'),

    # /register/           →  registration form
    path('register/', views.register_view, name='register'),

    # /logout/             →  log out and redirect
    path('logout/',   views.logout_view,   name='logout'),

    # /success/            →  post-login/registration success page
    path('success/',  views.success_view,  name='success'),
]
