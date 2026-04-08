"""
userauth_project/urls.py  —  Project-level URL configuration

This file routes incoming requests to the correct app.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # All URLs starting with "accounts/" are forwarded to accounts/urls.py
    path('', include('accounts.urls')),
]
