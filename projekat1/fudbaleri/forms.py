from django.forms import ModelForm
from .models import Fudbaler
from django.contrib.auth.models import User


class FudbalerForm(ModelForm):
    class Meta:
        model = Fudbaler
        fields = ['ime', 'prezime', 'godine', 'brojNaDresu', 'tim']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']