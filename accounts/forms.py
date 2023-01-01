from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserRegisterForm(UserCreationForm):
  
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'gender', 'telephone', 'email')

  

class CustomUserLoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')