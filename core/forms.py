import uuid

from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from project.core.models import AuthUser as User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()


def generate_username():
    hex_generate = uuid.uuid4().hex[:4].capitalize()
    val = "{0}{1}".format('animatflix', hex_generate).capitalize()
    return val


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=12, min_length=4, required=True,
                                 widget=forms.TextInput(attrs={'autofocus': ''}))
    last_name = forms.CharField(max_length=12, min_length=4, required=True)
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput())
    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput())
    username = forms.CharField(max_length=150, validators=[username_validator],
                               help_text="If don't put a Username, a name will be generated for you", required=False)
    email = forms.EmailField(max_length=50, required=True,)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email addresses must be unique.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username == '':
            username = generate_username()
        return username

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email or Username', required=True)
