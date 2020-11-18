from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    prompt = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','prompt']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    prompt = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email','prompt']

        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
    	model = Profile
    	fields = ['image']
