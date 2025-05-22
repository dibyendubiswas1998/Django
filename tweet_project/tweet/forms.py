from django import forms
from .models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TweetForms(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["text", "photo"]
        
        
# Class User Registration form :
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')