"""
accounts/forms.py  —  Registration Form

UserCreationForm is Django's built-in form for creating users.
We extend it to add an email field and custom password-match validation.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    """
    Extends Django's UserCreationForm to include:
      - email (required)
      - password1 (Password)
      - password2 (Confirm Password)

    UserCreationForm already provides password1, password2 and
    checks that they match — we add email and restyle labels.
    """

    email = forms.EmailField(
        required=True,
        help_text="Enter a valid email address.",
        widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'})
    )

    class Meta:
        model = User                                   # Uses Django's built-in User table
        fields = ['username', 'email', 'password1', 'password2']
        # Django maps these fields to: auth_user table columns

    # ------------------------------------------------------------------ #
    # Custom widget attributes — adds placeholder text to each field
    # ------------------------------------------------------------------ #
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Choose a username'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})
        self.fields['username'].help_text = "Letters, digits and @/./+/-/_ only."
        self.fields['password1'].help_text = "Minimum 8 characters. Cannot be entirely numeric."
        self.fields['password2'].help_text = "Re-enter the same password for verification."

    # ------------------------------------------------------------------ #
    # Extra validation: password match is already done by UserCreationForm,
    # but we add a clean_email check to prevent duplicate emails.
    # ------------------------------------------------------------------ #
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def save(self, commit=True):
        """Save the user with the email field properly stored."""
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
