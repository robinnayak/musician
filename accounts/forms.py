from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class MusicianForm(ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        exclude = ['user']

class Albumform(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email']

