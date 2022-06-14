from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, PasswordInput, EmailInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

        widgets = {

            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }),


            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),

        }
