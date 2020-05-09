from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from cities.models import City

class UserRegisterForm(UserCreationForm):
    postal_code = forms.CharField(label='Code postal')
    city = forms.ModelChoiceField(City.objects.all(), label='Ville ou commune')
    address = forms.CharField(label='Addresse')
    phone_number = forms.CharField(label='Numéro de telephone')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'postal_code', 'city', 'address', 'phone_number']