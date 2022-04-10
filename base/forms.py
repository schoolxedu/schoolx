from curses.ascii import US
from dataclasses import field, fields
from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
