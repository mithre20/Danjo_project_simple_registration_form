"""
accounts/models.py  —  Database Model

We use Django's built-in User model (django.contrib.auth.models.User)
which already provides:
  - username
  - email
  - password (stored as a secure hash, never plain text)
  - date_joined, is_active, etc.

No custom model is needed for basic registration.
If you want extra fields (e.g., phone, avatar), you would
create a UserProfile model here and link it via OneToOneField.

Example of a UserProfile extension (optional):

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE)
    phone      = models.CharField(max_length=15, blank=True)
    bio        = models.TextField(blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
"""

# No custom model required — Django's built-in User model is used directly.
