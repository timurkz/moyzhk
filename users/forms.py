from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['email','password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    #email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['first_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['zhk']
